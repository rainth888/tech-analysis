# 多用户、多角色 AI 软件团队项目模板

支持同角色多人以独立 Git 分支/worktree 并行开发。每名用户负责冻结自己交付的文档和代码；冻结修改须有明确接口或功能干涉及真人批准，批准可指定其他用户/角色接手。

## 使用入口

1. 先读 `AGENTS.md`，再读对应 `.agents/roles/` 与 `.agents/workflows/inbox.md`。
2. 复制为独立项目仓库后，按 `z-readme/08_冻结并行开发与Git合并操作手册.md` 初始化唯一协调中心、创建工作树、领取范围。
3. 开发、自检、显式提交、分别冻结成果，再经独立评审与合并队列验证候选版本。
4. 新工程文档统一放 `z-readme/`；静态文档按目录内序号排列，动态工件用任务与唯一单据编号命名，不加时间标签；`z-docs/` 只读原始需求。

## 文件与工具

- `.agents/parallel/policy.json`：唯一的机器路径权限配置；协作行为规则见 `AGENTS.md`。
- `z-scripts/team_guard.py`：claim、heartbeat、check、freeze、thaw、recover、snapshot、release。
- `z-scripts/validate_project.py`：只读结构/引用检查；格式化须显式 `--align --files`。
- `z-scripts/test_team_guard.py`：临时 Git 仓库、真实 worktree 与并发场景回归。
- `z-readme/07_工程文档导航.md`：迁移后的工程文档模板；`00` 至 `06` 手册保留岗位内容与演练。

```bash
python3.11 z-scripts/validate_project.py
python3.11 z-scripts/test_team_guard.py
```

要求 Python 3.10+，推荐 3.11。Windows 使用 `py -3.11`。团队工具应在独立项目根目录运行；本目录作为父仓库子模板时只运行只读校验和测试。

协调工具不提供身份认证或远程锁服务。跨机器必须落实同一受控协调中心；受保护分支、真人审批和业务 CI 需要在实际项目平台配置。`.ci/` 中只提供示例，不能声称已启用。
