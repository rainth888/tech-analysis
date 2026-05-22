# 🦞 OpenClaw 使用说明文档

> **版本**：2026.3.9 | **运行环境**：Node.js ≥ 22 | **官网**：https://***:***@latest
# 或者
pnpm add -g openclaw@latest
```

### 方式二：从源码构建

```bash
git clone https://***:***@gateway-host
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
