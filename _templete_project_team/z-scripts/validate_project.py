#!/usr/bin/env python3
"""validate_project.py —— 团队项目模板规范校验与 Markdown 表格对齐工具（工具无关）

用法：
  py -3.11 z-scripts/validate_project.py             # 仅校验项目结构、核心文件与代码块闭合
  py -3.11 z-scripts/validate_project.py --align --files readme.md  # 只格式化显式领取的文件
"""
import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_PATHS = [
    "AGENTS.md",
    "_STATE.md",
    "_TASKLISTS.md",
    "_STATE_HISTORY.md",
    "_CHECKLISTS.md",
    ".agents/parallel/policy.json",
    "z-scripts/team_guard.py",
    "z-scripts/test_team_guard.py",
    "z-readme/08_冻结并行开发与Git合并操作手册.md",
    ".agents/parallel/lanes/TEMPLATE.md",
    ".agents/roles/PM.md",
    ".agents/roles/PO.md",
    ".agents/roles/AR.md",
    ".agents/roles/BE.md",
    ".agents/roles/FE.md",
    ".agents/roles/QA.md",
    ".agents/roles/OPS.md",
    ".agents/roles/AI.md",
    ".agents/roles/REVIEWER-ARCH.md",
    ".agents/roles/ACCEPTOR-BIZ.md",
    ".agents/roles/CHECKER-QA.md",
    ".agents/roles/CHECKER-OPS.md",
    ".agents/workflows/inbox.md",
    ".agents/workflows/handoff.md",
    ".agents/workflows/ask.md",
    ".agents/workflows/answer.md",
    ".agents/workflows/review.md",
    ".agents/workflows/defect.md",
    ".agents/workflows/retest.md",
    ".agents/workflows/gate.md",
    ".agents/workflows/deployed.md",
    ".agents/workflows/ready.md",
    ".agents/workflows/accept.md",
    ".agents/workflows/cr.md",
    ".agents/workflows/wrapup.md",
    "z-readme/11_开发计划模板.md",
    "z-readme/12_进度看板模板.md",
    "z-readme/10_需求索引模板.md",
    "z-readme/collab/00_团队成员与职责.md",
    "z-readme/collab/01_文件归属与评审矩阵.md",
    "z-readme/collab/02_协作看板模板.md",
    "z-readme/collab/03_风险登记模板.md",
    "z-readme/collab/handoff/00_成果冻结交接模板.md",
    "z-readme/collab/issues/00_问题与缺陷模板.md",
    "z-readme/collab/reviews/00_独立评审模板.md",
    "z-readme/collab/changes/00_变更与人工解冻申请模板.md",
    "z-readme/00_团队项目模板使用与全员就位指南.md",
    "z-readme/01_大项目全技术规范与架构文档内容规范.md",
    "z-readme/02_各岗位角色项目文件夹与工作空间规范.md",
    "z-readme/03_项目沟通任务流转与接口对接规范.md",
    "z-readme/04_跨AI开发工具通用适配指南.md",
    "z-readme/05_分阶段分角色提示词总手册.md",
    "z-readme/06_各岗位角色提示词实操演练全流程手册.md",
]


def disp_width(s: str) -> int:
    w = 0
    for ch in s:
        if unicodedata.combining(ch):
            continue
        eaw = unicodedata.east_asian_width(ch)
        w += 2 if eaw in ("W", "F") else 1
    return w


def pad_cell(s: str, target: int) -> str:
    pad = max(0, target - disp_width(s))
    return s + (" " * pad)


def is_sep_row(cells: list[str]) -> bool:
    if not cells:
        return False
    for c in cells:
        t = c.strip()
        if not t or not all(ch in "-:" for ch in t) or "-" not in t:
            return False
    return True


