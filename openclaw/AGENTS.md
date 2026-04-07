# AGENTS.md — OpenClaw 管理项目

// turbo-all

## 自动执行规则

除删除操作外，所有命令均可自动执行（`SafeToAutoRun = true`）。

## 关键信息

- **源码**：`E:\openclaw` | **管理项目**：`E:\_projects\_tech-analysis\openclaw`（仅文档）
- **配置**：`%USERPROFILE%\.openclaw\`（`.env` + `openclaw.json`）
- **Gateway Token**：`local-dev-token-2026`
- **代理**：`http://127.0.0.1:7890`（Clash），需 `proxy-preload.cjs` 预加载，否则 LLM 请求超时
- **端点**：WebChat `http://127.0.0.1:18789` | API `/v1/chat/completions` | Health `/healthz`

## 启动 Gateway

```powershell
# 一键启动
powershell -ExecutionPolicy Bypass -File E:\openclaw\start-gateway.ps1

# 手动启动
$env:OPENCLAW_NO_RESPAWN="1"; $env:OPENCLAW_NODE_OPTIONS_READY="1"; $env:NO_COLOR="1"; $env:TERM="dumb"; $env:HTTPS_PROXY="http://127.0.0.1:7890"; node --disable-warning=ExperimentalWarning --require E:\openclaw\proxy-preload.cjs E:\openclaw\dist\index.js gateway --port 18789 --bind loopback --force
```

## 构建

```bash
pnpm install && pnpm build    # 安装 + 构建
pnpm ui:build                 # 构建 WebChat UI（WSL 中执行）
```
