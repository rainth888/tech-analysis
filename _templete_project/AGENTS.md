# AGENTS.md

This file is the universal operating guide for coding agents working in this repository template. It outlines core behaviors, folder structure conventions, execution safety rules, and project logging constraints to ensure consistency and prevent high-risk errors.

## Universal Project Layout

To maintain directory cleanliness, follow these folder conventions strictly. Do NOT place temporary scripts, random markdown files, or untracked resources directly in the root directory.

- `z-docs/`: General design specifications, architecture documentation, API definitions, and protocol standards.
- `z-logs/`: Iterative logs, change tracking, and modification records. Create records only under the opt-in rules in Version Logging.
- `z-readme/`: Critical step-by-step technical guides and how-tos. Written in Chinese for team reference.
- `z-prototype/`: Architectural prototypes, wireframes, flowcharts, or early draft implementations.
- `z-resource/`: Static assets, reference media (images/videos), binaries, and external library distributions.
- `z-scripts/`: Automation scripts, development helper utilities, startup scripts, and deploy recipes. All newly created scripts must go here.
- `z-temps/`: Sandbox testing files, temporary logs, or short-lived environment outputs.

---

## Hard Constraints (Must Follow)

1. **VERSION LOGGING — USER OPT-IN ONLY**: Routine code implementation, fixes, refactoring, configuration changes, builds, and ordinary feature improvements MUST NOT automatically create modification records or technical documentation in `z-logs/`, `z-readme/`, or elsewhere. Only when a change is a major architectural change, a major milestone, or a large-scale completion may a record be useful; before creating it, explicitly ask the user whether they want a modification-record technical document. Create the document only after the user confirms, unless the user already explicitly requested that document. Keep the question and any resulting document concise to minimize token usage. If confirmed, store a detailed verification record in `z-logs/` using `YYYYMMDDHHMM_FeatureName_TestResult.md` and include the verification date and time.
2. **CHINESE DOCUMENTATION**: Critical step-by-step technical guides belong in `z-readme/` and must be written in Chinese, but do not create them automatically for ordinary code work. Create one only when the user explicitly requests it or confirms it after the major-change prompt required above.
3. **MARKDOWN TABLE FORMAT**: Every table in your generated or modified markdown files MUST be column-aligned. Each row in the same table must have the same visible column width. Pad space before and after the `|` separators so that they align vertically in raw text view.
4. **SCRIPT PLACEMENT**: Any newly created shell scripts, PowerShell scripts, or automation runners must be stored in the `z-scripts/` directory.
5. **UNSURE CRITICAL OPERATIONS**: If you are unsure whether an operation is key, critical, or risky, stop and ask the user for confirmation before proceeding.
6. **GIT VERSION CONTROL**: **Never** execute `git reset`, `git checkout -- <file>`, `git revert`, or any form of code rollback without explicit prior user approval. If rollback is necessary, explain the reasons to the user first.
7. **PLANNING MODE**: Ignore/bypass Planning Mode. Do not write implementation plans (`implementation_plan.md`) or ask for user confirmation unless explicitly requested or working on massive architecture overhauls. Directly execute code analysis and modifications.
8. **PAUSE FOR PHYSICAL/HARDWARE VERIFICATION**: Whenever verification requires checking display quality, touch feedback, audio output, or physical/hardware interactions, you must pause immediately, explain the current state to the user, and wait for their physical verification feedback before proceeding.
9. **DOCUMENT NAMING**: All generated documents (excluding code source files and execution scripts) MUST prepend a timestamp formatted as `YYYYMMDDHHMM` (accurate to the minute, e.g., `202606171446_FileName.md`) to their filenames for sorting purposes.

## Stable Main Branch Protection (Mandatory)

- `main` is the stable release baseline only. Never directly modify application code, configuration, scripts, or resources on `main`, and never use `main` for new feature development, fixes, refactoring, tuning, experiments, or iterative validation.
- Before implementing any feature, fix, or improvement, create and switch to a dedicated branch from the latest `main`, such as `feature/<name>` or `fix/<name>`. Perform all edits, builds, debugging, deployment tests, and functional or hardware acceptance on that branch.
- Merge into `main` only after the branch has completed all required verification, hardware-dependent behavior has been physically accepted by the user when applicable, and the user has explicitly confirmed that the exact branch version is stable and approved for merging.
- The merge must preserve the exact verified commit and resulting file tree. Do not add unverified cleanup or incidental changes during or after the merge. If a problem is found after merging, create a new fix branch, validate it, and merge it only after acceptance.
- If the current branch is `main` and the user requests an implementation or code change, create and switch to a dedicated branch before modifying files. On `main`, only read-only inspection, stable release build/deployment/regression checks, and merging already accepted branches are allowed.

---

## Command Execution Safety

### ⚠️ Global Exception
- **Any command containing `rm -rf` MUST always require user confirmation**, regardless of any other auto-run rules below.

### SafeToAutoRun = true (No confirmation needed)
- **ALL commands** on Windows (PowerShell/CMD) and WSL (Ubuntu) are auto-allowed, **EXCEPT** the blocked commands listed below.
- This includes non-destructive operations such as local workspace searches (`grep`), code compilation via local Makefiles (`make`), log retrieval, safe file transfers (`pscp`, `scp`), state checking (`git log`, `diff`, `ps`), and short timers (`Start-Sleep`).

### BLOCKED (Must Confirm)
- **Destructive filesystem operations**: `rm`, `del`, `Remove-Item`, `mv`, `move`, `ren`, `Rename-Item`.
- **System or disk mutations**: `format`, `fdisk`, `dd`, `mkfs`.
- **Database schema modifications**: `DROP DATABASE`, `DROP TABLE`, `truncate`.
- **System control and networking modifications**: `iptables -F`, `shutdown`, `reboot`, `poweroff`.
- **Process termination**: `kill -9`, `systemctl stop`.
- **Risky Git operations**: `git push --force`, `git reset --hard`.
- **Production data mutations**: Any mutations touching production environments, live databases, or deployment streams.
- **Complex target compilations**: Android native builds (e.g. `gradlew.bat`/`gradlew assembleDebug`), Qt builds (e.g. `qmake`, `mingw32-make`, `nmake`).

---

## 任务状态跟踪执行模式 (STATE.md)

`STATE.md`（同目录）用于保障**跨会话任务连续性**。

### 强制执行规则

#### 1. 会话启动时
- **有明确任务指令**：读取 `STATE.md` → 写入当前任务（`🔄 IN_PROGRESS`）→ 记录会话ID/开始时间 → 执行
- **无明确任务指令**：读取 `STATE.md` →
  - `🔄 IN_PROGRESS` → 接管继续
  - `⏳ NEXT` 有排队 → 递补为当前任务并执行
  - `⏸️ IDLE` → 向 USER 汇报并请求指令

#### 2. 执行过程中
- 关键里程碑时更新「当前进度」
- 阻塞/暂停时标记 `❌ BLOCKED` / `⏸️ PAUSED` 并记录原因
- 关键环境状态变化时，同步更新「上下文快照」

#### 3. 任务完成时
- `⏳ NEXT` 递补为 `🔄 IN_PROGRESS`
- 回查任务源文档确定下一个 `⏳ NEXT`（不凭记忆猜测）
- 任务源全部完成 → `⏸️ IDLE`

#### 4. 状态流转
```
⏸️ IDLE → 🔄 IN_PROGRESS → ✅ COMPLETED → ⏳ NEXT 递补 (或 → ⏸️ IDLE)
                           → ❌ BLOCKED  → 条件解除后恢复
                           → ⏸️ PAUSED   → USER 反馈后恢复
```


