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

## Multi-Environment Parallel Work (Same Worktree / Same Branch)

This template permits multiple independent model environments to work in the same project folder and on the same branch when the user has determined that the tasks are unrelated. Parallel work uses `optimistic-disjoint-files`: concurrent reads are allowed, while concurrent writes require declared, non-overlapping ownership.

### Parallel configuration

- Configuration: `.agents/parallel/config.yaml`.
- Lane records: `.agents/parallel/lanes/<task-id>-<slug>.md`.
- Runtime leases: `.agents/parallel/leases/<resource>.lock/`.
- Every writing environment must declare a unique `actor_id`, one `task_id`, exact `owned_paths`, required resources, observed branch/HEAD, stable-function scope, heartbeat, verification and rollback notes.
- A user statement that tasks are independent authorizes parallel execution but does not authorize stable-function changes, destructive operations, release actions or overlapping writes.

### Ownership and failure behavior

- Read access does not require ownership. Write access does.
- Active lanes must not own the same file, overlapping directory, generated-output path or stable-function code range.
- If an overlap is discovered, stop writing that scope and report the conflict. Never overwrite, revert, discard or auto-merge another lane's work.
- Acquire a shared-resource lease using atomic directory creation equivalent to `mkdir .agents/parallel/leases/<resource>.lock`; creation failure means the resource is already owned.
- Store `owner.md` with `actor_id`, `task_id`, branch, acquisition time and heartbeat. Release only leases owned by the current actor.
- A stale-looking lease is never removed solely by age. Inspect its lane and operation first; if owner exit cannot be proven, fail closed and ask the user.

### Shared metadata and task lanes

- `_STATE.md` is a compact parallel dashboard, not a single-task mutex. Multiple unrelated lanes may be active.
- `_TASKLISTS.md`, `_CHECKLISTS.md`, `_STATE.md`, `_STATE_HISTORY.md`, `AGENTS.md` and `.agents/parallel/config.yaml` require the `task-metadata` lease and a fresh reread before editing.
- Detailed live progress belongs in each lane record. Shared files receive concise milestones, approvals, acceptance results and archive summaries.
- A new user task becomes highest priority only in the receiving environment unless the user explicitly pauses or replaces another named lane. Never evict unrelated active lanes automatically.
- One environment may not pause, complete, reassign or apply user acceptance to another lane's task.

### Git safety in a shared worktree

- Working-file edits and read-only Git commands may run in parallel only inside disjoint `owned_paths`.
- Acquire the global `git-index` lease before `git add`, commit, amend, merge, rebase, cherry-pick, tag, branch switch, pull or push.
- Record starting `HEAD`; immediately before staging, reread current `HEAD`, status and changed paths. If another lane committed, ensure intervening commits do not touch this lane's paths.
- Stage explicit owned paths only: `git add -- <paths>`. In parallel mode, `git add -A`, `git add .`, `git commit -a`, shared stash and pathless bulk staging are prohibited.
- `git diff --cached --name-only` must be a subset of the lane's ownership. If the index contains another lane's paths, do not unstage or alter them; coordinate with its owner.
- One commit contains one lane only and should include the task ID. Never use reset, restore/checkout, clean, revert, rebase, amend or stash to resolve parallel interference.
- If tasks must edit the same file or need divergent history, serialize them or use separate worktrees/branches.

### Builds, outputs and external resources

- Parallel builds require distinct build/output directories. Shared build trees require a build lease.
- Packaging uses lane-specific output paths; canonical release output requires `image-output`.
- Deployment, process restart, reboot, power cycle, serial capture, firmware/ENV writes, flashing and OTA installation require `target-device` plus the relevant resource lease.
- Hardware-verification pauses are per lane and do not block unrelated lanes.

## Hard Constraints (Must Follow)

