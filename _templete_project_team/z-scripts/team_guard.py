#!/usr/bin/env python3
"""团队协作本地协调器。只用标准库；不是身份认证、远程锁服务或 Git 权限边界。"""
import argparse
import contextlib
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import unicodedata
import uuid


class GuardError(Exception):
    pass


def require(ok, message):
    if not ok:
        raise GuardError(message)


def utcnow():
    return dt.datetime.now(dt.timezone.utc)


def stamp():
    return utcnow().isoformat()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    path = Path(path)
    temp = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    try:
        with temp.open("x", encoding="utf-8") as f:
            json.dump(value, f, ensure_ascii=False, indent=2)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def ident(value):
    require(isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,95}", value),
            "标识只允许字母、数字、点、横线和下划线，且不得为空")
    return value


def canonical(value):
    require(isinstance(value, str) and value and not any(c in value for c in "\\:*?[]\x00\n\r"),
            "路径必须为相对路径，不允许通配符、反斜线、控制符或盘符")
    bits = value.rstrip("/").split("/")
    require(all(x not in ("", ".", "..") and x == x.strip() and not x.endswith(".") for x in bits),
            "路径必须规范化，禁止绝对路径、父目录和含糊的 Windows 路径")
    require(bits[0].casefold() != ".git", "禁止占用 Git 内部文件")
    return unicodedata.normalize("NFC", value).casefold()


def contains(scope, path):
    a, b = canonical(scope), canonical(path)
    return b == a.rstrip("/") or (a.endswith("/") and b.startswith(a))


def overlap(a, b):
    return contains(a, b) or contains(b, a)


