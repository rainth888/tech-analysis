# 🦞 OpenClaw 使用说明文档

> **版本**：2026.3.9 | **运行环境**：Node.js ≥ 22 | **官网**：https://openclaw.ai | **文档**：https://docs.openclaw.ai

---

## 目录

- [一、项目简介](#一项目简介)
- [二、安装方式](#二安装方式)
- [三、首次配置（Onboard 向导）](#三首次配置onboard-向导)
- [四、Gateway 网关](#四gateway-网关)
- [五、CLI 命令行使用](#五cli-命令行使用)
- [六、聊天渠道集成](#六聊天渠道集成)
- [七、AI 模型配置](#七ai-模型配置)
- [八、工具与自动化](#八工具与自动化)
- [九、Skills 技能系统](#九skills-技能系统)
- [十、Docker 部署](#十docker-部署)
- [十一、远程访问](#十一远程访问)
- [十二、安全配置](#十二安全配置)
- [十三、聊天命令](#十三聊天命令)
- [十四、多 Agent 协同](#十四多-agent-协同)
- [十五、伴侣应用](#十五伴侣应用)
- [十六、故障排查](#十六故障排查)
- [十七、常用 pnpm 脚本](#十七常用-pnpm-脚本)

---

## 一、项目简介

**OpenClaw** 是一个**个人 AI 助手**，可以运行在你自己的设备上。它通过你已经使用的聊天渠道（WhatsApp、Telegram、Slack、Discord、微信（Feishu/飞书）、Signal、iMessage、IRC、Microsoft Teams、Matrix、LINE、Mattermost、WebChat 等 22+ 渠道）来回答你的消息。

### 核心架构

```
WhatsApp / Telegram / Slack / Discord / Signal / WebChat / ...
               │
               ▼
┌───────────────────────────────┐
│            Gateway            │
│        (控制平面/网关)          │
│     ws://127.0.0.1:18789      │
└──────────────┬────────────────┘
               │
               ├─ Pi Agent（RPC 模式）
               ├─ CLI（openclaw 命令）
               ├─ WebChat UI
               ├─ macOS 菜单栏应用
               └─ iOS / Android 节点
```

---

## 二、安装方式

### 方式一：npm 全局安装（推荐）

```bash
npm install -g openclaw@latest
# 或者
pnpm add -g openclaw@latest
```

### 方式二：从源码构建

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw

pnpm install          # 安装依赖
pnpm build            # 构建 dist/ 目录
# pnpm ui:build       # （可选）构建 Web UI

# 验证安装
node openclaw.mjs --version
# 输出示例：OpenClaw 2026.3.9 (6d0547d)
```

### 方式三：Docker 安装

详见 [十、Docker 部署](#十docker-部署) 章节。

### 环境要求

| 项目      | 要求         |
|-----------|-------------|
| Node.js   | ≥ 22.12     |
| 包管理器   | pnpm / npm / bun |
| 操作系统   | macOS、Linux、Windows（WSL2 推荐） |

---

## 三、首次配置（Onboard 向导）

安装完成后，运行引导向导完成初始配置：

```bash
openclaw onboard --install-daemon
```

向导将引导你完成：
1. **模型设置** — 选择 AI 模型提供商（OpenAI、Anthropic、Gemini 等）
2. **API Key 配置** — 输入模型 API 密钥
3. **渠道配置** — 连接聊天渠道（WhatsApp、Telegram 等）
4. **守护进程** — 安装 launchd/systemd 服务，让 Gateway 持续运行

---

## 四、Gateway 网关

Gateway 是 OpenClaw 的核心控制平面，管理会话、渠道、工具和事件。

### 启动 Gateway

```bash
# 基本启动
openclaw gateway

# 指定端口和详细输出
openclaw gateway --port 18789 --verbose

# 绑定到局域网（允许其他设备连接）
openclaw gateway --bind lan --port 18789

# 强制启动（忽略已有实例）
openclaw gateway --bind loopback --port 18789 --force
```

### Gateway 配置文件

配置文件位于 `~/.openclaw/openclaw.json`（或 `openclaw.json5`）：

```json5
{
  // 模型配置
  agent: {
    model: "anthropic/claude-opus-4-6",
  },

  // Gateway 设置
  gateway: {
    port: 18789,
    bind: "loopback",  // loopback | lan
    auth: {
      mode: "token",   // token | password
      token: "your-secret-token",
    },
  },
}
```

### 健康检查

```bash
# 访问健康检查端点
curl http://127.0.0.1:18789/healthz
```

---

## 五、CLI 命令行使用

### 发送消息

```bash
# 发送文本消息
openclaw message send --to +1234567890 --message "Hello from OpenClaw"

# 与 Agent 对话
openclaw agent --message "今天天气怎么样？"

# 带思考模式的对话
openclaw agent --message "分析这段代码" --thinking high
```

### 渠道管理

```bash
# 登录渠道（如 WhatsApp）
openclaw channels login

# 查看渠道状态
openclaw channels status
openclaw channels status --probe  # 深度探测

# 设备配对管理
openclaw pairing approve <channel> <code>
```

### 系统诊断

```bash
# 运行诊断检查
openclaw doctor

# 查看配置
openclaw config set <key> <value>

# 更新 OpenClaw
openclaw update --channel stable    # stable | beta | dev
```

### 节点管理

```bash
# 列出已连接的节点
openclaw nodes list

# 设备配对
openclaw devices pair
```

---

## 六、聊天渠道集成

OpenClaw 支持 22+ 聊天渠道。以下是常用渠道的配置方法：

### WhatsApp

```bash
# 通过扫码链接设备
openclaw channels login
```

配置文件中设置白名单：

```json5
{
  channels: {
    whatsapp: {
      allowFrom: ["+86138xxxx1234"],
      // 群组白名单（"*" 表示允许所有群）
      groups: { "*": { requireMention: true } },
    },
  },
}
```

### Telegram

```json5
{
  channels: {
    telegram: {
      botToken: "123456:ABCDEF-your-bot-token",
      // 可选：群组设置
      groups: { "*": { requireMention: true } },
      allowFrom: ["your-telegram-id"],
    },
  },
}
```

也可以设置环境变量 `TELEGRAM_BOT_TOKEN=123456:ABCDEF`。

### Discord

```json5
{
  channels: {
    discord: {
      token: "your-discord-bot-token",
      allowFrom: ["user-id"],
      guilds: { "guild-id": {} },
    },
  },
}
```

也可以设置环境变量 `DISCORD_BOT_TOKEN=your-token`。

### Slack

需要两个 Token：

```json5
{
  channels: {
    slack: {
      botToken: "xoxb-your-bot-token",
      appToken: "xapp-your-app-token",
    },
  },
}
```

环境变量：`SLACK_BOT_TOKEN` + `SLACK_APP_TOKEN`。

### 飞书 (Feishu)

```json5
{
  channels: {
    feishu: {
      appId: "cli_xxx",
      appSecret: "xxx",
    },
  },
}
```

### 其他渠道速览

| 渠道                 | 配置项                                | 说明                  |
|---------------------|--------------------------------------|----------------------|
| Signal              | `channels.signal`                    | 需要 signal-cli       |
| iMessage            | `channels.imessage`                  | macOS 专用（旧版）     |
| BlueBubbles         | `channels.bluebubbles`               | 推荐的 iMessage 集成   |
| Microsoft Teams     | `channels.msteams`                   | 需要 Bot Framework    |
| Matrix              | `channels.matrix`                    | 开源即时通讯           |
| IRC                 | `channels.irc`                       | 经典 IRC 协议         |
| LINE                | `channels.line`                      | LINE 消息平台          |
| Mattermost          | `channels.mattermost`                | 开源团队通讯           |
| Nextcloud Talk      | `channels.nextcloudtalk`             | Nextcloud 聊天        |
| Nostr               | `channels.nostr`                     | 去中心化协议           |
| Synology Chat       | `channels.synologychat`              | 群晖聊天              |
| Twitch              | `channels.twitch`                    | 直播聊天              |
| Zalo                | `channels.zalo`                      | 越南通讯应用           |
| WebChat             | 内置，通过 Gateway WebSocket          | 网页聊天界面           |

---

## 七、AI 模型配置

### 支持的模型提供商

通过环境变量或配置文件设置 API Key：

```bash
# .env 文件或环境变量
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=...
OPENROUTER_API_KEY=sk-or-...
```

### 配置文件示例

```json5
{
  agent: {
    // 主模型
    model: "openai/gpt-5.4",
    // 或使用 Anthropic
    // model: "anthropic/claude-opus-4-6",
    // 或使用 Gemini
    // model: "gemini/gemini-2.5-pro",
  },
}
```

### 模型故障转移（Failover）

支持多 Key 轮换和故障自动切换：

```bash
# 多个 API Key 用逗号分隔
OPENAI_API_KEYS=sk-key1,sk-key2,sk-key3
ANTHROPIC_API_KEYS=sk-ant-key1,sk-ant-key2
```

详见：[模型配置文档](https://docs.openclaw.ai/concepts/models) | [模型故障转移](https://docs.openclaw.ai/concepts/model-failover)

---

## 八、工具与自动化

### 浏览器控制

OpenClaw 可以通过 CDP 协议控制 Chrome/Chromium 浏览器：

```json5
{
  browser: {
    enabled: true,
    color: "#FF4500",
  },
}
```

### 定时任务（Cron）

设置定时任务让 Agent 自动执行操作：

详见：[Cron 文档](https://docs.openclaw.ai/automation/cron-jobs)

### Webhook

通过 Webhook 接收外部事件触发 Agent 响应：

详见：[Webhook 文档](https://docs.openclaw.ai/automation/webhook)

### Gmail 邮件触发

设置 Gmail Pub/Sub，在收到邮件时自动触发 Agent：

详见：[Gmail Pub/Sub 文档](https://docs.openclaw.ai/automation/gmail-pubsub)

### Canvas 画布

Agent 可驱动的可视化工作空间（A2UI）：

详见：[Canvas 文档](https://docs.openclaw.ai/platforms/mac/canvas)

---

## 九、Skills 技能系统

Skills 是扩展 Agent 能力的模块化组件。

### 技能类型

| 类型          | 位置                       | 说明           |
|--------------|---------------------------|----------------|
| Bundled      | 内置                       | 随 OpenClaw 分发 |
| Managed      | ClawHub 注册表             | 在线安装        |
| Workspace    | `~/.openclaw/workspace/skills/` | 用户自定义    |

### 工作区结构

```
~/.openclaw/workspace/
├── AGENTS.md          # 主提示文件
├── SOUL.md            # 人格提示
├── TOOLS.md           # 工具说明
└── skills/
    └── my-skill/
        └── SKILL.md   # 技能定义文件
```

### ClawHub 技能注册表

ClawHub 是最小化技能注册表，Agent 可自动搜索和安装技能：

- **网站**：https://clawhub.com

---

## 十、Docker 部署

### 快速部署

```bash
# 1. 复制环境变量文件
cp .env.example .env
# 编辑 .env 填入你的 API Key 和 Token

# 2. 构建 Docker 镜像
docker build -t openclaw:local .

# 3. 启动服务
docker compose up -d
```

### docker-compose.yml 关键配置

```yaml
services:
  openclaw-gateway:
    image: openclaw:local
    environment:
      OPENCLAW_GATEWAY_TOKEN: your-secret-token
    volumes:
      - ./config:/home/node/.openclaw          # 配置目录
      - ./workspace:/home/node/.openclaw/workspace  # 工作区
    ports:
      - "18789:18789"    # Gateway 端口
      - "18790:18790"    # Bridge 端口
    restart: unless-stopped

  openclaw-cli:
    image: openclaw:local
    network_mode: "service:openclaw-gateway"
    entrypoint: ["node", "dist/index.js"]
    depends_on:
      - openclaw-gateway
```

### 环境变量说明

| 变量                          | 说明                      | 示例                       |
|------------------------------|--------------------------|---------------------------|
| `OPENCLAW_GATEWAY_TOKEN`     | Gateway 认证 Token        | `openssl rand -hex 32`   |
| `OPENCLAW_GATEWAY_PASSWORD`  | 替代密码认证               | 强密码                    |
| `OPENAI_API_KEY`             | OpenAI API 密钥           | `sk-...`                 |
| `ANTHROPIC_API_KEY`          | Anthropic API 密钥        | `sk-ant-...`             |
| `GEMINI_API_KEY`             | Gemini API 密钥           | `...`                    |
| `TELEGRAM_BOT_TOKEN`         | Telegram Bot Token        | `123456:ABCDEF`          |
| `DISCORD_BOT_TOKEN`          | Discord Bot Token         | `...`                    |
| `SLACK_BOT_TOKEN`            | Slack Bot Token           | `xoxb-...`               |
| `SLACK_APP_TOKEN`            | Slack App Token           | `xapp-...`               |
| `ELEVENLABS_API_KEY`         | ElevenLabs TTS 密钥       | `...`                    |

### 自动化部署脚本

```bash
# 使用内置脚本快速部署
bash docker-setup.sh
```

---

## 十一、远程访问

### 方式一：Tailscale Serve/Funnel

```json5
{
  gateway: {
    tailscale: {
      mode: "serve",    // off | serve（仅内网）| funnel（公网）
      resetOnExit: true,
    },
    bind: "loopback",   // 必须是 loopback
    auth: {
      mode: "password",  // funnel 模式必须设密码
      password: "your-password",
    },
  },
}
```

| 模式    | 访问范围         | 安全要求                  |
|---------|----------------|--------------------------|
| `off`   | 仅本地          | 无                        |
| `serve` | Tailnet 内网    | 默认用 Tailscale 身份认证  |
| `funnel`| 公开互联网       | 必须设置密码认证           |

### 方式二：SSH 隧道

在远程 Linux 服务器上运行 Gateway，通过 SSH 隧道连接：

```bash
# 在本地创建 SSH 隧道
ssh -L 18789:127.0.0.1:18789 user@gateway-host
```

详见：[远程访问文档](https://docs.openclaw.ai/gateway/remote)

---

## 十二、安全配置

### DM 访问策略

默认行为：未知发送者在 DM 中会收到配对码，Bot 不处理其消息。

```json5
{
  channels: {
    telegram: {
      // "pairing"（默认）= 需要配对码
      // "open" = 公开接受所有 DM
      dmPolicy: "pairing",
      allowFrom: ["your-id"],
    },
  },
}
```

审批配对请求：

```bash
openclaw pairing approve telegram <code>
```

### 沙箱隔离

非 `main` 会话可以在 Docker 沙箱中运行：

```json5
{
  agents: {
    defaults: {
      sandbox: {
        mode: "non-main",  // 非主会话使用沙箱
      },
    },
  },
}
```

### 安全检查

```bash
openclaw doctor  # 检查安全配置和风险
```

---

## 十三、聊天命令

在任何已连接的聊天渠道中，发送以下命令：

| 命令                  | 说明                        |
|----------------------|----------------------------|
| `/status`            | 查看会话状态（模型 + Token）   |
| `/new` 或 `/reset`   | 重置当前会话                 |
| `/compact`           | 压缩会话上下文（生成摘要）     |
| `/think <level>`     | 设置思考深度：`off\|minimal\|low\|medium\|high\|xhigh` |
| `/verbose on\|off`   | 开关详细模式                 |
| `/usage off\|tokens\|full` | 使用量统计显示级别      |
| `/restart`           | 重启 Gateway（仅所有者）      |
| `/activation mention\|always` | 群组激活方式（仅群组） |
| `/elevated on\|off`  | 切换提权 bash 模式           |

---

## 十四、多 Agent 协同

OpenClaw 支持多会话/多 Agent 协同工作：

### Sessions 工具

| 工具                   | 说明                        |
|-----------------------|----------------------------|
| `sessions_list`       | 发现活跃会话及其元数据        |
| `sessions_history`    | 获取会话的对话日志           |
| `sessions_send`       | 向另一个会话发送消息          |

### 多 Agent 路由

```json5
{
  // 路由不同渠道/账户到隔离的 Agent
  agents: {
    routing: {
      // 按渠道/账户路由到不同工作区
    },
  },
}
```

详见：[多 Agent 路由文档](https://docs.openclaw.ai/gateway/configuration)

---

## 十五、伴侣应用

Gateway 本身即可提供完整体验，以下应用均为可选。

### macOS 应用

- 菜单栏控制 Gateway 状态和健康
- Voice Wake + 按键说话
- WebChat + 调试工具
- 远程 Gateway 控制

### iOS 节点

- 通过 Gateway WebSocket 配对
- 语音触发 + Canvas 界面
- 相机/屏幕录制

### Android 节点

- Connect/Chat/Voice 选项卡
- Canvas、相机、屏幕捕获
- Android 设备命令（通知/位置/短信/照片/联系人/日历等）

---

## 十六、故障排查

### 常用诊断命令

```bash
# 运行全面诊断
openclaw doctor

# 检查 Gateway 状态
curl http://127.0.0.1:18789/healthz

# 查看渠道连接状态
openclaw channels status --probe

# 检查端口占用
ss -ltnp | grep 18789  # Linux
netstat -an | findstr 18789  # Windows
```

### 常见问题

| 问题                     | 解决方案                         |
|-------------------------|--------------------------------|
| Node.js 版本不满足        | 升级到 Node.js ≥ 22.12         |
| `missing dist/entry.js`  | 运行 `pnpm build` 构建         |
| Gateway 连接失败          | 检查端口是否被占用，运行 `--force` |
| 渠道不回复消息            | 检查 `allowFrom` 白名单配置     |
| 配对码不工作              | 运行 `openclaw pairing approve` |

详见：[故障排查文档](https://docs.openclaw.ai/channels/troubleshooting)

---

## 十七、常用 pnpm 脚本

从源码运行时的开发命令：

| 命令                    | 说明                    |
|------------------------|------------------------|
| `pnpm install`         | 安装依赖                |
| `pnpm build`           | 构建生产版本到 `dist/`   |
| `pnpm dev`             | 开发模式运行             |
| `pnpm openclaw`        | 直接运行 CLI（TypeScript）|
| `pnpm gateway:watch`   | 开发模式 + 自动重载      |
| `pnpm test`            | 运行测试                |
| `pnpm test:coverage`   | 运行测试 + 覆盖率报告    |
| `pnpm lint`            | 代码检查                |
| `pnpm format`          | 代码格式化              |
| `pnpm ui:build`        | 构建 Web UI             |
| `pnpm ui:dev`          | 开发模式运行 Web UI      |

---

## 附录：环境变量 .env 模板

```bash
# 复制到 .env 或 ~/.openclaw/.env
# 优先级：进程环境变量 > ./.env > ~/.openclaw/.env > openclaw.json env 块

# Gateway 认证
OPENCLAW_GATEWAY_TOKEN=change-me-to-a-long-random-token

# 模型 API Key（至少设置一个）
OPENAI_API_KEY=sk-...
# ANTHROPIC_API_KEY=sk-ant-...
# GEMINI_API_KEY=...
# OPENROUTER_API_KEY=sk-or-...

# 渠道 Token（按需设置）
# TELEGRAM_BOT_TOKEN=123456:ABCDEF
# DISCORD_BOT_TOKEN=...
# SLACK_BOT_TOKEN=xoxb-...
# SLACK_APP_TOKEN=xapp-...

# 工具（可选）
# BRAVE_API_KEY=...
# ELEVENLABS_API_KEY=...
```

---

## 参考链接

| 项目          | 链接                                          |
|--------------|----------------------------------------------|
| 官网          | https://openclaw.ai                          |
| 完整文档      | https://docs.openclaw.ai                     |
| 快速入门      | https://docs.openclaw.ai/start/getting-started |
| 配置参考      | https://docs.openclaw.ai/gateway/configuration |
| 安全指南      | https://docs.openclaw.ai/gateway/security    |
| 架构概述      | https://docs.openclaw.ai/concepts/architecture |
| ClawHub 技能  | https://clawhub.com                          |
| GitHub 仓库   | https://github.com/openclaw/openclaw         |
| Discord 社区  | https://discord.gg/clawd                     |

---

*文档生成时间：2026-03-12 | OpenClaw 2026.3.9*
