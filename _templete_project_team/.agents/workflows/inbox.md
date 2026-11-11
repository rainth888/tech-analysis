# 标准协作剧本：会话开场与待办巡检（/inbox）

1. 确认当前会话扮演的唯一角色 `{ROLE}`，阅读 `AGENTS.md`、`.agents/roles/{ROLE}.md`、`docs/collab/OWNERS.md`。
2. 阅读 `_STATE.md`、`_TASKLISTS.md`、`docs/PROGRESS.md`、`docs/collab/BOARD.md` 以及 `.agents/parallel/lanes/` 下所有活跃泳道。
3. 按优先级列出：
   - ① 指派给 `{ROLE}` 的未关闭阻塞项与致命/严重缺陷单（`IS-*`）；
   - ② 指派给 `{ROLE}` 的待确认交接单（`HO-*`）、待处理评审单（`RV-*`）、待答复问题单（`IS-*`）、待分析变更单（`CR-*`）；
   - ③ `{ROLE}` 当前进行中或下一项前置已满足的任务（`Txx-{ROLE}`）；
   - ④ 本次会话拟写入的精确文件路径清单（核对均在 `{ROLE}` 的 `OWNERS.md` 范围内且与其它活跃泳道无交集）。
4. 创建或更新 `.agents/parallel/lanes/<task-id>-{ROLE}.md` 心跳与状态后，开始执行最高优事项。
