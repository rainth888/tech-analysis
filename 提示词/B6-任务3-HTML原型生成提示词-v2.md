# 任务3：AI生成HTML原型页面 - 提示词

> **📌 使用说明**: 本提示词用于生成可交互的HTML原型页面，包含样式、交互逻辑和用户反馈机制。

**前置依赖**: 需要先完成任务1（设计元素）和任务2（交互流程）

---

## 🎭 R - 角色定义

你是一位资深前端开发工程师，拥有10年Web应用开发经验，擅长：

- 原生HTML/CSS/JavaScript开发（无框架依赖）
- 响应式布局与现代CSS技术（Flexbox/Grid）
- 表单验证与用户交互设计
- 浏览器存储与状态管理（localStorage/sessionStorage）
- 代码规范与可维护性设计

---

## 📋 T - 任务描述

基于任务1和任务2的产出，生成ITSM需求助手插件的HTML原型页面。

### 输入材料

#### 材料1：设计元素（来自任务1）

```
{在这里粘贴任务1的完整输出：页面结构分析、UI组件清单、数据字段定义}
```

#### 材料2：交互流程（来自任务2）

```
{在这里粘贴任务2的关键交互说明表格、交互反馈设计表格和状态流转定义}
```

### 任务上下文

本任务是敏捷开发流程中原型开发阶段，需要将设计元素和交互规范转化为可运行的HTML原型。原型用于产品评审和用户验证，需保证视觉效果和交互逻辑的完整性。

---

## 🎯 G - 目标与意图

### 核心目标

生成可独立运行的HTML原型，准确还原设计元素和交互规范，支持产品评审和用户体验验证。

### 具体目标

1. **视觉还原度**: 准确实现设计元素中定义的UI组件和样式规范
2. **交互完整性**: 实现交互流程中定义的所有交互行为和反馈机制
3. **代码可维护性**: 代码结构清晰、注释完善、命名规范
4. **独立运行性**: 无需任何构建工具，浏览器直接打开即可使用

### 业务价值

- **为产品经理**: 提供可操作的原型，支持需求评审和用户验证
- **为UI设计师**: 验证设计方案的可实现性和视觉效果
- **为开发团队**: 提供前端开发的参考实现和代码模板
- **为测试团队**: 提供交互测试的早期验证环境

### 成功标准

- ✅ HTML文件可在浏览器直接打开并正常运行
- ✅ UI组件样式符合设计规范（配色、圆角、阴影、间距）
- ✅ 交互行为符合交互规范（触发、响应、反馈、状态流转）
- ✅ 表单验证逻辑完整（必填、格式、长度）
- ✅ 代码包含详细的中文注释

---

## 📤 O - 输出要求

### 1. 技术规范

#### 基础技术栈
- 使用纯HTML + CSS + JavaScript实现
- 无需任何框架（Vue/React/Angular），可直接在浏览器打开
- 所有代码在一个HTML文件中（含内联CSS和JS）

#### 样式设计规范
- 参考Ant Design设计语言
- 布局：Flexbox或Grid
- 圆角：4-8px
- 阴影：0 2px 8px rgba(0,0,0,0.1)
- 主色调：蓝色#1890ff
- 成功色：绿色#52c41a
- 警告色：橙色#faad14
- 错误色：红色#f5222d
- 侧边栏宽度：400px

#### 交互功能规范
- 完整的表单验证逻辑（必填、长度、格式）
- localStorage存储模拟数据
- 成功/错误/警告提示消息（自动消失）
- 按钮loading状态和disabled状态
- 防抖优化（搜索200ms、检测500ms）

#### 代码质量规范
- 代码结构清晰，HTML语义化
- 添加详细的中文注释（每个函数、关键逻辑）
- 变量和函数命名语义化（驼峰命名）
- CSS样式模块化（使用类选择器，避免ID选择器）

### 2. 输出结构

生成以下HTML原型页面的**完整代码**：

#### 第1个文件：侧边栏主界面.html（必须）

包含以下功能区域：

1. **系统选择区域**
   - 6个系统分类卡片（客户管理、计费系统、网络运维、数据平台、运维工具、HR系统）
   - 搜索框（支持实时过滤，防抖200ms）
   - 系统列表（可点击选择，选中高亮）
   - 信心度反馈（确定/不太确定/不确定 三个选项）

2. **模板推荐区域**
   - 模板推荐卡片（显示推荐理由和匹配度百分比）
   - 手动选择模板（Bug反馈/功能优化/新功能 三种类型）
   - 切换模板按钮

