# T002 智能体操作规范中文化与完善

- task_id: `T002`
- actor_id: `codex-agents-zh-20261111-2148`
- status: `AWAITING_USER_CONFIRMATION`（等待用户确认）
- branch: `docs/agents-chinese-20261111`
- starting_head: `65950367163a84c61dca08751d0c6d8959f5509e`
- owned_paths:
  - `AGENTS.md`
  - `_STATE.md`
  - `_TASKLISTS.md`
  - `_CHECKLISTS.md`
  - `.agents/parallel/lanes/T002-agents-zh.md`
- resources: `task-metadata` 与 `git-index` 均仅在对应操作期间持有，交付前释放。
- stable_features: 无冻结功能；用户明确要求修改 `AGENTS.md`。
- last_heartbeat: 2026-11-11T21:53:43+08:00
- next_action: 等待用户对中文化结果与规则完善进行验收；不代替 T001 应用验收。
- verification: 英文残留、机器标识兼容、章节与表格、差异检查；最终验收由用户确认。
- rollback: 保留已有未提交修改及现有副本；不执行自动回退，回退需用户明确授权。
- 原始文件摘要：`0898ebd162f2301ddd6e1b96a1a8d495d3235458cfa172174b3d1bce31497b47`。
- 范围边界：不修改现有副本、并行配置、历史记录、其他项目文件；不提交、不合并、不推送。
- 旧任务关系：T001 无活跃泳道，仅保留历史待验收记录；本次依用户新指令修订同一文件，不代表 T001 已通过验收。

## 内部验证结果

- 已完成：12 节中文操作规范，正文英文说明残留为 0；保留命令、路径、字段及机器状态。
- 已完成：4 组表格显示宽度对齐，章节无重复，行内代码成对，无乱码及行尾空白。
- 已完成：36 项关键机器标识与安全限制覆盖；版本库差异检查通过。
- 原有副本与原始目标摘要一致；并行配置未改动。
- 当前文档摘要：`ac48a6d02af23677e04c72d56bde7c7698fb28f0ce75deaff9d1735bbe1ce207`。
- 规则调整：统一文档目录、固定文件命名例外、授权边界、共享文件短时租约及稳定主分支规则；补充指令作用范围与验证交付要求。
- 验收边界：仅内部检查通过，未声明稳定；无提交、合并和推送。
