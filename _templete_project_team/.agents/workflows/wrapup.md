# 标准协作剧本：会话收尾与防串角自检（/wrapup）

1. **防串角自检**：运行 `git status` / `git diff --name-only`，核对本次会话新增或修改的每一个文件是否全部属于当前角色在 `docs/collab/OWNERS.md` 中拥有的路径范围；若发现误改他人文件，立即停止并报告真人，不得提交。
2. 运行 `py -3.11 z-scripts/validate_project.py --align` 自动对齐本次修改的 Markdown 表格并执行规范检查。
3. 为需要移交下游的产出创建交接单（`/handoff`），为发现的他人工件问题创建问题单（`/ask` 或 `/defect`）。
4. 更新本会话泳道文件 `.agents/parallel/lanes/<task-id>-{ROLE}.md` 的状态与心跳；如持有任何 `.agents/parallel/leases/*.lock` 租约，确保已全部释放。
5. 输出本次会话产出清单、建议的 Git 显式暂存命令（`git add -- <explicit-owned-paths>`）与符合规范的提交信息 `<type>(<task-id>-<role>): <summary>`。
