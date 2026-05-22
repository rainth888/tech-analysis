# 通用 Skills 与 项目专用 Skills 的区分及使用技巧

正如您所理解的，**以前写过的很多 Shell 脚本、Python 自动化脚本、SQL 查询语句，只要为其加上一层“自然语言描述（API Schema）”，让 AI 知道“这个脚本是干什么的、需要传入什么参数、返回什么结果”，它们就直接化身成为了强大的 AI Skills。**

随着您积累的脚本和功能越来越多，如何管理和调用这些 Skills 就成了一个关键问题。业界通常将它们划分为**通用 Skills**和**项目专用 Skills**。

---

## 一、 如何区分两者？

### 1. 通用 Skills (Generic Skills)
**定义**：不依赖于特定业务逻辑、特定代码库或特定公司的底层工具。它们具有极高的复用性，可以跨项目、跨行业使用。
**特征**：底层、原子化、无状态。
**典型案例**：
- **文件操作**：`读取文件内容 (read_file)`、`全局内容搜索 (grep_search)`、`写入文件 (write_file)`
- **系统交互**：`执行终端命令 (run_bash_command)`、`获取系统状态 (get_system_info)`
- **基础网络**：`网页内容抓取 (fetch_url)`、`执行 Web 搜索 (web_search)`
- **基础 Git**：`获取分支状态 (git_status)`、`提交代码 (git_commit)`

### 2. 项目专用 Skills (Project-Specific Skills)
**定义**：深度绑定某个特定业务场景、硬件平台、私有数据库或内部工作流的工具。一旦脱离了这个特定项目，该 Skill 就毫无意义。
**特征**：高度封装、包含复杂的业务校验逻辑、通常聚合了多个底层操作。
**典型案例**：
- **软件/Odoo项目**：`重启特定Odoo开发环境 (restart_odoo_docker)`、`查询 ChowTaiKing 数据库昨日订单总额 (query_ctk_daily_sales)`
- **硬件嵌入式项目**：`编译 GK7201c300 固件并烧录 (build_and_flash_gk7201)`、`通过串口发送心跳包以唤醒机械臂 (wake_up_robotic_arm_via_serial)`
- **运维/部署**：`将当前 Tech-Analysis 仓库增量同步至内部文档服务器 (sync_tech_docs)`

---

## 二、 核心使用与管理技巧

在实际让 AI Agent 工作时，区分这两者的最大意义在于**上下文管理**和**大模型防止“幻觉”**。

### 技巧 1：控制 AI 的工具箱大小（动态加载）
大模型在一次对话中能记住的“技能说明书”是有限的。如果把几百个项目专用 Skills 全部扔给 AI，它会陷入混乱（即所谓的“工具分配幻觉”）。
- **做法**：**通用 Skills 设为常驻（Global）**，任何对话都默认提供（比如读写文件、跑基础命令）。**项目专用 Skills 设为动态加载（Local/Dynamic）**，只有当 AI 识别到当前处于 `Odoo` 目录或正在处理 `GK7201c300` 任务时，才把特定的项目 Skills 暴露给它。

### 技巧 2：用“项目专用 Skill”屏蔽复杂流程
AI 在执行长长的 Bash 命令或复杂的环境配置时极易出错。
- **反面教材**：给 AI 提供一个通用的 `run_bash_command`，指望它自己去拼凑出针对 GK7201 的交叉编译命令。
- **最佳实践**：写一个包含好所有环境路径、依赖检查的 `build_gk7201.sh` 脚本。然后将这个脚本封装成项目专用 Skill `compile_firmware`。AI 只需要决定“何时调用”，而具体的“怎么编译”由您写死的可靠脚本来兜底。**用传统的确定性代码，来兜底 AI 的不确定性。**

### 技巧 3：让脚本返回“AI 友好”的错误提示
以前写 Shell/Python 脚本，报错信息是给人类工程师看的（比如 `Error: NullPointerException at line 42`）。现在作为 Skill，报错信息是给 AI 看的。
- **优化方法**：在项目专用 Skill 中捕获异常，并返回带有指导意义的自然语言建议。
  - *普通报错*：`Command failed with exit code 1.` (AI 可能会卡住，不知道怎么办)
  - *AI 友好报错*：`编译失败，因为找不到头文件 'hardware_def.h'。请使用 generic_search 技能去查找该头文件是否在 include 目录下，然后修改 Makefile。` (AI 看到这句话，会立即按照你的指导展开自我修复)。

### 技巧 4：组合技 (Chain of Skills)
通用 Skills 往往是用来**获取上下文**的，项目专用 Skills 是用来**执行决定性动作**的。
- **工作流范例**：AI 先使用通用 Skill `grep_search` 在 `E:\_projects\_tech-analysis` 寻找最新的编译规则 -> 然后使用通用 Skill `read_file` 阅读规则详情 -> 最后调用项目专用 Skill `trigger_remote_build_server` 执行构建。

---

## 三、 给您的下一步建议

在您的 `E:\_projects\_tech-analysis` 或具体的代码仓库中，您可以建立一个名为 `.agents/skills/` 的目录。
开始将您以前写得最好的那些 Python 或 Bash 自动化脚本移动进去，并在同级目录下写一个简单的 JSON 或 Markdown 描述文件，清晰地告诉 AI：**“这个脚本叫什么、用来解决什么特定问题、需要什么输入”**。这便是打造您个人专属智能体帝国的第一步。
