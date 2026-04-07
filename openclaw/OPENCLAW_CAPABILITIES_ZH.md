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
Browser control listening on http://127.0.0.1:18791/
```

**使用示例**：
```
帮我搜索"2026年人工智能发展趋势"
```
```
打开 https://news.ycombinator.com 看看今天的热门新闻
```
```
帮我截图 https://github.com 的首页
```

**能力范围**：
- ✅ 打开网页、提取文字内容
- ✅ 截图网页
- ✅ 搜索引擎搜索
- ❌ 不能登录需要账号的网站（无法处理复杂 JS 交互）

---

### 3.2 PowerShell 命令执行 ✅

OpenClaw 内置了 `bash_exec` 和 `bash_process` 工具（源码 `src/agents/bash-tools.exec.ts`，21KB），在 Windows 上默认使用 PowerShell 执行命令。

**安全机制**：每次命令执行前会弹出 **审批请求**，你需要在界面中手动点击「允许」才会执行。

**使用示例**：
```
查看当前系统的磁盘使用情况
```
```
帮我列出 E:\openclaw 目录下的所有文件
```
```
查看目前运行的 Node.js 进程
```
```
查看系统内存和 CPU 使用率
```

---

### 3.3 WSL Ubuntu 命令 ✅

因为 PowerShell 可以通过 `wsl` 命令调用 Ubuntu，Agent 可以间接执行 Linux 命令。

**使用示例**：
```
在 WSL Ubuntu 中查看 Linux 内核版本
```
```
用 WSL 运行 "ls -la /mnt/e/openclaw"
```
```
在 WSL 中安装 htop 工具并查看系统状态
```

Agent 实际会执行类似 `wsl -d Ubuntu-22.04 -- bash -c "uname -a"` 的命令。

---

### 3.4 Windows 应用访问 ⚠️ 有限支持

OpenClaw **不能直接操控 Windows GUI 应用**（不像 RPA 工具那样点击按钮），但可以通过命令行与应用交互：

| 能力 | 说明 |
|------|------|
| ✅ 启动应用 | 通过 `Start-Process` 命令启动 |
| ✅ 操作文件 | 读写文件系统上的任何文件 |
| ✅ 命令行工具 | 调用 git、npm、python 等 CLI 工具 |
| ❌ GUI 操控 | 不能点击、拖拽桌面应用的界面 |

**使用示例**：
```
用记事本打开 E:\openclaw\QUICKSTART_ZH.md
```
```
帮我用 python 写一个脚本，批量重命名 D:\photos 目录下的照片
```

---

### 3.5 Excel 操作 ✅

OpenClaw Agent 通过 `bash_exec` 工具执行 Python 脚本来读写 Excel。你只需在聊天中直接说你要做什么。

**前提**：系统上需要有 Python 和相关库。如果没有，让 Agent 帮你装：
```
帮我安装 Python 的 pandas 和 openpyxl 库
```

#### 可执行的 Excel 操作

| 操作 | 示例指令 |
|------|---------|
| 读取内容 | "读取 xx.xlsx 的内容" |
| 数据统计 | "统计 xx.xlsx 中每个部门的平均工资" |
| 筛选数据 | "筛选出金额大于1万的记录" |
| 修改数据 | "把A列的所有空值替换为0" |
| 新建 Excel | "帮我创建一个包含本周工作计划的 Excel" |
| 格式转换 | "把 xx.xlsx 转换成 CSV 格式" |
| 合并文件 | "把 a.xlsx 和 b.xlsx 合并成一个文件" |
| 生成图表 | "根据 xx.xlsx 的数据生成折线图" |
| 数据透视 | "对销售数据做一个按地区分组的透视表" |

#### 工作流程

```
用户: "帮我读取 D:\data\销售报表.xlsx，统计每月销售总额"
  ↓
Agent: 自动编写 Python 脚本（使用 pandas + openpyxl）
  ↓
系统: 弹出审批请求 → 你点"允许"
  ↓
Agent: 执行脚本，返回统计结果
```

对于 **CSV 文件**（纯文本表格），Agent 可以用 `file_read` 工具直接读取，无需 Python。

---

### 3.6 发送邮件 ⚠️ 间接支持

OpenClaw 没有内置邮件发送工具，但有三种方式实现：

#### 方式一：让 Agent 写 Python 脚本发邮件（推荐）

```
帮我用 Python 发一封邮件到 test@example.com，
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