3. **结构化字段区域**
   - 需求标题输入框（带字数统计）
   - 需求背景文本域（带引导问题提示）
   - 优化目标文本域
   - 使用场景文本域
   - 验收标准文本域
   - 字段验证提示（实时显示）

4. **示例库区域**
   - "查看示例"按钮
   - 示例列表（至少2个示例）
   - "使用此示例"按钮

5. **质量检测区域**
   - 实时质量评分（0-100分，带颜色分级）
   - 评分细项展开（完整性、字数、关键词、逻辑）
   - 缺失字段高亮提示

6. **操作区域**
   - "填充到ITSM"主按钮（带loading状态）
   - "重置"按钮
   - 提交前警告对话框（模态框）

### 3. 质量要求

#### 视觉一致性（强制）
- 所有组件遵循相同的设计规范
- 间距统一（8px/16px/24px）
- 字体大小统一（12px/14px/16px/20px）
- 颜色使用CSS变量统一管理

#### 交互完整性（强制）
- 所有按钮有hover/active/disabled状态
- 表单验证有实时反馈
- 操作有成功/失败提示

#### 代码可读性（强制）
- HTML结构语义化（section/header/form等）
- CSS使用类选择器，命名语义化
- JS函数单一职责，添加注释

### 4. 特别说明

#### 模拟数据
请在JavaScript中定义模拟数据：
- 系统分类和系统列表
- 模板配置（字段、提示语）
- 示例数据（至少2条完整示例）

#### 提示消息组件
实现一个通用的Toast组件：
- 支持success/error/warning/info四种类型
- 支持自动消失（可配置时长）
- 支持手动关闭
- 显示在页面顶部居中

#### 模态对话框组件
实现一个通用的Modal组件：
- 支持标题、内容、按钮配置
- 支持遮罩层点击关闭
- 支持ESC键关闭

---

## ✨ 输出格式

直接输出完整的HTML文件代码，不要有任何前言或解释。代码需包含完整的HTML结构、CSS样式和JavaScript逻辑。

---

## ✅ 期望输出格式

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ITSM需求助手 - 侧边栏</title>
    <style>
        /* ========== CSS变量定义 ========== */
        :root {
            --primary-color: #1890ff;
            --success-color: #52c41a;
            --warning-color: #faad14;
            --error-color: #f5222d;
            --border-radius: 8px;
            --shadow: 0 2px 8px rgba(0,0,0,0.1);
            --spacing-sm: 8px;
            --spacing-md: 16px;
            --spacing-lg: 24px;
        }
        
        /* ========== 全局样式 ========== */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
            font-size: 14px;
            color: #333;
        }
        
        /* ========== 侧边栏容器 ========== */
        .sidebar { 
            width: 400px; 
            height: 100vh; 
            overflow-y: auto; 
            padding: var(--spacing-md); 
            background: #f0f2f5; 
        }
        
        /* ========== 区域卡片 ========== */
        .section { 
            background: white; 
            padding: var(--spacing-md); 
            margin-bottom: var(--spacing-md); 
            border-radius: var(--border-radius); 
            box-shadow: var(--shadow); 
        }
        
        .section-title {
            font-size: 16px;
            font-weight: 600;
            margin-bottom: var(--spacing-md);
            color: #333;
        }
        
        /* ========== 按钮样式 ========== */
        .btn {
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.2s;
        }
        
        .btn-primary {
            background: var(--primary-color);
            color: white;
        }
        
        .btn-primary:hover {
            background: #40a9ff;
        }
        
        .btn-primary:disabled {
            background: #d9d9d9;
            cursor: not-allowed;
        }
        
        .btn-loading {
            position: relative;
            pointer-events: none;
        }
        
        /* ========== Toast提示组件 ========== */
        .toast {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            padding: 12px 24px;
            border-radius: 4px;
            color: white;
            z-index: 1000;
            animation: fadeIn 0.3s ease;
        }
        
        .toast-success { background: var(--success-color); }
        .toast-error { background: var(--error-color); }
        .toast-warning { background: var(--warning-color); }
        
        /* ... 更多样式 ... */
    </style>
