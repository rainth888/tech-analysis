# 🦞 OpenClaw 个人助手能力详解

> 适用版本：OpenClaw 2026.3.9 | 基于源码深度分析

---

## 一、OpenClaw 作为个人助手的核心能力

OpenClaw 是一个**本地优先的 AI 助手网关**，运行在你自己的电脑上，通过网页界面或聊天渠道（Telegram/WhatsApp 等）与你交互。AI Agent 可以调用多种内置工具来完成实际任务。

---

## 二、能力矩阵

| 能力 | 支持情况 | 实现方式 |
|------|---------|---------|
| 🌐 访问浏览器 | ✅ 支持 | 内置 Browser 工具（Chrome CDP） |
| 💻 PowerShell 命令 | ✅ 支持 | 内置 bash_exec 工具 |
| 🐧 WSL Ubuntu 命令 | ✅ 支持 | 通过 PowerShell 调用 `wsl` 命令 |
| 📁 文件读写 | ✅ 支持 | 内置 file_read/file_write 工具 |
| 📊 Excel 操作 | ✅ 支持 | Agent 自动编写 Python 脚本 |
| 🖥️ Windows GUI 操控 | ❌ 不支持 | 无 RPA 能力，不能点击桌面应用 |
| 📧 发送邮件 | ⚠️ 间接支持 | Agent 编写 Python/PowerShell 脚本 |
| ⏰ 定时任务 | ✅ 支持 | 内置 Cron 系统 |
| 📱 手机远程 | ✅ 支持 | 伴侣 App（iOS/Android） |

---

## 三、各能力详解

### 3.1 浏览器访问 ✅

OpenClaw 内置了 **Browser 工具**（源码 `src/browser/`），基于 Chrome CDP 协议，Gateway 启动时自动监听：

```
Browser control listening on http://***:***@example.com，
主题是"项目进度汇报"，
内容是"本周完成了 OpenClaw 的安装和配置测试"。
我的邮箱是 myemail@gmail.com，SMTP 服务器是 smtp.gmail.com。
```

Agent 会自动编写使用 `smtplib` 的 Python 脚本并执行（需审批）。

#### 方式二：通过 PowerShell 发邮件

```
用 PowerShell 的 Send-MailMessage 帮我发一封测试邮件
```

#### 方式三：安装邮件 Skill（未来扩展）

OpenClaw 的 Skills 系统支持从 ClawHub 安装扩展，未来可能有专用邮件 Skill。

---

## 四、典型个人助手使用场景

| 场景 | 具体指令示例 |
|------|-----------|
| **文件管理** | "帮我整理 D:\downloads 目录，按文件类型分类" |
| **信息搜索** | "搜索最近的 Node.js 安全更新" |
| **代码开发** | "读取 E:\project\app.js 并修复其中的 bug" |
| **数据处理** | "帮我分析 data.csv 文件，生成统计图表" |
| **Excel 报表** | "读取销售数据，生成月度汇总报表" |
| **系统管理** | "查看系统内存和 CPU 使用率" |
| **定时任务** | 在 WebChat 的"定时任务"页面配置 Cron 定期执行 |
| **多渠道** | 配置 Telegram/WhatsApp Bot Token 后在手机上对话 |
| **脚本编写** | "帮我写一个 Python 脚本批量处理图片" |
| **Git 操作** | "查看 E:\project 的 git log 最近10条提交" |

---

## 五、当前系统状态

| 项目 | 状态 | 说明 |
|------|------|------|
| Gateway 运行 | ✅ 已可用 | `start-gateway.ps1` 一键启动 |
| WebChat UI | ✅ 已可用 | `http://127.0.0.1:18789` |
| **API Key** | ❌ **需更换** | 当前 Key 超时，换一个有效的即可 |
| 浏览器工具 | ✅ 内置 | 自动使用 Chrome |
| 命令执行 | ✅ 内置 | PowerShell + WSL 都支持 |
| 文件读写 | ✅ 内置 | 任意文件 |
| Excel 操作 | ✅ 通过 Python | 需安装 pandas/openpyxl |

### 让系统完全可用的唯一步骤

编辑 `C:\Users\Administrator\.openclaw\.env`，将 `OPENAI_API_KEY=` 替换为有效的 Key，重启 Gateway 即可。

---

*文档生成时间：2026-03-14 | 基于 OpenClaw 2026.3.9 源码分析*