def split_row(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    out, cur, esc = [], [], False
    for ch in s:
        if esc:
            cur.append(ch)
            esc = False
        elif ch == "\\":
            cur.append(ch)
            esc = True
        elif ch == "|":
            out.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    out.append("".join(cur).strip())
    return out


def format_table(block: list[str]) -> list[str]:
    rows = [split_row(l) for l in block]
    if len(rows) < 2 or not is_sep_row(rows[1]):
        return block
    ncols = max(len(r) for r in rows)
    for r in rows:
        while len(r) < ncols:
            r.append("")
    widths = [3] * ncols
    for idx, r in enumerate(rows):
        if idx == 1 or is_sep_row(r):
            continue
        for c_i, cell in enumerate(r):
            widths[c_i] = max(widths[c_i], disp_width(cell))
    out = []
    for idx, r in enumerate(rows):
        if idx == 1 or is_sep_row(r):
            sep_cells = []
            for c_i, cell in enumerate(r):
                t = cell.strip()
                w = widths[c_i]
                if t.startswith(":") and t.endswith(":"):
                    sep_cells.append(":" + "-" * max(1, w - 2) + ":")
                elif t.startswith(":"):
                    sep_cells.append(":" + "-" * max(1, w - 1))
                elif t.endswith(":"):
                    sep_cells.append("-" * max(1, w - 1) + ":")
                else:
                    sep_cells.append("-" * w)
            out.append("| " + " | ".join(sep_cells) + " |")
        else:
            padded = [pad_cell(r[c_i], widths[c_i]) for c_i in range(ncols)]
            out.append("| " + " | ".join(padded) + " |")
    return out


def align_tables(text: str) -> str:
    lines = text.replace("\r\n", "\n").split("\n")
    out, buf, in_fence = [], [], False
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("```"):
            if buf:
                out.extend(format_table(buf))
                buf = []
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence and stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2:
            buf.append(line)
        else:
            if buf:
                out.extend(format_table(buf))
                buf = []
            out.append(line)
    if buf:
        out.extend(format_table(buf))
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--align", action="store_true")
    parser.add_argument("--files", nargs="+")
    args = parser.parse_args()
    if args.align and not args.files:
        parser.error("--align 必须配合 --files 显式列出已领取文件，禁止全仓格式化")
    selected = set()
    for value in args.files or []:
        path = ROOT / value
        if (path.is_symlink() or not path.is_file() or path.suffix != ".md" or
                not path.resolve().is_relative_to(ROOT.resolve()) or
                any(p.is_symlink() for p in path.parents if p != ROOT.parent)):
            parser.error("文件必须是模板内的普通 Markdown 文件：" + value)
        selected.add(path.resolve())
    errors = []
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            errors.append(f"MISSING required file: {rel}")

    for path in (ROOT / "z-readme").rglob("*"):
        if path.is_file() and re.match(r"(?:19|20)\d{6}(?:\d{4}(?:\d{2})?)?[_-]", path.name):
            errors.append(f"DATED filename (use an ordered or unique identifier): {path.relative_to(ROOT)}")

    md_files = sorted(p for p in ROOT.rglob("*.md") if not set(p.parts) &
                      {".git", "node_modules", "z-temps", ".venv", "leases"})
    aligned_count = 0
    for md in md_files:
        raw = md.read_text(encoding="utf-8")
        if args.align and md.resolve() in selected:
            new_text = align_tables(raw)
            if new_text != raw.replace("\r\n", "\n"):
                md.write_text(new_text, encoding="utf-8")
                aligned_count += 1
                raw = new_text
        fences = sum(1 for l in raw.splitlines() if l.lstrip().startswith("```"))
        if fences % 2 != 0:
            errors.append(f"UNCLOSED code fence ({fences}) in {md.relative_to(ROOT)}")
        for ref in re.findall(r'`(z-readme/(?:[^`\n]*/)?\d{2}_[^`\n]+\.md)`', raw):
            if not (ROOT / ref).exists():
                errors.append(f"MISSING numbered reference: {ref} in {md.relative_to(ROOT)}")

    try:
        policy = json.loads((ROOT / ".agents/parallel/policy.json").read_text(encoding="utf-8"))
        seen = set()
        for rule in policy["paths"]:
            if rule["path"].casefold() in seen or not set(rule["roles"]) <= set(policy["roles"]):
                errors.append("INVALID or DUPLICATE policy rule: " + rule["path"])
            seen.add(rule["path"].casefold())
    except (OSError, ValueError, KeyError, TypeError) as e:
        errors.append("INVALID policy: " + str(e))

    print(f"[validate_project] Checked {len(md_files)} markdown files (aligned {aligned_count}).")
    if errors:
        for e in errors:
            print("  ERROR:", e)
        return 1
    print("[validate_project] ALL CHECKS PASSED.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
