# Antigravity CDP Usage Summary (with Clash)
本文档总结了在运行 Clash 代理环境下，使用 Antigravity (VS Code IDE) 进行 CDP (Chrome DevTools Protocol) 浏览器自动化连接的配置要点及故障排查经验。
## 1. 核心前提：Chrome 浏览器安装
Antigravity 的浏览器代理（Browser Agent）依赖于系统本地的 Chrome 浏览器实例。
*   **必须安装 Google Chrome**：系统无法自动找到 Chrome 时会出现 `Failed to launch browser: Chrome installation not found` 错误。
*   **下载地址**：[https://www.google.com/chrome/](https://www.google.com/chrome/)
*   **路径配置**：通常安装在默认位置即可。如果安装在非标准路径，需在 Antigravity 设置中指定 Chrome 二进制文件路径。
## 2. Clash 与 CDP 连接的网络环境
CDP 通讯通过本地 WebSocket (通常是 `ws://127.0.0.1:xxxx`) 进行。在开启 Clash 等代理软件时，可能会出现连接干扰。
### 常见问题
*   **端口拦截**：如果 Clash 开启了“系统代理”或“TUN 模式”，且配置不当，可能会拦截发送往 `127.0.0.1` 或 `localhost` 的流量，导致 Antigravity 无法连接到浏览器实例（连接超时或拒绝连接）。
### 最佳实践配置
1.  **Clash 模式**：建议使用 **Rule (规则)** 模式，而不是 Global (全局) 模式。
2.  **Bypass (绕过) 设置**：
    *   确保 Clash 配置或系统代理设置中，`localhost`, `127.0.0.1` 在“请勿使用代理服务器的地址”列表中。
    *   Antigravity 内部通常会尝试设置 `NO_PROXY` 环境变量，但在某些强接管模式（如 TUN 模式）下可能需要手动检查。
3.  **连接测试**：
    *   在确保 Chrome 已安装的前提下，让 Agent 尝试访问一个简单页面（如 `example.com`）。
    *   如果成功获取页面标题，说明 CDP 通道畅通。
## 3. 故障排查清单
如果遇到无法打开浏览器或“黑屏/连接失败”：
1.  [x] **检查 Chrome 是否安装**：这是最常见的原因。
2.  [ ] **检查 Clash 设置**：暂时关闭 Clash System Proxy 观察是否恢复正常。如果是，由于代理规则导致，需调整规则放行本地回环流量。
3.  [ ] **检查端口占用**：确保没有其他程序占用了 CDP 调试端口（Antigravity 会自动选择空闲端口，但在极端情况下可能冲突）。
## 4. 验证结果
经过测试，在正确安装 Chrome 并保持默认 Clash 规则模式下，Antigravity 可成功启动浏览器并完成 CDP 指令交互（如截图、读取 DOM、点击操作）。


#
打开“setting”，搜“proxy”，找到“Http: No Proxy”，然后添加“localhost, 127.0.0.1, ::1”，重启即可。

