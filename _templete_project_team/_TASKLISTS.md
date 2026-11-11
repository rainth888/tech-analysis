# _TASKLISTS.md —— 团队项目任务总池

## 使用规则

1. 本文件登记用户直接发布的项目级任务，以及各阶段按规范拆解的角色任务（进入 P4 后，详细的 40+ 张迭代开发任务卡正文登记在 `docs/PLAN.md`，本文件保留阶段主任务与跨阶段专项任务）。
2. 每个子任务必须明确唯一责任角色（`PM | PO | AR | BE | FE | QA | OPS | AI`）、前置依赖、可写路径范围与可验证的完成标准。
3. 角色代理完成内部工作与自检后：
   - 需下游评审/测试的，发交接单（`HO-xxx`）并将子任务置为 `🧪 AWAITING_REVIEW` / `🧪 AWAITING_TEST`；
   - 需真人最终确认的，置为 `🧪 AWAITING_USER_CONFIRMATION`；
   - **只有收到下游正式签字及真人明确确认后**，PM 才可将任务标记为 `✅ COMPLETED` 并归档至 `_STATE_HISTORY.md`。
4. 修改本文件前必须先获取 `task-metadata` 租约并重新读取最新内容。

## 状态定义

| 状态                            | 含义                                                        |
| ------------------------------- | ----------------------------------------------------------- |
| `⏳ TODO`                       | 尚未领取                                                    |
| `⏳ NEXT`                       | 前置依赖已满足，列为下一待领任务                            |
| `🔄 IN_PROGRESS`                | 已被某角色泳道领取并正在执行                                |
| `🧪 AWAITING_REVIEW`            | 已提交评审请求，等待 AR / PO / FE / QA 等必审角色出具评审单 |
| `🧪 AWAITING_DEPLOY`            | 代码已合入，等待 OPS 部署到测试/预发布环境                  |
| `🧪 AWAITING_TEST`              | 已部署测试环境，等待 QA 执行独立测试或复测                  |
| `🧪 AWAITING_USER_CONFIRMATION` | 内部验证与角色交叉验证已完成，等待真人最终确认/签字         |
| `⏸️ PAUSED`                     | 等待外部条件、业务方澄清或硬件资源                          |
| `❌ BLOCKED`                    | 存在明确阻塞项（对应 `BOARD.md` 中阻塞单）                  |
| `✅ COMPLETED`                  | 完成标准全部满足并已归档至 `_STATE_HISTORY.md`              |
| `🚫 CANCELLED`                  | 经真人明确取消                                              |

## 阶段主任务池（新项目复制模板后的默认启动队列）

### T000 阶段 P0：项目启动与全员就位

- 状态：`⏳ NEXT`
- 优先级：`P0`
- 前置条件：真人已将原始需求规格说明书（SRS）放入 `z-docs/`。
- 范围：建立团队章程、目录与所有权、项目宪法初版，完成全角色需求通读笔记与启动会。
- 角色子任务：
  - `T000-PM`（PM）：执行 `PM-01`、`PM-02`，完善 `docs/collab/TEAM.md`、`BOARD.md`、`RISKS.md` 及 `docs/PLAN.md` 阶段里程碑。
  - `T000-AR`（AR）：执行 `AR-01`、`AR-02`，核对仓库目录、更新 `AGENTS.md` 项目信息与 `docs/collab/OWNERS.md` 初版。
  - `T000-PO`（PO）：执行 `PO-01`，输出 `docs/analysis/00-PO需求通读笔记.md`。
  - `T000-BE`（BE）：执行 `BE-01`，输出 `docs/collab/notes/BE-需求通读笔记.md`。
  - `T000-FE`（FE）：执行 `FE-01`，输出 `docs/collab/notes/FE-需求通读笔记.md`。
  - `T000-QA`（QA）：执行 `QA-01`，输出 `docs/collab/notes/QA-需求通读笔记.md`。
  - `T000-OPS`（OPS）：执行 `OPS-01`，输出 `docs/collab/notes/OPS-需求通读笔记.md`。
- 完成标准：七份产出全部落盘并通过 `z-scripts/validate_project.py` 校验，真人确认 P0 关卡通过。

### 后续阶段任务占位（随关卡推进依次激活）

| 任务ID | 阶段              | 主导角色     | 核心交付物路径                                                                                   | 状态      |
| ------ | ----------------- | ------------ | ------------------------------------------------------------------------------------------------ | --------- |
| `T001` | P1 需求分析       | PO           | `docs/SRS-INDEX.md`、`docs/analysis/01~05`、各角色评审单 `RV-*`                                  | `⏳ TODO` |
| `T002` | P2 架构设计       | AR           | `docs/architecture/01~02`、`CONVENTIONS.md`、`docs/adr/`、`OWNERS.md` 定稿                       | `⏳ TODO` |
| `T003` | P3 详细设计       | BE/FE/QA/OPS | `docs/design/db,api,ui,04~08`、`docs/acceptance/`、`docs/test/测试数据*`                         | `⏳ TODO` |
| `T004` | P4 开发计划       | PM           | `docs/PLAN.md`、`docs/PROGRESS.md`、`docs/test/测试计划.md`、`docs/ops/环境*`                    | `⏳ TODO` |
| `T005` | P5 迭代开发       | BE/FE/QA/OPS | `server/`、`web/`、`mobile/`、`ai/`、`tests/`、`deploy/`、`.ci/`（按 `PLAN.md`）                 | `⏳ TODO` |
| `T006` | P6 系统测试与发布 | QA / OPS     | `docs/test/系统测试与准出报告*`、`docs/ops/预发布与演练报告*`、`docs/acceptance/系统验收报告.md` | `⏳ TODO` |
| `T007` | P7 交付与收尾     | PM 统筹      | `docs/delivery/*`、`docs/collab/项目总结.md`                                                     | `⏳ TODO` |