</head>
<body>
    <!-- ========== 侧边栏主容器 ========== -->
    <div class="sidebar">
        
        <!-- ========== 系统选择区域 ========== -->
        <div class="section">
            <h3 class="section-title">📌 系统选择</h3>
            <!-- 系统分类卡片 -->
            <div class="category-grid">
                <!-- 6个分类卡片 -->
            </div>
            <!-- 搜索框 -->
            <input type="text" class="search-box" placeholder="搜索系统名称...">
            <!-- 系统列表 -->
            <div class="system-list">
                <!-- 系统列表项 -->
            </div>
        </div>
        
        <!-- ========== 模板推荐区域 ========== -->
        <div class="section">
            <h3 class="section-title">📋 需求模板</h3>
            <!-- 模板推荐卡片 -->
            <!-- 手动选择模板 -->
        </div>
        
        <!-- ========== 结构化字段区域 ========== -->
        <div class="section">
            <h3 class="section-title">✏️ 需求详情</h3>
            <!-- 表单字段 -->
        </div>
        
        <!-- ========== 质量检测区域 ========== -->
        <div class="section">
            <h3 class="section-title">📊 质量评分</h3>
            <!-- 评分显示 -->
        </div>
        
        <!-- ========== 操作区域 ========== -->
        <div class="section action-section">
            <button class="btn btn-primary" id="fillBtn">填充到ITSM</button>
            <button class="btn btn-default" id="resetBtn">重置</button>
        </div>
        
    </div>
    
    <!-- ========== Toast提示容器 ========== -->
    <div id="toastContainer"></div>
    
    <!-- ========== 模态对话框 ========== -->
    <div class="modal" id="confirmModal">
        <!-- 对话框内容 -->
    </div>
    
    <script>
        // ========================================
        // 模拟数据定义
        // ========================================
        
        /**
         * 系统分类数据
         */
        const systemCategories = [
            { id: 'crm', name: '客户管理', icon: '👥', systems: ['CRM系统', '客户画像', '营销系统'] },
            { id: 'billing', name: '计费系统', icon: '💰', systems: ['计费中心', '账务系统', '支付网关'] },
            // ... 更多分类
        ];
        
        /**
         * 模板配置
         */
        const templates = [
            { 
                id: 'bug', 
                name: 'Bug反馈', 
                fields: ['背景', '复现步骤', '期望结果', '实际结果'],
                placeholders: {
                    background: '请描述发现Bug的场景...',
                    // ...
                }
            },
            // ... 更多模板
        ];
        
        /**
         * 示例数据
         */
        const examples = [
            {
                id: 1,
                title: 'CRM系统客户列表加载缓慢',
                template: 'bug',
                content: {
                    background: '在处理大客户订单时...',
                    // ...
                }
            },
            // ... 更多示例
        ];
        
        // ========================================
        // 通用工具函数
        // ========================================
        
        /**
         * 防抖函数
         * @param {Function} fn 要执行的函数
         * @param {number} delay 延迟时间（毫秒）
         */
        function debounce(fn, delay) {
            let timer = null;
            return function(...args) {
                clearTimeout(timer);
                timer = setTimeout(() => fn.apply(this, args), delay);
            };
        }
        
        /**
         * 显示Toast提示
         * @param {string} message 提示内容
         * @param {string} type 类型：success/error/warning/info
         * @param {number} duration 持续时间（毫秒）
         */
        function showToast(message, type = 'info', duration = 3000) {
            const toast = document.createElement('div');
            toast.className = `toast toast-${type}`;
            toast.textContent = message;
            document.getElementById('toastContainer').appendChild(toast);
            
            setTimeout(() => toast.remove(), duration);
        }
        
        /**
         * 显示确认对话框
         * @param {string} title 标题
         * @param {string} content 内容
         * @param {Function} onConfirm 确认回调
         * @param {Function} onCancel 取消回调
         */
        function showConfirm(title, content, onConfirm, onCancel) {
            // 实现模态对话框逻辑
        }
        
        // ========================================
        // 业务逻辑函数
        // ========================================
        
        /**
         * 计算质量评分
         * @returns {number} 0-100的评分
         */
        function calculateQualityScore() {
            let score = 0;
            // 完整性评分（40分）
            // 字数评分（20分）
            // 关键词评分（20分）
            // 逻辑评分（20分）
            return score;
        }
        
        /**
         * 验证表单
         * @returns {object} { valid: boolean, errors: string[] }
         */
        function validateForm() {
            const errors = [];
            // 验证各字段
            return { valid: errors.length === 0, errors };
        }
        
        /**
         * 填充到ITSM
         */
        async function fillToItsm() {
            // 1. 验证表单
            // 2. 检查质量评分
            // 3. 显示警告（如需要）
            // 4. 拼接Markdown
            // 5. 填充到ITSM描述框
            // 6. 显示成功提示
        }
        
        // ========================================
        // 事件绑定
        // ========================================
        
        document.addEventListener('DOMContentLoaded', function() {
            // 初始化页面
            // 绑定事件监听
        });
    </script>
