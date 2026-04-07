# 🦞 OpenClaw 技术分析与管理项目

> OpenClaw 技术研究、使用文档、深度分析的管理仓库。

---

## 项目简介

**OpenClaw** 是一个**本地优先（Local-First）的个人 AI 助手网关**，运行在用户自己的设备上，通过 22+ 聊天渠道（WhatsApp、Telegram、Discord、Slack、WebChat、飞书、Signal、iMessage 等）与用户交互。

### 核心架构

```
WhatsApp / Telegram / Slack / Discord / Signal / WebChat / ...
               │
               ▼
┌───────────────────────────────────┐
│         Gateway (控制平面)          │
│      ws://127.0.0.1:18789         │
│                                   │
│  ├─ Pi Agent（嵌入式 AI 运行时）     │
│  ├─ 渠道插件系统（40+ 扩展）        │
│  ├─ 工具系统（Bash/文件/浏览器等）   │
│  ├─ Skills 技能系统                │
│  └─ OpenAI 兼容 HTTP API          │
└───────────────────────────────────┘
               │
    ┌──────────┴──────────┐
    ▼                     ▼
模型提供商 API          伴侣节点
(OpenAI/Anthropic/     (macOS/iOS/
 Gemini/Ollama/...)     Android)
```

### 技术栈

| 项目 | 技术 |
|------|------|
| 语言 | TypeScript (strict ESM) |
| 运行时 | Node.js ≥ 22.12 |
| 包管理 | pnpm 10.x |
| 构建 | tsdown (基于 rolldown/Rust) |
| 测试 | Vitest |
| 代码规范 | Oxlint + Oxfmt |

### 源码结构

```
E:\openclaw\
├── src/           # 核心源码（Gateway/Agent/Plugins/CLI）
├── extensions/    # 渠道插件扩展（40 个独立包）
├── apps/          # 伴侣应用（macOS/iOS/Android）
├── ui/            # Web UI 源码
├── docs/          # 用户文档
├── scripts/       # 构建/部署脚本
├── skills/        # 内置技能
├── dist/          # 构建产物
└── docker-compose.yml
```

---

## 本项目文档清单

| 文件 | 说明 |
|------|------|
| [AGENTS.md](AGENTS.md) | AI Agent 开发注意事项（关键信息速查） |
| [USAGE_GUIDE_ZH.md](USAGE_GUIDE_ZH.md) | OpenClaw 完整使用指南 |
| [TECHNICAL_ANALYSIS_ZH.md](TECHNICAL_ANALYSIS_ZH.md) | 技术深度分析（架构/源码/设计决策） |
| [OPENCLAW_CAPABILITIES_ZH.md](OPENCLAW_CAPABILITIES_ZH.md) | 功能概览 |

---

## 本地运行环境

| 环境 | 状态 | 备注 |
|------|------|------|
| Windows 11 | ✅ 运行中 | PowerShell 启动 |
| WSL Ubuntu 24.04 | ✅ 运行中 | `/mnt/e/openclaw` |
| WSL Ubuntu 22.04 | ✅ 运行中 | `/mnt/e/openclaw` |

### 快速启动

**Windows:**
```powershell
powershell -ExecutionPolicy Bypass -File E:\openclaw\start-gateway.ps1
```

**WSL:**
```bash
cd /mnt/e/openclaw
OPENCLAW_NO_RESPAWN=1 OPENCLAW_NODE_OPTIONS_READY=1 \
  node --disable-warning=ExperimentalWarning dist/index.js gateway --port 18789 --bind loopback --force
```

### 访问

- **WebChat**: http://127.0.0.1:18789
- **健康检查**: http://127.0.0.1:18789/healthz
- **API**: http://127.0.0.1:18789/v1/chat/completions

---

## 参考链接

| 项目 | 链接 |
|------|------|
| GitHub | https://github.com/openclaw/openclaw |
| 官网 | https://openclaw.ai |
| 文档 | https://docs.openclaw.ai |
| ClawHub | https://clawhub.com |

---

*更新时间：2026-03-14*
