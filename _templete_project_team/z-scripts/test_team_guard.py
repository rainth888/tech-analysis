#!/usr/bin/env python3
"""在临时 Git 仓库和真实 worktree 中验证协作边界，不改项目工作树。"""
import datetime as dt
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("team_guard", Path(__file__).with_name("team_guard.py"))
guard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(guard)
TEMPLATE = Path(__file__).resolve().parent.parent


class GuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="team-guard-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        self.git("init")
        self.git("symbolic-ref", "HEAD", "refs/heads/main")
        self.git("config", "user.name", "Test User")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        for p in ["server/a.txt", "server/b.txt", "web/ui.txt", "web/e2e/test.txt"]:
            (self.root / p).parent.mkdir(parents=True, exist_ok=True)
            (self.root / p).write_text("initial\n")
        target = self.root / ".agents/parallel/policy.json"
        target.parent.mkdir(parents=True)
        shutil.copy(TEMPLATE / ".agents/parallel/policy.json", target)
        self.git("add", "--", "server", "web", ".agents")
        self.git("commit", "-qm", "initial")
        self.git("checkout", "-b", "feature/T1-be-u1")
        self.call("init", "--project", "test-team")

    def git(self, *args, root=None):
        p = subprocess.run(["git", "-C", str(root or self.root), *args], stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        return p.stdout.strip()

    def call(self, *args, root=None, coord=None):
        root = root or self.root
        parsed = guard.parser().parse_args(["--root", str(root), *args])
        return guard.Guard(root, coord).run(parsed)

    def claim(self, paths=None, root=None, lane="l1", user="u1", actor="a1", role="BE", task="T1", resource=None):
        args = ["claim", "--lane", lane, "--user", user, "--actor", actor, "--role", role,
                "--task", task, "--paths", *(paths or ["server/a.txt"])]
        if resource:
            args += ["--resource", resource]
        return self.call(*args, root=root)

    def second(self):
        root = Path(self.temp.name) / "other"
        self.git("worktree", "add", "-b", "feature/T2-be-u2", str(root), "HEAD")
        return root

    def freeze(self, paths=None):
        return self.call("freeze", "--lane", "l1", "--actor", "a1", "--freeze-id", "F1",
                         "--paths", *(paths or ["server/a.txt"]), "--evidence", "unit-tests-passed")

    def approval(self, freeze, **overrides):
        a = dict(approval_id="AP1", freeze_id="F1", revision=freeze["revision"],
                 baseline_commit=freeze["commit"], user_id="u2", actor_id="a2", role_id="QA", task_id="T2",
                 paths=["server/a.txt"], approved_by="human-reviewer",
                 approved_at=(guard.utcnow() - dt.timedelta(minutes=1)).isoformat(),
                 expires_at=(guard.utcnow() + dt.timedelta(hours=1)).isoformat(),
                 human_evidence="https://example.invalid/reviews/1", reason_kind="functional_interference",
                 reason="相关功能错误影响测试", impact="F1", regression="重新运行受影响测试", rollback="保留原提交")
        a.update(overrides)
        p = Path(self.temp.name) / "approval.json"
        p.write_text(json.dumps(a))
        return p

    def release(self):
        return self.call("release", "--lane", "l1", "--actor", "a1")

    def test_same_role_disjoint_worktrees_share_authority(self):
        self.claim()
        other = self.second()
        self.claim(["server/b.txt"], root=other, lane="l2", user="u2", actor="a2")
        self.assertEqual(len(self.call("status")["lanes"]), 2)

    def test_worktree_conflict(self):
        self.claim()
        with self.assertRaises(guard.GuardError):
            self.claim(["server/b.txt"], lane="l2", actor="a2")

    def test_directory_overlap_across_worktrees(self):
        self.claim(["server/"])
        with self.assertRaises(guard.GuardError):
            self.claim(root=self.second(), lane="l2", actor="a2")

    def test_case_insensitive_overlap(self):
        self.assertTrue(guard.overlap("server/", "SERVER/a.txt"))
        self.assertFalse(guard.overlap("server/a", "server/ab"))

    def test_role_specific_child_exclusion(self):
        with self.assertRaises(guard.GuardError):
            self.claim(["web/"], role="FE")
        self.claim(["web/ui.txt"], role="FE")

    def test_same_resource_conflicts(self):
        self.claim(resource="db-migration")
        with self.assertRaises(guard.GuardError):
            self.claim(["server/b.txt"], root=self.second(), lane="l2", actor="a2", resource="db-migration")

    def test_cannot_release_another_actor(self):
        self.claim()
        with self.assertRaises(guard.GuardError):
            self.call("release", "--lane", "l1", "--actor", "a2")

    def test_invalid_paths(self):
        for path in ("../server/a", "/server/a", "server/../a", "server\\a", "server/**", ".git/config", "server//a", "server/a."):
            with self.subTest(path=path), self.assertRaises(guard.GuardError):
                self.claim([path])

    def test_symlink_rejected(self):
        (self.root / "server/link").symlink_to(self.root / "web", target_is_directory=True)
        with self.assertRaises(guard.GuardError):
            self.claim(["server/link/ui.txt"])

    def test_protected_branch_rejected(self):
        self.git("checkout", "main")
        with self.assertRaises(guard.GuardError):
            self.claim()

    def test_parent_repo_rejected(self):
        with self.assertRaises(guard.GuardError):
            guard.Guard(self.root / "server")

    def test_raw_inputs_and_legacy_docs_readonly(self):
        for path in ("z-docs/new.md", "docs/new.md"):
            with self.subTest(path=path), self.assertRaises(guard.GuardError):
                self.claim([path], role="AR")

    def test_metadata_requires_resource(self):
        with self.assertRaises(guard.GuardError):
            self.claim(["AGENTS.md"], role="AR")
        self.claim(["AGENTS.md"], role="AR", resource="task-metadata")

    def test_freeze_persists_after_release_and_blocks_original_owner(self):
        self.claim()
        self.freeze()
        self.release()
        with self.assertRaises(guard.GuardError):
            self.claim()
        self.assertEqual(self.call("status")["freezes"]["F1"]["status"], "FROZEN")

    def test_dirty_freeze_rejected(self):
        self.claim()
        (self.root / "server/a.txt").write_text("dirty\n")
        with self.assertRaises(guard.GuardError):
            self.freeze()

    def test_human_approved_cross_role_takeover_and_refreeze(self):
        self.claim(["server/"])
        f = self.freeze(["server/"])
        self.release()
        approval = self.approval(f)
        self.call("thaw", "--approval", str(approval))
        self.claim(lane="l2", user="u2", actor="a2", role="QA", task="T2")
        (self.root / "server/a.txt").write_text("fixed\n")
        self.call("check", "--lane", "l2", "--actor", "a2")
        self.git("add", "--", "server/a.txt")
        self.git("commit", "-qm", "fix")
        self.call("freeze", "--lane", "l2", "--actor", "a2", "--freeze-id", "F1",
                  "--paths", "server/", "--evidence", "regression-passed")
        self.call("release", "--lane", "l2", "--actor", "a2")
        f2 = self.call("status")["freezes"]["F1"]
        self.assertEqual(f2["revision"], 2)
        self.assertEqual(f2["owner_user"], "u2")

    def test_thaw_cannot_steal_active_lane(self):
        self.claim()
        approval = self.approval(self.freeze())
        with self.assertRaises(guard.GuardError):
            self.call("thaw", "--approval", str(approval))

    def test_wrong_baseline_and_expired_approval(self):
        self.claim()
        f = self.freeze()
        self.release()
        for overrides in ({"baseline_commit": "0" * 40}, {"revision": 999},
                          {"expires_at": (guard.utcnow()-dt.timedelta(hours=1)).isoformat()},
                          {"reason_kind": "cleanup"}, {"human_evidence": ""}, {"paths": ["server/"]}):
            with self.subTest(overrides=overrides), self.assertRaises(guard.GuardError):
                self.call("thaw", "--approval", str(self.approval(f, **overrides)))

    def test_approval_bound_to_recipient(self):
        self.claim()
        f = self.freeze()
        self.release()
        self.call("thaw", "--approval", str(self.approval(f)))
        with self.assertRaises(guard.GuardError):
            self.claim(lane="l2", user="wrong", actor="a2", role="QA", task="T2")

    def test_pending_thaw_cannot_be_silently_released(self):
        self.claim()
        f = self.freeze()
        self.release()
        self.call("thaw", "--approval", str(self.approval(f)))
        self.claim(lane="l2", user="u2", actor="a2", role="QA", task="T2")
        with self.assertRaises(guard.GuardError):
            self.call("release", "--lane", "l2", "--actor", "a2")

    def test_rename_both_paths_checked(self):
        self.claim()
        (self.root / "server/a.txt").rename(self.root / "server/new.txt")
        self.git("add", "--", "server/a.txt", "server/new.txt")
        with self.assertRaises(guard.GuardError):
            self.call("check", "--lane", "l1", "--actor", "a1", "--staged")

    def test_frozen_content_change_check_fails(self):
        self.claim()
        self.freeze()
        (self.root / "server/a.txt").write_text("illegal\n")
        with self.assertRaises(guard.GuardError):
            self.call("check", "--lane", "l1", "--actor", "a1")

    def test_foreign_staged_file_rejected(self):
        self.claim()
        (self.root / "server/b.txt").write_text("foreign\n")
        self.git("add", "--", "server/b.txt")
        with self.assertRaises(guard.GuardError):
            self.call("check", "--lane", "l1", "--actor", "a1", "--staged")

    def test_commit_message(self):
        self.claim()
        self.call("check", "--lane", "l1", "--actor", "a1", "--message", "[BE][T1][u1] fix: 修复问题")
        with self.assertRaises(guard.GuardError):
            self.call("check", "--lane", "l1", "--actor", "a1", "--message", "[BE][T1][u2] fix: 修复问题")

    def test_atomic_claim_race(self):
        other = self.second()
        processes = []
        for n, root in enumerate((self.root, other)):
            cmd = [sys.executable, str(TEMPLATE / "z-scripts/team_guard.py"), "--root", str(root),
                   "claim", "--lane", "l"+str(n), "--actor", "a"+str(n), "--user", "u"+str(n),
                   "--role", "BE", "--task", "T1", "--paths", "server/a.txt"]
            processes.append(subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        for p in processes:
            p.communicate(timeout=20)
        self.assertEqual(sorted(p.returncode for p in processes), [0, 2])
        self.assertEqual(len(self.call("status")["lanes"]), 1)

    def test_interrupted_transaction_fail_closed(self):
        g = guard.Guard(self.root)
        (g.coord / "transaction.lock").mkdir()
        with self.assertRaises(guard.GuardError):
            self.claim()
        self.assertTrue((g.coord / "transaction.lock").exists())

    def test_human_recovery_does_not_thaw(self):
        lane = self.claim()
        self.freeze()
        proof = Path(self.temp.name) / "recovery.json"
        proof.write_text(json.dumps(dict(lane_id="l1", lane_hash=guard.digest(lane), approved_by="human",
            human_evidence="review-2", preserved_work="backup-ref", process_stopped_evidence="confirmed-stopped")))
        self.call("recover", "--approval", str(proof))
        self.assertFalse(self.call("status")["lanes"])
        with self.assertRaises(guard.GuardError):
            self.claim()

    def test_snapshot_roundtrip_preserves_freeze(self):
        self.claim()
        self.freeze()
        self.release()
        path = "z-readme/202611122304_冻结快照.json"
        self.claim([path], role="AR")
        self.call("snapshot", "--lane", "l1", "--actor", "a1", "--output", path)
        other = Path(self.temp.name) / "new-authority"
        self.call("init", "--project", "test-team", "--snapshot", str(self.root/path), coord=other)
        self.assertEqual(self.call("status", coord=other)["freezes"]["F1"]["status"], "FROZEN")

    def test_release_requires_own_deliverables_frozen(self):
        self.claim()
        (self.root / "server/a.txt").write_text("new deliverable\n")
        self.git("add", "--", "server/a.txt")
        self.git("commit", "-qm", "deliverable")
        with self.assertRaises(guard.GuardError):
            self.release()
        self.freeze()
        self.release()

    def test_release_refuses_dirty_work(self):
        self.claim()
        (self.root / "server/a.txt").write_text("unfinished\n")
        with self.assertRaises(guard.GuardError):
            self.release()

    def test_claim_stale_heartbeat_does_not_unlock(self):
        self.claim()
        g = guard.Guard(self.root)
        with g.transaction() as state:
            state["lanes"]["l1"]["heartbeat"] = "2000-01-01T00:00:00+00:00"
        with self.assertRaises(guard.GuardError):
            self.claim(root=self.second(), lane="l2", actor="a2")

    def test_cross_clone_shared_authority_conflict(self):
        self.claim()
        other = Path(self.temp.name) / "clone"
        self.git("clone", "--quiet", str(self.root), str(other))
        self.git("checkout", "-b", "feature/clone", root=other)
        args = guard.parser().parse_args(["--root", str(other), "claim", "--lane", "l2", "--actor", "a2",
                  "--user", "u2", "--role", "BE", "--task", "T2", "--paths", "server/a.txt"])
        with self.assertRaises(guard.GuardError):
            guard.Guard(other, guard.Guard(self.root).coord).run(args)

    def test_wrong_actor_cannot_refreeze(self):
        self.claim()
        f = self.freeze()
        self.release()
        self.call("thaw", "--approval", str(self.approval(f)))
        self.claim(lane="l2", user="u2", actor="a2", role="QA", task="T2")
        with self.assertRaises(guard.GuardError):
            self.call("freeze", "--lane", "l2", "--actor", "a3", "--freeze-id", "F1",
                      "--paths", "server/a.txt", "--evidence", "tests")

    def test_policy_change_fails_closed(self):
        p = self.root / ".agents/parallel/policy.json"
        policy = guard.read_json(p)
        policy["protected_branches"].append("release")
        p.write_text(json.dumps(policy))
        with self.assertRaises(guard.GuardError):
            self.call("status")

    def test_approved_takeover_requires_frozen_commit_in_history(self):
        other = self.second()
        self.claim()
        (self.root / "server/a.txt").write_text("new baseline\n")
        self.git("add", "--", "server/a.txt")
        self.git("commit", "-qm", "new baseline")
        f = self.freeze()
        self.release()
        self.call("thaw", "--approval", str(self.approval(f)))
        with self.assertRaises(guard.GuardError):
            self.claim(root=other, lane="l2", user="u2", actor="a2", role="QA", task="T2")

    def test_refreeze_rejects_unapproved_sibling_change(self):
        self.claim(["server/"])
        f = self.freeze(["server/"])
        self.release()
        self.call("thaw", "--approval", str(self.approval(f)))
        self.claim(lane="l2", user="u2", actor="a2", role="QA", task="T2")
        (self.root / "server/b.txt").write_text("unauthorized sibling\n")
        self.git("add", "--", "server/b.txt")
        self.git("commit", "-qm", "bad change")
        with self.assertRaises(guard.GuardError):
            self.call("freeze", "--lane", "l2", "--actor", "a2", "--freeze-id", "F1",
                      "--paths", "server/", "--evidence", "tests")

    def test_failed_transaction_does_not_persist(self):
        g = guard.Guard(self.root)
        with self.assertRaises(RuntimeError):
            with g.transaction() as state:
                state["project_id"] = "bad"
                raise RuntimeError("simulated interruption")
        self.assertEqual(self.call("status")["project_id"], "test-team")

    def test_approval_renewal_and_replay(self):
        self.claim()
        f = self.freeze()
        self.release()
        self.call("thaw", "--approval", str(self.approval(f)))
        self.claim(lane="l2", user="u2", actor="a2", role="QA", task="T2")
        with self.assertRaises(guard.GuardError):
            self.call("thaw", "--approval", str(self.approval(f)))
        self.call("thaw", "--approval", str(self.approval(f, approval_id="AP2", supersedes="AP1")))
        self.assertEqual(self.call("status")["freezes"]["F1"]["approval"]["approval_id"], "AP2")

    def test_formatter_requires_explicit_files(self):
        p = subprocess.run([sys.executable, str(TEMPLATE / "z-scripts/validate_project.py"), "--align"],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(p.returncode, 2)

    def test_narrow_formatting_leaves_other_files_intact(self):
        spec = importlib.util.spec_from_file_location("validator", TEMPLATE / "z-scripts/validate_project.py")
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        root = Path(self.temp.name) / "formatting"
        root.mkdir()
        raw = "| 名字 | 值 |\n| --- | --- |\n| 一 | 1234 |\n"
        for name in ("one.md", "two.md"):
            (root/name).write_text(raw)
        (root/".agents/parallel").mkdir(parents=True)
        shutil.copy(TEMPLATE/".agents/parallel/policy.json", root/".agents/parallel/policy.json")
        validator.ROOT = root
        validator.REQUIRED_PATHS = []
        from unittest.mock import patch
        with patch.object(sys, "argv", ["validate", "--align", "--files", "one.md"]):
            self.assertEqual(validator.main(), 0)
        self.assertNotEqual((root/"one.md").read_text(), raw)
        self.assertEqual((root/"two.md").read_text(), raw)


if __name__ == "__main__":
    unittest.main(verbosity=2)