1. **VERSION LOGGING — USER OPT-IN ONLY**: Routine code implementation, fixes, refactoring, configuration changes, builds, and ordinary feature improvements MUST NOT automatically create modification records or technical documentation in `z-logs/`, `z-readme/`, or elsewhere. Only when a change is a major architectural change, a major milestone, or a large-scale completion may a record be useful; before creating it, explicitly ask the user whether they want a modification-record technical document. Create the document only after the user confirms, unless the user already explicitly requested that document. Keep the question and any resulting document concise to minimize token usage. If confirmed, store a detailed verification record in `z-logs/` using `YYYYMMDDHHMM_FeatureName_TestResult.md` and include the verification date and time.
2. **CHINESE DOCUMENTATION**: Critical step-by-step technical guides belong in `z-readme/` and must be written in Chinese, but do not create them automatically for ordinary code work. Create one only when the user explicitly requests it or confirms it after the major-change prompt required above.
3. **MARKDOWN TABLE FORMAT**: Every table in your generated or modified markdown files MUST be column-aligned. Each row in the same table must have the same visible column width. Pad space before and after the `|` separators so that they align vertically in raw text view.
4. **SCRIPT PLACEMENT**: Any newly created shell scripts, PowerShell scripts, or automation runners must be stored in the `z-scripts/` directory.
5. **UNSURE CRITICAL OPERATIONS**: If you are unsure whether an operation is key, critical, or risky, stop and ask the user for confirmation before proceeding.
6. **GIT VERSION CONTROL**: **Never** execute `git reset`, `git checkout -- <file>`, `git revert`, or any form of code rollback without explicit prior user approval. If rollback is necessary, explain the reasons to the user first.
7. **PLANNING MODE**: Ignore/bypass Planning Mode. Do not write implementation plans (`implementation_plan.md`) or ask for user confirmation unless explicitly requested or working on massive architecture overhauls. Directly execute code analysis and modifications.
8. **PAUSE FOR PHYSICAL/HARDWARE VERIFICATION**: Whenever verification requires checking display quality, touch feedback, audio output, or physical/hardware interactions, you must pause immediately, explain the current state to the user, and wait for their physical verification feedback before proceeding.
9. **DOCUMENT NAMING**: All generated documents (excluding code source files and execution scripts) MUST prepend a timestamp formatted as `YYYYMMDDHHMM` (accurate to the minute, e.g., `202606171446_FileName.md`) to their filenames for sorting purposes. The four fixed root control files `_STATE.md`, `_TASKLISTS.md`, `_STATE_HISTORY.md`, and `_CHECKLISTS.md` are explicit exceptions and must keep these exact names.

## Stable Main Branch Protection (Mandatory)

- Before any Git operation, run `git rev-parse --show-toplevel` and inspect the current branch to identify the actual project repository and its stable primary branch. When nested repositories exist, never mistake a parent repository's `master`, `main`, or other branch for the current project's stable branch.
- `main` is the stable release baseline only. Never directly modify application code, configuration, scripts, or resources on `main`, and never use `main` for new feature development, fixes, refactoring, tuning, experiments, or iterative validation.
- Before implementing any feature, fix, or improvement, create and switch to a dedicated branch from the latest `main`, such as `feature/<name>` or `fix/<name>`. Perform all edits, builds, debugging, deployment tests, and functional or hardware acceptance on that branch.
- Merge into `main` only after the branch has completed all required verification, hardware-dependent behavior has been physically accepted by the user when applicable, and the user has explicitly confirmed that the exact branch version is stable and approved for merging.
- Never merge a branch while verification has failed, remains incomplete, or is still waiting for user hardware acceptance.
- The merge must preserve the exact verified commit and resulting file tree. Do not add unverified cleanup or incidental changes during or after the merge. If a problem is found after merging, create a new fix branch, validate it, and merge it only after acceptance.
- If the current branch is `main` and the user requests an implementation or code change, create and switch to a dedicated branch before modifying files. On `main`, only read-only inspection, stable release build/deployment/regression checks, and merging already accepted branches are allowed.

## Stable Function Freeze and Feature Checklist (Mandatory)

- `_CHECKLISTS.md` is the project's authoritative feature inventory. Before any feature, Bug, refactoring, tuning, or adaptation task, read it and identify the target function, code scope, status, and cross-feature effects.
- Never modify, weaken, remove, or break an existing `🔒 STABLE` function while implementing a new requirement or Bug fix. Prefer isolated additions and the smallest possible change, then regress every listed cross-affected function.
- A function may become `🔒 STABLE` only after a developer or the user has tested it and explicitly declared it stable. Code presence, successful compilation, automated tests, or Agent judgment alone are insufficient.
- Once marked `🔒 STABLE`, the registered code scope is frozen. If a change is genuinely necessary, stop before editing and clearly report the function, exact code scope, reason, affected functions, regression plan, and rollback plan.
- Modify stable code only after explicit user approval. First change its checklist status to `⚠️ CHANGE_APPROVED` or `🔄 REVALIDATING`, record the approval and scope, then perform the approved change.
- After modification, regress the original stable function and all cross-affected functions. Restore `🔒 STABLE` only after the developer or user explicitly accepts the new result.
- Keep `_CHECKLISTS.md` synchronized whenever a function is added, changed, tested, accepted, disabled, or superseded.

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

