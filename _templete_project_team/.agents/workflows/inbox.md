# 标准协作剧本：会话开场与待办巡检（/inbox）

1. 阅读 AGENTS.md、角色卡、任务与冻结清单；核对 Git 根目录、分支、HEAD 与已有改动。
2. 声明 user_id、actor_id、role_id、task_id、lane_id，使用独立 worktree/分支；同角色成员也分别登记。
3. 读取共享协调中心 status，检查依赖、冻结范围及人工批准；先运行 claim 成功，再进行写入。
4. 泳道摘要保存至 z-readme/lanes/<TASK>-<ROLE>-<USER>-<SESSION>.md；该摘要不是锁。共享文件另行领取。

详细命令与人工审批格式见 `z-readme/08_冻结并行开发与Git合并操作手册.md`。