</body>
</html>
```

---

## ✅ 完成检查清单

- [ ] HTML文件是否可以在浏览器直接打开？
- [ ] 页面样式是否符合设计规范（配色、圆角、阴影）？
- [ ] 是否包含完整的表单验证逻辑？
- [ ] 是否实现了localStorage数据存储？
- [ ] 是否包含Toast提示组件（4种类型）？
- [ ] 是否包含模态对话框组件？
- [ ] 是否添加了详细的中文注释？
- [ ] 按钮是否有loading和disabled状态？
- [ ] 是否实现了防抖优化（200ms/500ms）？
- [ ] 是否使用了CSS变量管理主题色？

---

## 💡 分步骤生成建议

如果一次性生成内容过长，可以分步骤请求：

### 步骤1：生成基础框架和样式

```
请先生成"侧边栏主界面.html"的基础框架，包括：
1. HTML基础结构（6个主要区域的div容器）
2. 完整的CSS样式（使用CSS变量、所有组件样式）
3. 模拟数据定义（系统列表、模板配置、示例数据）

暂时不需要实现JavaScript交互逻辑，只需要静态展示。
```

### 步骤2：添加交互逻辑

```
在上一步的基础上，添加以下JavaScript交互功能：
1. 系统选择功能（分类点击展开、搜索过滤、系统选择高亮）
2. 模板推荐功能（监听标题输入、推荐模板、切换模板）
3. 表单验证功能（实时验证、错误提示、字数统计）
4. 质量评分功能（实时计算、分级显示颜色）

请补充完整的JavaScript代码，保留原有的HTML和CSS。
```

### 步骤3：完善通用组件

```
请补充以下通用组件的完整实现：
1. Toast提示组件（success/error/warning/info，自动消失）
2. 模态对话框组件（标题、内容、双按钮、遮罩层）
3. 按钮loading状态（loading图标、禁用交互）
4. 防抖函数封装（统一的debounce实现）

请提供完整的优化后代码。
```

---

## 🔧 测试步骤

### 1. 保存文件
将生成的HTML保存为`侧边栏主界面.html`

### 2. 浏览器测试
1. 双击打开HTML文件
2. 测试系统选择功能（点击分类、搜索、选择系统）
3. 测试模板推荐功能（输入标题、查看推荐）
4. 测试字段填写功能（填写各字段、查看实时验证）
5. 测试质量评分功能（查看实时评分、评分细项）
6. 测试示例库功能（查看示例、使用示例）
7. 测试填充功能（点击填充按钮、查看警告对话框）

### 3. 功能验证清单
- [ ] 表单验证是否正常（必填、长度）
- [ ] 数据是否保存到localStorage
- [ ] Toast提示是否正常显示和消失
- [ ] 模态对话框是否正常弹出和关闭
- [ ] 质量评分是否实时更新
- [ ] 按钮loading状态是否正常
- [ ] 样式是否美观一致

---

## 🚨 常见问题解决

| 问题 | 原因 | 解决方案 |
|-----|-----|---------|
| 样式显示异常 | CSS选择器优先级问题 | 使用更具体的类选择器，避免!important |
| JavaScript报错 | DOM元素未找到 | 确保在DOMContentLoaded后执行JS |
| localStorage数据丢失 | 浏览器隐私模式或数据格式错误 | 使用JSON.stringify/parse，检查浏览器设置 |
| Toast不消失 | setTimeout未正确设置 | 检查定时器是否正确清除 |
| 按钮无法点击 | disabled状态未恢复 | 确保异步操作完成后恢复按钮状态 |

---

## 📚 优化提示词示例

如果生成的页面不够理想，可以追加要求：

```
请优化以下方面：

1. 样式优化：
   - 统一组件间距（使用8的倍数：8px/16px/24px）
   - 添加过渡动画（transition: all 0.2s ease）
   - 优化按钮hover效果（颜色变浅、阴影增强）
   - 添加focus状态样式（outline或box-shadow）

2. 交互优化：
   - 添加骨架屏加载状态
   - 优化Toast的淡入淡出动画
   - 添加确认对话框的遮罩层动画
   - 表单字段focus时高亮标签

3. 功能增强：
   - 添加键盘快捷键（Ctrl+Enter提交、Esc关闭对话框）
   - 添加草稿自动保存（每30秒保存一次）
   - 添加字段输入时的实时字数统计
   - 添加历史记录功能（最近5条）

请提供优化后的完整代码。
```
