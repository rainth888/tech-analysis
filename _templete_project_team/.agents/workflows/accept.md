# 标准协作剧本：PO 业务验收（/accept <用户故事编号或任务号>）

1. **PO 专用**。加载 `.agents/roles/ACCEPTOR-BIZ.md` 核对清单。
2. 确认已收到 QA 针对该故事的“测试通过可验收 `HO`”交接单。
3. 对照 `docs/acceptance/用户故事与验收标准.md` 的每条 `AC-xxx`（Given/When/Then），结合真人演示操作或 QA 客观测试证据逐条判定，结果追加至 `docs/acceptance/验收记录.md`。
4. 存在不通过项时创建问题单（类型=`验收缺陷`）；全部通过时 `/handoff PM` 通知更新进度。
