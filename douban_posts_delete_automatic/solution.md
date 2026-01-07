# 豆瓣讨论帖自动删除方案

本文档概述了自动删除豆瓣讨论帖的解决方案。涵盖了不同用户账号的设置、使用和特定操作流程。

## 1. 方案概述

该方案使用由 **Selenium WebDriver** 驱动的 Python 脚本 (`delete_douban_posts.py`)。它自动化浏览器执行以下操作：
1.  **登录**：检测登录状态，并在需要时提示手动登录。
2.  **导航**：打开用户的“发表的讨论”页面 (`.../publish`)。
3.  **删除**：遍历帖子，点击“删除”链接。
4.  **确认**：处理豆瓣自定义的“菜单式”弹窗以及随后的浏览器原生确认警告。

## 2. 环境设置

### 前置条件
- **Python 3.10+**：已安装在系统中。
- **Chrome 浏览器**：已安装。
- **Selenium**：已通过 pip 安装 (`pip install selenium`)。

### 目录结构
```
E:\temp\20251225\
    ├── delete_douban_posts.py    # 主自动化脚本
    └── chrome_profile\           # 本地 Chrome 用户数据（用于持久化登录 Cookie）
```

## 3. 账号流程

该脚本旨在通过修改目标 URL 来处理多个账号。

### 用户 1：`12345678`（已完成）
- **目标 URL**：`https://www.douban.com/group/people/12345678/publish`
- **状态**：所有有效帖子已被删除。

### 用户 2：`87654321`（活跃）
- **目标 URL**：`https://www.douban.com/group/people/87654321/publish`
- **逻辑**：
    - 脚本自动检查已登录用户是否匹配目标 ID (`87654321`)。
    - 如果检测到不匹配（例如，仍登录为上一个用户），它将**自动登出**并刷新页面以允许切换账号。

## 4. 如何运行

1.  打开终端（PowerShell 或 CMD）。
2.  导航到目录：
    ```powershell
    cd e:\temp\20251225
    ```
3.  运行脚本：
    ```powershell
    python delete_douban_posts.py
    ```
4.  **登录**：会打开一个 Chrome 窗口。如果尚未登录，它会提示您。请使用该浏览器窗口登录目标账号。
5.  **监控**：一旦确认登录，脚本将自动开始删除帖子。**请勿关闭浏览器窗口。**

## 5. 技术细节与故障排除

- **弹窗处理**：豆瓣使用非标准的“移除/删除”菜单 div (`div.author-action-menu-item`) 而非简单的按钮。脚本使用 XPath 专门定位此元素。
- **原生警告**：点击菜单中的“删除”后，会出现浏览器原生警告（“确定要删除吗？”）。脚本使用 `driver.switch_to.alert.accept()` 来处理此情况。
- **“未找到删除链接”**：某些旧的或锁定的帖子可能没有删除选项。脚本将这些 URL 记录在 `failed_urls` 集合中以避免死循环，并在后续尝试中跳过它们。
- **登录检测**：脚本在尝试任何操作之前，会等待 `nav-user-account` 元素出现以确认登录成功。

## 6. 修改以用于新用户

如需将此脚本用于其他用户：
1.  打开 `delete_douban_posts.py`。
2.  将第 21 行的 `list_url` 变量更改为新用户的发布页面 URL。
    ```python
    list_url = "https://www.douban.com/group/people/YOUR_NEW_ID/publish"
    ```
3.  照常运行脚本。
