# 个人泳道记录格式示例（本文件只读引用）

实际记录保存到 z-readme/lanes/<TASK>-<ROLE>-<USER>-<SESSION>.md；运行锁由 team_guard 维护。

- user_id：稳定人员标识
- actor_id：本次会话唯一标识
- role_id：PM / PO / AR / BE / FE / QA / OPS / AI
- task_id、lane_id：任务与唯一泳道
- branch、starting_head、worktree 标识：不记录敏感绝对目录
- owned_paths：精确文件或以 / 结尾的窄目录
- resources：共享构建、迁移、测试环境或元数据
- frozen_artifacts：冻结号、版本、提交、原责任人
- approved_changes：真实人工批准编号、目标范围与有效期
- dependencies、verification、rollback：依赖、自检与回退
- state、heartbeat、next_action：进度、心跳与下一步

同角色多人不能复用 lane_id。源角色/用户不是人工批准接手后的必需处理人。新文档和代码由当前责任人分别冻结，冻结不等于 STABLE。