class Guard:
    def __init__(self, root, coord=None):
        self.root = Path(root).resolve()
        self.repo = Path(self.git("rev-parse", "--show-toplevel").strip()).resolve()
        require(self.repo == self.root, "请在复制后的独立项目 Git 根目录运行；禁止误用父仓库")
        common = Path(self.git("rev-parse", "--git-common-dir").strip())
        if not common.is_absolute():
            common = self.root / common
        self.coord = Path(coord).resolve() if coord else common.resolve() / "team-guard"
        self.state_file = self.coord / "state.json"
        self.policy = read_json(self.root / ".agents/parallel/policy.json")
        self.worktree = hashlib.sha256(str(self.root).encode()).hexdigest()

    def git(self, *args, binary=False):
        p = subprocess.run(["git", "-C", str(self.root), *args], stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
        require(p.returncode == 0, p.stderr.decode(errors="replace").strip() or "Git 命令失败")
        return p.stdout if binary else p.stdout.decode("utf-8")

    @contextlib.contextmanager
    def transaction(self, initializing=False):
        self.coord.mkdir(parents=True, exist_ok=True)
        lock = self.coord / "transaction.lock"
        try:
            lock.mkdir()
        except FileExistsError:
            raise GuardError("协调事务正在运行或异常中断；稍后重试，禁止按超时自动删除锁")
        try:
            if initializing:
                require(not self.state_file.exists(), "协调中心已存在，不能覆盖")
                state = {}
            else:
                require(self.state_file.is_file(), "协调中心未初始化；先执行 init 或连接团队已存在的 --coord-dir")
                state = read_json(self.state_file)
                require(state.get("schema") == 1 and state.get("policy_hash") == digest(self.policy),
                        "协调中心版本或策略不匹配；须由维护者审核迁移，禁止重置绕过")
            before = digest(state)
            yield state
            if digest(state) != before:
                write_json(self.state_file, state)
        finally:
            lock.rmdir()

    def path(self, value):
        canonical(value)
        p = self.root
        for part in value.rstrip("/").split("/"):
            p = p / part
            require(not p.is_symlink(), "禁止通过符号链接绕过路径锁：" + value)
        require(not p.is_dir() or value.endswith("/"), "目录必须以 / 结尾：" + value)
        return value

    def role_allowed(self, role, scope):
        rules = self.policy["paths"]
        matched = [r for r in rules if contains(r["path"], scope)]
        if not matched:
            return False
        best = max(matched, key=lambda r: len(r["path"]))
        if role not in best["roles"]:
            return False
        # 不能用父目录覆盖被更具体规则排除的子目录。
        return all(role in r["roles"] for r in rules if contains(scope, r["path"]))

    def head(self):
        return self.git("rev-parse", "HEAD").strip()

    def branch(self):
        branch = self.git("symbolic-ref", "--short", "HEAD").strip()
        require(branch not in self.policy["protected_branches"], "禁止在受保护分支领取开发泳道")
        return branch

    def owned(self, state, lane_id, actor):
        lane = state["lanes"].get(lane_id)
        require(lane is not None and lane["actor_id"] == actor, "泳道不存在或 actor_id 不匹配")
        require(lane["worktree"] == self.worktree and lane["branch"] == self.branch(),
                "泳道所属工作树或分支已变化")
        return lane

    def grant(self, freeze, lane, path):
        a = freeze.get("approval")
        if not a or freeze["status"] != "CHANGE_APPROVED":
            return False
        expiry = dt.datetime.fromisoformat(a["expires_at"])
        return (expiry > utcnow() and all(a[k] == lane[k] for k in
                ("user_id", "actor_id", "role_id", "task_id")) and
                any(contains(p, path) for p in a["paths"]))

    def permitted(self, state, lane, path):
        self.path(path)
        require(not contains("z-docs/", path) and not contains("docs/", path),
                "原始输入区与历史模板区只读")
        hits = [f for f in state["freezes"].values() if any(overlap(p, path) for p in f["paths"])]
        require(self.role_allowed(lane["role_id"], path) or
                any(self.grant(f, lane, path) for f in hits), "路径不属于角色且无人工接手授权：" + path)
        for freeze in hits:
            require(self.grant(freeze, lane, path), "路径已冻结，必须人工批准解冻：" + freeze["freeze_id"])
            # 审批引用了旧版本，不代表当前工作树已经包含该版本。
            self.git("merge-base", "--is-ancestor", freeze["commit"], "HEAD")

    def event(self, state, kind, **details):
        state["events"].append({"at": stamp(), "kind": kind, **details})

    def claim(self, state, args):
        for value in (args.lane, args.actor, args.user, args.task, args.role):
            ident(value)
        require(args.role in self.policy["roles"], "未知角色")
        require(args.lane not in state["lanes"], "泳道已存在；使用 heartbeat 续约")
        paths = [self.path(p) for p in args.paths]
        require(len({canonical(p) for p in paths}) == len(paths), "路径重复")
        lane = dict(lane_id=args.lane, actor_id=args.actor, user_id=args.user, role_id=args.role,
                    task_id=args.task, paths=paths, resources=args.resource, worktree=self.worktree,
                    branch=self.branch(), starting_head=self.head(), heartbeat=stamp())
        for resource in args.resource:
            ident(resource)
        for path in paths:
            self.permitted(state, lane, path)
        for other in state["lanes"].values():
            require(other["worktree"] != self.worktree, "一个工作树只允许一个写泳道")
            require(other["branch"] != lane["branch"], "一个分支只允许一个写泳道")
            require(not any(overlap(p, q) for p in paths for q in other["paths"]),
                    "路径与活跃泳道冲突：" + other["lane_id"])
            require(not set(args.resource) & set(other["resources"]), "共享资源已被占用")
        metadata = self.policy["metadata_paths"]
        require(not any(overlap(p, q) for p in paths for q in metadata) or
                "task-metadata" in args.resource, "修改共享控制文件必须持有 task-metadata")
        state["lanes"][args.lane] = lane
        self.event(state, "claim", lane_id=args.lane)
        return lane

    def manifest(self, scopes, ref="HEAD"):
        result = {}
        raw = self.git("ls-tree", "-r", "-z", ref, "--", *scopes, binary=True)
        for entry in raw.split(b"\0"):
            if not entry:
                continue
            meta, name = entry.split(b"\t", 1)
            mode, kind, oid = meta.decode().split()
            path = name.decode("utf-8")
            self.path(path)
            require(mode in ("100644", "100755") and kind == "blob", "冻结范围不能含符号链接或子模块")
            result[path] = {"mode": mode, "sha256": hashlib.sha256(
                self.git("cat-file", "blob", oid, binary=True)).hexdigest()}
        return result

    def freeze(self, state, args):
        ident(args.freeze_id)
        lane = self.owned(state, args.lane, args.actor)
        scopes = [self.path(p) for p in args.paths]
        old = state["freezes"].get(args.freeze_id)
        if not old:
            require(all(any(contains(p, q) for p in lane["paths"]) for q in scopes), "只能冻结本泳道拥有的范围")
        require(not self.git("status", "--porcelain", "--untracked-files=all", "--", *scopes),
                "请先提交并核验产出；不能冻结脏文件或未跟踪文件")
        for freeze in state["freezes"].values():
            if any(overlap(p, q) for p in scopes for q in freeze["paths"]):
                require(freeze is old, "冻结范围与其他冻结记录重叠")
        if old:
            require(old["paths"] == scopes and old.get("approval") and
                    all(self.grant(old, lane, p) for p in old["approval"]["paths"]),
                    "重新冻结须保持原范围并持有有效的人工授权")
        manifest = self.manifest(scopes)
        require(manifest or old is not None, "冻结范围没有已提交文件")
        if old:
            changed = [p for p in set(manifest) | set(old["manifest"])
                       if manifest.get(p) != old["manifest"].get(p)]
            require(all(self.grant(old, lane, p) and any(contains(q, p) for q in lane["paths"])
                        for p in changed), "重新冻结包含未经批准或未领取的改动")
        record = dict(freeze_id=args.freeze_id, paths=scopes, owner_user=lane["user_id"],
                      owner_actor=lane["actor_id"], owner_role=lane["role_id"], task_id=lane["task_id"],
                      status="FROZEN", revision=(old["revision"] + 1 if old else 1),
                      commit=self.head(), manifest=manifest, evidence=args.evidence, at=stamp())
        state["freezes"][args.freeze_id] = record
        self.event(state, "freeze", record=record, previous=old)
        return record

    def thaw(self, state, args):
        a = read_json(args.approval)
        required = ("approval_id", "freeze_id", "revision", "baseline_commit", "user_id", "actor_id",
                    "role_id", "task_id", "paths", "approved_by", "approved_at", "expires_at",
                    "human_evidence", "reason_kind", "reason", "impact", "regression", "rollback")
        require(all(k in a and a[k] not in (None, "", [], "***") for k in required), "人工批准记录缺少必填字段")
        for key in ("approval_id", "user_id", "actor_id", "task_id", "approved_by"):
            ident(a[key])
        require(a["role_id"] in self.policy["roles"], "批准的目标角色不存在")
        require(a["reason_kind"] in ("interface_interference", "functional_interference"),
                "解冻必须有明确接口或功能干涉依据")
        approved = dt.datetime.fromisoformat(a["approved_at"])
        expiry = dt.datetime.fromisoformat(a["expires_at"])
        require(approved.tzinfo is not None and expiry.tzinfo is not None and approved <= utcnow() < expiry,
                "人工批准尚未生效或已经到期（时间必须含时区）")
        freeze = state["freezes"].get(a["freeze_id"])
        require(freeze is not None, "冻结记录不存在")
        if freeze["status"] == "CHANGE_APPROVED":
            require(a.get("supersedes") == freeze["approval"]["approval_id"],
                    "续批必须明确 supersedes 原批准编号")
        require(a["revision"] == freeze["revision"] and a["baseline_commit"] == freeze["commit"],
                "批准绑定的冻结版本已变化")
        require(a["approval_id"] not in state["used_approvals"], "人工批准记录不可重放")
        require(isinstance(a["paths"], list) and a["paths"], "批准范围不能为空")
        for path in a["paths"]:
            self.path(path)
            require(any(contains(p, path) for p in freeze["paths"]), "批准范围超出冻结范围")
        for lane in state["lanes"].values():
            if any(overlap(p, q) for p in lane["paths"] for q in freeze["paths"]):
                require(freeze["status"] == "CHANGE_APPROVED" and
                        all(a[k] == lane[k] for k in ("user_id", "actor_id", "role_id", "task_id")),
                        "原写锁尚未释放；先保全工作并释放或以人工批准 recover 接管")
        freeze["approval"] = a
        freeze["status"] = "CHANGE_APPROVED"
        state["used_approvals"].append(a["approval_id"])
        self.event(state, "thaw", approval=a, approval_hash=digest(a))
        return freeze

    def recover(self, state, args):
        a = read_json(args.approval)
        require(all(a.get(k) for k in ("lane_id", "lane_hash", "approved_by", "human_evidence",
                                       "preserved_work", "process_stopped_evidence")),
                "接管须有真人证据、原工作保全记录和原进程已停止的证据")
        lane = state["lanes"].get(a["lane_id"])
        require(lane is not None and digest(lane) == a["lane_hash"], "泳道已变化，必须重新确认接管")
        del state["lanes"][a["lane_id"]]
        self.event(state, "human_recover", lane=lane, approval=a)
        return {"released_lane": a["lane_id"], "notice": "冻结继续有效；接手须另行获得解冻授权"}

    def changed(self, base=None, staged=False):
        commands = [("diff", "--cached", "--name-only", "--no-renames", "-z")]
        if not staged:
            commands += [("diff", "HEAD", "--name-only", "--no-renames", "-z"),
                         ("ls-files", "--others", "--exclude-standard", "-z")]
        if base:
            # 检查精确双端树差异；不使用可能漏掉目标侧变更的三点比较。
            commands.append(("diff", base, "HEAD", "--name-only", "--no-renames", "-z"))
        result = set()
        for command in commands:
            result.update(x.decode() for x in self.git(*command, binary=True).split(b"\0") if x)
        return sorted(result)

    def check(self, state, args):
        lane = self.owned(state, args.lane, args.actor)
        changes = self.changed(args.base, args.staged)
        for path in changes:
            require(any(contains(scope, path) for scope in lane["paths"]), "改动越出泳道范围：" + path)
            # 已由本泳道冻结的提交允许交接，但索引与工作文件仍须等于冻结内容。
            freezes = [f for f in state["freezes"].values() if any(contains(p, path) for p in f["paths"])]
            unchanged = False
            if freezes:
                unchanged = all(self.manifest(f["paths"]) == f["manifest"] and
                                not self.git("status", "--porcelain", "--untracked-files=all", "--", *f["paths"])
                                for f in freezes)
            if not unchanged:
                self.permitted(state, lane, path)
        if args.message:
            prefix = "[{}][{}][{}] ".format(lane["role_id"], lane["task_id"], lane["user_id"])
            require(args.message.startswith(prefix) and re.fullmatch(
                r"(feat|fix|docs|test|chore|refactor|perf|build|ci): .+", args.message[len(prefix):]),
                "提交信息须为 [ROLE][TASK][USER] type: 中文说明")
        return {"checked_paths": changes, "head": self.head(), "lane": args.lane}

    def run(self, args):
        with self.transaction(initializing=args.command == "init") as state:
            if args.command == "init":
                ident(args.project)
                state.update(schema=1, project_id=args.project, policy_hash=digest(self.policy),
                             lanes={}, freezes={}, used_approvals=[], events=[])
                if args.snapshot:
                    imported = read_json(args.snapshot)
                    require(imported["project_id"] == args.project and imported["policy_hash"] == digest(self.policy),
                            "快照项目或策略不匹配")
                    require(not imported["lanes"] and all(f["status"] == "FROZEN" for f in imported["freezes"].values()),
                            "只能导入无活跃泳道、无待完成解冻的已审核快照")
                    state.update(imported)
                self.event(state, "init")
                return {"project_id": args.project, "notice": "仅本协调中心可见；多机器必须指向同一受控协调目录"}
            if args.command == "claim":
                return self.claim(state, args)
            if args.command == "freeze":
                return self.freeze(state, args)
            if args.command == "thaw":
                return self.thaw(state, args)
            if args.command == "recover":
                return self.recover(state, args)
            if args.command == "check":
                return self.check(state, args)
            if args.command in ("heartbeat", "release"):
                lane = self.owned(state, args.lane, args.actor)
                if args.command == "heartbeat":
                    lane["heartbeat"] = stamp()
                else:
                    require(not any(f.get("approval", {}).get("actor_id") == args.actor and
                                    f["status"] == "CHANGE_APPROVED" for f in state["freezes"].values()),
                            "尚有已批准变更未重新冻结，禁止静默释放")
                    changed = self.changed(lane["starting_head"])
                    require(not self.git("status", "--porcelain", "--untracked-files=all"),
                            "泳道有未提交工作，先保全、提交与冻结，不能用释放隐藏未交付成果")
                    for path in changed:
                        require(any(f["status"] == "FROZEN" and
                                    any(contains(p, path) for p in f["paths"]) and
                                    self.manifest(f["paths"]) == f["manifest"]
                                    for f in state["freezes"].values()),
                                "本泳道产出尚未冻结：" + path)
                    del state["lanes"][args.lane]
                self.event(state, args.command, lane_id=args.lane)
                return {"lane": args.lane, "action": args.command}
            if args.command == "snapshot":
                lane = self.owned(state, args.lane, args.actor)
                output = self.path(args.output)
                require(any(contains(p, output) for p in lane["paths"]), "快照输出必须属于当前泳道")
                self.permitted(state, lane, output)
                require(output.startswith("z-readme/") and re.match(r"\d{12}_", Path(output).name),
                        "快照必须写入 z-readme 并带分钟时间戳")
                require(not (self.root / output).exists(), "快照只能新建，不覆盖历史记录")
                (self.root / output).parent.mkdir(parents=True, exist_ok=True)
                exported = json.loads(json.dumps(state))
                # 导出动作的纯文档泳道不应让已静止的协调中心永远无法迁移。
                if all(p.startswith("z-readme/") for p in lane["paths"]):
                    del exported["lanes"][args.lane]
                write_json(self.root / output, exported)
                return {"snapshot": output, "sha256": digest(exported)}
            return state


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".")
    p.add_argument("--coord-dir", help="由团队统一配置的受控共享目录，不能用各自克隆目录代替")
    sub = p.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("--project", required=True)
    init.add_argument("--snapshot")
    claim = sub.add_parser("claim")
    claim.add_argument("--user", required=True)
    claim.add_argument("--role", required=True)
    claim.add_argument("--task", required=True)
    claim.add_argument("--paths", nargs="+", required=True)
    claim.add_argument("--resource", action="append", default=[])
    freeze = sub.add_parser("freeze")
    freeze.add_argument("--freeze-id", required=True)
    freeze.add_argument("--paths", nargs="+", required=True)
    freeze.add_argument("--evidence", required=True, help="自检或交付证据引用；不代表 STABLE 验收")
    thaw = sub.add_parser("thaw")
    thaw.add_argument("--approval", required=True, help="已获真人批准的结构化记录；工具不证明真人身份")
    recover = sub.add_parser("recover")
    recover.add_argument("--approval", required=True)
    check = sub.add_parser("check")
    check.add_argument("--base", help="精确基线提交 SHA")
    check.add_argument("--staged", action="store_true")
    check.add_argument("--message")
    heart = sub.add_parser("heartbeat")
    release = sub.add_parser("release")
    snapshot = sub.add_parser("snapshot")
    snapshot.add_argument("--output", required=True)
    for cmd in (claim, freeze, check, heart, release, snapshot):
        cmd.add_argument("--lane", required=True)
        cmd.add_argument("--actor", required=True)
    sub.add_parser("status")
    return p


def main():
    args = parser().parse_args()
    try:
        result = Guard(args.root, args.coord_dir).run(args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (GuardError, OSError, ValueError, KeyError, TypeError) as e:
        print("拒绝操作：" + str(e), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
