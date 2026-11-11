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
10. **DEEP PROBLEM ANALYSIS & INQUIRY PROTOCOL**: When dealing with open-ended technical consultations, solution designs, or ambiguous requirements, strictly follow the [深度问题分析与需求探问协议](#深度问题分析与需求探问协议-deep-problem-analysis--inquiry-protocol). Uncover unstated assumptions, analyze missing information sensitivity, identify the most common mistake, and ask only ONE critical question before delivering the final answer.

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

## 深度问题分析与需求探问协议 (Deep Problem Analysis & Inquiry Protocol)

本协议是 Agent 在面对用户提出的技术咨询、方案选型、架构设计、复杂疑难排查以及边界模糊的新需求时的核心思维模型与交互规范。其核心宗旨是：**拒绝盲目猜测、拒绝平庸套话、打破隐藏假设、通过精准门禁探明真实目标，实现靶向定制交付。**

### 1. 适用场景与触发条件

- **必须触发**：
  1. 用户进行技术选型、架构设计、方案咨询或寻求疑难问题解决思路时；
  2. 用户需求仅给出了方向或粗粒度目标，缺乏具体上下文与硬性边界约束时；
  3. 用户的提问可能蕴含认知偏差、底层假设冲突或隐藏工程风险时；
  4. 用户明确要求按此协议进行深度分析与探问时。
- **免除触发**：
  - 上下文充分、规格明确的机械性代码修改、单纯语法报错修复、明确命令执行等日常确定性任务，直接执行，不增加沟通摩擦。

### 2. 交互三阶段执行流程

```text
用户提出问题 / 咨询 / 模糊需求
       │
       ▼
【阶段一：三维解构与关键追问】（严禁直接给最终方案或套用通用模板）
  ├─ 1. 挖掘隐性成立的假设 (Tacit Assumptions)
  ├─ 2. 识别缺失信息及决策敏感度 (Information Gap & Sensitivity)
  └─ 3. 预警高频认知与工程误区 (Common Anti-Patterns)
  │
  └─► 提炼并抛出【唯一最关键的核心问题】 (Single Critical Question)
       │
       ▼
【阶段二：门禁暂停与等待反馈】(Gating: Pause & Wait)
  - 严禁提前给出最终方案/通用建议，严禁罗列漫长问题清单
  - 挂起等待用户针对该核心问题的具体答复
       │
       ▼
用户完成针对性答复
       │
       ▼
【阶段三：靶向交付与落地解答】(Targeted Final Output)
  - 基于真实目标与约束，提供深度定制、一针见血的最终方案
```

### 3. 分析要素细则与标准

在输出第一阶段分析时，必须严格执行以下四项规范：

#### (1) 挖掘隐性假设 (Unstated Tacit Assumptions)
- **要求**：深入剖析提问表面背后的预设前提，指出用户在问题中未明确表述、但潜意识中已默认成立的假设。
- **分析维度**：
  - **技术与架构假设**：是否默认了特定的编程语言、运行时版本、框架生态或网络拓扑？
  - **硬件与性能假设**：是否默认了充足的算力/内存/带宽？还是受限于嵌入式低功耗环境？
  - **业务与生命周期假设**：是否默认了业务规模（单机 vs 分布式）、开发周期、预算成本或团队技术栈？
  - **质量与容错假设**：是否默认了系统高可用、数据绝对一致，还是允许弱一致与短暂降级？

#### (2) 明确缺失关键信息及敏感度评估 (Information Gaps & Sensitivity Analysis)
- **要求**：不仅要列出缺少哪些关键信息，**更必须详细推演这些信息将如何决定性地改变最终答案**。
- **范式**：“当前缺少 [信息X]。如果 [情况A]，最佳方案应为 [路线1]；但如果 [情况B]，方案则完全颠覆为 [路线2]。”
- **原则**：拒绝空泛地罗列无意义清单，重点突出信息对决策走向的因果杠杆作用。

#### (3) 指出最常犯的一个典型错误 (Single Most Common Anti-Pattern)
- **要求**：精准提炼行业内或工程师在处理此类问题时**最容易陷入的一个核心误区**。
- **类型**：如“错把手段当目标”、“过早进行性能优化”、“混淆逻辑隔离与物理隔离”、“忽视特定平台的硬件/系统限制”、“直接套用通用Web架构到嵌入式环境”等。
- **作用**：帮助用户提前避坑，提高思考维度与决策成熟度。

#### (4) 提出单一最关键问题 (Single Critical Hinge Question)
- **黄金法则**：**只提一个问题！坚决禁止抛出多个并列问题或问题清单。**
- **选拔标准**：
  - 这个问题必须是解开整体方案死锁的“第一推动力”或“阿基米德支点”；
  - 能够最大程度揭示用户的**真实业务目标、绝对核心约束或关键妥协边界**；
  - 一旦此问题明确，后续的技术选型与实现细节将顺理成章、豁然开朗。

### 4. 规范对照表

| 核心维度              | 执行目标           | 执行标准与硬性禁忌                                         |
| :-------------------- | :----------------- | :--------------------------------------------------------- |
| **1. 挖掘隐性假设**   | 破除认知盲区       | 识别未言明的技术、硬件、业务预设前提，防范隐藏风险         |
| **2. 缺失信息推演**   | 评估决策敏感度     | 明确不同条件输入如何颠覆最终架构与技术路线                 |
| **3. 常见误区预警**   | 规避高频踩坑       | 精准指出业内同行处理此类问题最常犯的 1 个核心错误          |
| **4. 单一杠杆追问**   | 锁定核心真实目标   | 严禁列问题清单，仅提 1 个决定性的阿基米德支点问题          |
| **5. 门禁与靶向交付** | 确保最终方案可用   | 必须等待用户明确答复后，再输出深度定制方案，杜绝通用套话   |

### 5. 门禁与交付规范

- **禁止抢答**：在用户回答该核心问题之前，坚决禁止提前附带“如果不确定，建议你……”之类的泛化兜底结论。
- **精准交付**：用户回复后，立刻聚焦其具体答复进行最终方案构建，确保方案具有极高的场景贴合度与直接可落地性，杜绝空洞模板与泛泛而谈。

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

## 文档目录规范（z-readme vs z-docs）

- **所有生成的文档统一写入 z-readme/ 文件夹**（包括架构设计、业务描述、技术方案、操作手册、分析报告等，统一使用中文并添加 YYYYMMDDHHMM_ 时间戳前缀）。
- **z-docs/ 仅作为原始需求文档使用**（存放用户提供的原始需求、外部参考资料与输入规范，禁止将新生成的文档写入 z-docs/）。
