# OWNERS.md —— 团队项目文件所有权与必需评审矩阵

> **拥有角色**：`AR`（修改需获取 `task-metadata` 租约）。
> **刚性规则**：
> 1. 任何角色会话只允许新建或修改“拥有角色”列包含本角色的路径；
> 2. 路径匹配采用“最具体路径优先”原则（例如 `web/e2e/**` 归 `QA`，优先于 `web/**` 的 `FE`）；
> 3. 任何合并或基线冻结必须获得“必需评审角色”列全部角色出具的 `通过` 评审单（`RV-xxx`）或签字。

| 路径模式                                                     | 拥有角色（唯一可写）       | 可读角色 | 必需评审角色                  | 说明                                                       |
| ------------------------------------------------------------ | -------------------------- | -------- | ----------------------------- | ---------------------------------------------------------- |
| `AGENTS.md`                                                  | `AR`                       | 全体     | `PM`、真人批准                | 项目最高操作与技术宪法（需 `task-metadata` 租约）          |
| `_STATE.md`、`_TASKLISTS.md`、`_STATE_HISTORY.md`            | `PM`                       | 全体     | —                             | 全局阶段与任务池看板（需 `task-metadata` 租约）            |
| `_CHECKLISTS.md`                                             | `AR`、`QA`                 | 全体     | `PM`、真人批准                | 稳定功能冻结与回归清单（需 `task-metadata` 租约）          |
| `.agents/roles/**`、`.agents/workflows/**`                   | `AR`                       | 全体     | `PM`                          | 工具无关角色准则卡与标准协作动作剧本                       |
| `.agents/parallel/config.yaml`                               | `AR`                       | 全体     | `PM`                          | 多环境并行与租约配置                                       |
| `.agents/parallel/lanes/<task>-<ROLE>.md`                    | 对应 `<ROLE>`              | 全体     | —                             | 各角色活跃泳道实时进度                                     |
| `z-docs/**`                                                  | 只读（真人放入）           | 全体     | —                             | 原始需求规格说明书与外部输入资料（严禁 AI 写入）           |
| `z-readme/**`                                                | `AR`、`PM`                 | 全体     | 真人确认                      | 团队制度规范与中文技术指南                                 |
| `z-logs/**`                                                  | 当事角色（Opt-in）         | 全体     | 真人确认                      | 仅在用户明确要求时写入验证记录                             |
| `z-scripts/**`                                               | `AR`、`OPS`、`QA`          | 全体     | `AR`                          | 自动化校验、文档转换与开发辅助脚本                         |
| `docs/SRS.md`、`docs/SRS-INDEX.md`                           | `PO`                       | 全体     | `AR`、`QA`                    | 需求基线与唯一需求条款索引                                 |
| `docs/analysis/00~04-*.md`                                   | `PO`                       | 全体     | `AR`、`BE`、`FE`、`QA`、`OPS` | 需求澄清、用例、业务规则、状态机规格                       |
| `docs/analysis/05-领域模型.md`                               | `AR`                       | 全体     | `PO`、`BE`                    | 领域模型与限界上下文                                       |
| `docs/architecture/**`、`docs/adr/**`                        | `AR`                       | 全体     | `PO`、`BE`、`FE`、`QA`、`OPS` | 技术选型、ADR、概要设计、编码规范                          |
| `docs/design/db/**`                                          | `BE`                       | 全体     | `AR`、`OPS`                   | 数据库总体设计、分模块表结构与汇总 DDL                     |
| `docs/design/api/**`                                         | `BE`                       | 全体     | `FE`、`AR`、`QA`              | 接口规范与各模块冻结契约（破坏性变更须走 `CR`）            |
| `docs/design/ui/**`                                          | `FE`                       | 全体     | `PO`（业务签字）、`AR`、`QA`  | 信息架构与分模块页面规格                                   |
| `docs/design/04-流程引擎与闭环设计.md`                       | `AR`                       | 全体     | `PO`、`BE`、`QA`              | 核心业务状态机与闭环流转设计                               |
| `docs/design/05-AI服务设计.md`、`docs/design/ai/**`          | `AI`（未设时 `AR`）        | 全体     | `PO`、`AR`、`BE`、`FE`、`QA`  | AI 服务架构、提示词模板与评估设计                          |
| `docs/design/06-安全设计.md`                                 | `AR`                       | 全体     | `BE`、`FE`、`QA`、`OPS`       | 认证、功能权限、数据权限、加密脱敏与审计设计               |
| `docs/design/07-测试策略与用例.md`、`docs/test/**`           | `QA`                       | 全体     | `PO`、`AR`                    | 测试策略、全量用例、测试计划、执行记录与准出报告           |
| `docs/design/08-部署与运维设计.md`、`docs/ops/**`            | `OPS`                      | 全体     | `AR`、`QA`                    | 部署拓扑、容器规范、可观测性、部署与演练记录               |
| `docs/acceptance/**`                                         | `PO`                       | 全体     | `QA`（前置测试通过）          | 用户故事验收标准、迭代验收记录、系统验收报告               |
| `docs/reviews/**`                                            | `AR`                       | 全体     | `PM`                          | 阶段设计评审汇总报告                                       |
| `docs/PLAN.md`、`docs/PROGRESS.md`                           | `PM`                       | 全体     | 全体核心角色确认              | 迭代开发计划、任务卡与实时进度看板                         |
| `docs/collab/TEAM.md`、`BOARD.md`、`RISKS.md`、`meetings/**` | `PM`                       | 全体     | —                             | 团队章程、协作看板、风险册、会议纪要                       |
| `docs/collab/notes/<ROLE>-*.md`                              | 对应 `<ROLE>`              | 全体     | —                             | 各角色需求通读笔记                                         |
| `docs/collab/handoff/HO-*.md`                                | 发起角色创建，接收角色确认 | 全体     | —                             | 跨角色正式交接单                                           |
| `docs/collab/issues/IS-*.md`                                 | 发起角色创建，指派角色处理 | 全体     | `QA`（缺陷关闭权）            | 问题单与测试缺陷单                                         |
| `docs/collab/reviews/RV-*.md`                                | 评审角色创建，作者角色回复 | 全体     | 评审角色复核关闭              | 设计与代码评审单                                           |
| `docs/collab/changes/CR-*.md`                                | 发起角色创建，五方评估     | 全体     | `PM` + 真人批准               | 受控基线变更单                                             |
| `docs/delivery/用户手册.md`、`配置手册.md`                   | `PO`                       | 全体     | `PM`                          | 面向最终用户与业务管理员的交付手册                         |
| `docs/delivery/测试报告.md`                                  | `QA`                       | 全体     | `PM`、`PO`、`AR`              | 终版系统测试报告                                           |
| `docs/delivery/部署手册.md`、`运维手册.md`                   | `OPS`                      | 全体     | `AR`、`PM`                    | 终版安装部署手册与日常运维应急手册                         |
| `server/**`                                                  | `BE`                       | 全体     | `AR`                          | 服务端源码、Flyway 迁移脚本、后端单测与集成测试            |
| `web/e2e/**`                                                 | `QA`                       | 全体     | `AR`                          | 前端端到端自动化测试工程（优先于 `web/**`）                |
| `web/**`（除 `web/e2e/**`）、`mobile/**`                     | `FE`                       | 全体     | `AR`                          | Web 与移动端前端源码、Mock、组件单测                       |
| `ai/**`                                                      | `AI`（未设时 `BE`）        | 全体     | `AR`                          | AI 服务源码、提示词模板、离线评估脚本与假模型桩            |
| `tests/**`                                                   | `QA`                       | 全体     | `AR`                          | 接口自动化（`api/`）、性能（`perf/`）、安全（`security/`） |
| `deploy/**`、`.ci/**`                                        | `OPS`                      | 全体     | `AR`                          | 容器编排、Dockerfile、环境变量模板、监控与流水线           |