## 任务状态跟踪与并行领取模式

根目录使用四个共享控制文件和独立 lane 文件：

- `_STATE.md`：紧凑并行看板，可显示多个活跃 lane。
- `_TASKLISTS.md`：保存全部任务、优先级、依赖、完成标准和 lane 归属。
- `_STATE_HISTORY.md`：追加保存完成或取消任务。
- `_CHECKLISTS.md`：保存稳定功能和交叉影响。
- `.agents/parallel/lanes/`：保存各环境详细实时进度、文件所有权和资源需求。

### 强制执行规则

#### 1. 任务来源与并行语义

- 任务只能由用户发布，或为完成用户任务而拆解的必要子任务。
- 用户判定任务互不相关时，多个 lane 可在同一目录和同一分支上同时处于 `🔄 IN_PROGRESS`。
- 新任务只在接收它的 lane 中成为最高优先级；未经用户明确指定，不得暂停或替换其他不相关 lane。
- 并行执行不扩大稳定功能、破坏性操作、发布、硬件验收或生产变更授权。

#### 2. 会话启动与 lane 领取

- 每次会话先读取 `AGENTS.md`、`.agents/parallel/config.yaml`、`_STATE.md`、`_TASKLISTS.md`、`_CHECKLISTS.md` 和活跃 lane 摘要。
- 有新任务时，先获取 `task-metadata` 租约，登记任务并创建唯一 lane。
- 声明 `actor_id`、`task_id`、分支/HEAD、`owned_paths`、所需资源、稳定范围、心跳、验证和回退。
- 领取前比较活跃 lane：文件和资源无重叠可并行；有重叠则失败关闭。
- 无新任务时，只自动领取依赖满足、未被领取且不冲突的最高优先级任务。

#### 3. 执行与共享文件

- 每个环境只修改自己 `owned_paths`。发现重叠后立即停止写入，保留现状并报告，不得覆盖、回退或自动合并。
- 详细实时进度写 lane 文件；共享状态文件只写必要里程碑。
- 修改 `_STATE.md`、`_TASKLISTS.md`、`_CHECKLISTS.md`、`_STATE_HISTORY.md`、`AGENTS.md` 或并行配置前，必须获取 `task-metadata` 租约并立即重读。
- 某 lane 等待用户或硬件时，不阻塞其他无关 lane。

#### 4. Git、构建与外部资源

- Git 写操作获取 `git-index` 租约，仅显式暂存自有路径，一次提交一个 lane，并复核期间 HEAD 变化。
- 禁止 `git add -A`、`git add .`、`git commit -a`、共享 stash 和无路径批量暂存。索引中出现他人路径时不得擅自取消暂存。
- 构建/输出目录重叠时获取对应租约并串行；只有独立输出目录允许并行。
- 部署、重启、断上电、串口采集、固件/环境写入、烧录和OTA安装必须按 `target-device` 及对应子资源租约串行。

#### 5. 完成与归档

- 内部验证完成后只能标记 `🧪 AWAITING_USER_CONFIRMATION`；只有用户明确回复通过、稳定、完成或验收通过后才标记 `✅ COMPLETED`。
- 新任务不代表旧 lane 验收通过，也不自动暂停旧 lane。
- 用户反馈失败时，只恢复对应 lane 为 `🔄 IN_PROGRESS`。
- 验收通过后获取 `task-metadata` 租约，同步共享状态与历史，将 lane 标记完成并释放其租约。

#### 6. 状态流转

```text
⏳ TODO → lane领取 → 🔄 IN_PROGRESS → 🧪 AWAITING_USER_CONFIRMATION
                         ├→ 用户明确通过 → ✅ COMPLETED → 归档
                         ├→ 用户反馈失败 → 🔄 IN_PROGRESS
                         ├→ 文件/资源冲突 → ❌ BLOCKED（仅该lane/范围）
                         ├→ ⏸️ PAUSED → 条件解除后恢复
                         └→ 🚫 CANCELLED → 归档

多个无重叠 lane 可同时处于 🔄 IN_PROGRESS。
```


