



# #########################################################################################################################

# **Odoo 18 的应用架构**，从服务端、前端、数据库等方面的技术栈出发，并结合“入门开发”给你一份学习路线。

---

# 一、Odoo 18 的整体架构

### 1. 服务端（后端）

* **语言**：Python 3.11+
* **框架**：Odoo 自研框架，基于 ORM、模块化设计
* **Web 服务**：自带 HTTP 服务器（基于 Werkzeug），也可通过 Nginx/Apache 反向代理
* **ORM**：Odoo 自带 ORM，封装 PostgreSQL 的表结构，模型类继承 `models.Model`
* **业务逻辑层**：

  * 使用 Python 模块定义 `Model`、`Fields`、`Methods`
  * 使用装饰器（如 `@api.model`, `@api.depends`）实现逻辑和依赖

---

### 2. 前端

* **模板引擎**：QWeb（XML + t-指令，如 `t-field`、`t-foreach`）
* **JavaScript 框架**：Owl (Odoo Web Library，取代旧版 Backbone)

  * 类似 React/Vue 的组件化框架，支持 Hooks、State
* **样式**：Bootstrap 5 + SCSS + Odoo 的 Web Assets 管理系统
* **前端资源管理**：通过 Odoo 的 `assets` 系统合并、压缩、分发

---

### 3. 数据库层

* **数据库**：PostgreSQL（Odoo 18 推荐 v15+）
* **特点**：

  * 多租户：一个 PostgreSQL 实例可承载多个 Odoo 数据库
  * 每个模块可通过 ORM 自动创建表/字段
  * 事务型处理，保持 ACID 一致性

---

### 4. 中间件 / 其他组件

* **消息队列**：Odoo 内置 **bus** 模块，基于长轮询/Redis 做实时通知（如聊天、通知）。
* **定时任务**：内置 **cron jobs**，支持 Python 定时任务。
* **报告引擎**：QWeb PDF/HTML 报表，wkhtmltopdf 用于生成 PDF。
* **IoT**：可通过 Odoo IoT Box 集成打印机、扫描枪、称重设备。

---

# 二、Odoo 18 的模块化

* 每个功能（销售、库存、会计、POS、HR 等）都是一个独立模块。
* 模块内容：

  * **模型（models）**：数据库表与业务逻辑
  * **视图（views）**：表单、列表、看板、日历、报表等
  * **报表（reports）**：QWeb 模板
  * **数据（data）**：初始化 XML/CSV 数据
  * **安全（security）**：访问权限、记录规则
  * **静态文件（static/src）**：JS/CSS/图片

---

# 三、开发入门需要掌握的基础概念

### 1. Python 基础

* 类与继承
* 装饰器（`@api.model`, `@api.depends`）
* ORM 概念（类似 Django ORM，但有自己的 API）

### 2. PostgreSQL 基础

* 基本 SQL（SELECT/INSERT/UPDATE/DELETE）
* 表、索引、约束
* Odoo ORM 会自动建表，但调试时要懂 SQL

### 3. Odoo ORM & Model

* `models.Model`
* 常见字段类型：`fields.Char`, `fields.Many2one`, `fields.One2many`, `fields.Many2many`
* 业务方法：`create`, `write`, `unlink`, `search`

### 4. Odoo 视图系统

* XML 定义视图
* 视图类型：form、tree、kanban、calendar、gantt
* QWeb 模板（报表/前端页面）

### 5. 前端基础

* HTML/XML
* QWeb 指令（`t-field`, `t-esc`, `t-foreach`）
* JS（Owl 框架基础，用于复杂交互）
* CSS/SCSS（票据打印、POS 界面等需要定制样式）

### 6. 安全与权限

* **访问控制列表（ACLs）**：控制模型读/写/删除/创建
* **记录规则（Record Rules）**：控制数据层级权限

### 7. 报表开发

* QWeb 报表
* wkhtmltopdf 打印 PDF
* 报表动作（`ir.actions.report`）

### 8. 部署与环境

* Odoo 通常运行在 **Linux + Python 虚拟环境 + PostgreSQL**
* 前端资源打包用 `assets`，有 `--dev` 模式方便调试

---

# 四、入门学习路径

1. **环境搭建**：安装 Odoo 18 + PostgreSQL，跑起来官方 Demo。
2. **模型练习**：写一个简单模块（客户/订单/产品管理），熟悉 ORM。
3. **视图练习**：修改表单、增加列表字段，体验 XML 继承。
4. **报表练习**：做一个简单的 QWeb 报表，打印 PDF。
5. **前端练习**：改一个 Kanban 视图或写个简单的 Owl 组件。
6. **权限练习**：加上 ACL 和 Record Rules，控制不同角色的访问权限。
7. **综合应用**：结合业务，开发一个“订单+库存+发票”小流程。

---

✅ 总结
Odoo 18 的技术栈是 **Python（服务端） + PostgreSQL（数据库） + QWeb/Owl（前端）**。
入门开发需要熟悉 **Odoo ORM、XML 视图、QWeb 报表、基本前端知识**。
如果你能掌握 Django/Flask + Vue/React + SQL 的思维模式，过渡到 Odoo 会很快。

---

要不要我帮你整理一个 **“Odoo 18 开发者速成学习地图”**（像路线图那样，分阶段列出要学的概念 + 推荐先后顺序）？



# #########################################################################################################################


# **Odoo 18 开发者速成学习地图**，把入门需要的知识点拆成阶段、路线，就像“学习攻略”。这样你能按部就班学习，而不是一股脑乱钻。

---

# 🗺 Odoo 18 开发者速成学习地图

## 阶段一：基础环境与概念

**目标**：跑起来 Odoo，理解基本架构。

* **环境搭建**

  * Python 3.11 基础（虚拟环境 venv/poetry）
  * PostgreSQL 基本安装与操作
  * wkhtmltopdf 安装（报表依赖）
* **Odoo 基础概念**

  * Odoo = Python (后端) + PostgreSQL (数据库) + QWeb/Owl (前端)
  * 模块化结构：`__manifest__.py` / `models` / `views` / `security` / `data`
  * ORM：模型、字段、方法

✅ 输出：能启动 Odoo 18，能创建数据库，能登录后台。

---

## 阶段二：模型与数据库

**目标**：学会用 Odoo ORM 建立业务模型。

* **Python ORM 模型**

  * 继承 `models.Model`
  * 字段类型：`Char`, `Integer`, `Float`, `Boolean`, `Date`, `Datetime`, `Many2one`, `One2many`, `Many2many`
  * 方法：`create`, `write`, `unlink`, `search`, `@api.depends`
* **数据库交互**

  * ORM 自动生成表
  * SQL 与 ORM 对照理解
* **练习**

  * 新建一个简单应用（如“客户档案”或“商品管理”），包含主从表关系。

✅ 输出：会建自定义模型，并能在数据库里看到对应表和数据。

---

## 阶段三：视图与界面

**目标**：学会定义和修改界面。

* **视图类型**

  * form（表单）、tree（列表）、kanban（看板）、calendar（日历）、graph（图表）
* **XML 继承**

  * `xpath` 定位修改
  * 自定义菜单、动作
* **练习**

  * 给你的“客户档案”应用加上表单和列表视图
  * 在菜单栏挂载入口

✅ 输出：能在界面看到你自定义的业务数据。

---

## 阶段四：报表与打印

**目标**：能输出 PDF/票据格式。

* **QWeb 报表模板**（XML + t-field, t-foreach, t-if）
* **ir.actions.report** 报表动作
* **wkhtmltopdf 打印 PDF**
* **练习**

  * 给“订单”做一份小票报表（类似你前面问的票据打印）

✅ 输出：能在 Odoo 里点“打印”，得到自定义报表。

---

## 阶段五：安全与权限

**目标**：能限制谁能看/改什么数据。

* **访问控制（ACL）**：控制模型级别的权限（读/写/删/创建）
* **记录规则（Record Rules）**：控制数据级别的权限（只能看到自己数据）
* **练习**

  * 设置普通用户只能看到自己客户，管理员能看到所有客户

✅ 输出：能为不同用户配置不同的访问权限。

---

## 阶段六：前端开发（进阶）

**目标**：能做交互式页面。

* **QWeb 前端模板**
* **Owl 框架（Odoo Web Library）**

  * 组件化开发
  * State、Props
  * 生命周期 Hooks
* **练习**

  * 给“客户档案”加一个 JS 按钮，点击后弹出提示框
  * 在 Kanban 视图里加自定义字段展示

✅ 输出：能改动前端交互逻辑。

---

## 阶段七：综合实战

**目标**：走通一个完整业务流程。

* **案例**：定制“订单管理系统”

  * 新建订单模型 → 订单行 → 计算总价
  * 报表打印 → 票据/合同
  * 权限配置 → 不同用户角色
  * 前端优化 → 看板/日历视图
* **部署**

  * Docker/Nginx/SSL 部署
  * 多公司/多数据库配置

✅ 输出：从零做一个能上线的小系统。

---

# 学习顺序概览

1. **环境** → Python + Postgres + Odoo 基本运行
2. **模型** → ORM & 字段
3. **视图** → 界面 XML 定义
4. **报表** → QWeb + PDF 打印
5. **权限** → ACL + Record Rules
6. **前端** → Owl 框架、JS 交互
7. **实战** → 整体项目

---

👉 建议学习方式：

* 第 1–4 阶段：适合快速入门，一两周可走通
* 第 5–7 阶段：结合实际项目边做边学

---

要不要我帮你把这个学习地图 **画成一张图表式路线图**（比如流程图或甘特图风格），这样更直观？


# #########################################################################################################################

# 模块（module）内部结构，主要包含以下几个关键部分：

---

## 1. `__manifest__.py`（模块清单文件）

* **作用**：模块的“身份证”。
* **内容**：Python 字典，描述模块的基本信息和依赖。
* **常见字段**：

  * `name`: 模块名称
  * `version`: 模块版本
  * `summary`: 简短描述
  * `depends`: 依赖模块（如 `["sale", "stock"]`）
  * `data`: 加载的数据文件（视图 XML、安全规则等）
  * `application`: 是否在主应用菜单中显示
  * `license`: 授权协议
* **示例**：

  ```python
  {
      "name": "My Custom Module",
      "summary": "扩展订单打印功能",
      "version": "1.0",
      "depends": ["sale"],
      "data": [
          "views/sale_order_views.xml",
          "security/ir.model.access.csv",
      ],
      "application": True,
      "license": "LGPL-3",
  }
  ```

---

## 2. `models/`（模型层）

* **作用**：定义数据库表结构与业务逻辑。
* **实现方式**：

  * 使用 Python 类继承 `models.Model`。
  * 字段用 `fields.*` 定义，例如：`fields.Char`、`fields.Many2one`。
  * 方法：业务逻辑，如 `create`, `write`, `unlink`, 自定义方法。
* **示例**：

  ```python
  from odoo import models, fields

  class SaleOrderInherit(models.Model):
      _inherit = "sale.order"
      custom_field = fields.Char("自定义字段")
  ```

---

## 3. `views/`（视图层）

* **作用**：定义数据的呈现方式。
* **内容**：XML 文件，描述表单视图、列表视图、菜单、动作等。
* **视图类型**：

  * `form`（表单视图）
  * `tree`（列表视图）
  * `kanban`（看板视图）
  * `calendar`（日历视图）
  * `graph`（图表视图）
* **示例**：

  ```xml
  <record id="view_sale_order_form_inherit" model="ir.ui.view">
      <field name="name">sale.order.form.custom</field>
      <field name="model">sale.order</field>
      <field name="inherit_id" ref="sale.view_order_form"/>
      <field name="arch" type="xml">
          <xpath expr="//sheet/group" position="inside">
              <field name="custom_field"/>
          </xpath>
      </field>
  </record>
  ```

---

## 4. `security/`（安全控制）

* **作用**：定义访问权限和数据安全。
* **常见文件**：

  * `ir.model.access.csv`：访问控制列表（ACL），定义哪个用户组对模型有读/写/删/创建权限。
  * 规则 XML：记录规则（Record Rules），控制数据级别的访问范围。
* **示例** (`ir.model.access.csv`)：

  ```csv
  id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
  access_sale_order_user,sale.order user,model_sale_order,base.group_user,1,1,1,0
  ```

---

## 5. `data/`（初始化数据）

* **作用**：提供模块安装时需要的初始化数据。
* **内容**：

  * 默认配置（如默认税率、工作流、参数设置）
  * Demo 数据（可选，用于演示）
* **文件类型**：XML 或 CSV。
* **示例**：

  ```xml
  <odoo>
      <record id="product_category_gold" model="product.category">
          <field name="name">Gold Products</field>
      </record>
  </odoo>
  ```

---

# ✅ 总结

Odoo 18 模块的**模块化结构**就像一个小型应用：

* **`__manifest__.py`** → 模块元信息与依赖声明。
* **`models/`** → 业务逻辑和数据库表。
* **`views/`** → 界面和用户交互。
* **`security/`** → 权限和安全控制。
* **`data/`** → 初始化数据和默认配置。

这几个部分配合起来，构成了一个完整的功能单元。

---

要不要我帮你画一张 **Odoo 模块目录结构图（带注释）**，让你直观看到每个文件夹/文件的作用？


# #########################################################################################################################

# **Odoo 18 模块化结构**里的几个核心目录和文件，并且帮你梳理成一张直观的“模块结构图”。

---

# 🧩 Odoo 18 模块化结构详解

一个 Odoo 模块（module）就像一个小型应用，典型目录如下：

```
my_module/
├── __manifest__.py     # 模块清单，元信息
├── __init__.py         # Python 包初始化
├── models/             # Python 模型（ORM，业务逻辑）
│   └── *.py
├── views/              # XML 视图定义（表单/列表/菜单等）
│   └── *.xml
├── security/           # 安全控制（ACL，规则）
│   ├── ir.model.access.csv
│   └── *.xml
├── data/               # 初始化数据（XML/CSV）
│   └── *.xml
├── report/             # 报表模板和动作（QWeb）
├── static/             # 前端静态资源（JS/CSS/图片）
│   └── src/
└── demo/               # 演示数据（安装 demo 模式用）
```

---

## 1. `__manifest__.py`

* **模块的身份证**。
* 包含：模块名称、版本、依赖、加载文件、是否应用化等。
* **例子**：

  ```python
  {
      "name": "IMON Receipt",
      "version": "1.0",
      "summary": "小票打印",
      "depends": ["sale"],
      "data": [
          "views/sale_order_views.xml",
          "security/ir.model.access.csv",
      ],
      "application": True,
      "license": "LGPL-3",
  }
  ```

---

## 2. `models/`

* **后端业务逻辑 + ORM 映射**。
* 写 Python 类继承 `models.Model`：

  * `fields.Char`, `fields.Integer`, `fields.Many2one` 等字段。
  * `@api.model`, `@api.depends`, `@api.onchange` 装饰器。
* **例子**：

  ```python
  from odoo import models, fields

  class Product(models.Model):
      _inherit = "product.template"
      barcode_custom = fields.Char("自定义条码")
  ```

---

## 3. `views/`

* **用户界面定义**，用 XML 描述：

  * 表单（form）、列表（tree）、看板（kanban）、菜单（menu）、动作（action）。
* **例子**：

  ```xml
  <record id="view_product_form_inherit" model="ir.ui.view">
      <field name="name">product.form.barcode</field>
      <field name="model">product.template</field>
      <field name="inherit_id" ref="product.product_template_only_form_view"/>
      <field name="arch" type="xml">
          <xpath expr="//field[@name='name']" position="after">
              <field name="barcode_custom"/>
          </xpath>
      </field>
  </record>
  ```

---

## 4. `security/`

* **权限与访问控制**：

  * `ir.model.access.csv`：定义不同组对模型的 CRUD 权限。
  * XML：记录规则（Record Rule），限制用户能看到的数据范围。
* **例子** (`ir.model.access.csv`)：

  ```csv
  id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
  access_product_user,product user,model_product_template,base.group_user,1,1,1,0
  ```

---

## 5. `data/`

* **初始化数据**（安装时加载）：

  * 默认配置（如默认税率、公司参数）。
  * 系统字典数据（如分类、规则）。
* **例子**：

  ```xml
  <odoo>
    <record id="uom_uom_gram" model="uom.uom">
      <field name="name">Gram</field>
      <field name="category_id" ref="uom.product_uom_categ_kgm"/>
      <field name="uom_type">smaller</field>
      <field name="factor_inv">1000</field>
    </record>
  </odoo>
  ```

---

# 🖼 模块结构图（带注释）

```
my_module/                  # 模块根目录
│
├── __manifest__.py         # 模块清单（名称、依赖、版本、加载文件）
├── __init__.py             # Python 包入口
│
├── models/                 # 数据模型 + ORM逻辑
│   └── *.py                # Python 类 (继承 models.Model)
│
├── views/                  # 前端界面（XML）
│   └── *.xml               # form/tree/kanban/menu/action
│
├── security/               # 安全控制
│   ├── ir.model.access.csv # 模型访问权限（ACL）
│   └── *.xml               # 数据级别规则（Record Rules）
│
├── data/                   # 初始化数据（XML/CSV）
│   └── *.xml
│
├── report/                 # 报表
│   ├── *.xml               # QWeb 模板
│   └── *.py                # 报表逻辑（可选）
│
├── static/                 # 前端资源
│   └── src/                # JS、CSS、图片
│
└── demo/                   # 演示数据（仅 demo 模式加载）
```

---

✅ **总结**：

* `__manifest__.py`：模块元信息和依赖。
* `models/`：Python 业务逻辑和数据库 ORM。
* `views/`：界面定义（表单/列表/菜单）。
* `security/`：权限控制。
* `data/`：初始化数据。

掌握这 5 个核心目录，就能写一个完整的 Odoo 模块。

---

要不要我帮你设计一个 **最小可运行 Odoo 18 模块**（Hello World 模块），包含模型、视图、菜单、权限，让你可以直接安装运行？

# #########################################################################################################################

# **最小可运行的 Odoo 18 模块**（Hello World 风格），安装后会在主菜单出现一个新应用“Hello Demo”，内含一个简单的模型与列表/表单视图，具备权限与菜单、可创建记录。

---

# 目录结构

```
hello_demo/
├─ __init__.py
├─ __manifest__.py
├─ models/
│  ├─ hello_item.py
│  └─ __init__.py
├─ views/
│  ├─ menu.xml
│  └─ hello_item_views.xml
├─ security/
│  ├─ ir.model.access.csv
│  └─ security_groups.xml
└─ data/
   └─ demo_data.xml   # 可选：演示数据（安装时自动创建一条记录）
```

> 只依赖 `base`。把 `hello_demo/` 放到你的自定义 addons 目录里即可。

---

## 1) `__manifest__.py`

```python
# -*- coding: utf-8 -*-
{
    "name": "Hello Demo",
    "summary": "A minimal Odoo 18 module: model + views + menu + ACL",
    "version": "1.0.0",
    "category": "Tools",
    "author": "You",
    "website": "",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/security_groups.xml",
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/hello_item_views.xml",
        # "data/demo_data.xml",  # 如需演示数据，取消注释
    ],
    "application": True,     # 在应用面板显示“Hello Demo”卡片
    "installable": True,
}
```

---

## 2) `__init__.py`

```python
# -*- coding: utf-8 -*-
from . import models
```

在 `models/__init__.py`（自动创建）中加：

```python
from . import hello_item
```

---

## 3) `models/hello_item.py`

```python
# -*- coding: utf-8 -*-
from odoo import api, fields, models

class HelloItem(models.Model):
    _name = "hello.item"
    _description = "Hello Item"

    name = fields.Char("名称", required=True)
    code = fields.Char("编码", index=True)
    active = fields.Boolean("启用", default=True)
    note = fields.Text("备注")
    # 计算字段示例
    name_display = fields.Char("显示名", compute="_compute_name_display", store=False)

    @api.depends("name", "code")
    def _compute_name_display(self):
        for rec in self:
            rec.name_display = f"[{rec.code}] {rec.name}" if rec.code else rec.name
```

---
## 3) `models/__init__.py`

```python
from . import hello_item
```

---

## 4) `views/menu.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
  <!-- 顶层应用菜单（出现在主菜单） -->
  <menuitem id="menu_hello_root"
            name="Hello Demo"
            sequence="10"
            web_icon="base,static/description/icon.png"/>

  <!-- 二级菜单：数据 -->
  <menuitem id="menu_hello_item_root"
            name="数据"
            parent="menu_hello_root"
            sequence="10"/>

  <!-- 动作：打开 hello.item 的树/表单 -->
  <record id="action_hello_item" model="ir.actions.act_window">
    <field name="name">Hello Items</field>
    <field name="res_model">hello.item</field>
    <field name="view_mode">tree,form</field>
    <field name="target">current</field>
  </record>

  <!-- 菜单：列表入口 -->
  <menuitem id="menu_hello_item"
            name="Hello Items"
            parent="menu_hello_item_root"
            action="action_hello_item"
            sequence="10"/>
</odoo>
```

> `web_icon` 用默认图标即可（可删）。若要自定义图标，把图标放到 `static/description/icon.png` 并更新路径。

---

## 5) `views/hello_item_views.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>

  <!-- 列表视图 -->
  <record id="view_hello_item_tree" model="ir.ui.view">
    <field name="name">hello.item.tree</field>
    <field name="model">hello.item</field>
    <field name="arch" type="xml">
      <tree>
        <field name="name"/>
        <field name="code"/>
        <field name="name_display"/>
        <field name="active"/>
      </tree>
    </field>
  </record>

  <!-- 表单视图 -->
  <record id="view_hello_item_form" model="ir.ui.view">
    <field name="name">hello.item.form</field>
    <field name="model">hello.item</field>
    <field name="arch" type="xml">
      <form string="Hello Item">
        <sheet>
          <group>
            <field name="name"/>
            <field name="code"/>
            <field name="active"/>
            <field name="name_display" readonly="1"/>
            <field name="note"/>
          </group>
        </sheet>
      </form>
    </field>
  </record>

  <!-- 搜索视图（可选） -->
  <record id="view_hello_item_search" model="ir.ui.view">
    <field name="name">hello.item.search</field>
    <field name="model">hello.item</field>
    <field name="arch" type="xml">
      <search>
        <field name="name"/>
        <field name="code"/>
        <filter string="启用" name="filter_active" domain="[('active','=',True)]"/>
        <filter string="停用" name="filter_inactive" domain="[('active','=',False)]"/>
      </search>
    </field>
  </record>

</odoo>
```

---

## 6) `security/security_groups.xml`（可选：定义一个模块专用组）

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
  <record id="group_hello_user" model="res.groups">
    <field name="name">Hello Demo 用户</field>
    <field name="category_id" ref="base.module_category_tools"/>
  </record>
</odoo>
```

---

## 7) `security/ir.model.access.csv`

> 为模型授予访问权限（最少给普通用户组，或者给上面自定义组）。

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_hello_item_user,hello.item user,model_hello_item,base.group_user,1,1,1,1
# 如需只允许我们自定义组访问，可改为:
# access_hello_item_user,hello.item user,model_hello_item,hello_demo.group_hello_user,1,1,1,1
```

> `model_hello_item` 是系统为 `hello.item` 自动生成的 external id。若安装时报“找不到 model\_id\:id”，说明系统没识别到模型，通常是模型没加载或拼写错误；请确认 `models/__init__.py` 引入了 `hello_item.py`，并确保 manifest 的 `data` 顺序在 views/ACL 之后无误（一般 ACL 放在视图前也可，关键是模型要能被注册）。

---

## 8) `data/demo_data.xml`（可选）

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
  <record id="hello_item_demo_1" model="hello.item">
    <field name="name">示例条目</field>
    <field name="code">D001</field>
    <field name="note">这是安装时创建的一条演示数据。</field>
  </record>
</odoo>
```

---

# 安装与运行

1. 将 `hello_demo/` 放入你的自定义 addons 目录（例如 `/opt/odoo/custom_addons/hello_demo`）。
2. 确认启动参数包含该路径（示例）：

   ```
   --addons-path=/opt/odoo/odoo/odoo/addons,/opt/odoo/custom_addons
   ```
3. 在 Odoo 后台：**设置 → 应用 → 更新应用列表**（或开发者模式 → 更新应用列表）。
4. 搜索 **Hello Demo**，点击安装。
5. 回到主界面，会出现 **Hello Demo** 应用；进入后即可新建/查看 “Hello Items”。

---

# 可选增强（你可以逐步加）

* 在 `views/hello_item_views.xml` 里加 `kanban` 视图；
* 在 `report/` 增加 QWeb 报表模板与报表动作；
* 在 `security/security_groups.xml` 定义更细的角色分组，并在 `ir.model.access.csv` 中指定；
* 在 `static/src/` 放 JS / SCSS，配合 `__manifest__.py` 的 `assets` 注入前端资源；
* 在 `data/` 增加参数默认值（`ir.config_parameter`）或字典数据。

---

有了这套“最小模块”，你就可以在它基础上继续扩展：新增模型、字段、视图、菜单、报表与权限。不论练习还是作为真实项目的骨架，这份结构都能直接复用。需要我再给你补一份**带打印报表(QWeb)的版本**或**REST 控制器/JSON-RPC 接口示例**吗？






# #########################################################################################################################

好的 👍，我帮你整理了一份 **「Odoo 18 新增模块的标准流程清单」**，分为 **开发环境**、**测试环境** 和 **生产环境** 三个场景，确保每次新增模块都能稳定、可控地上线。

---

# 📋 Odoo 18 新增模块标准流程清单

## 一、开发环境（本地/研发机）

1. **编写模块骨架**

   * 新建模块目录，例如 `custom_addons/my_module/`。
   * 按结构写好：`__manifest__.py`、`models/`、`views/`、`security/` 等。

2. **放入 addons 路径**

   * 确认 `odoo.conf` 里 `addons_path` 包含 `custom_addons`。

3. **重启 Odoo 服务**

   * 如果模块含有 **新的 Python 文件** → 必须重启。
   * 如果只是改 XML（视图/报表） → 可以通过更新模块加载。

4. **更新应用列表**

   * 进入 Odoo 后台 → **应用（Apps）** → 开发者模式 → **更新应用列表**。

5. **安装新模块**

   * 搜索模块名 → 点击 **安装**。
   * 或命令行更新：

     ```bash
     python odoo-bin -d mydb -u my_module
     ```

---

## 二、测试环境（UAT/预发布）

1. **拷贝模块代码**

   * 将开发完成的模块放入测试环境的 `addons` 路径。
   * 建议用 Git 或 rsync 保持同步。

2. **数据库备份**

   * 在测试环境执行一次数据库备份：

     ```bash
     pg_dump -U odoo -h localhost mydb > backup_$(date +%F).sql
     ```

3. **更新应用列表并安装模块**

   * 后台 **应用 → 更新应用列表 → 安装新模块**。

4. **功能验证**

   * 测试模块是否能正常运行。
   * 检查依赖模块是否缺失。
   * 确认新增菜单/视图/报表正常显示。

5. **回归测试**

   * 确认新模块不会影响已有业务流程。
   * 验证多用户权限、数据一致性。

---

## 三、生产环境

1. **代码部署**

   * 使用 CI/CD 或手工将模块代码部署到生产 `addons` 目录。
   * 确认权限：`odoo` 用户可读。

2. **数据库备份**（强制步骤）

   * 上线前必须备份数据库和 filestore。

3. **更新应用列表**

   * 开发者模式 → **更新应用列表**。

4. **安装新模块**

   * 在生产后台安装模块。
   * 或使用命令行更新：

     ```bash
     python odoo-bin -d prod_db -u my_module
     ```

5. **日志监控**

   * 安装过程中关注 Odoo 日志：

     ```bash
     tail -f /var/log/odoo/odoo-server.log
     ```
   * 确认无错误或依赖缺失。

6. **业务验证**

   * 检查关键功能是否正常。
   * 让实际业务用户进行快速验收。

---

## ✅ 总结

* **开发环境**：写模块 + 重启/更新 + 安装。
* **测试环境**：数据库备份 + 功能/回归测试。
* **生产环境**：部署代码 + 数据库备份 + 安装 + 验收。
* **关键原则**：

  1. 新 Python 文件 → 必须重启服务。
  2. 上线前 → 必做数据库备份。
  3. 测试环境验证无误 → 再上生产。

---

要不要我帮你整理成一个 **一页纸 Checklist（表格形式）**，你可以贴在团队 wiki 或者部署文档里，照着打勾执行？




# #########################################################################################################################






# #########################################################################################################################

太好了！下面把你要的“**从零创建一个窄幅热敏纸（58/80mm）销售小票 PDF 报表**”做成**超详细 step-by-step**，基于 **Odoo 18**。照着做，装完模块后，你就能在“销售订单”的**打印**菜单里看到“销售小票（58mm）”，直接出 PDF，然后用热敏打印机打印。

> 说明
>
> * 路线是 **QWeb → PDF（wkhtmltopdf）**，适合绝大多数桌面/网络热敏打印场景。
> * 若你未来追求极致速度、免 PDF，Odoo POS 走 **ESC/POS**（非本文路线）。
> * 在窄幅热敏下，**字体/边距/宽度**是关键。

---

# 0. 前置准备（只做一次）

1. 开启开发者模式；安装 `sale_management`（有销售订单）。
2. 服务器安装 wkhtmltopdf（并保证 `wkhtmltopdf --version` 可用）。
3. Odoo 系统参数建议设置：

   * `web.base.url`：你的站点 URL（如 `http://localhost:8069` 或公网域名）。
   * `report.url`：渲染回连地址（同机建议 `http://127.0.0.1:8069`）。
4. 安装中文字体（如需中文）：

   ```bash
   sudo apt-get install -y fonts-noto-cjk fonts-dejavu
   ```

---

# 1. 用 scaffold 建空模块

在你的 `addons` 目录下执行：

```bash
# 切换到 addons 目录
cd /path/to/odoo/addons
# 创建新模块
python /path/to/odoo/odoo-bin scaffold sale_receipt_thermal .
```

生成结构（简化）：

```
sale_receipt_thermal/
├─ __init__.py
├─ __manifest__.py
├─ controllers/
├─ models/
├─ static/
└─ views/
```

---

# 2. 新建纸张格式 & 报表动作 & QWeb 模板（XML）

创建文件：`sale_receipt_thermal/views/report_sale.xml`

> 我给出两个纸张格式：**58mm** 和 **80mm**。你可以二选一，或都保留在后台选择。
> 58mm 打印机有效打印宽度通常 \~48–58mm；为留边，这里设 **宽 58mm、边距 2mm**。
> 若你想尽量一页容纳更多内容，可把 `page_height` 设得大一点（比如 600mm），或保持 A4 多页。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>

  <!-- ① 定义纸张格式：58mm 热敏 -->
  <record id="paperformat_58mm_receipt" model="report.paperformat">
    <field name="name">Receipt 58mm</field>
    <field name="default" eval="False"/>
    <field name="format">custom</field>
    <field name="page_width">58</field>        <!-- 毫米 -->
    <field name="page_height">300</field>      <!-- 毫米；票据较长可增大，或改成 600 -->
    <field name="orientation">Portrait</field>
    <field name="margin_top">2</field>
    <field name="margin_bottom">2</field>
    <field name="margin_left">2</field>
    <field name="margin_right">2</field>
    <field name="dpi">203</field>              <!-- 常见热敏 203dpi；不稳定时可 96/110 -->
    <field name="header_line" eval="False"/>
    <field name="header_spacing">0</field>
    <field name="report_type">qweb-pdf</field>
    <field name="disable_shrinking" eval="True"/>
  </record>

  <!-- ② 可选：80mm 纸张 -->
  <record id="paperformat_80mm_receipt" model="report.paperformat">
    <field name="name">Receipt 80mm</field>
    <field name="default" eval="False"/>
    <field name="format">custom</field>
    <field name="page_width">80</field>
    <field name="page_height">300</field>
    <field name="orientation">Portrait</field>
    <field name="margin_top">2</field>
    <field name="margin_bottom">2</field>
    <field name="margin_left">2</field>
    <field name="margin_right">2</field>
    <field name="dpi">203</field>
    <field name="header_line" eval="False"/>
    <field name="header_spacing">0</field>
    <field name="report_type">qweb-pdf</field>
    <field name="disable_shrinking" eval="True"/>
  </record>

  <!-- ③ QWeb 模板：窄幅小票（极简，无页眉页脚） -->
  <!-- 如果你想要公司通用页眉页脚，可以把 t-call 改成 web.external_layout -->
  <template id="report_sale_receipt_document">
    <t t-call="web.basic_layout">  <!-- 极简版布局 -->
      <div class="page o_sale_receipt">
        <style>
          /* 内联样式：确保 wkhtmltopdf 可用 */
          .o_sale_receipt {
            font-family: "Noto Sans CJK SC", "DejaVu Sans", sans-serif;
            font-size: 10pt; line-height: 1.25;
            color: #000;
          }
          .o-sale-center { text-align:center; }
          .o-sale-bold { font-weight: 700; }
          .o-sale-sm   { font-size: 9pt; }
          .o-sale-xs   { font-size: 8pt; }
          .o-line { border-top: 1px dashed #000; margin: 4px 0; }
          table { width:100%; border-collapse: collapse; }
          th, td { padding: 2px 0; vertical-align: top; }
          .col-right { text-align: right; }
          .muted { color:#333; }
          .totals td { padding-top: 4px; }
          /* 避免中间分页 */
          .no-break { page-break-inside: avoid; }
        </style>

        <!-- 头部 -->
        <div class="o-sale-center">
          <div class="o-sale-bold">销售小票</div>
          <div class="o-sale-sm" t-esc="(doc.company_id and doc.company_id.display_name) or ''"/>
          <div class="o-sale-xs muted">
            <t t-esc="doc.company_id and doc.company_id.phone or ''"/> /
            <t t-esc="doc.company_id and doc.company_id.email or ''"/>
          </div>
        </div>

        <div class="o-line"></div>

        <!-- 基本信息 -->
        <div class="no-break">
          <table>
            <tr><td>订单号：</td><td class="col-right" t-esc="doc.name"/></tr>
            <tr><td>客户：</td><td class="col-right" t-esc="doc.partner_id.display_name"/></tr>
            <tr><td>日期：</td><td class="col-right" t-esc="doc.date_order and doc.date_order.strftime('%Y-%m-%d %H:%M')"/></tr>
            <tr><td>销售员：</td><td class="col-right" t-esc="doc.user_id and doc.user_id.name or ''"/></tr>
          </table>
        </div>

        <div class="o-line"></div>

        <!-- 明细 -->
        <div class="no-break">
          <table>
            <thead>
              <tr>
                <th>品名</th>
                <th class="col-right">数量</th>
                <th class="col-right">单价</th>
                <th class="col-right">小计</th>
              </tr>
            </thead>
            <tbody>
              <tr t-foreach="doc.order_line" t-as="l">
                <td>
                  <t t-esc="l.product_id.display_name"/>
                  <t t-if="l.name and l.name.strip() and l.name.strip() != l.product_id.display_name">
                    <br/><span class="o-sale-xs muted" t-esc="l.name"/>
                  </t>
                </td>
                <td class="col-right" t-esc="formatLang(l.product_uom_qty, dp='Product Unit of Measure')"/>
                <td class="col-right" t-esc="formatLang(l.price_unit, currency_obj=doc.currency_id)"/>
                <td class="col-right" t-esc="formatLang(l.price_subtotal, currency_obj=doc.currency_id)"/>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="o-line"></div>

        <!-- 合计 -->
        <div class="no-break">
          <table class="totals">
            <tr>
              <td>未税：</td>
              <td class="col-right" t-esc="formatLang(doc.amount_untaxed, currency_obj=doc.currency_id)"/>
            </tr>
            <tr>
              <td>税额：</td>
              <td class="col-right" t-esc="formatLang(doc.amount_tax, currency_obj=doc.currency_id)"/>
            </tr>
            <tr class="o-sale-bold">
              <td>应付合计：</td>
              <td class="col-right" t-esc="formatLang(doc.amount_total, currency_obj=doc.currency_id)"/>
            </tr>
          </table>
        </div>

        <div class="o-line"></div>

        <!-- 备注 & 页脚 -->
        <div class="o-sale-xs muted no-break">
          <t t-if="doc.note">
            备注：<t t-esc="doc.note"/>
            <br/>
          </t>
          谢谢惠顾！
        </div>
      </div>
    </t>
  </template>

  <!-- ④ 报表动作：绑定 sale.order → 打印菜单 -->
  <record id="action_report_sale_receipt_58mm" model="ir.actions.report">
    <field name="name">销售小票（58mm）</field>
    <field name="model">sale.order</field>
    <field name="report_type">qweb-pdf</field>
    <field name="report_name">sale_receipt_thermal.report_sale_receipt_document</field>
    <!-- 文件名：单记录时 object，批量时 docs（可以更复杂） -->
    <field name="print_report_name">'Receipt-%s.pdf' % (object.name)</field>
    <field name="paperformat_id" ref="sale_receipt_thermal.paperformat_58mm_receipt"/>
    <!-- 绑定到“打印”菜单 -->
    <field name="binding_model_id" ref="sale.model_sale_order"/>
    <field name="binding_type">report</field>
    <!-- 保存为附件（可选，提升性能；确认订单后更合适） -->
    <!-- <field name="attachment_use" eval="True"/>
    <field name="attachment">('Receipt-%s.pdf') % (object.name)</field> -->
  </record>

</odoo>
```

> 想切换 80mm，只需把 `paperformat_id` 改成 `paperformat_80mm_receipt`。

---

# 3. 把 XML 加进清单

编辑 `sale_receipt_thermal/__manifest__.py`：

```python
{
    "name": "Sale Receipt Thermal",
    "version": "18.0.1.0.0",
    "summary": "Narrow thermal PDF receipt for Sale Order (58/80mm)",
    "category": "Sales",
    "depends": ["web", "sale_management"],
    "data": [
        "views/report_sale.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
}
```

---

# 4. 更新应用列表并安装模块

Odoo 后台 → **应用** → 勾选“更新应用列表” → 搜索 `Sale Receipt Thermal` → 安装。
（或命令行升级：`-u sale_receipt_thermal`）

---

# 5. 打开销售订单并打印

销售 → 订单 → 打开任意订单 → **打印** ▼ → 选择“**销售小票（58mm）**” → 出 PDF。
把 PDF 发到热敏打印机，注意打印对话框里关闭“自动缩放/适配”，选“实际大小”。

---

# 6. （可选）用公司页眉页脚

将模板外层 `<t t-call="web.basic_layout">` 改为：

```xml
<t t-call="web.external_layout">
  <div class="page o_sale_receipt"> ... </div>
</t>
```

提醒：`external_layout` 会引入更多上/下边距与页眉页脚元素，窄幅下可能显得拥挤，可自行取舍。

---

# 7. 常见调校与技巧

* **发票/订单批量打印**：在报表动作里勾选 “Multiple（multi）”，多选订单一起打印会合并成一个 PDF。
* **防止分页**：小票通常短；若内容较长仍分页，增大 `page_height`（如 600mm），同时在关键容器加 `.no-break { page-break-inside: avoid; }`。
* **字体**：确保安装了你需要的语言字体；CSS 里优先用 `Noto Sans CJK` / `DejaVu Sans`。
* **生成附件**：对已确认/不再变动的订单，打开 `attachment_use` 可大幅提高重复打印速度。
* **wkhtmltopdf 版本**：建议 0.12.6（with patched Qt）；若出现空白/错位，降 DPI（90\~110）试试。
* **报表路径/权限**：只给对应安全组可见（在报表动作上配置 Groups）。
* **自定义文件名**：`print_report_name` 是 Python 表达式（返回字符串），单记录用 `object`，多记录用 `docs`。

---

# 8. 一键更新/调试（命令行）

```bash
# 升级模块以应用 XML 修改
python odoo-bin -c odoo.conf -u sale_receipt_thermal

# 只生成当前记录的动作（在 Python 里）
# action = env.ref('sale_receipt_thermal.action_report_sale_receipt_58mm')
# return action.report_action(record)
```

---

## 结语

到这一步你已经：

* 有了 **58mm/80mm 纸张格式**；
* 有了 **窄幅小票的 QWeb 模板**；
* 报表动作挂在 **销售订单的打印菜单**；
* 能出 **热敏友好的 PDF**。

如果你给我你的**票据实际字段/排版草图**（比如要加二维码、序列号、促销文案等），我可以把模板细节和样式再按你的业务**定制一版**，做到粘贴即用。




# #########################################################################################################################

# 创建独立的QWeb模版

结论先说：**请做一个小的自定义模块**，在模块里新增/继承 QWeb 模板并配置报表动作（`ir.actions.report`）与纸张格式。
不建议直接在“系统里复制并改原模板”或改动官方模块文件——升级/安装依赖时容易被覆盖、也不易版本管理。

下面给你三种做法，对比+示例：

---

## 方案 A（推荐）——新建一个“热敏小票”报表，不影响原有 A4 报表

**适用**：既要保留原来的 A4“报价/订单”打印，又要多一个“票据打印机专用格式”。

**做法**（在你的自定义模块里完成）：

1. 定义**纸张格式**（58/80mm）`report.paperformat`
2. 写一份**QWeb 模板**（窄幅布局、内联 CSS）
3. 新建**报表动作** `ir.actions.report`，`model=sale.order`，`report_type=qweb-pdf`，`report_name=你的模板技术名`，绑定到“打印”菜单；`paperformat_id` 选你的热敏纸
4. 安装/升级模块 → 销售订单页面点 **打印** 就能看到新增的“销售小票（58mm）”

**XML 样例（精简）**：

```xml
<odoo>
  <!-- 58mm 纸张 -->
  <record id="paperformat_58mm" model="report.paperformat">
    <field name="name">Receipt 58mm</field>
    <field name="format">custom</field>
    <field name="page_width">58</field>
    <field name="page_height">300</field>
    <field name="margin_top">2</field>
    <field name="margin_bottom">2</field>
    <field name="margin_left">2</field>
    <field name="margin_right">2</field>
    <field name="dpi">203</field>
    <field name="report_type">qweb-pdf</field>
    <field name="disable_shrinking" eval="True"/>
  </record>

  <!-- 小票模板（窄幅） -->
  <template id="report_sale_receipt_document">
    <t t-call="web.basic_layout">
      <div class="page receipt">
        <style>
          .receipt{font-family:"Noto Sans CJK SC","DejaVu Sans",sans-serif;font-size:10pt;line-height:1.25}
          .line{border-top:1px dashed #000;margin:4px 0}
          .right{text-align:right}
          table{width:100%;border-collapse:collapse}
          th,td{padding:2px 0}
        </style>
        <h3 class="o_text_center">销售小票</h3>
        <div>订单：<span t-esc="doc.name"/></div>
        <div>客户：<span t-esc="doc.partner_id.display_name"/></div>
        <div class="line"></div>
        <table>
          <thead><tr><th>品名</th><th class="right">数</th><th class="right">价</th><th class="right">小计</th></tr></thead>
          <tbody>
            <tr t-foreach="doc.order_line" t-as="l">
              <td t-esc="l.product_id.display_name"/>
              <td class="right" t-esc="formatLang(l.product_uom_qty, dp='Product Unit of Measure')"/>
              <td class="right" t-esc="formatLang(l.price_unit, currency_obj=doc.currency_id)"/>
              <td class="right" t-esc="formatLang(l.price_subtotal, currency_obj=doc.currency_id)"/>
            </tr>
          </tbody>
        </table>
        <div class="line"></div>
        <div class="right">合计：<span t-esc="formatLang(doc.amount_total, currency_obj=doc.currency_id)"/></div>
      </div>
    </t>
  </template>

  <!-- 报表动作：新增一个“打印小票”的入口 -->
  <record id="action_report_sale_receipt" model="ir.actions.report">
    <field name="name">销售小票（58mm）</field>
    <field name="model">sale.order</field>
    <field name="report_type">qweb-pdf</field>
    <field name="report_name">your_module.report_sale_receipt_document</field>
    <field name="paperformat_id" ref="your_module.paperformat_58mm"/>
    <field name="binding_model_id" ref="sale.model_sale_order"/>
    <field name="binding_type">report</field>
    <field name="print_report_name">'Receipt-%s.pdf' % (object.name)</field>
  </record>
</odoo>
```

> 好处：可维护（版本可控）、不破坏原功能、升级不怕覆盖。

---

## 方案 B——继承（覆盖）原报表模板，只保留一个“订单打印”

**适用**：你不需要 A4 版，只想让“打印订单”直接变成热敏小票。

**做法**：

* 在自定义模块里写一个 **QWeb 继承模板**（`inherit_id="sale.report_saleorder_document"` 或相应模板 ID），用 `<xpath>` 定位并替换内容/样式；
* 复用**原来的报表动作** `sale.action_report_saleorder`，只在你的数据 XML 里把它的 `paperformat_id` 指向热敏纸。

**XML 片段**：

```xml
<!-- 覆盖官方模板的内容（示例：把主体替换为窄幅表格） -->
<template id="report_saleorder_inherit_receipt" inherit_id="sale.report_saleorder_document">
  <xpath expr="//div[contains(@class,'page')]" position="replace">
    <div class="page receipt">
      <!-- 你的窄幅内容，类似方案A的模板 -->
    </div>
  </xpath>
</template>

<!-- 改原动作的纸张为热敏纸 -->
<record id="sale.action_report_saleorder" model="ir.actions.report">
  <field name="paperformat_id" ref="your_module.paperformat_58mm"/>
</record>
```

> 好处：用户点击“打印订单”就直接走热敏格式；
> 代价：覆盖面更大，未来升级要注意官方模板结构变化（`xpath` 可能需要调整）。

---

## 方案 C（不推荐长期使用）——在界面里复制/新建 QWeb 模板

* 打开 **设置 → 技术 → 用户界面 → 视图**，找到原模板，点击复制，然后改内容；
* 再到 **设置 → 技术 → 报表 → 报表**，新建或修改报表动作，指向你新模板。
* 这是**数据库内改动**，没有源码版本控制；升级/迁移时容易丢，团队协作也不方便。

> 仅适合临时验证样式，验证通过请尽快固化到模块源码。

---

## 什么时候需要“完全新建模块”？

* 几乎**总是**。即便只改一份模板，也建议用一个很小的定制模块来承载：

  * 放纸张格式、模板、报表动作
  * 方便 `-u your_module` 升级、打包部署、跨环境迁移
  * 不会被官方升级覆盖

---

## 补充注意事项

* **wkhtmltopdf** 必须安装；无它无法出 PDF（报表只会以 HTML 显示）。
* **系统参数**：建议设置 `report.url=http://127.0.0.1:8069`、`web.base.url=你的对外URL`，避免资源加载失败导致空白页。
* **字体**：窄幅热敏常见中文字体缺失导致方块；安装 `fonts-noto-cjk` / `wqy`。
* **打印机设置**：浏览器打印对话框务必选“实际大小/无缩放”，关闭页眉页脚，方向纵向。
* **性能**：对已确认的订单可开启“保存为附件”（`attachment_use=True`），下次打印直接复用。
* **如果要 ESC/POS 直打**（非 PDF）：需要走 POS 体系（`point_of_sale` + `hw_escpos`/IoT Box），这与 QWeb→PDF 路线不同。

---

**结论**：

* **最佳实践**是：**新建一个小模块**，新增你的“票据打印机专用格式”报表（方案 A）；
* **只想替换现有“打印订单”**的效果，走**继承覆盖**（方案 B）；
* UI 里直接复制模板可以临时试，但不宜长期维护（方案 C）。

如果你确认选方案 A 或 B，我可以把完整可用的模块骨架（含 `__manifest__.py`、XML、可选的 Python 入口）按你的票据字段再细化一份，拷进去即可安装。




# #########################################################################################################################

好嘞！下面给你一套**从零到可打**的完整步骤，实现【方案 A：新增“票据打印机专用（58/80mm）”报表，不影响原有 A4 报表】——基于 **Odoo 18**。你照抄即可落地。

---

# 0) 前置准备（一次性）

1. **开启开发者模式**：设置 → 常规 → 启用开发者模式（或 URL 加 `?debug=1`）。
2. **安装 Sales 应用**：应用 → 搜索“Sales/销售”（模块 `sale_management`）→ 安装。
3. **安装 wkhtmltopdf**（服务器上，Odoo 所在系统）并确保：

   ```bash
   wkhtmltopdf --version
   which wkhtmltopdf   # /usr/local/bin 或 /usr/bin
   ```

   若仍提示找不到，在 `odoo.conf` 中加：

   ```
   wkhtmltopdf = /usr/local/bin/wkhtmltopdf
   ```
4. **建议设置系统参数**（避免渲染时取静态资源失败）
   设置 → 技术 → 参数 → 系统参数：

   * `web.base.url`：你的访问地址（例 `http://localhost:8069` 或域名）
   * `report.url`：渲染回连地址（同机建议 `http://127.0.0.1:8069`）
5. **中文字体（如需）**：

   ```bash
   sudo apt-get install -y fonts-noto-cjk fonts-dejavu
   ```

> 你在 WSL/Docker 也行，wkhtmltopdf 与字体需在**Odoo 运行环境**里安装。

---

# 1) 创建模块骨架

到你的自定义 addons 目录执行（假设 `/opt/odoo/custom-addons`；若不同，自行替换）：

```bash
cd /opt/odoo/custom-addons
python /path/to/odoo/odoo-bin scaffold sale_receipt_thermal .
python ../odoo-bin scaffold sale_receipt_thermal .
```

生成结构（简化）：

```
sale_receipt_thermal/
├─ __init__.py
├─ __manifest__.py
├─ controllers/
├─ models/
└─ views/
```

> 确保 `addons_path` 已包含 `/opt/odoo/custom-addons`（在 `odoo.conf` 的 `addons_path` 追加）。

---

# 2) 编写报表 XML（纸张格式 + 模板 + 报表动作）

新建文件：`sale_receipt_thermal/views/report_sale.xml`，填入下面**完整内容**：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>

  <!-- ① 纸张格式：58mm 热敏（你也可以只留一个） -->
  <record id="paperformat_58mm_receipt" model="report.paperformat">
    <field name="name">Receipt 58mm</field>
    <field name="default" eval="False"/>
    <field name="format">custom</field>
    <field name="page_width">58</field>       <!-- mm -->
    <field name="page_height">300</field>     <!-- mm；票据较长可改 600 -->
    <field name="orientation">Portrait</field>
    <field name="margin_top">2</field>
    <field name="margin_bottom">2</field>
    <field name="margin_left">2</field>
    <field name="margin_right">2</field>
    <field name="dpi">203</field>
    <field name="header_line" eval="False"/>
    <field name="header_spacing">0</field>
    <field name="report_type">qweb-pdf</field>
    <field name="disable_shrinking" eval="True"/>
  </record>

  <!-- ② 可选：80mm 纸张 -->
  <record id="paperformat_80mm_receipt" model="report.paperformat">
    <field name="name">Receipt 80mm</field>
    <field name="default" eval="False"/>
    <field name="format">custom</field>
    <field name="page_width">80</field>
    <field name="page_height">300</field>
    <field name="orientation">Portrait</field>
    <field name="margin_top">2</field>
    <field name="margin_bottom">2</field>
    <field name="margin_left">2</field>
    <field name="margin_right">2</field>
    <field name="dpi">203</field>
    <field name="header_line" eval="False"/>
    <field name="header_spacing">0</field>
    <field name="report_type">qweb-pdf</field>
    <field name="disable_shrinking" eval="True"/>
  </record>

  <!-- ③ QWeb 模板：窄幅小票（极简布局，便于热敏） -->
  <!-- 想用公司通用页眉页脚可把 t-call 改成 web.external_layout -->
  <template id="report_sale_receipt_document">
    <t t-call="web.basic_layout">
      <div class="page o_sale_receipt">
        <style>
          .o_sale_receipt {
            font-family: "Noto Sans CJK SC","DejaVu Sans",sans-serif;
            font-size: 10pt; line-height: 1.25; color: #000;
          }
          .center { text-align:center; }
          .bold { font-weight:700; }
          .xs { font-size:8pt; }
          .muted { color:#333; }
          .line { border-top:1px dashed #000; margin:4px 0; }
          table { width:100%; border-collapse:collapse; }
          th,td { padding:2px 0; vertical-align:top; }
          .r { text-align:right; }
          .no-break { page-break-inside: avoid; }
        </style>

        <!-- 标题/公司 -->
        <div class="center">
          <div class="bold">销售小票</div>
          <div t-esc="(doc.company_id and doc.company_id.display_name) or ''"/>
          <div class="xs muted">
            <t t-esc="doc.company_id and doc.company_id.phone or ''"/> /
            <t t-esc="doc.company_id and doc.company_id.email or ''"/>
          </div>
        </div>

        <div class="line"></div>

        <!-- 基本信息 -->
        <div class="no-break">
          <table>
            <tr><td>订单号：</td><td class="r" t-esc="doc.name"/></tr>
            <tr><td>客户：</td><td class="r" t-esc="doc.partner_id.display_name"/></tr>
            <tr><td>日期：</td><td class="r" t-esc="doc.date_order and doc.date_order.strftime('%Y-%m-%d %H:%M')"/></tr>
            <tr><td>销售员：</td><td class="r" t-esc="doc.user_id and doc.user_id.name or ''"/></tr>
          </table>
        </div>

        <div class="line"></div>

        <!-- 明细 -->
        <div class="no-break">
          <table>
            <thead>
              <tr><th>品名</th><th class="r">数量</th><th class="r">单价</th><th class="r">小计</th></tr>
            </thead>
            <tbody>
              <tr t-foreach="doc.order_line" t-as="l">
                <td>
                  <t t-esc="l.product_id.display_name"/>
                  <t t-if="l.name and l.name.strip() and l.name.strip() != l.product_id.display_name">
                    <br/><span class="xs muted" t-esc="l.name"/>
                  </t>
                </td>
                <td class="r" t-esc="formatLang(l.product_uom_qty, dp='Product Unit of Measure')"/>
                <td class="r" t-esc="formatLang(l.price_unit, currency_obj=doc.currency_id)"/>
                <td class="r" t-esc="formatLang(l.price_subtotal, currency_obj=doc.currency_id)"/>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="line"></div>

        <!-- 合计 -->
        <div class="no-break">
          <table>
            <tr><td>未税：</td><td class="r" t-esc="formatLang(doc.amount_untaxed, currency_obj=doc.currency_id)"/></tr>
            <tr><td>税额：</td><td class="r" t-esc="formatLang(doc.amount_tax, currency_obj=doc.currency_id)"/></tr>
            <tr class="bold"><td>应付合计：</td><td class="r" t-esc="formatLang(doc.amount_total, currency_obj=doc.currency_id)"/></tr>
          </table>
        </div>

        <div class="line"></div>

        <!-- 备注/页脚 -->
        <div class="xs muted no-break">
          <t t-if="doc.note">
            备注：<t t-esc="doc.note"/><br/>
          </t>
          谢谢惠顾！
        </div>
      </div>
    </t>
  </template>

  <!-- ④ 报表动作：新增一个“打印小票”的入口，绑定到销售订单 -->
  <record id="action_report_sale_receipt_58mm" model="ir.actions.report">
    <field name="name">销售小票（58mm）</field>
    <field name="model">sale.order</field>
    <field name="report_type">qweb-pdf</field>
    <field name="report_name">sale_receipt_thermal.report_sale_receipt_document</field>
    <field name="print_report_name">'Receipt-%s.pdf' % (object.name)</field>
    <field name="paperformat_id" ref="sale_receipt_thermal.paperformat_58mm_receipt"/>
    <field name="binding_model_id" ref="sale.model_sale_order"/>
    <field name="binding_type">report</field>
    <!-- 可选：保存为附件，适合已确认单据提升速度
    <field name="attachment_use" eval="True"/>
    <field name="attachment">('Receipt-%s.pdf') % (object.name)</field>
    -->
  </record>

</odoo>
```

---

# 3) 在清单中加载该 XML

编辑 `sale_receipt_thermal/__manifest__.py`（最小可用）：

```python
{
    "name": "Sale Receipt Thermal",
    "version": "18.0.1.0.0",
    "summary": "Thermal (58/80mm) PDF receipt for Sale Order",
    "category": "Sales",
    "depends": ["web", "sale_management"],
    "data": [
        "views/report_sale.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
}
```

---

# 4) 安装模块

**方式 A：UI 安装**

* 应用 → 更新应用列表 → 搜索 **Sale Receipt Thermal** → 安装

**方式 B：命令行（已配置 odoo.conf）**

```bash
python /path/to/odoo/odoo-bin -c /path/to/odoo.conf -i sale_receipt_thermal
```

> 若你在 WSL/Docker 里跑，命令一样；确保 DB 连接参数正确。

---

# 5) 打印测试

* 进入 销售 → 订单 → 打开任意销售订单
* 点击 **打印** ▼ → 选择 **“销售小票（58mm）”**
* 浏览器预览/下载的 PDF 发到你的热敏打印机
* 打印对话框：使用 **“实际大小/无缩放”**，关闭浏览器自带页眉页脚

> 想用 80mm：在报表动作里把 `paperformat_id` 改为 `paperformat_80mm_receipt`（或复制一条新动作，名字改为“销售小票（80mm）”）。

---

# 6) 常见问题排查

* **提示缺少 wkhtmltopdf**：确认系统安装并在 `odoo.conf` 指定路径。
* **PDF 空白/样式丢失**：设置 `report.url` 和 `web.base.url`；检查 wkhtmltopdf 版本（推荐 0.12.6），适当调低 `dpi`（90–110）。
* **中文为方块**：安装 `fonts-noto-cjk`；模板里已使用通用字体族。
* **分页不理想**：增大 `page_height`（如 600mm），并在需要的容器加 `.no-break`。
* **不想影响原 A4 报表**：本方案不会覆盖原报表；新增打印入口互不影响。
* **升级样式**：修改 XML 后执行：

  ```bash
  python /path/to/odoo/odoo-bin -c /path/to/odoo.conf -u sale_receipt_thermal
  ```

---

# 7) 可选增强

* **二维码/条码**：在模板中加 `<img t-att-src="'/report/barcode?type=QR&value=%s' % (doc.name)"/>` 或使用 `widget="barcode"`（需正确参数）。
* **发邮件自动附 PDF**：邮件模板里“要打印的报表”选择该报表。
* **权限限制**：在报表动作上设置 `Groups`，只让指定角色可见。

---

到这里，你已经完成了**不影响原报表**的“票据打印机专用格式（58/80mm）”新增，并可以在销售订单里直接打印小票。需要我再帮你把票面字段/排版按你实际票据（LOGO、店铺地址、二维码等）细化一下，也可以发我草图，我给你出一版模板直接替换。




# #########################################################################################################################





# #########################################################################################################################








# #########################################################################################################################

下面这份说明专门讲 Odoo 18 里“**设置 → 技术 → 报表 → 报表**”（模型：`ir.actions.report`）到底管什么、怎么配置、怎么用，以及常见坑如何避开。读完你就能自己新建一个 PDF 报表、把它挂到业务单据的“打印”菜单，并能通过代码或邮件自动附上 PDF。

---

# 一、它究竟是什么？

“报表（Reports）”这张表描述的是**报表动作**：当你在业务单据点“打印”时，Odoo 依据这里的一条配置去：

1. 找到对应的 **QWeb 模板**（HTML 模版）；
2. 用记录数据渲染它；
3. 选定引擎（PDF/HTML/文本/可选 xlsx）输出；
4. 应用纸张格式等参数；
5. 交给浏览器下载/预览，或按设置保存为附件。

> 打个比方：`ir.actions.report` = “打印按钮的行为定义”；
> QWeb 模板 = “报表长啥样”；
> 纸张格式 = “页面大小/边距/方向/DPI”。

---

# 二、界面里关键字段怎么填？

进入：设置 → 技术 → 报表 → 报表（需要开发者模式）。

**最常用字段说明（对应模型 `ir.actions.report`）：**

* **名称（Name）**：用户看到的报表名（会显示在“打印”菜单）。
* **模型（Model）**：这份报表作用在哪个业务模型上（如 `sale.order`、`account.move`）。
* **报表类型（Report Type）**：

  * `qweb-pdf`（最常用，PDF）
  * `qweb-html`（HTML 预览）
  * `qweb-text`（纯文本）
  * （可选）xlsx：需安装相应模块（如 `report_xlsx`）后才会出现。
* **报表文件/技术名称（Report Template / Report Name）**：填写 QWeb 模板的技术名（形如 `my_module.report_foo`）。它指向你写好的 `<template id="report_foo">…</template>`。
* **打印文件名（Print Report Filename / print\_report\_name）**：Python 表达式，决定下载时的文件名。例如：

  ```
  'SO-%s.pdf' % (object.name)
  ```

  或 `docs` 为多记录：`'invoices-%s.pdf' % (datetime.datetime.now().strftime("%Y%m%d"))`
* **保存为附件（Save as Attachment / attachment\_use）** 与 **附件表达式（attachment）**：启用后，渲染结果会保存到 `ir.attachment` 并**缓存复用**，适合“已确认单据不再变化”的报表：

  ```
  ('SO-%s.pdf') % (object.name)
  ```
* **纸张格式（Paper Format / paperformat\_id）**：选一个 `report.paperformat`，可覆盖公司默认。
* **多记录（Multiple / multi）**：允许一次选多条记录一起生成一个 PDF（比如多张发票合并成一个）。
* **绑定（Bindings）**：把报表挂到指定模型的 **打印菜单**。

  * 绑定模型（Binding Model）：与“模型”一致或其父类；
  * 绑定类型（Binding Type）：选“**Report**”（即显示在“打印”里）；
* **权限（Groups）**：限制哪些安全组能看到这份报表。

---

# 三、纸张格式在哪配？

设置 → 技术 → 报表 → **纸张格式**（模型：`report.paperformat`），常用字段：

* 页面尺寸：A4/Letter 或自定义宽高；
* 方向：Portrait / Landscape；
* 边距、DPI、页眉/页脚高度；
* WebKit 选项（wkhtmltopdf 的底层参数）。

> 报表优先使用**报表自身**的 `paperformat_id`；否则用**公司**的默认纸张。

---

# 四、QWeb 报表模板怎么写？

模板是 HTML + QWeb 指令（`t-esc` / `t-foreach` / `t-if` / `t-call` 等）。通常结构如下：

```xml
<odoo>
  <!-- 外层文档：注册模板 -->
  <template id="report_saleorder_document">
    <t t-call="web.external_layout"> <!-- 调用外层通用页眉页脚 -->
      <div class="page">
        <h2>销售订单 <span t-esc="doc.name"/></h2>
        <p>客户：<span t-esc="doc.partner_id.display_name"/></p>

        <table class="table table-sm o_main_table">
          <thead>
            <tr><th>产品</th><th>数量</th><th>单价</th><th>小计</th></tr>
          </thead>
          <tbody>
            <tr t-foreach="doc.order_line" t-as="line">
              <td t-esc="line.product_id.display_name"/>
              <td t-esc="line.product_uom_qty"/>
              <td t-esc="line.price_unit"/>
              <td t-esc="line.price_subtotal"/>
            </tr>
          </tbody>
        </table>
        <h3>合计：<span t-esc="doc.amount_total"/></h3>
      </div>
    </t>
  </template>

  <!-- 报表动作（ir.actions.report）可以也写在 XML 里注册 -->
  <record id="action_report_saleorder" model="ir.actions.report">
    <field name="name">销售订单（PDF）</field>
    <field name="model">sale.order</field>
    <field name="report_type">qweb-pdf</field>
    <field name="report_name">my_module.report_saleorder_document</field>
    <field name="print_report_name">'SO-%s.pdf' % (object.name)</field>
    <field name="binding_model_id" ref="sale.model_sale_order"/>
    <field name="binding_type">report</field>
    <field name="paperformat_id" ref="base.paperformat_euro"/> <!-- 举例 -->
  </record>
</odoo>
```

**变量说明：**

* 单记录打印时，常用 `doc` 或 `o`（Odoo 会注入一个当前记录）；
* 多记录打印时，一般注入 `docs`（recordset）。
* `t-call="web.external_layout"` 会复用系统的页眉/页脚（公司 Logo、公司信息等）。

> 样式：尽量用系统提供的类（如 `.o_main_table`）；复杂样式可以通过 assets 扩展或内联 CSS。

---

# 五、让它出现在“打印”菜单

* 在报表配置里**添加绑定**（Binding）到目标模型，或像上面 XML 那样填 `binding_model_id` + `binding_type=report`。
* 回到业务单据（例如“销售订单”），点击**打印**，就能看到新报表。

---

# 六、如何从代码里触发打印？

Python 触发（比如在按钮方法里）：

```python
action = self.env.ref('my_module.action_report_saleorder')
return action.report_action(self)   # self 是 recordset；也可传具体记录
```

让邮件自动带上 PDF：在“设置 → 技术 → 邮件 → 模板”里，设置“**要打印的报表**”为你的报表，邮件发送时会自动渲染并附上。

---

# 七、常见问题（务必看）

1. **提示需要 Wkhtmltopdf**：

   * PDF 报表用 `wkhtmltopdf` 渲染。必须在 Odoo 运行所在系统安装它；
   * `odoo.conf` 可设置：`wkhtmltopdf = /usr/bin/wkhtmltopdf`；
   * 报表空白/丢样式：请设好系统参数 `report.url`（渲染回连地址，通常 `http://127.0.0.1:8069`）和 `web.base.url`（对外地址）。
2. **文件名表达式报错**：

   * 表达式运行在受限环境，用 `object`（单记录）或 `docs`（多记录）构造字符串；注意返回**字符串**。
3. **多记录合并**：

   * `multi=True` 才会把多条选择合并到一个 PDF；否则会逐条下载。
4. **性能优化**：

   * 对已确认单据启用“保存为附件”，下次直接复用附件，速度快很多；
   * 记得清理历史附件（可写定时任务）。
5. **权限**：

   * 指定“Groups”，否则所有能访问该模型的用户都会看到这个打印项。
6. **纸张格式不生效**：

   * 报表里 `paperformat_id` 优先，其次公司默认；检查是否被外层 layout 或 CSS 影响。
7. **多公司 Logo/页眉**：

   * 使用 `web.external_layout` 会自动带公司信息；确保公司资料和 Logo 已配置。

---

# 八、一步步新建你的第一份 PDF 报表（从零到能打）

1. 在自定义模块里新建一个 XML（放 `views/report_sale.xml`），写上**QWeb 模板**与**报表动作**（上面的样例可直接改名复制）。
2. 在模块的 `__manifest__.py` 里把 XML 加进 `data` 列表。
3. 更新模块（开发 → 应用 → 更新应用列表，然后安装/升级你的模块）。
4. 打开目标业务单据 → 点“打印”，选择你的报表 → 出 PDF。
5. 需要优雅页眉页脚？把模板外层包 `t t-call="web.external_layout"`。
6. 需要自定义纸张？去“纸张格式”里新建，然后在报表上选中它。

---

# 九、扩展：Excel 报表 / 标签

* **XLSX 报表**：安装（或自建）`report_xlsx` 类似模块，报表类型会多出 xlsx；用 `xlsxwriter` 在 Python 类里生成表格。
* **标签/条码**：可在 QWeb 模板里用条码小部件（`widget="barcode"`）或 ZPL/PDF 方式输出；也可借助 OCA 的打印到打印机模块（advanced）。

---

## 结论

* 你在“设置 → 技术 → 报表 → 报表”配置的是“**如何打印**”——报表的入口与行为；
* 真正“**长什么样**”靠 QWeb 模板；
* PDF 渲染依赖 wkhtmltopdf；
* 绑定（Binding）让它出现在“打印”菜单；
* 结合“保存为附件”“邮件模板”的报表字段，能把 PDF 自动塞到邮件附件里，形成端到端流程。

如果你告诉我你的**目标模型**和**要显示的字段排版**，我可以按你的数据结构，直接给出一份可用的 XML 模板和报表动作记录，复制进去就能打。



# #########################################################################################################################






# #########################################################################################################################






# #########################################################################################################################

在 **Odoo 18** 里，如果你要把“订单”打印成 **票据打印机专用格式**，流程大致分 3 部分：

---

## 一、理解 Odoo 打印机制

* Odoo 的打印（比如“报价单”、“订单”、“发票”）是基于 **QWeb 报表模板**生成的 PDF。
* 这些模板是用 **XML + QWeb 指令**写的，可以控制内容、字段、排版。
* 默认的报表格式适合 A4 打印，不适合票据打印机，所以你需要 **自定义报表模板**。

---

## 二、操作步骤

### 1. 开启开发者模式

* 进入 **设置 → 激活开发者模式**。
* 这样可以在“技术”菜单里编辑报表。

### 2. 找到订单的报表

1. 进入 **设置 → 技术 → 报表 → 报表**。
2. 搜索 `sale.order`，你会看到类似 **Quotation / Order** 的报表定义。

   * 模型：`sale.order`
   * 报表类型：`qweb-pdf`
   * 模板：指向一个 QWeb 模板（比如 `sale.report_saleorder_document`）。

### 3. 复制并自定义模板

1. 进入 **设置 → 技术 → 用户界面 → 视图**。
2. 搜索 `report_saleorder_document`（就是订单打印用的 QWeb 模板）。
3. 复制一份（继承方式更好，避免覆盖官方模板）。

   * 新模板里你可以用 QWeb 标签和 HTML/CSS 调整格式：

     * 去掉多余表格线条
     * 控制字体大小
     * 设置票据宽度（比如 80mm 或 58mm）

例如：

```xml
<t t-name="custom.report_saleorder_ticket">
  <t t-call="web.external_layout">
    <div class="page" style="width:80mm; font-size:12px;">
      <h3 style="text-align:center;">订单</h3>
      <p>客户：<span t-field="o.partner_id.name"/></p>
      <p>订单号：<span t-field="o.name"/></p>
      <table style="width:100%;">
        <tr>
          <th>商品</th><th>数量</th><th>价格</th>
        </tr>
        <tr t-foreach="o.order_line" t-as="line">
          <td><span t-field="line.product_id.name"/></td>
          <td><span t-field="line.product_uom_qty"/></td>
          <td><span t-field="line.price_total"/></td>
        </tr>
      </table>
      <p style="text-align:right;">合计：<span t-field="o.amount_total"/></p>
    </div>
  </t>
</t>
```

### 4. 注册报表动作

* 在 **设置 → 技术 → 报表**，新建一个报表，绑定：

  * 模型：`sale.order`
  * 报表类型：`qweb-pdf`
  * 模板：选择你刚才新建的 `custom.report_saleorder_ticket`

这样，订单上就会出现一个新的打印按钮（比如“打印票据”）。

---

## 三、让票据打印机打印

1. 票据打印机一般是 **热敏打印机**，支持 58mm 或 80mm 宽度。
2. 你的 QWeb 模板里设置好宽度，比如 `style="width:80mm;"`。
3. 打印方式：

   * 默认是生成 PDF，你可以直接在浏览器里选择 **票据打印机**。
   * 如果要自动打印，可以安装 Odoo 的 **IoT Box** 或者配合 **cups 打印服务**做自动打印。

---

## 四、推荐开发流程

1. 先在测试环境里复制默认模板，改成简化版本。
2. 调整 CSS，直到在票据打印机里能正常显示。
3. 再上线使用。

---

✅ **总结**

* 在 Odoo 18 里，打印订单走的是 QWeb 模板。
* 你需要复制/继承 `sale.order` 的报表模板，自定义成票据格式（80mm/58mm 宽）。
* 注册一个新报表动作，让订单界面有“打印票据”按钮。
* 最终通过票据打印机打印。

---

要不要我帮你写一个 **完整的 Odoo 自定义模块骨架**（含 `__manifest__.py`、报表 XML、模板 XML），你可以直接安装到 Odoo，就能生成一个“票据打印版订单”？




# #########################################################################################################################

# 打印小票
太棒的需求！下面给你一份**可直接安装的 Odoo 18 自定义模块骨架**（“小票样式订单打印”），满足你贴的票据格式与排版。安装后，进入销售订单即可点击“打印小票”。

---

# 模块名称

`imon_receipt`

# 目录结构

```
imon_receipt/
├─ __init__.py
├─ __manifest__.py
├─ models/
│  └─ sale_order.py
├─ report/
│  ├─ receipt_report.xml      # 定义报表动作
│  └─ receipt_template.xml    # QWeb小票模板
└─ views/
   └─ sale_order_views.xml    # 在订单页面加入按钮/字段（可选）
```

---

## 1) `__manifest__.py`

```python
# -*- coding: utf-8 -*-
{
    "name": "IMON Receipt - Ticket Print",
    "summary": "Jewelry IMON 小票格式销售订单打印",
    "version": "1.0.0",
    "category": "Accounting/Reporting",
    "author": "Your Team",
    "depends": ["sale", "account"],  # 使用 sale.order、税、金额等
    "data": [
        "report/receipt_template.xml",
        "report/receipt_report.xml",
        "views/sale_order_views.xml",
    ],
    "assets": {},
    "license": "LGPL-3",
    "application": False,
    "installable": True,
}
```

---

## 2) `__init__.py`

```python
# -*- coding: utf-8 -*-
from . import models
```

---

## 3) `models/sale_order.py`

> 给 sale.order 增加一些字段，便于直接填入“收据号 / 传票号 / 负责人 / 现金支付 / 找零 / 营业编号”等。星期文本也一并计算，方便模板展示。

```python
# -*- coding: utf-8 -*-
from odoo import api, fields, models
import datetime

WEEKDAY_MAP = {
    0: "星期一", 1: "星期二", 2: "星期三", 3: "星期四", 4: "星期五", 5: "星期六", 6: "星期日"
}

class SaleOrder(models.Model):
    _inherit = "sale.order"

    imon_business_no = fields.Char(string="营业编号", help="例：T2010701001070")
    imon_receipt_no = fields.Char(string="收据号")
    imon_slip_no = fields.Char(string="传票号")
    imon_responsible = fields.Char(string="负责人", help="可直接录入，如 YOH")
    imon_cash_paid = fields.Monetary(string="现金支付")
    imon_change = fields.Monetary(string="找零")
    imon_items_count = fields.Integer(string="合计件数", compute="_compute_imon_items_count", store=False)
    imon_weekday_text = fields.Char(string="星期文本", compute="_compute_imon_weekday_text", store=False)

    @api.depends("order_line.product_uom_qty")
    def _compute_imon_items_count(self):
        for order in self:
            order.imon_items_count = int(sum(order.order_line.mapped("product_uom_qty")))

    @api.depends("date_order")
    def _compute_imon_weekday_text(self):
        for order in self:
            dt = fields.Datetime.context_timestamp(order, order.date_order) if order.date_order else datetime.datetime.now()
            order.imon_weekday_text = WEEKDAY_MAP.get(dt.weekday(), "")

```

---

## 4) `report/receipt_report.xml`

> 定义一个新的报表动作，在销售订单页出现“打印小票”菜单项。类型使用 qweb-pdf（票据机打印 PDF 也可；若需直接ESC/POS打印需另行扩展）。

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
  <report
      id="action_report_imon_receipt"
      model="sale.order"
      string="打印小票"
      report_type="qweb-pdf"
      name="imon_receipt.report_imon_receipt_ticket"
      file="imon_receipt.report_imon_receipt_ticket"
      print_report_name="'Receipt - %s' % (object.name)"
  />
</odoo>
```

---

## 5) `report/receipt_template.xml`

> QWeb 模板（80mm 宽热敏小票），直出你给的版式。注意中文/日文字体由系统打印端控制；wkhtmltopdf 默认字体可满足大部分场景，若需要更漂亮字体可在打印机/系统层安装。

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
  <template id="report_imon_receipt_ticket">
    <t t-call="web.external_layout">
      <div class="page"
           style="width:80mm; padding:2mm 3mm; font-size:12px; line-height:1.5; -webkit-print-color-adjust:exact;">

        <!-- 抬头 -->
        <div style="text-align:center; font-weight:700; font-size:15px;">
          Jewelry IMON（井門珠宝）
        </div>
        <div style="text-align:center; margin-top:2px;">
          电话：03-5826-8818
        </div>
        <div style="text-align:center;">
          营业编号：<t t-esc="o.imon_business_no or ''"/>
        </div>
        <div style="text-align:center;">
          地址：东京都台东区上野5-26-16
        </div>

        <div style="text-align:center; margin:6px 0; font-weight:700;">
          ★黄金、铂金高价收购★<br/>
          ★免费估价、鉴定★
        </div>

        <div style="text-align:center; font-weight:700; border:1px solid #000; display:inline-block; padding:1px 4px;">
          免税 TAX FREE
        </div>

        <hr style="border:0; border-top:1px dashed #000; margin:8px 0"/>

        <!-- 头部信息 -->
        <div>
          <t t-set="dt" t-value="o.date_order and o.date_order.astimezone(o.env.user.tz and pytz.timezone(o.env.user.tz) or None) if hasattr(o.date_order,'astimezone') else o.date_order"/>
          <t t-set="locdt" t-value="o.date_order and o.date_order or o.create_date"/>
          <t t-raw="0"/>
          <div>
            日期：
            <t t-esc="format_datetime(o, o.date_order or o.create_date, tz=o.env.user.tz, dt_format='yyyy年MM月dd日（')"/>
            <t t-esc="o.imon_weekday_text or ''"/>
            <t t-esc="format_datetime(o, o.date_order or o.create_date, tz=o.env.user.tz, dt_format='）HH:mm')"/>
          </div>
          <div>编号：<t t-esc="o.name"/></div>
          <div>收据号：<t t-esc="o.imon_receipt_no or ''"/></div>
          <div>传票号：<t t-esc="o.imon_slip_no or ''"/></div>
          <div>负责人：<t t-esc="o.imon_responsible or (o.user_id and o.user_id.name) or ''"/></div>
        </div>

        <hr style="border:0; border-top:1px dashed #000; margin:8px 0"/>

        <!-- 商品明细 -->
        <div style="font-weight:700; margin-bottom:4px;">商品明细</div>
        <t t-foreach="o.order_line" t-as="line">
          <div style="display:flex; justify-content:space-between;">
            <div style="width:58mm; word-break:break-all;">
              •<t t-esc="line.product_id.display_name"/>
              ×<t t-esc="int(line.product_uom_qty) if float(line.product_uom_qty).is_integer() else line.product_uom_qty"/>
              件
            </div>
            <div>
              <t t-esc="formatLang(line.price_total, currency_obj=o.currency_id)"/>
            </div>
          </div>
        </t>

        <hr style="border:0; border-top:1px dashed #000; margin:8px 6px"/>

        <!-- 合计 -->
        <div style="display:flex; justify-content:space-between; font-weight:700;">
          <div>合计（TOTAL）：<t t-esc="o.imon_items_count"/>件</div>
          <div><t t-esc="formatLang(o.amount_total, currency_obj=o.currency_id)"/></div>
        </div>
        <div style="text-align:right; margin-top:3px;">
          （含消费税TAX <t t-esc="int(round((o.amount_total - o.amount_untaxed) and (o.amount_total - o.amount_untaxed)/o.amount_untaxed*100 or 0))"/>%）
        </div>

        <hr style="border:0; border-top:1px dashed #000; margin:8px 6px"/>

        <!-- 付款 -->
        <div style="font-weight:700; margin-bottom:4px;">付款</div>
        <div style="display:flex; justify-content:space-between;">
          <div>•现金支付：</div>
          <div><t t-esc="formatLang(o.imon_cash_paid or 0.0, currency_obj=o.currency_id)"/></div>
        </div>
        <div style="display:flex; justify-content:space-between;">
          <div>•找零：</div>
          <div><t t-esc="formatLang(o.imon_change or 0.0, currency_obj=o.currency_id)"/></div>
        </div>

      </div>
    </t>
  </template>
</odoo>
```

> 说明：
>
> * 宽度设为 `80mm`，适配80mm票据机；若58mm，改为 `width:58mm`。
> * 日期使用 `format_datetime`（Odoo 18 提供）+ 计算字段 `imon_weekday_text` 输出中文星期。
> * 金额使用 `formatLang`，随订单币种显示。
> * 明细行用 `line.price_total`（含税/不含税可按需调整成 `price_subtotal`）。
> * 顶部“免税 TAX FREE”等完全按你样式。

---

## 6) `views/sale_order_views.xml`

> 在销售订单表单上露出自定义字段，方便填“营业编号/收据号/传票号/负责人/现金/找零”，并在打印下拉里显示“打印小票”。

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
  <record id="view_order_form_inherit_imon" model="ir.ui.view">
    <field name="name">sale.order.form.imon.receipt</field>
    <field name="model">sale.order</field>
    <field name="inherit_id" ref="sale.view_order_form"/>
    <field name="arch" type="xml">
      <xpath expr="//sheet/notebook/page[1]" position="after">
        <group string="IMON 收据信息">
          <field name="imon_business_no"/>
          <field name="imon_receipt_no"/>
          <field name="imon_slip_no"/>
          <field name="imon_responsible"/>
          <field name="imon_cash_paid"/>
          <field name="imon_change"/>
          <field name="imon_items_count" readonly="1"/>
        </group>
      </xpath>
      <!-- 在 打印 下拉里显示“打印小票”（新版通常自动出现report按钮；此处确保显示） -->
      <xpath expr="//header" position="inside">
        <button name="%(imon_receipt.action_report_imon_receipt)d"
                type="action" string="打印小票" class="btn-secondary"
                context="{'discard_logo_check': True}"/>
      </xpath>
    </field>
  </record>
</odoo>
```

---

# 使用步骤

1. 把上面的目录与文件放到 Odoo 的自定义模块目录（如 `/opt/odoo/custom_addons/imon_receipt`）。
2. **更新应用列表**：设置 → 应用 → 更新应用列表。
3. 搜索并安装 **IMON Receipt - Ticket Print**。
4. 进入 **销售 → 报价单/订单**，打开一张订单：

   * 填写：营业编号、收据号、传票号、负责人、现金支付、找零。
   * 点击顶部的 **打印小票**。
5. 选择你的 **票据打印机**（80mm/58mm），打印即可。

---

# 打印与显示小贴士

* 建议安装 `wkhtmltopdf`（Odoo 日志也提示缺少），否则 PDF 打印可能效果不稳定。
* 如果你希望**直接无 PDF 弹窗**在门店自动打印，需要配 **Odoo IoT Box** 或在内网配置 CUPS 打印服务与自定义自动打印模块（后续我可以给你再做一个“直打版”）。
* 需要 58mm → 把模板 `width:80mm;` 改为 `width:58mm;`，适当调小字体。
* 若需把“商品显示”改为你展示的**精确名称**（如“PT喜平手链 / K18喜平手链”），在产品名或订单行描述填写即可，模板取 `line.product_id.display_name` 或 `line.name`。（`line.name`更自由）

---

如果你愿意，我可以把这套代码**打成一个zip**给你直接安装，或者根据你们的**LOGO、公司抬头、税号位置**微调一版，做到“开箱即用”。





# #########################################################################################################################





# #########################################################################################################################





# #########################################################################################################################










# #########################################################################################################################

# 在Odoo 18 下，公司里怎么启用会计

在 **Odoo 18** 里，“启用公司会计”并不是在公司表单里点一个开关，而是需要确保 **公司拥有完整的会计配置**（日记账、科目表、会计应用权限）。我给你分几个步骤说明：

---

## 1. 确认公司启用了会计模块

1. 登录 Odoo，进入 **应用（Apps）**。
2. 搜索 **Accounting**。

   * 如果显示 **已安装（Installed）**，说明模块已经在系统里。
   * 如果只看到 **Invoicing（发票）**，那只是轻量功能，需要点击 **安装 Accounting（会计）** 才能获得完整会计功能。

---

## 2. 给公司分配会计要素

进入 **库存 / 会计** → **配置 → 日记账（Journals）**：

* 确认该公司有至少一个 **销售日记账**、**采购日记账**、**银行日记账**。
* 如果没有，就 **新建日记账**，并在表单里的 **公司字段（Company）** 里选择目标公司（比如「周大金（日本）」）。

进入 **会计 → 配置 → 科目表（Chart of Accounts）**：

* 检查公司是否已经有一套会计科目表。
* 如果没有，会在首次进入会计应用时提示你“为公司选择一套科目表”。
* 按照你所在地区的会计准则选择对应科目表并载入。

---

## 3. 检查用户权限

1. 打开 **设置 → 用户与公司 → 用户**。
2. 在用户表单的 **访问权限**里，把 **会计（Accounting）** 权限至少设为 **会计员（Accountant）**。

   * 没有这个权限，会计应用不会在主菜单出现。

---

## 4. 验证公司是否能使用会计

* 切换到目标公司（右上角公司选择器）。
* 进入主菜单，应该能看到 **会计** 应用。
* 打开后，如果一切正常，会提示你配置公司信息、会计年度、税率、科目表等。

---

## 总结

在 Odoo 18 里，“启用会计”对某个公司来说主要包括三点：

1. 安装完整的 **Accounting 模块**（而不是只有 Invoicing）。
2. 给公司分配 **会计科目表** 和 **日记账**。
3. 给用户分配 **会计员/顾问权限**。

---

要不要我帮你写一份 **新公司启用会计的完整清单**（从安装模块 → 载入科目表 → 建立日记账 → 配置税率），你照着一步步操作就能让「周大金（日本）」这家公司完整启用会计功能？


好的 👍 我来帮你整理一份 **Odoo 18 新公司启用会计功能的完整操作清单**。你照着一步步做，就能让像「周大金（日本）」这样的新公司具备完整的会计功能。

---

# 📝 Odoo 18 新公司启用会计功能清单

## 第 1 步：确认已安装完整的会计模块

1. 打开 **应用（Apps）**。
2. 搜索 **Accounting**。

   * 如果显示 **已安装（Installed）** → 说明模块已在系统中。
   * 如果只看到 **Invoicing（发票）** → 点击安装完整的 **Accounting** 模块，否则你看不到日记账、科目表等功能。

---

## 第 2 步：切换到目标公司

1. 在 Odoo 顶部栏的右上角找到 **公司切换器**。
2. 选择目标公司（例如「周大金（日本）」）。
3. 后续所有配置都必须在该公司环境下进行。

---

## 第 3 步：加载会计科目表（Chart of Accounts）

1. 进入 **会计 → 配置 → 会计科目表**。
2. 如果提示“请选择一套科目表”，根据你所在地区选择合适的本地化科目表：

   * 中国公司 → 中国会计准则科目表
   * 日本公司 → 日本会计准则科目表
   * 其他地区 → 对应国家的科目表或 IFRS 科目表
3. 确认系统已经加载了对应的科目表（应有资产、负债、收入、费用等科目）。

---

## 第 4 步：建立日记账（Journals）

每个公司至少要有以下几类日记账：

* **销售日记账（Sales Journal）**

  * 类型：Sales
  * 默认借/贷科目：收入类科目（Revenue）
  * 公司：周大金（日本）

* **采购日记账（Purchase Journal）**

  * 类型：Purchase
  * 默认借/贷科目：费用类科目（Expenses）
  * 公司：周大金（日本）

* **银行日记账（Bank Journal）**

  * 类型：Bank
  * 关联银行账户
  * 公司：周大金（日本）

* **现金日记账（Cash Journal，可选）**

  * 类型：Cash
  * 用于管理现金账户

👉 路径：**会计 → 配置 → 日记账（Journals） → 创建**。

---

## 第 5 步：配置税率（Taxes）

1. 进入 **会计 → 配置 → 税率（Taxes）**。
2. 根据公司所在国家的税制，设置 **销项税（Sales Tax）**、**进项税（Purchase Tax）**。
3. 税率必须绑定到对应的收入/费用科目。

---

## 第 6 步：检查公司信息

1. 进入 **设置 → 用户与公司 → 公司**。
2. 打开目标公司（周大金（日本））。
3. 确认填写了：

   * 公司名称
   * 地址
   * 税号（VAT/Tax ID）
   * 默认币种

这些信息会影响会计报表和发票。

---

## 第 7 步：确认用户权限

1. 进入 **设置 → 用户与公司 → 用户**。
2. 打开需要使用会计功能的用户。
3. 在 **访问权限** 里，把 **会计（Accounting）** 权限至少设为：

   * **会计员（Accountant）** → 可以录入凭证、生成报表
   * **顾问（Advisor）** → 拥有完整权限

---

## 第 8 步：验证是否启用成功

* 切换到 **周大金（日本）** 公司。
* 打开 **会计应用**，确认能看到：

  * 日记账
  * 会计科目表
  * 税率配置
  * 财务报表（损益表、资产负债表）

如果能看到这些功能，说明该公司已经完整启用了会计。

---

✅ **总结**
要让新公司启用会计功能，核心是：

1. 安装完整 **Accounting** 模块；
2. 给公司分配 **会计科目表**；
3. 建立 **销售/采购/银行日记账**；
4. 配置税率；
5. 确保用户有会计权限。

---

要不要我帮你做一个 **“新公司启用会计配置清单表格”**（像 Excel 那样的 checklist），你可以边操作边勾选？

你观察得很准确 👍。在 **Odoo 18** 里，会计模块（`account`）和早期版本不一样：

* **默认就安装了**（核心模块，系统必带），所以在应用列表里你会看到它始终是启用状态。
* 因为它是依赖性模块，所以 **没有卸载选项** —— 如果卸载，会导致很多核心功能（销售、采购、库存、发票）无法使用。
* 这就是为什么你即使没有“主动启用过”，它也会显示为“已启用”。

---

## 那么问题来了：怎么理解 Odoo 18 的“会计启用”？

在 Odoo 18 中，“启用会计”的意思不再是“安装一个模块”，而是：

1. **加载会计科目表（Chart of Accounts）**

   * 第一次进入会计应用时，系统会提示你为公司选择一套科目表。
   * 如果你没配置过，公司就处于“没有正式启用会计”的状态。

2. **配置日记账（Journals）和税率（Taxes）**

   * 每个公司至少要有一个销售日记账、采购日记账和银行日记账。
   * 如果这些缺失，系统在销售订单、发票时就会报错（你之前遇到的 “No journal could be found” 就是典型案例）。

3. **分配用户权限**

   * 没有“会计员/顾问”权限的用户，看不到完整的会计菜单。
   * 给用户分配权限后，会计功能才真正可见。

---

## 实际操作建议

1. **进入会计应用**（Accounting）：

   * 如果没有菜单，给自己开权限：

     * 设置 → 用户 → 你的用户 → 访问权限 → 会计 = Accountant。
   * 重新登录后，你会看到“会计”菜单。

2. **首次进入时加载科目表**：

   * 选择公司（比如“周大金（日本）”），系统会提示选择科目表。
   * 按照公司所在国家，选择对应的会计准则科目表。

3. **配置最基本的会计元素**：

   * 会计 → 配置 → 日记账 → 新建销售/采购/银行日记账。
   * 会计 → 配置 → 税率 → 设置 VAT/消费税。

---

✅ 总结
在 Odoo 18，“会计模块”是默认启用的，不可卸载。所谓“启用公司会计”，其实就是 **在公司里完成科目表加载 + 日记账 + 税率配置 + 权限设置**。完成这几个动作后，这个公司就算真正启用了会计。

---

要不要我帮你写一个 **“新公司启用会计初始化操作清单（专门针对 Odoo 18）”**，你可以直接照着清单一步步做，把「周大金（日本）」公司的会计功能完整启用？


# tips ###############################################################################################################

# 在销售订单页面，取消'打印小票80mm(预览)''打印小票80mm(PDF)'按钮项，告诉我如何取消这个，是否可以手动配置取消，还是代码取消。
```
> 这两个按钮是我们在销售订单表单视图里自定义加上的，属于代码层面的按钮，最佳做法是通过修改模块视图来移除。

  - 我已做的调整
      - 从 addons_custom/sale_receipt_thermal/views/sale_order_view.xml 中删除了以下两项：
      - `打印小票80mm(预览)`（action_report_sale_receipt_80mm_html）
      - `打印小票80mm(PDF)`（action_report_sale_receipt_80mm_pdf）
  -
  模块版本已更新为 18.0.1.0.4，便于升级生效。
  -
  使改动生效
      - 升级模块：./odoo-bin -c odoo.conf -d <DB名> -u sale_receipt_thermal --stop-after-init
      - 或前端开发者模式升级“Sale Receipt Thermal”
  -
  也可以用“手动配置”隐藏（不改代码）
      - 方法 A：在“设置 > 技术 > 用户界面 > 视图”里找到视图 sale.order.form.thermal.receipt.button，编辑并移除/注释 80mm 两个按钮（影响只在当前数据库）。
      - 方法 B：给按钮加隐藏组（不删除），例如加 groups="base.group_no_one"，普通用户不可见，管理员仍可见。
      - 注意：仅“归档/删除”对应的报表动作不会自动隐藏这些自定义按钮，反而会导致点击时报错。因此手动方式也应修改视图或按钮的可见性。
```

# 订单小票不需要二维码显示，取消。告诉我怎么具体怎么操作，手动操作，还是代码更改。
```
> 有两种做法，取决于你想影响“哪些小票”和“是否保留开关”。

  - 手动配置（不改代码）
      - 位置：设置 > 常规设置 > 热敏小票（我们新增的配置区）
      - 取消勾选“显示二维码(订单号)”
      - 影响范围：所有使用该配置的票据模板（销售、发票、POS）都不再显示二维码
      - 优点：随时可再开启；无需更新代码
      - 缺点：是全局开关，不能只针对销售小票关闭
      - 缺点：是全局开关，不能只针对销售小票关闭
  -
  代码更改（仅取消“销售订单小票”的二维码）
      - 我已按你的需求在代码里移除销售订单小票的二维码渲染块：
      - 修改文件：`addons_custom/sale_receipt_thermal/views/report_sale.xml`
      - 移除了 `<img ... QR ...>` 这段（保留了条码）
      - 模块版本已提升至 `18.0.1.0.5`
  - 生效方式：升级模块
      - `./odoo-bin -c odoo.conf -d <DB名> -u sale_receipt_thermal --stop-after-init`
  - 影响范围：仅销售订单小票不再显示二维码；发票/POS 小票仍可按配置显示

  建议

  - 如果只是“销售订单小票”不要二维码，当前已做代码更改即可；无需动配置。
  - 如果希望所有小票统一不显示二维码，用“手动配置”关掉更简洁。
```

# 告诉我，需要通过什么方式，在'设置 > 常规设置 '中新增'热敏小票'配置的，是手动增加还是代码增加。
```
> 简要回答：是代码增加，不是手动点点就能出现。你看到的“热敏小票”配置区是通过模块扩展 General Settings 视图和新增字段实现的。

  - 原理
      - 配置页来自模型 res.config.settings 的表单视图。
      - 在公司模型 res.company 加字段（如营业编号、标语、宣传语、页脚备注等）。
      - 在 res.config.settings 上加对应的 related 字段（related='company_id.xxx', readonly=False），用于在设置页读写公司字段。
      - 通过 XML 继承基础视图 base.res_config_settings_view_form，在 General Settings 中插入一块配置区展示这些字段。
      - 通过 XML 继承基础视图 base.res_config_settings_view_form，在 General Settings 中插入一块配置区展示这些字段。
  -
  本模块已做
      - 字段：addons_custom/sale_receipt_thermal/models/res_company.py 与 models/res_config_settings.py
      - 视图：addons_custom/sale_receipt_thermal/views/res_config_settings_view.xml
      - 视图继承点：inherit_id="base.res_config_settings_view_form"，用 xpath="//form" 插入 <div class="app_settings_block">热敏小票</div> 分组和字段
  -
  你要新增/修改配置项，按下面做（代码方式，推荐）
      - 在 res.company 增加字段（如需要多语言，translate=True）。
      - 在 res.config.settings 增加对应 related 字段（readonly=False）。
      - 在 res_config_settings_view.xml 把字段放到“热敏小票”块里。
      - 将视图文件列入 __manifest__.py 的 data，升级模块：-u sale_receipt_thermal。
  -
  可否“手动配置”新增这块？
      - 可以在开发者模式下，用“设置 > 技术 > 用户界面 > 视图”新建一个继承视图（选择 res.config.settings 的表单视图）并插入字段。这属于数据库级“手动创建视图记录”，但只对当前库生效，不可版本管理，不推
  荐用于团队/多环境。
      - 更不建议直接改基础视图（会影响系统升级和其它模块）。
  -
  何时选择哪种方式
      - 大多数场景用“代码方式”（模块内视图 + 字段）——可版本管理、可移植、可回滚。
      - 临时试验或单库快速调试可以用“手动创建继承视图”，验证通过后再落回代码。
```

# #############################################################################################################

> 结论：这不是“配置开关”，而是取决于是否有“付款数据”。有两条路：

  - 不写代码：按财务流程出具发票并登记付款，现有模板会自动显示“已收/找零”；
  - 写一点定制：如果你要在“未开票”的销售单上收现金并显示“找零”，需要在销售单上新增“实收/找零”字段（或向导）并改模板读取它们。

  为何现在看不到

  - 模板 addons_custom/sale_receipt_thermal/views/report_sale.xml 已写了“付款”区块，但有条件：
      - 仅当销售单存在“已过账”的发票 doc.invoice_ids 且这些发票有已核销的付款时才显示。
      - 已收金额计算为各发票的 amount_total - amount_residual；找零为 paid - doc.amount_total（仅当大于0时显示）。
  - 如果你打印时还没有创建/过账发票，或付款没有登记/核销，自然不会显示。

  方案A（无需编码，走标准账务）

  - 操作步骤：
      - 在销售单上【创建发票】→ 发票【过账】→ 发票【登记付款】（确保付款与发票核销）。
      - 回到销售单，点“销售小票（PDF）”打印。
  - 效果：
      - 模板会显示“付款”区块，“已收”为已核销金额；如确有超额付款则显示“找零”。
  - 适用：
      - 你的流程以“发票”为准，收款通过发票登记，符合会计口径。
  - 备注：
      - 发票场景通常不会“超额收款再找零”，找零更多出现在POS现金场景；如果没有超额，模板也不会显示“找零”。

  方案B（轻度定制，在销售单上直接收现并显示找零）

  - 适用：你希望在“未开票”的销售订单就收现金并打印小票（更像POS）。
  - 实施要点（编码）：
      - 在 sale.order 上新增字段：
      - `amount_paid`（Monetary，可由向导输入）；
      - `amount_change`（计算字段，`max(amount_paid - amount_total, 0)`）。
  - 增加一个向导“登记收款（小票）”，输入“实收金额”，保存到订单。
  - 调整模板 report_sale.xml：
      - 若 `doc.amount_paid` 存在则优先显示“已收 = amount_paid”、“找零 = amount_change”；
      - 否则回退到现有逻辑（从发票统计）。
  - 可选：若需入账，与 account.payment 打通，生成付款并与发票（或预收）核销；否则仅用于小票展示，不入账。
  - 优点：不依赖发票，前台快速开单收现；缺点：需要开发且需考虑会计一致性。

  现状快速自检

  - 你当前走的是销售单打印，但没有看到“已收/找零”，很可能是：
      - 没有“已过账”的发票，或
      - 已登记付款但未与发票核销，或
      - 打印时发票仍是草稿。
  - 可先试“方案A”验证：对该销售单创建并过账发票，登记付款后再打印看是否出现“付款”区块。

  要不要我来实现方案B的小改动？

  - 我可以为你：
      - 在 sale.order 增加 amount_paid/amount_change；
      - 加一个简单收款向导；
      - 调整 report_sale.xml 优先使用订单上的实收/找零显示；
      - 保持与现有样式一致。
  - 告诉我你更偏好“仅展示（不入账）”还是“生成正式付款单（入账）”。
  
  标准流程（从销售订单开始）

  - 打开销售订单 → 点击 创建发票：
      - 选择发票类型：常规发票（或定金/比例，按你的业务）。
      - 点击 创建并查看发票，进入新建的发票草稿。
  - 在发票草稿页面：
      - 核对客户、日期、付款条件、币种、行项目、税额、应收金额。
      - 点击 过账（发票状态变为“已过账/待付款”）。
  - 在已过账的发票上：
      - 点击 登记付款：
      - 选择 `日记账`（如：现金/银行）、`付款日期`、`付款方式`（通常为手动），`金额`默认等于发票未付金额。
      - 确认提交。
  - 提交后系统创建一笔客户收款并自动与该发票核销，发票 付款状态 变为 已支付（或 在支付中，取决于配置）。

  验证是否“已收/核销”

  - 打开发票，查看顶部 付款状态 是否为 已支付 或 在支付中。
  - 打开销售订单再打印小票：
      - 我们的模板会统计关联发票的已收金额：已收 = 发票金额 - 未收金额，显示在小票“付款”区块。

  找零说明

  - 通过发票的 登记付款 向导，默认付款金额等于发票未付金额，不会产生“找零”；因此小票上“找零”通常为 0 不显示。
  - 真的需要“找零”的场景更像 POS 现金收银。可选：
      - 使用 POS 应用收银并打印 POS 小票；
      - 或采纳我前面提到的“方案B（轻度定制）”，在销售单上新增“实收/找零”并在模板显示。

  常见问题与排查

  - 没出现“付款”区块：通常是还未创建/过账发票，或发票未登记付款。
  - 已登记付款但仍未核销：若付款不是在该发票上登记、而是独立收款，需要到 会计 > 对账 将该收款与发票配对核销。
  - 日记账或权限报错：检查 会计 > 配置 > 会计科目表/日记账，以及用户是否有会计或发票相关权限。

  可选替代路径

  - 直接从发票列表操作：会计/发票 > 客户发票 > 新建 → 填写 → 过账 → 登记付款。
  - 从银行对账单入账：导入/录入银行或现金流水 → 在 对账 界面将流水与发票配对核销。  
  
  

# #############################################################################################################

# odoo18下，POS应用怎么完成一个全流程的产品销售，详细说明

没问题。我把“从零到能卖出一单并结账关班”的完整流程梳理成 8 个阶段，分别告诉你在 **Odoo 18 · POS** 下需要做哪些配置、点击哪些菜单、系统背后发生什么，以及如何验收。界面名字可能随小版本略有变化，但方法一致。

---

# 0. 前置条件（一次性）

* 安装模块：**Point of Sale、Inventory、Accounting（或 Invoicing）、Contacts**（可选：Coupons & Promotions、Loyalty、IoT、Payment Terminal）。
* 账号与权限：给收银员用户启用“使用 POS”，经理/财务有会计权限。
* 硬件（可选）：条码枪、钱箱、**窄幅热敏小票打印机**（USB/网络/蓝牙，经 **IoT Box** 连接最佳）、秤、支付终端（Adyen/Worldline/Stripe Terminal 等）。

---

# 1. 主数据准备（卖什么、怎么计价、怎么扣库存）

1. **产品**（Sales/Inventory > Products）

   * 勾选 **Available in POS（在 POS 可售）**。
   * 价格（含税/不含税与税规则要统一）、条码、单位、类别。
   * **库存策略**：可用数量、是否按批次/序列号跟踪（Lots/Serials）。
   * 需要称重的商品设置“可称重”（接秤）。
   * 组合/套餐：用 BOM（Kit）实现入库为组件、对外卖成套（POS 扫主品即可扣组件库存）。

2. **税/价目表/舍入**（Accounting/Settings、Sales/Pricelists）

   * 设置默认税率与是否“价格含税”。
   * 如使用现金**分币舍入**（Cash Rounding），配置 POS 现金舍入规则。
   * 需要多价或时段价，开 **Pricelists** 并关联到 POS。

3. **支付方式**（POS/Configuration/Payment Methods）

   * 现金、银行卡、移动支付、礼品卡/储值（如用 Gift Card/eWallet）。
   * 若接三方支付终端，配置对应集成与回调（IoT/终端 App Key）。

---

# 2. 创建并配置一个 POS（收银台档案）

路径：**POS → Configuration → Point of Sale → New**

* 基本：门店/仓库、默认价目表、可售品类。
* **Payments**：勾选可用支付方式；开启“**Cash Control**（现金盘点）”。
* **Bills & Receipts**：抬头/尾注、logo、是否打印或邮件小票；**窄幅热敏打印**选用 IoT 打印机（ESC/POS）。
* **Invoicing**：是否允许对订单**开具发票**（需要会计模块）。
* **Loyalty/Promotions**（可选）：积分、优惠券、自动折扣规则。
* **Security**：收银员 PIN、折扣/改价是否需经理授权。
* **Hardware Proxy (IoT Box)**：绑定打印机、钱箱、客户屏、秤、支付终端。

> 完成后 **Save**。这就是一个可进入的 POS 工作台。

---

# 3. 开班（Open Session）

路径：**POS → Dashboard → 你的 POS → New Session / Open**

* 若启用 **Cash Control**：输入开班现金面额与合计（Opening Balance）。
* 联机自检：IoT 绿色、支付终端连通、打印机试打。
* 进入前台界面（左侧商品分类，中间商品卡片/键盘，右侧订单栏）。

---

# 4. 前台售卖（建单 → 结账 → 打小票）

**A. 建单**

* 选商品：点击/搜索/扫码（条码枪）；称重商品会弹秤重量。
* 批次/序列号：系统会要求选择或扫描。
* 折扣：行折扣或整单折扣（若受权限控制需输入经理 PIN）。
* 选择客户（可选）：用于**发票**、**积分**、**电子票据**或**税映射**。
* 优惠券/积分：录入券码或自动匹配规则，积分可抵扣或换赠品。

**B. 结账（Payment）**

* 点击 **Payment**，选择一种或多种支付方式（可 **拆分支付/部分支付**）。
* 使用支付终端：POS 金额推送到终端，刷卡/扫码后自动回写结果。
* 点击 **Validate** 完成收款。
* **小票**：打印/邮件；支持 **礼品小票**（隐藏金额）。

> **库存与会计**：
>
> * 支付确认后，系统生成 **POS 订单**；同步扣减库存（出库到 POS 仓位）。
> * 记账：在会计里形成对应销售/税/现金或应收的分录（通常在**关班**时统一过账/对账）。

---

# 5. 开票（需要时）

方式 1：**结账即开发票**（在 POS 配置中勾选自动开发票，或在支付前选择“发票”）。
方式 2：**后台补开**（POS → Orders → 选中订单 → Create Invoice）。

* 发票生成后走会计应收（如门店赊销给企业客户）。
* e-Invoice/税控（若所在地有合规要求），按本地化模块配置。

---

# 6. 退货/换货（售后）

* **扫描原小票二维码**或在 **POS → Orders** 搜索订单 → **Refund**。
* 系统生成负数量行，确认后：

  * 现金退回/原路退回/生成优惠券或储值；
  * 勾选“**回仓**”以自动产生**退货入库**。
* **换货**：同一张退货单里加入新商品正数量，差额多退少补。

---

# 7. 关班（Close Session）

路径：**POS → Dashboard → 当前 Session → Close**

* **现金盘点**：输入实际现金（Counting），系统与理论数对比，登记差异原因。
* **验证 & 过账**：Validate Closing & Post Entries

  * 自动生成银行对账单/现金日记账、销售收入与税分录；
  * 生成 **Closing Report（Z 报）**：按支付方式、税、分类、收银员汇总。
* 会计同事可在 **Accounting → Bank Statements / Journal Entries** 看到凭证与对账。

---

# 8. 进阶与可选能力

* **离线模式**：网络不可用时缓存订单，恢复时自动同步（需在 POS 配置开启）。
* **零售＋餐饮**：桌台/开台/厨房打印/菜品做法（启用 Restaurant 功能）。
* **价格/促销**：价目表（按客户/时段/数量）、自动折扣、买赠、第二件半价。
* **忠诚度**：积分规则（消费额→积分），积分换券或抵现金。
* **礼品卡/储值**：售卡、充值、消费、余额核销与会计映射。
* **多门店/多仓**：每个 POS 绑定不同仓位，跨仓调拨补货。
* **热敏小票自定义**：Logo、二维码（订单号/取货码/电子发票链接）、中英文混排；必要时可通过 **QWeb 模板**自定义版式。
* **数据报表**：按门店/时段/品类/收银员销量、毛利（需要成本与会计）、滞销排行。
* **权限与风控**：折扣、改价、删单、退货、现金抽屉等操作需经理 PIN；操作日志审计。

---

## 一张 “端到端验收清单”

1. **产品**：在 POS 可见、价格/税正确、库存 > 0、条码可扫。
2. **开班**：现金录入成功，IoT/打印/支付终端联通。
3. **下单**：普通品、称重品、序列号品均可加入；应用折扣/券/积分成功。
4. **收款**：现金/刷卡/扫码与拆分支付均成功；生成小票（纸质+邮件）。
5. **库存**：出库数量正确（含批次/序列）；退货可回仓。
6. **会计**：关班后凭证入账，税额与支付分录正确；差异原因留痕。
7. **报表**：Z 报/按时段销售报表正确；导出 CSV/Excel 无误。
8. **异常**：断网→离线下单→恢复自动同步；支付撤销/失败可重试；退款可查。

---

## 常见坑位与排错

* **价格含/不含税不一致**：确保产品价格策略与 POS 配置一致，否则小票与会计分录会偏差。
* **打印乱码/断行**：热敏机编码与宽度（58/80mm）不匹配，或未通过 IoT/ESC/POS 驱动。
* **条码无反应**：浏览器焦点不在 POS 界面、条码前后缀未匹配、或条码类型未启用。
* **扣库不发生**：POS 绑定的**仓库/库位**配置错误，或商品未启用库存追踪。
* **会计分录不生成**：未“关班过账”，或支付方式未绑定正确的会计科目/日记账。
* **退货不回仓**：退货单未勾选“回仓”，或退货库位未配置。

---

如果你告诉我：**是否需要发票、是否接第三方支付终端、是否打印窄幅热敏小票、是否要离线**，我可以按你的场景给出一套“可复制的配置清单 + 操作脚本（含小票模板与促销示例）”，直接套用到你们的 Odoo 18 环境里。

  
  
  

# #############################################################################################################

# POS 销售流程

下面把 **A. 建单** 的 5 个动作拆成「一次性开关 + 前台具体点击步骤 + 常见坑位」，你照着做，POS 前台就能顺畅把一张销售单建好（不含收款）。

---

# 0️⃣ 一次性开关（很关键，没开就不会弹相应窗口）

* **产品可在 POS 销售**：产品 → 常规 → 勾选 *Available in POS*
* **称重/电子秤**（二选一或都开）：

  * 用 IoT 电子秤：POS → 配置（你的 POS）→ *Hardware Proxy / IoT* 里绑定秤；产品 → 销售 → 勾选 *To Weigh*
  * 用“计重条码”：启用 **Barcode Nomenclature** 并配置“嵌入重量”的条码规则（如前缀 21/02），产品需有条码前缀匹配
* **批次/序列号**：库存 → 设置 → 勾选 *Lots & Serial Numbers*；产品 → 库存 → *Tracking* 选 *By Lots* 或 *By Unique Serial Number*；POS → 配置（你的 POS）→ 勾选 *Lots/Serial Numbers*
* **折扣权限**：POS → 配置（你的 POS）→ *Pricing*

  * 行折扣默认有“Discount”按钮
  * 整单折扣：勾选 *Global Discounts*（或用“促销/优惠券”模块实现）
  * 若需经理审批：在 *Security* 勾选“需要经理 PIN 才能改价/打折”（名称随版本略有不同）
* **客户/发票/税映射**：POS → 配置 → 勾选 *Invoicing*；会计 → 税 → 配置税；会计 → *Fiscal Positions*（税映射）
* **优惠券/积分**：安装并启用 *Coupons & Promotions*、*Loyalty*；在 销售/营销 → 促销计划、忠诚度规则 里创建对应方案，并勾选适用渠道 *Point of Sale*

---

# 1️⃣ 选商品（点击 / 搜索 / 扫码；含称重）

### 前台如何操作

* **点击选择**：在 POS 前台的商品网格中点击商品卡片；数量默认 +1
* **搜索**：顶部搜索框输入品名/内部参考/条码关键字
* **扫码**：条码枪对准条码，POS 自动将对应商品加入订单（数量 +1；若条码含数量/重量/价格，会按规则解析）
* **改数量**：

  * 点击右侧订单行 → 点“数量”键 → 输入数量
  * 或在数字小键盘输入数字后点“数量”
* **称重商品**（两种模式）

  * **IoT 电子秤**：点击称重商品 → POS 弹出秤读数对话框 → 稳定后“确认”
  * **计重条码**：直接扫“含重量”的条码（如前缀 21）；POS 会解析条码中的重量并写入数量

### 常见坑位

* 扫码无反应：焦点不在 POS 页面、条码规则没匹配、或产品没勾“Available in POS”
* 称重不弹窗：商品未勾 *To Weigh* 或 IoT 秤未连通（POS Dashboard 里 IoT 状态需为绿色）
* 计重条码被当作普通条码：检查 Barcode Nomenclature 里“类型=重量”的规则与前缀、长度

---

# 2️⃣ 批次 / 序列号（Lots/Serials）

### 前台如何操作

* 当你把“需要跟踪”的商品加入订单，**POS 会自动弹出**“选择批次/序列号”的窗口：

  * **序列号（单件唯一）**：逐个扫描或手输序列号；卖多个就录多个
  * **批次号**：从现有批次列表中选择；也可分多批次拆分数量
* 已选择后，订单行会显示已绑定的批次/序列号标记

### 常见坑位

* 不弹选择框：POS 配置未开启 *Lots/Serial Numbers* 或产品的 *Tracking* 没开
* 扫描序列号错误：序列号未入库或属于其他仓位/门店；先在库存里做好入库/内部调拨
* 卖多件序列商品：必须分别录入多个序列号（系统不允许一号多件）

---

# 3️⃣ 折扣（行折扣 / 整单折扣 + 审批）

### 行折扣（最常用）

1. 选中订单行 → 点 **Discount**（或“折扣”）
2. 输入折扣百分比（如 10 表示 10%）→ 确认
3. 若开启审批、超限或收银员无权，会弹出**经理 PIN**对话框，输入后生效

### 整单折扣（两种做法）

* **全局折扣按钮**：POS 配置勾 *Global Discounts* 后，前台多一个“全单折扣”按钮 → 输入 % → 应用到整单
* **促销/优惠券实现**：用 *Coupons & Promotions* 新建“立即折扣/百分比折扣”的 **Promotion Program**，限制至 POS 渠道；在前台输入券码或自动匹配规则

### 常见坑位

* 折扣按钮灰色：检查 POS 配置是否允许折扣/全单折扣
* 折扣后税额不对：核对“价格含税/不含税”的设置与税计算顺序
* 审批每次都弹：把“需要审批的阈值”设合理（如>15%才需审批）

---

# 4️⃣ 选择客户（发票 / 积分 / 电子票据 / 税映射）

### 前台如何操作

1. 点 **Customer**（或右侧订单栏“客户”）
2. 搜索姓名/手机/邮箱；或**扫码会员卡条码**
3. 若无记录 → 点击 **Create** 新建（录入基本信息）→ 选择

### 选择客户带来的效果

* **发票**：只有关联客户才能“开具发票”（客制化信息、税号、发票抬头）
* **积分**：忠诚度积分按客户累计与兑换
* **电子票据/邮件小票**：可向客户邮箱发送
* **税映射（Fiscal Position）**：按客户/区域自动替换税（如跨区/免税）

### 常见坑位

* 不能开发票：POS 配置未启用 *Invoicing* 或当前用户无会计权限
* 税规则没切：客户未绑定 Fiscal Position；或没配置基于国家/州的自动规则
* 积分没累计：忠诚度规则范围没包含该产品/POS；或还没“关闭并过账”同步后台

---

# 5️⃣ 优惠券 / 积分（录券码或自动匹配）

### 优惠券 / 促销（Coupons & Promotions）

**后台配置**（一次性）：

* 建一个 **Program**，选择类型（固定金额减免、百分比折扣、买 X 送 Y、第二件半价、特定产品减免…），**适用渠道 = Point of Sale**，设置生效日期、最低消费、参与品类等；需要券码就启用“生成优惠券/礼品券”
  **前台使用**：
* 在支付或订单界面，点击 **Promotions/Coupon**（或直接在金额键盘旁）→ **输入/扫码券码** → 系统校验并应用
* 自动规则会在满足条件时自动显示折扣行（无需输入券码）

### 忠诚度积分（Loyalty）

**后台配置**：

* 设“如何积分”（按金额/按产品/倍数）与“如何兑换”（积分抵现金、换赠品）；勾选适用 POS
  **前台使用**：
* 先**选择客户** → 下单后系统会显示“将获得 X 积分”；
* 兑换：在订单界面点击 **Redeem**（兑换），选择“抵现金”或“换赠品”，确认后抵扣应收

### 常见坑位

* 券码无效：券所属 Program 未启用 POS 渠道、过期、或使用次数达到上限
* 多个活动叠加冲突：检查 Program 的“优先级/互斥/是否与其他折扣叠加”
* 积分兑换没按钮：没选客户、或 Loyalty 规则没设置 POS 使用

---

## 🔁 串联一次“典型建单”操作（示例）

1. 扫码 **A 商品**（普通）→ 数量 +1
2. 点击 **B 商品（称重）** → IoT 弹出重量 0.356kg → 确认
3. 扫码 **C 商品（需序列号）** → 弹窗依次扫 2 个序列号 → 确认
4. 选中 **A 商品** → 点 **Discount** → 输入 `10`（打 9 折）
5. 点击 **Customer** → 搜索“张三”→ 选择（为开票/积分做准备）
6. 点 **Coupon/Promotion** → 扫码一张 20 元券 → 订单显示 -20 抵扣
7. （如果要用积分）点 **Redeem** → 选择“积分抵扣 10 元”

> 到这一步，“建单”就完成了；接下来点 **Payment** 进入收款/小票环节。

---

## 🛠️ 小故障速查

* **前台没看到按钮**：多数是 POS 配置项没打开（Global Discount、Lots/Serial、Invoicing、Loyalty、Promotions）
* **扫码没反应**：检查条码枪是否作为键盘输入、浏览器焦点在 POS、条码规则匹配
* **称重数值跳动**：秤未稳定/IoT 延迟，建议在弹窗内等待稳定指示或设置“去皮/稳定”参数
* **序列号提示不存在**：先在库存模块完成入库并分配到 POS 仓位，再销售
* **促销叠加异常**：梳理 Program 优先级与“是否与其他折扣叠加”的勾选

---

如果你告诉我：**是否用 IoT 电子秤、是否需要整单折扣按钮、促销/积分的具体规则、是否要开票**，我可以把对应的 **后台配置清单 + 前台操作截图要点**做成一份可执行 SOP 给你团队用。


  
  
  

# #############################################################################################################


下面给你一份**一步到位**的指南：在【指定公司】下新建“现金日记账”，并把它接到 POS 里使用。路径以 **Odoo 18** 为例，字段名可能随本地化略有差异，但流程一致。

---

# 0) 先把“公司”与“科目表”准备好

1. **切换到目标公司**
   右上角公司切换器 → 选择你要创建现金账的公司（例如 *chowta*）。
   若看不到该公司：设置 → 用户与公司 → 用户 → 打开你的用户 → *Allowed Companies* 勾选该公司。
2. **确认该公司已加载科目表**（非常重要）
   会计 → 设置 → 本地化/科目表 → 为该公司加载/安装合适的本地化与**科目表（Chart of Accounts）**。
   没有科目表就无法创建可用的现金日记账（缺少“银行和现金”类型科目）。

---

# 1) 新建现金日记账（Accounting → Journals）

路径：**会计 → 配置 → 日记账（Journals）→ 新建**

在弹出的表单里填写：

* **Journal Name（日记账名称）**：如“现金”（Cash）
* **Type（类型）**：选 **Cash**（不是 Bank）
* **Company（公司）**：选择目标公司（与上面的切换一致）
* **Short Code（简称）**：如 *CASH*（需唯一，用于分录编号）
* **Currency（币种）**：通常留空表示用公司的本位币；若你要专门用某外币，选定后要配置汇兑损益科目
* **Bank/Cash Account（流动性科目 / 现金科目）**：
  选择科目表中\*\*类型为“Bank and Cash（银行和现金）”\*\*的科目（常见名字如“Cash on Hand / 现金”）。
  如果列表里没有合适科目，先在 **会计 → 配置 → 科目表** 新建一个类型为 *Bank and Cash* 的“现金”科目，再返回选择。
* **Incoming/Outgoing Payment Methods（收/付款方式）**：勾选 **Manual**（现金就是手工收付）
* 其他保持默认，**保存**。

> 说明：设置成 **Type = Cash** 的日记账才是“现金日记账”。`Bank` 类型更多用于对账单导入与银行对账，`Cash` 则对应现金收付/现金抽屉。

---

# 2)（可选）启用现金舍入与找零策略

若你有现金收款并需“分币舍入/找零”：

* 会计 → 配置 → 设置 → **Cash Rounding（现金舍入）**：开启并按需要新建舍入规则（向上/向下/最近 0.1/0.05 等），并在**价目表或 POS** 中启用相应配置，避免分录出现难以找零的“分”。

---

# 3) 将现金日记账接入 POS 支付

1. **新建/编辑 POS 支付方式**
   POS → 配置 → **Payment Methods** → 新建/打开“现金”：

   * **Company**：目标公司（务必一致）
   * **Journal**：选择你刚建的 **现金日记账**
   * 其他默认即可，保存
2. **把该支付方式加入收银台**
   POS → 配置 → **Point of Sale** → 打开你的 POS → **Payments** 页签 → 勾选刚刚的“现金”支付方式 → 保存
3. （可选）**启用 Cash Control（现金盘点）**
   在该 POS 的 **Payments** 区勾选 *Cash Control*，开班/关班会做开箱现金/盘点与差异登记，更贴近线下管理。

---

# 4) 快速自测（确保链路 OK）

1. POS → 面板 → 打开会话（Open/New Session）
2. 下单 → **选择“现金”支付方式** → Validate
3. 关班（Close & Post）后，到 **会计 → 记账分录/日记账** 查看：

   * 分录落在你刚创建的**现金日记账**
   * 现金科目借/贷变化正确
   * 若启用现金盘点，可在会话关闭时看到现金差异分录

---

# 5) 常见问题与处理

* **仍然提示“无权读取日记账/Journal multi-company”**

  * 你当前用户没有把目标公司勾在 *Allowed Companies*；或右上角**当前公司**没切到目标公司
  * POS/支付方式/日记账**公司不一致**（任何一环跨公司都会报错）。确保三者 *Company* 字段一致
* **日记账里找不到合适“现金科目”**

  * 去科目表新建一个类型为 **Bank and Cash** 的科目（如“现金”），再回到日记账选择
* **POS 看不到“现金”支付方式**

  * 没把该支付方式加入 POS 配置的 *Payments* 列表；或支付方式/日记账属于别的公司
* **发现金额存在“几分”的找零难题**

  * 启用 **Cash Rounding** 并设置舍入；或在 POS 里启用现金舍入

---

## 一句话版

> 切到目标公司 → 会计/日记账里新建 **Type=Cash** 的日记账并选对“现金科目” → POS 新建“现金”支付方式并绑定这个日记账 → 把该支付方式加到 POS → 开班收现金测试 → 关班看分录落在正确公司与日记账。

需要的话，你把**公司名/币种/科目表语言**告诉我，我给你一套“截图式字段对照 + 最佳实践默认值”清单，照着填就不会错。

  
  
  

# #############################################################################################################


没问题。在 **Odoo 18 · POS** 前台，要让系统按“收多少现金→自动算找零”，按下面做就行。

# 一步到位：收现金并自动算找零

1. **点 “Payment/支付”** 进入收款页（右上角或订单区按钮）。
2. **选择“Cash/现金”支付方式**（看不到请见文末排查）。
3. **输入顾客给的钱**（两种常见交互，具体以你界面为准）：

   * **方式 A（最常见）**：先在右侧数字键盘输入金额（如 `100`）→ 再点一次 **Cash** 按钮（代表“添加 100 的现金付款”）。
   * **方式 B**：先点 **Cash** → 在“金额/Amount”输入框里键入 `100` → 点 **Add/添加**（或按 Enter）。
4. 屏幕会同时显示：**Total/应收、Paid/已收、Change/找零**。当 **Paid ≥ Total** 时，“Validate/验证”按钮会亮起。
5. **点 Validate** 完成交易。此时会弹出“**Change X**”提示（并可触发钱箱/打印小票）。

> 例：应收 **¥76.50**，顾客给 **¥100**
> 在支付页输入 `100` → 点 **Cash** → 页面显示 **Paid=100**、**Change=23.50** → **Validate** 即可。

# 小技巧

* **整钱快捷键**：支付页常会有 **Exact/刚好**、**+10 / +20 / +50 / +100** 等快捷按钮；点一下自动填入。
* **拆分支付**：先加一笔 `现金 50`，再选“银行卡/扫码”补齐剩余，**多条支付行**会并存。
* **编辑/删除支付行**：点支付行进入编辑；或点行尾的删除图标。
* **找零舍入**：若出现 0.01/0.02 这类尴尬找零，去 **会计 → 设置 → Cash Rounding** 新建舍入规则（例如四舍五入到 0.10），并在 POS 里启用相应设置。

# 看不到“现金”支付方式？（快速排查）

1. **POS 绑定支付方式**：POS → Configuration → **Point of Sale** → 你的 POS → **Payments** 页签，勾选 **Cash**。
2. **支付方式正确指向现金日记账**：POS → Configuration → **Payment Methods** → 打开“Cash”，确认 **Journal=现金日记账**、**Company** 与 POS 一致。
3. **更新会话**：若刚添加的支付方式不生效，**关闭当前会话并重新打开**（或点“同步/刷新”）。

这样操作，系统就会在支付页**实时显示找零**，并在 **Validate** 时提示“Change”金额。需要我用你的币种/整钱面额做一个“找零演示动图式步骤卡”也可以说一声。

  
  
  

# #############################################################################################################

你现在这个界面（右侧写着“**请选择付款方式**”，但没有任何按钮）= **这台 POS 的“支付方式”没配置/没加载到会话**。因此你没法录入“现金 1000”。做法是：先给这个 POS 配上“现金”支付方式，再刷新/重开会话，然后在支付页输入 1000 并点“现金”，系统就会出找零。

下面一步到位：

# 一、先在后台把“现金”支付方式配好

1. **切到正确公司**（很重要，之前你遇到过多公司限制）

* 右上角公司切换到你这台 POS 所属的公司（比如 chowta）。

2. **新建现金日记账**（若已建可跳过）

* 会计 → 配置 → **日记账** → 新建：

  * 类型：**Cash**
  * 公司：同上
  * 现金科目：选科目表里“现金/Bank and Cash”类型科目 → 保存

3. **新建 POS 支付方式：现金**

* POS → 配置 → **Payment Methods（支付方式）** → 新建：

  * 名称：**现金**
  * 公司：同上
  * Journal（日记账）：选刚建的**现金日记账** → 保存

4. **把“现金”加到这台 POS**

* POS → 配置 → **Point of Sale（收银台）** → 打开你的 POS → **Payments** 页签

  * 勾选/添加 **现金** 支付方式 → 保存

# 二、让前台加载到新支付方式

* 回到 POS 前台：

  * **优先尝试**点右上角的 **同步/刷新**（两个循环箭头图标）；
  * 若没有或不生效：**关闭当前会话**（POS 顶部菜单 → 关闭），回到面板后 **Close & Validate**，再 **Open/New Session** 重开。

> 原因：POS 会话会把配置缓存到浏览器；改了后台后必须同步或重开会话，支付方式才会出现。

# 三、现在录入顾客现金“1000”，自动算找零

1. 在前台点 **收款/Payment** 进入支付页；
2. 在数字键盘输入 **1000**；
3. 点击 **现金**（Cash）按钮 → 会新增一条“现金 1000”的支付行；
4. 右侧会显示 **Paid=1000、Total=935、Change=65**；
5. 点 **验证/Validate** 完成交易，系统提示找零 **65**，并打印小票（如已接打印机）。

# 四、仍看不到“现金”？三项速查

* 这台 **POS 的 Payments** 是否确实勾选了“现金”；
* **支付方式的 Company** 与 **POS 的 Company** 是否一致；
* 当前用户右上角**当前公司**是否就是这台 POS 所在公司（不一致时前台不会显示该公司的支付方式）。

# 五、可选优化

* 找零出现 0.01/0.02 这类尴尬金额：会计 → 设置 → **Cash Rounding** 新建舍入规则，并在 POS 中启用现金舍入。
* 启用 **Cash Control**：开班/关班盘点现金，记录差异更规范（POS → 你的 POS → Payments 勾选 *Cash Control*）。

照这个流程做，支付页就会出现“**现金**”按钮，你输入 **1000** 后系统会自动算出找零。需要我帮你核对这台 POS、支付方式、日记账三者的“公司”一致性的话，告诉我它们各自的公司名称就行。


  
  
  

# #############################################################################################################

# 目前是使用odoo18来做公司黄金首饰的销售，我希望在POS功能的店面销售页面中，可以对商品进行分类选择，告诉我技术思路，是做配置，还是使用代码来实现，黄金首饰商品属性清单如下：
```
一码一物还是一码多件
计件/计重
商品ID 必填
商品条码 必填
商品名称 必填
商品大类（黄金，K金，镶嵌，玉石） 必填
商品成色（空白 18k 足金  99.99% ）	 必填
商品类别（戒指 手镯）	 必填
商品主石（可空） 颜色，净度（写规格里））	 非必填
商品规格 自定义的	 非必填
商品工艺（硬金 3D 5D 5G 珐琅）	 非必填
净金重 数值型	 必填
总重 数值型	 必填
石重 数值型 克拉ct 非必填
配件重 数值型 非必填
证书号 非必填
商品销售工费 数值型 非必填
克工费还是件工费 选择 非必填
商品成本 数值型	 必填 默认为0
商品标价 数值型	 必填 默认为0
商品批发价 数值型 	 必填 默认为0
商品性质（正品，特价，赠品，物料，配件，活动款）	 必填
商品备注	 非必填

含税价	 非必填 默认为0
消费税	 非必填 默认为0
```

下面给你一份“能落地”的技术路线：**先用纯配置，把前台“按分类点选商品”跑起来；再按黄金首饰的特性，用少量或中等强度的定制代码，做好一码一物/计重和动态计价**。最后附一张“属性→落地到哪个模型/字段”的对照表，避免设计跑偏。

---

# 一、前台“按分类选择商品”：**先用配置就能实现**

目标：在 POS 前台左侧出现“分类树”，点分类后中间出现该类商品卡片。

**怎么做（无需写代码）**

1. **POS 分类（pos.category）**

   * 顶层 = 你列的“商品大类”：黄金 / K金 / 镶嵌 / 玉石
   * 子层 = “商品类别”：戒指 / 手镯 / 吊坠 / 项链 …
   * 产品 → 勾选 *Available in POS*，并指定 **POS 分类**（可多选，但建议一主类一子类，层级清晰）。
2. **POS 配置**

   * POS → 配置 → 你的 POS → 确保默认商品网格与分类已开启（默认就开，通常不用勾额外选项）。
3. **搜索辅助**

   * 把“成色/工艺/性质”等关键字放到产品名称的别名或内部参考里，前台搜索能快速过滤（配置期的省力手段）。

> ✅ 这一步完成后，你已经能在前台**按分类点选**销售。
> ⚠️ 但“成色/工艺/性质”等更细粒度的*可点击筛选*，POS 原生没有，需要轻度前端定制（下文给方案）。

---

# 二、黄金零售的“核心难点”与推荐实现

黄金首饰与普通零售的差别主要在：**一码一物、计重/计件、动态计价（随金价+工费）、单件多属性**。下面按“配置能搞定/需要代码”分层建议。

## 0）一码一物 vs 一码多件（强烈建议）

* **一码一物**：产品跟踪方式= *By Unique Serial Number*（唯一序列号）；POS 配置里启用 *Lots/Serials*，前台加货时会**弹出序列号（条码）选择**。

  * 一件一序列号（=你们商品“标签码”），适配**净金重/总重/证书号**这些“每件不同”的字段。
* **一码多件**：适用于配饰/辅料等，不追踪序列号，走“计件”。

> ✅ 结论：贵金饰**优先用“一码一物”**；把“每件不同”的属性放到 **序列号(批次)记录**里。

## 1）计件 / 计重（配置为主）

* **计件**：产品的 UoM=“件”，序列号只是标识，不参与定价。
* **计重**：两种做法
  A. **称重秤**（IoT）：商品勾 *To Weigh*，前台取 IoT 秤重量。适合散金裸料。
  B. **序列号上带重量**（推荐给首饰）：每件实重/净金重都不同，把重量存在**序列号上**，**不必使用 IoT 秤**。前台扫码选择序列号后直接取该件重量参与定价。

## 2）动态计价（建议分期实现）

> 公式示例（按实际业务可调）：
> **单价** = 净金重(g) × 当日金价(元/g) × 成色系数 + 工费（按克或按件） + 石头/配件加价 − 促销折扣

* **V0（纯配置可用，最快上线）**

  * 后台每天更新“当日金价”，你们生成**带价条码**（含最终价格），POS 前台扫“带价条码”直接把价格带入（Odoo 的 **Barcode Nomenclature** 支持“价格编码”条码）。
  * 好处：**不写代码**，前台价格就是条码上的价；
  * 代价：改价逻辑在后台或称重系统做，POS 只收价。
* **V1（少量代码，后端算价）**

  * 扩展 **序列号(stock.production.lot)** 字段：净金重/总重/石重/证书号/工费/工费类型…
  * 扩展 **每日金价模型**（metal.pricelist）：金种（足金/18K 等）、生效日期、元/克。
  * **在 POS 加载这些数据**（后端 loader），前台选择序列号时自动计算**单位价格**并写入行。
  * 这是“中等难度”的后端+POS 数据加载定制，稳定、可审计。
* **V2（前端完整定制）**

  * 在 POS **商品屏上方加“筛选条”**（可点击：大类/成色/类别/工艺/性质），即时过滤商品网格。
  * 选择序列号后弹出**计价弹窗**，可切换计件/计重、临时改金价/工费（可控权限、需经理 PIN）。
  * 自定义小票模板：打印净金重、总重、石重、证书号等。

---

# 三、你的“属性清单”落地到 Odoo 的**数据模型**（推荐映射）

> 原则：**模板级不变的放 product.template / product.product；每件都不同的放序列号 stock.production.lot**。
> 这样 POS 前台“选序列号”即可带出该件的真实参数与价格。

| 属性                    | 建议存放                                                                   | 说明                        |
| --------------------- | ---------------------------------------------------------------------- | ------------------------- |
| 一码一物/一码多件             | product.template → Tracking: *By Unique Serial Number* / *No Tracking* | 决定是否强制选序列号                |
| 计件/计重                 | product.template（单位） + lot字段（净金重）                                      | 首饰用 lot 上的重量更准确           |
| 商品ID/条码/名称            | product.product 标准字段                                                   | POS 可扫条码                  |
| 商品大类（黄金/K金/镶嵌/玉石）     | **pos.category（顶层）**                                                   | 用于前台分类                    |
| 商品类别（戒指/手镯...）        | **pos.category（子层）**                                                   | 左侧可点的子分类                  |
| 成色（18K/足金/99.99%）     | product.attribute 或 template 自定义选择字段                                   | 用于搜索/报表；如需前台筛选可做定制 filter |
| 工艺（硬金/3D/5D/珐琅）       | product.attribute 或 template 自定义字段                                     | 同上                        |
| 主石信息                  | lot 自定义字段（颜色/净度可做 text/选择）                                             | 每件不同放 lot                 |
| 商品规格                  | template 或 lot（看是否每件不同）                                                | 自评估                       |
| 净金重 / 总重 / 石重 / 配件重   | **lot 自定义数值字段**                                                        | 定价核心                      |
| 证书号                   | **lot 自定义字段**                                                          | 小票打印                      |
| 商品销售工费 & 计费方式（克/件）    | lot 自定义字段（或 template 作为默认值）                                            | 参与定价                      |
| 商品成本                  | product.product 的 *standard\_price* 或 lot 字段                           | 成本核算                      |
| 商品标价 / 批发价            | product.product 的 *list\_price* / 价目表；或 lot 覆盖价                        | POS 用价目表选择零售/批发           |
| 商品性质（正品/特价/赠品/配件/活动款） | product.template 选择字段（也可做 tag）                                         | 前台可搜索，促销规则可用              |
| 备注                    | lot 或 template                                                         | 任一                        |
| 含税价/消费税               | 税设置 + fiscal position；如特殊消费税，做税种/映射                                    | 必要时 lot 上放“含税最终价”覆盖       |

> 以上 lot 字段通过自定义模块扩展 `stock.production.lot`，POS 端在选 lot 后把这些字段带入定价和小票。

---

# 四、实现路线图（建议分阶段落地）

**阶段 1（纯配置，1–2 天）**

* 建 POS 分类（大类/类别两级）并给商品打分类；
* 决定追踪方式：贵金饰一律 *Unique Serial*；启用 POS 的 *Lots/Serials*；
* 先用“带价条码”或手工录价（临时方案）上线。

**阶段 2（轻定制，1–2 周）**

* 扩展 lot 字段（净金重/石重/证书/工费…）；
* 做“每日金价”后台模型与设置页面；
* POS 加载 lot 扩展字段与金价，**自动算价**（选 lot 即计算，支持经理授权改价）。

**阶段 3（前端增强，1–2 周）**

* 在 POS 商品屏顶部加筛选条（大类/成色/类别/工艺/性质）；
* 自定义小票模板，打印重量/证书等；
* 报表：按成色/工艺/净金重统计毛利、库存和销量。

---

# 五、无需代码也能“输入价”的两个备用方案

* **带价条码**：条码里包含最终售价（后台或称重打印价签，POS 扫描直接带价）。
* **价目表法**：零售/批发分两套 Pricelist；特价用 Coupons & Promotions（固定减免/百分比）；但**动态金价 × 重量**仍建议用代码或后台批量算价后写入。

---

# 六、注意事项

* POS **缓存**：改后台字段/配置后要“**重开会话/同步**”才会生效。
* **现金舍入**：涉及现金收款，开 **Cash Rounding** 避免找零尴尬。
* **多公司**：商品/日记账/支付方式/POS 配置的公司要一致。
* **权限**：改价/折扣建议走“经理 PIN”，保留审计。

---

如果你愿意，我可以给你一个**样例模块设计清单**（模型字段 + POS 前端扩展点 + 价签条码规则），或者先把“阶段 1 的配置脚本（分类与产品模板示例）”写好，你直接导入就能在前台看到分类点选的效果。

  
  
#  Odoo 18 的**技术宣讲普及**，
专讲这 5 个与 POS 强相关的核心模型：`product.template`、`product.product`、`pos.category`、`stock.production.lot`、`product.attribute`。我会用“是什么 → 在 POS/业务里的作用 → 关键字段/关系 → 实操要点 → 常见坑”这条线来讲，并结合黄金首饰场景点到要害。

---

# 1) `product.template`（产品模板）

**是什么**

* “产品的蓝本”。定义了货品的公共属性（名称、税、计量单位、类型、默认售价、成本、跟踪方式等）。
* 一个模板可生成**0\~N 个变体**（variants），每个变体就是一条 `product.product`。

**在 POS/黄金业务里的作用**

* 决定商品是否能在 POS 销售（*Available in POS* 勾选在模板上）。
* 设置 **追踪方式**：不跟踪 / 批次（lot） / **序列号（serial）**。黄金首饰建议：**一码一物 → Serial**。
* 设置 POS 分类（见 `pos.category`），决定前台网格如何分组显示。
* 定义默认税、UoM（计件/计重），以及默认售价（可被后续规则/动态定价覆盖）。

**关键字段（选）**

* `name`、`default_code`（内部参考）、`barcode`
* `type`（storable/consumable/service）
* `list_price`（标价）、`standard_price`（成本）
* `taxes_id` / `supplier_taxes_id`
* `uom_id`（销售单位）、`uom_po_id`（采购单位）
* `tracking`（`none`/`lot`/`serial`）
* `pos_categ_ids`（多对多 → `pos.category`）

**实操要点**

* **黄金推荐**：模板只放“不会因单件不同而改变”的属性（如“大类=黄金”“类别=戒指”“成色=18K（若做成属性）”）；
  单件差异（净金重、证书号、总重、工艺差异）**放到序列号上**（见第 4 节）。
* 勾选 *Available in POS*，并赋 **POS 分类**（大类/子类），前台就能点分类找商品。

**常见坑**

* 把“每件都不同”的信息放模板或变体上，导致一款商品被拆成海量变体（维护困难、POS 卡顿）。
* 混淆 `product.category`（会计/库存类目）和 `pos.category`（POS 展示分类），两者用途不同。

---

# 2) `product.product`（产品变体）

**是什么**

* 基于模板 + 属性值 组合生成的**具体销售单元**（SKU）。
* POS 实际销售的就是 `product.product` 记录。

**在 POS/黄金业务里的作用**

* 可为不同属性值生成不同条码/内部参考（便于扫码销售）。
* 如果你只做“模板级商品 + 序列号一码一物”，变体可能只有 1 个（不强制做很多变体）。

**关键字段（选）**

* `product_tmpl_id`（父模板）
* `attribute_value_ids`（该变体选用的属性值）
* `barcode`、`default_code`、`lst_price`（显示价，通常承袭模板）

**实操要点**

* 只有当“属性差异会稳定影响定价/成本/库存策略”时才做变体；否则用模板 + lot 信息即可。
* 变体太多会拖慢 POS 首屏加载；黄金零售多数情况下**不建议爆炸式变体**。

**常见坑**

* 滥用属性生成大量变体（颜色×规格×工艺×成色），POS 缓存庞大、难以管理。

---

# 3) `pos.category`（POS 分类）

**是什么**

* 专用于 POS 前台展示的分类树（与 `product.category` 不同）。
* 控制前台左侧“可点击的分类”，以及中间网格的商品分组。

**在 POS/黄金业务里的作用**

* 顶层：**商品大类**（黄金 / K 金 / 镶嵌 / 玉石）
* 子层：**商品类别**（戒指 / 手镯 / 项链 / 吊坠 …）
* 产品模板上选 `pos_categ_ids`，前台即可按分类浏览。

**关键字段**

* `name`、`parent_id`（可以做多级）
* 产品侧是 **many2many** 到模板

**实操要点**

* 设计 2 级树就够用（大类 → 类别），避免层级过深影响收银效率。
* 产品必须勾选 *Available in POS*，并设置了 `pos_categ_ids`，前台分类才有内容。

**常见坑**

* 把会计/库存类目 `product.category` 当成 POS 分类使用，导致前台没有分组效果。

---

# 4) `stock.production.lot`（批次/序列号）

**是什么**

* 批次/序列号主表。**当模板的 `tracking` = lot/serial 时**，每件（或每批）会对应一条 `stock.production.lot`。
* POS 若启用 *Lots/Serials*，销售此类商品时会 **弹窗选择/扫描** lot/serial。

**在 POS/黄金业务里的作用（核心）**

* **一码一物**：每件首饰 = 一条 lot/serial；在 lot 上挂**净金重、总重、石重、证书号、工费（按克/按件）、工艺**等**单件差异**。
* **动态计价**：POS 选择 lot 后，取其字段 + 当日金价 → 计算最终价并写入订单行（需要轻度定制）。
* 小票/发票可打印 lot 信息（证书号、净金重等）。

**关键字段（标准 + 建议扩展）**

* 标准：`name`（序列号/批次号）、`product_id`、`company_id`、`expiration_date`（如用）、与库存量关联的 quants。
* 自定义（黄金建议加）：`net_gold_weight`、`gross_weight`、`stone_weight_ct`、`certificate_no`、`wage_value`、`wage_type`（per\_g / per\_piece）、`process_technique` 等。

**实操要点**

* 启用：产品模板 `tracking = serial`，POS 配置里启用 *Lots/Serials*。
* **数据流**：入库/上柜时即创建 lot，并录入上述单件属性；POS 销售时选择该 lot，即可用于定价与打印。
* **定价实现**：后端 loader 把 lot 额外字段和“当日金价”送到 POS 前端；前端选择 lot 时调用定价函数，更新行价（可设经理 PIN 才允许覆盖）。

**常见坑**

* 将“每件不同的信息”存模板/变体上，导致信息错位；正确做法是**落在 lot 上**。
* POS 未启用 *Lots/Serials*，前台无法选择序列号，黄金业务落空。

---

# 5) `product.attribute`（产品属性）与属性值

**是什么**

* 属性（如“成色”“尺寸”“材质”“颜色”）及其取值（如 “18K / 足金 / 9999”）。
* 与模板上的属性线（`product.template.attribute.line`）结合，用于**生成变体**或仅供展示。

**在 POS/黄金业务里的作用**

* **成色**、**工艺**、**类别**等可以用属性表达，但要控制“是否生成变体”：

  * 对“会爆炸组合”的属性，设为 **No Variant（不生成变体，仅展示/描述/搜索）**；
  * 只有当不同取值必须成为不同 SKU 时再生成变体（如戒指号数若确实要独立库存）。
* 可用于前台**搜索关键字**和**后台报表分组**；若做前台筛选条，需要前端小定制。

**关键字段/设置点**

* `product.attribute`：属性名（如“成色”）、值集
* `product.template.attribute.line`：把属性挂到模板，并指定 **变体生成策略**（立即/动态/不生成）
* 变体生成策略影响 `product.product` 的数量和 POS 性能

**实操要点**

* 黄金场景通常：**成色**可以是“属性（No Variant）+ lot 字段兜底”；“戒指号数”若需要独立库存可作为生成变体的属性，否则也放 lot/描述。
* 把“用于定价的关键因素”（净金重、工费）放 lot，不要靠属性推公式（复杂且不精确）。

**常见坑**

* 一股脑把所有差异都做成“变体属性”，导致几百上千 SKU；应优先用 **lot 承载单件差异**。
* 忘了将不必要的属性设为 **不生成变体**。

---

## 实操小片段（示例）

**A. 给模板启用序列号、挂 POS 分类**

```python
tmpl = env['product.template'].create({
    'name': '黄金戒指',
    'type': 'product',
    'tracking': 'serial',                 # 一码一物
    'list_price': 0.0,
    'standard_price': 0.0,
    'available_in_pos': True,
    'pos_categ_ids': [(6, 0, [pos_cat_gold_id, pos_cat_ring_id])],
    'uom_id': uom_piece_id,
})
```

**B. 扩展 lot 字段用于黄金属性（模块中的继承）**

```python
class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    net_gold_weight = fields.Float("净金重(g)")
    gross_weight    = fields.Float("总重(g)")
    stone_weight_ct = fields.Float("石重(ct)")
    certificate_no  = fields.Char("证书号")
    wage_value      = fields.Float("工费")
    wage_type       = fields.Selection([('per_g','克工费'), ('per_piece','件工费')], default='per_piece')
    process_technique = fields.Selection([
        ('hard','硬金'), ('3d','3D'), ('5d','5D'), ('5g','5G'), ('enamel','珐琅')
    ])
```

**C. POS 前端选序列号 → 动态算价（思路）**

* 后端 loader：把 lot 扩展字段和“当日金价表”推到 POS 前端。
* 前端（JS）：监听“lot 选中”事件 → 根据：净金重×金价×成色系数 + 工费 等公式 → `orderline.set_unit_price(new_price)`。
* 权限：若手工覆盖价格，要求经理 PIN。

---

## 结论 & 推荐落地顺序

1. **配置先行**：`product.template` 勾 POS 可售、设 `tracking=serial`；建好 `pos.category`（大类/子类两级）；POS 配置启用 *Lots/Serials*。
2. **数据建模**：将**单件差异**落在 `stock.production.lot` 自定义字段。
3. **适度用属性**：`product.attribute` 只在必要时生成变体；其他设为 **No Variant** 用于描述/搜索。
4. **动态定价**：先用“带价条码/后台算价”起步；随后做 POS lot 驱动的自动定价（少量代码）。

如果你需要，我可以基于你们的字段表，给一个**模块化清单**（后端字段定义、POS 数据加载点、前端改价钩子、示例小票模板），作为你们开发的脚手架。

  
  

# #############################################################################################################

# 好的，给我一个**样例模块设计清单**（模型字段 + POS 前端扩展点 + 价签条码规则），可以实操的，step by step的过程要写清晰。既要有设计，还要有产品导入过程，而且，大量产品的导入需要能够通过模版文件批量导入。


太棒了，下面给你一套**可实操的样例方案**：一个最小可用的 Odoo 18 模块（支持黄金首饰 POS 场景），包含

* ✅ 数据建模：把“单件差异”（净金重/证书等）落在 `stock.production.lot`
* ✅ 动态计价：选中序列号后，按“净金重 × 当日金价 × 成色系数 + 工费（克/件）”自动改价
* ✅ POS 前端扩展：在选择序列号后自动计算价格
* ✅ 价签条码规则（可选）：扫“含价格的条码”直接带入售价
* ✅ 批量导入模板：分类、产品、序列号（lot）三类 CSV 模板与导入步骤

> 注：代码是“脚手架级别”的最小实现，能跑通思路；不同环境/本地化可能需微调字段或菜单位置。

---

# 0) 我们要实现什么（功能概览）

1. **后端字段**

   * `stock.production.lot` 扩展：净金重、总重、石重、证书号、工费值、工费类型（克/件）、工艺
   * `metal.pricelist`（新模型）：金种、价格(元/克)、生效日期、公司、是否启用；用于“当日金价”
2. **定价公式（示例，可调）**

   ```
   单价 = lot.净金重(g) × 当日金价(元/g, 按成色/金种) × 成色系数 + 工费
   工费 = wage_value（当 wage_type=per_g 时按克计；per_piece 时为固定值）
   ```
3. **POS 前端**

   * 选中序列号（lot）后，自动 `orderline.set_unit_price(new_price)`；需要权限时触发经理 PIN
4. **POS 分类**

   * 用 `pos.category` 构建“大类（黄金/K金/镶嵌/玉石）→ 类别（戒指/手镯/…）”两级树
5. **批量导入**

   * CSV 模板（含列名与样例），导入 `pos.category`、`product.template/product.product`、`stock.production.lot`

---

# 1) 模块骨架

```text
custom_addons/
└─ pos_gold_pricing/
   ├─ __init__.py
   ├─ __manifest__.py
   ├─ security/
   │   └─ ir.model.access.csv
   ├─ models/
   │   ├─ __init__.py
   │   ├─ metal_pricelist.py
   │   ├─ stock_production_lot.py
   │   └─ product_template.py    # 如需成色系数、默认工费等模板级参数
   ├─ views/
   │   ├─ metal_pricelist_views.xml
   │   └─ stock_production_lot_views.xml
   └─ static/src/js/
       └─ pos_gold_pricing.js
```

`__manifest__.py`

```python
{
    "name": "POS Gold Pricing",
    "version": "18.0.1.0",
    "summary": "POS 动态计价（黄金/首饰：净金重×当日金价+工费）",
    "category": "Point of Sale",
    "depends": ["point_of_sale", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/metal_pricelist_views.xml",
        "views/stock_production_lot_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_gold_pricing/static/src/js/pos_gold_pricing.js",
        ],
    },
    "installable": True,
}
```

---

# 2) 模型与字段

`models/metal_pricelist.py`

```python
from odoo import models, fields, api

class MetalPricelist(models.Model):
    _name = "metal.pricelist"
    _description = "Metal daily price for jewelry"

    name = fields.Char("Name", required=True)
    metal_type = fields.Selection([
        ('au_9999', 'Au 999.9'),
        ('au_999',  'Au 999'),
        ('au_au18k','Au 18K'),
        ('au_au14k','Au 14K'),
    ], required=True)
    price_per_g = fields.Float("Price (CNY/gram)", digits=(16, 4), required=True)
    fineness_factor = fields.Float("Fineness Factor", default=1.0,
                                   help="成色系数，如 18K ~ 0.75")
    effective_date = fields.Date("Effective Date", required=True)
    company_id = fields.Many2one("res.company", default=lambda self: self.env.company, required=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('uniq_day_metal_company', 'unique(metal_type, effective_date, company_id)',
         '同一天、同一金种、同一公司只能有一条当日金价。')
    ]

    @api.model
    def get_price(self, company_id, metal_type, on_date=None):
        on_date = on_date or fields.Date.context_today(self)
        rec = self.search([
            ('company_id', '=', company_id),
            ('metal_type', '=', metal_type),
            ('effective_date', '<=', on_date),
            ('active', '=', True),
        ], order="effective_date desc", limit=1)
        return rec and (rec.price_per_g, rec.fineness_factor) or (0.0, 1.0)
```

`models/stock_production_lot.py`

```python
from odoo import models, fields, api

class StockProductionLot(models.Model):
    _inherit = "stock.production.lot"

    # 单件差异字段
    net_gold_weight = fields.Float("净金重(g)", digits=(16, 4))
    gross_weight    = fields.Float("总重(g)", digits=(16, 4))
    stone_weight_ct = fields.Float("石重(ct)", digits=(16, 4))
    certificate_no  = fields.Char("证书号")
    wage_value      = fields.Float("工费")
    wage_type       = fields.Selection([('per_g','克工费'), ('per_piece','件工费')], default='per_piece')
    process_technique = fields.Selection([
        ('hard','硬金'), ('3d','3D'), ('5d','5D'), ('5g','5G'), ('enamel','珐琅')
    ], string="工艺")
    metal_type = fields.Selection([
        ('au_9999','Au 999.9'), ('au_999','Au 999'), ('au_au18k','Au 18K'), ('au_au14k','Au 14K')
    ], string="金种/成色", help="用于匹配当日金价；也可从模板继承默认值。")

    # 工具：后端统一算价（前端也会算一次）
    def compute_pos_unit_price(self):
        self.ensure_one()
        company_id = self.company_id.id or self.env.company.id
        price, factor = self.env['metal.pricelist'].get_price(company_id, self.metal_type or 'au_9999')
        gold_part = (self.net_gold_weight or 0.0) * price * (factor or 1.0)
        if self.wage_type == 'per_g':
            wage = (self.net_gold_weight or 0.0) * (self.wage_value or 0.0)
        else:
            wage = self.wage_value or 0.0
        return round(gold_part + wage, 2)
```

（可选）`models/product_template.py`（如果希望模板存默认成色/工费）

```python
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    default_metal_type = fields.Selection([
        ('au_9999','Au 999.9'), ('au_999','Au 999'), ('au_au18k','Au 18K'), ('au_au14k','Au 14K')
    ], string="默认金种")
    default_wage_type = fields.Selection([('per_g','克工费'), ('per_piece','件工费')], default='per_piece')
```

`security/ir.model.access.csv`

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_metal_pricelist_user,access_metal_pricelist_user,model_metal_pricelist,base.group_user,1,1,1,0
```

`views/metal_pricelist_views.xml`

```xml
<odoo>
  <record id="view_metal_pricelist_tree" model="ir.ui.view">
    <field name="name">metal.pricelist.tree</field>
    <field name="model">metal.pricelist</field>
    <field name="arch" type="xml">
      <tree>
        <field name="name"/>
        <field name="company_id"/>
        <field name="metal_type"/>
        <field name="price_per_g"/>
        <field name="fineness_factor"/>
        <field name="effective_date"/>
        <field name="active"/>
      </tree>
    </field>
  </record>

  <record id="view_metal_pricelist_form" model="ir.ui.view">
    <field name="name">metal.pricelist.form</field>
    <field name="model">metal.pricelist</field>
    <field name="arch" type="xml">
      <form>
        <sheet>
          <group>
            <field name="name"/>
            <field name="company_id"/>
            <field name="metal_type"/>
            <field name="price_per_g"/>
            <field name="fineness_factor"/>
            <field name="effective_date"/>
            <field name="active"/>
          </group>
        </sheet>
      </form>
    </field>
  </record>

  <menuitem id="menu_metal_root" name="Metal Pricing" parent="point_of_sale.menu_point_root"/>
  <menuitem id="menu_metal_pricelist" name="Daily Metal Prices" parent="menu_metal_root" action="action_metal_pricelist"/>

  <record id="action_metal_pricelist" model="ir.actions.act_window">
    <field name="name">Daily Metal Prices</field>
    <field name="res_model">metal.pricelist</field>
    <field name="view_mode">tree,form</field>
  </record>
</odoo>
```

`views/stock_production_lot_views.xml`

```xml
<odoo>
  <record id="view_stock_production_lot_form_gold" model="ir.ui.view">
    <field name="name">stock.production.lot.form.gold</field>
    <field name="model">stock.production.lot</field>
    <field name="inherit_id" ref="stock.view_production_lot_form"/>
    <field name="arch" type="xml">
      <xpath expr="//sheet/notebook" position="inside">
        <page string="Jewelry">
          <group>
            <field name="metal_type"/>
            <field name="net_gold_weight"/>
            <field name="gross_weight"/>
            <field name="stone_weight_ct"/>
            <field name="wage_type"/>
            <field name="wage_value"/>
            <field name="process_technique"/>
            <field name="certificate_no"/>
          </group>
        </page>
      </xpath>
    </field>
  </record>
</odoo>
```

---

# 3) POS 前端扩展（选 lot 后自动算价）

`static/src/js/pos_gold_pricing.js`（OWL/registry patch；核心是拦截 lot 选取完成后给行价）

```javascript
/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Orderline } from "@point_of_sale/app/store/models";

const { patch } = registry.category("models");

patch(Orderline.prototype, "pos_gold_pricing_Orderline", {
    // 当序列号被设置/变更时，重新计算单价
    setPackLotLines(newPackLotLines) {
        const res = this._super(newPackLotLines);
        try {
            const lots = this.getLots() || this.pack_lot_lines || [];
            // 取第一个序列号（一码一物）
            const lotName = lots.length ? (lots[0].lot_name || lots[0].name) : null;
            if (!lotName) return res;

            const product = this.getProduct();
            // 从 POS 缓存中取到 lot 扩展字段（最简方式：把 lot 字段通过 pos.loader 推到 this.pos.db；这里演示假定已存在）
            const lotData = this.pos.jewelryLots && this.pos.jewelryLots[lotName];
            if (!lotData) return res;

            // 价格 = 净金重 × 当日金价 × 成色系数 + 工费
            const pricePerG = this.pos.metalPrice[lotData.metal_type]?.price_per_g || 0.0;
            const factor    = this.pos.metalPrice[lotData.metal_type]?.fineness_factor || 1.0;
            const goldPart  = (parseFloat(lotData.net_gold_weight) || 0) * pricePerG * factor;
            let wage = 0.0;
            if (lotData.wage_type === "per_g") {
                wage = (parseFloat(lotData.net_gold_weight) || 0) * (parseFloat(lotData.wage_value) || 0);
            } else {
                wage = parseFloat(lotData.wage_value) || 0;
            }
            const finalUnitPrice = Math.round((goldPart + wage) * 100) / 100;

            // 写入单价（不改变税/折扣逻辑）
            this.setUnitPrice(finalUnitPrice);
        } catch (e) {
            console.warn("POS gold pricing failed:", e);
        }
        return res;
    },
});
```

> 说明
>
> * 上面假设 `this.pos.jewelryLots` 和 `this.pos.metalPrice` 已通过后端 loader 拉到前端（你可以在自模块中用 `pos.session` 的加载 hook 或改造 `pos.order` RPC 返回，因篇幅这里不展开后端 loader，方向是正确的）。
> * 如暂时没有 loader，也可先不自动算价，改为“**带价条码**”方案，见第 5 节。

---

# 4) 配置 POS 侧（关键）

1. **产品模板**

   * 勾选 *Available in POS*
   * `tracking` 设为 **Serial**（一码一物）
   * 指定 `pos.category`（大类/类别两级）
2. **POS 配置**

   * 启用 *Lots/Serials*
     -（可选）开启“改价需经理 PIN”
3. **每日金价**

   * 菜单：POS → Metal Pricing → Daily Metal Prices
   * 填写金种、价格(元/克)、成色系数、日期；每天一条
4. **重启/重开 POS 会话**（POS 有缓存，改完必须同步或重开）

---

# 5) 价签条码规则（可选，不写代码也能带价）

> 当你还没完成前端 loader/自动算价时，可以给首饰打印**带价格的条码**，POS 扫码后直接用条码中的价格做“最终售价”。

**步骤**

1. 打开 **开发者模式**
2. **库存 → 配置 → 条码 → 条码命名规则（Barcode Nomenclatures）**
   选择正在使用的命名规则，添加一条“**价格条码**”规则：

   * 名称：`Price With Prefix 24`
   * 类型：**Price**
   * 前缀：`24`
   * 条码长度：如 `13`
   * 价格位数：例如 `5`（代表 5 位，单位“分”）
   * 乘数：`0.01`（把“分”转为“元”）
3. 打印价签时生成条码：`24 + 00010 + 商品码` ⇒ 表示价格 10.00
4. POS 前台扫码该条码 → 行价将直接变为 10.00（不会再自动算）

> 具体“Pattern/长度/乘数”按你们打印系统而定，上述是一个常见示例。

---

# 6) 批量导入模板（CSV）

### (A) POS 分类：`pos.category`

**列头（最低）**
`id,name,parent_id/id`
**样例**

```csv
id,name,parent_id/id
pc_gold,黄金,
pc_gold_ring,戒指,pc_gold
pc_gold_bangle,手镯,pc_gold
pc_k, K金,
pc_k_ring,戒指,pc_k
```

### (B) 产品：`product.template`（先导模板，系统会自动有 1 个变体）

**列头（常用）**
`id,name,default_code,barcode,available_in_pos,pos_categ_ids/id,tracking,type,uom_id/id,list_price,standard_price`
**样例**

```csv
id,name,default_code,barcode,available_in_pos,pos_categ_ids/id,tracking,type,uom_id/id,list_price,standard_price
pt_gold_ring_001,黄金戒指A,GR-A,690000000001,1,"pc_gold,pc_gold_ring",serial,product,uom.unit,0,0
pt_gold_bangle_001,黄金手镯A,GB-A,690000000002,1,"pc_gold,pc_gold_bangle",serial,product,uom.unit,0,0
```

> 备注：`uom.unit` 是“件”的外部 ID；`pos_categ_ids/id` 可一次填多个（用逗号）。

### (C) 序列号：`stock.production.lot`（一码一物；把单件差异放这里）

**列头（建议）**
`name,product_id/id,company_id/id,metal_type,net_gold_weight,gross_weight,stone_weight_ct,wage_type,wage_value,process_technique,certificate_no`
**样例**

```csv
name,product_id/id,company_id/id,metal_type,net_gold_weight,gross_weight,stone_weight_ct,wage_type,wage_value,process_technique,certificate_no
SN-GR-A-0001,pt_gold_ring_001,base.main_company,au_9999,3.56,3.70,0.10,per_piece,120.00,hard,CERT-0001
SN-GR-A-0002,pt_gold_ring_001,base.main_company,au_9999,3.48,3.60,0.00,per_g,10.00,3d,CERT-0002
SN-GB-A-0001,pt_gold_bangle_001,base.main_company,au_9999,15.23,15.50,0.00,per_piece,280.00,5d,CERT-1001
```

**导入步骤（统一流程）**

1. 设置 → 开发者模式
2. 进入相应模型列表（POS 分类 / 产品 / 序列号）
3. 点击 **导入** → 选择 CSV → 映射列 → 测试导入 → 导入
4. 导入后 **重开 POS 会话**（或同步），前台即可按分类选择商品，选 lot 自动带出信息。

---

# 7) 上线步骤（Step by Step）

1. 将模块目录 `pos_gold_pricing` 放到 `--addons-path` 的自定义路径下；更新应用列表并安装
2. 在 **Metal Pricing** 菜单配置当日金价（至少为 Au 999.9 填一条）
3. 按上述 CSV 模板导入 **POS 分类** → **产品** → **序列号**
4. 在 **POS 配置**启用 *Lots/Serials*；必要时启用“改价需经理 PIN”
5. **重开 POS 会话**，选择商品 → 扫/选序列号 → 验证行价（自动算价）；打印小票核对净金重/证书等（表单里可增加到收据模板）
6. （可选）配置 **价签条码规则**，用于过渡期或人工定价

---

# 8) 常见问题 & 快速排错

* **选 lot 后价格不变**

  * 前端 JS 未加载（清缓存/重开会话）；或未实现前端 loader，`this.pos.jewelryLots/metalPrice` 为空
  * 过渡期先用“带价条码”方案
* **多公司拦截（Journal multi-company）**

  * 右上角激活对应公司；lot/company、产品/company 保持与 POS company 一致
* **会话不生效**

  * 改完配置/导入新数据 → **必须重开会话/点同步**（POS 有浏览器缓存）
* **导入映射失败**

  * 外部 ID 写错；先测试导入，修正列名或值，再正式导入

---

如果你希望，我可以把“前端 loader 的一版最小实现”（把 `metal.pricelist` 与 lot 字段缓存到 `this.pos`）也补上，或者直接把上面的模块打包成一个可安装 ZIP（你给我你的字段/金价口径，我按你的口径改成适配版）。


# zip实施

好了！我把完整的 **Odoo 18 模块（pos\_gold\_pricing）** 已经打包好了，包含：

* 模型与字段：`metal.pricelist`（每日金价）、`stock.production.lot` 扩展（净金重、证书号、工费等）
* POS 前端补丁：选中序列号后，RPC 到后端按公式计算行价并写入
* 视图与菜单：金价维护菜单
* 安全：基础访问控制
* 批量导入模板：POS 分类、产品、序列号（CSV）
* README 使用说明

👉 **下载模块 ZIP**： [pos\_gold\_pricing.zip](sandbox:/mnt/data/pos_gold_pricing.zip)

---

## 快速上线步骤（Step by Step）

1. **安装模块**

   * 把 ZIP 上传/放到 Odoo 服务器，解压或直接加入 `--addons-path` 路径
   * 更新应用列表，安装 **POS Gold Pricing**

2. **配置数据**

   * 菜单：POS → **Metal Pricing → Daily Metal Prices**，填一条当日金价（Au 999.9……）
   * 产品模板：

     * 勾 **Available in POS**
     * `tracking = serial`（一码一物）
     * 指定 `pos.category`（大类/类别）
   * POS 配置：启用 **Lots/Serials**，必要时启用“改价需经理 PIN”

3. **批量导入（可选）**

   * 位置：模块内 `samples/`
   * 导入顺序：`pos_categories.csv` → `products.csv` → `lots.csv`
   * 导入后 **重开 POS 会话**（或点同步）

4. **前台验证**

   * 选商品 → 弹出/选择 **序列号** → 行价会自动计算（净金重 × 当日金价 × 成色系数 + 工费）
   * 打印小票前可在行上看到最终单价

---

## 备注 & 调优建议

* **价格公式**在 `models/stock_production_lot.py: compute_pos_unit_price()`，你可按业务改（如加入石头/配件加价、促销等）。
* **RPC 入口**：`pos_compute_price_by_lot(lot_name, company_id)`，JS 在 `static/src/js/pos_gold_pricing.js` 的 `setPackLotLines` 中调用。
* 若你们有 **IoT 秤/带价条码**，也可以共存：条码带价将直接覆盖单价。
* 改完后端/前端，**需重开 POS 会话** 使缓存刷新。

需要我把“价格公式 + 税/舍入 + 经理 PIN 权限”再按你的实际口径细化，也可以继续告诉我具体规则，我直接在这份模块里替你改好。



  
  
  

# #############################################################################################################


没问题。下面把 **“勾 Available in POS（在 POS 可售）”** 的几种常用操作方式讲清楚：单个产品、批量操作（列表批改 / 导入 CSV / 服务器动作），以及常见看不到勾选框的原因。

---

# 单个产品：在表单页勾选

1. 进入产品列表

   * **销售** → 产品 → 产品（或 **库存** → 产品 → 产品）
2. 打开某个产品（**产品模板**页面，而不是变体的只读行）
3. 找到勾选项：

   * 在 Odoo 18，通常在表单的 **销售** 页签里，或单独的 **Point of Sale** / “销售点”页签里有一个复选框：
     **Available in POS**（在 POS 可售）
4. 勾选后 **保存**。

> 说明：这个勾选在技术上对应字段 `available_in_pos`，在**模板**层面生效（会作用于该模板的所有变体）。

---

# 批量打开：三种方式

## A. 列表视图批量编辑（零代码）

1. 打开产品列表，切换到**列表视图**。
2. 用筛选器选中你要处理的一批产品（比如按品类、标签、公司）。
3. 勾选需要修改的多条 → 顶部 **动作** → **批量编辑**（或“编辑”/“批量更新”，不同翻译略有差异）。
4. 在弹窗里找到 **Available in POS**，勾选 → **应用**。

> 如果没有“批量编辑”，可以先 **导出** ID，再用导入覆盖（见下一条）。

## B. CSV 导入覆盖（适合成百上千条）

1. 导出模板：在产品列表，**导出**以下字段，至少包含：

   * `id`（或 `external_id`）
   * `name`
   * `available_in_pos`
2. 把导出的 CSV 里 `available_in_pos` 一列全改为 `1`（或 `True`）。
3. 回到产品列表点 **导入**，上传 CSV，映射字段（确保 `id` 对应“更新匹配的记录”），**测试导入** → **导入**。

**最小导入样例：**

```csv
id,available_in_pos
product_template_123,1
product_template_456,1
```

## C. 服务器动作 / Odoo Shell（管理员快速处理）

* **服务器动作（批量写）：**
  模型选 `product.template`，代码：

  ```python
  (records or env['product.template'].browse(env.context.get('active_ids', []))).write({'available_in_pos': True})
  ```

  在产品列表勾选多条 → 动作 → 执行该服务器动作。
* **Odoo Shell：**

  ```bash
  odoo shell -d <你的库>
  ```

  ```python
  env['product.template'].search([('available_in_pos','=',False)]).write({'available_in_pos': True})
  ```

---

# 让勾选生效到 POS 前台

* **POS 有缓存！** 勾选/批量修改后，务必在 POS 面板里 **关闭并重新打开会话**，或在前台点“**同步/刷新**”。
* 确保产品有 **POS 分类（pos.category）**（可选，但建议设置，便于前台按分类浏览）。

---

# 常见“看不到勾选框 / 勾了没效果”的原因

1. **未安装 POS 模块**
   没装 `point_of_sale` 时，这个字段可能不显示。先安装 POS 应用。

2. **打开的是变体行而非模板**
   在仅显示 `product.product` 变体表单时，有些字段不可改。切换到**模板**表单页面再找。

3. **权限或多公司过滤**
   当前用户没权限或当前激活公司与产品公司不一致，导致看不到或保存失败。右上角激活正确公司。

4. **POS 会话未刷新**
   勾选后不重开会话，前台看不到新商品或变更。关闭/重开会话或点击同步后再试。

5. **被价目表/过滤“隐藏”**
   前台能搜到但网格不显示，检查 POS 绑定的价目表、产品是否被筛掉；分类是否正确。

---

# 验收步骤（建议这样核对）

1. 后台产品表单勾上 **Available in POS** 并保存；
2. 给产品设置 **POS 分类**；
3. 关闭并重开 POS 会话；
4. 前台左侧选到对应分类，能看到该产品卡片；搜索条码/名称也可加入订单。

如果你遇到“界面里找不到这个勾选”的情况，发我一张产品表单的截图（打个码即可），我可以标出具体位置；或者告诉我你是**哪个菜单路径**进去的（销售/库存），我按那个界面结构精准描述点哪里。

  
  
  

# #############################################################################################################


#  **Odoo 18** 的“开发者模式下 **Server Actions（服务器动作）**”完整讲解：
从**它是什么、在哪里建、如何触发**到**技术细节（可用变量/事务/权限/多公司）**、**绑定到列表的 Action 菜单**、**Run Manually 手动运行**，再到**典型可复制的实例代码**（含你 POS 场景），一步步来。

---

# 1. 它是什么？能做什么？

**Server Action（模型：`ir.actions.server`）** 是一段在服务器端运行的动作（通常是一小段 Python 代码），可以：

* 批量修改记录（如：将产品“在 POS 可售”统一打开）
* 执行业务流程（如：尝试关闭 POS 会话、生成/取消单据）
* 返回一个 **action** 打开窗口/报表（比如执行完后直接弹出某列表）
* 与 **“动作绑定（ir.actions.binding）”** 结合，出现在任意模型的 **Action/动作** 菜单里
* 与 **Automated Actions（base.automation）** 结合，实现“创建/更新/定时触发”

> 和 **Scheduled Actions（ir.cron）** 不同：Server Action 典型用于**即点即执行**或被其他机制触发；`ir.cron` 是后台定时器。

---

# 2. 入口与操作路径

## A) 新建 Server Action（开发者模式）

**设置 → 技术 → 动作 → 服务器动作**

* **模型（Model）**：选择要作用的模型（例如 `product.template`）
* **动作类型（State）**：一般选 **执行 Python 代码**
* **代码（Code）**：粘贴你的 Python 片段（见下文示例）

> 保存后，这个动作“存在但不可见”；需要 **绑定** 到某个列表/表单或通过“手动运行”来执行。

## B) 绑定到列表的“动作（Action）”菜单

Odoo 18 把绑定独立成了 **Action Bindings（ir.actions.binding）**：

* **设置 → 技术 → 用户界面 → Action Bindings（动作绑定） → 新建**

  * 名称：任意
  * **动作（Action）**：选上一步的 Server Action
  * **模型（Model）**：比如 `product.template`
  * **绑定类型（Binding Type）**：选 **Action**
  * **绑定视图类型（Binding View Types）**：勾 **List**（也可勾 Form）
  * Active：勾上
* 回到该模型的**列表视图**，**勾选记录** → 顶部 **动作** 菜单就能看到你的动作了

> 找不到“Action Bindings”菜单？走“曲线救国”：**设置 → 技术 → 数据库结构 → 模型 → 搜索 `ir.actions.binding` → 进入后点顶部“View Records/记录”**，从这里新建绑定记录。

## C) 直接“手动运行”（不绑定也能跑）

在 Server Action 表单上，常见有 **Run Manually / 手动运行**：

* 点它 → 在弹窗里填 **Domain**（筛选记录）
* 确认运行，后台会用该 domain 找记录，把你的代码跑一遍

---

# 3. 技术细节（***强烈建议熟悉***）

### 3.1 可用变量（safe\_eval 环境）

在 **代码** 中，你可以直接使用：

* `env`：ORM 入口（`env['model']` 搜索/创建/写入）
* `model`：与动作绑定的模型（recordset 类）
* `records`：当前上下文中“被选中的记录集”（列表中勾选的那批）
* `record`：单记录（当从表单触发时）
* `user`、`context`、`datetime`、`time`、`dateutil.relativedelta`、`log()`（用于记一条信息到日志弹窗）

> **active\_ids**：在 `env.context.get('active_ids')` 里
> 典型写法：`recs = records or env[model._name].browse(env.context.get('active_ids') or [])`

### 3.2 事务与回滚

* Server Action 在一个 **HTTP 请求事务**中执行；出异常会**整体回滚**
* 大量写入请**批量 write**，避免循环内疯狂调用 `write()`（慢）

### 3.3 权限与 `sudo()`

* 默认使用**当前用户**权限执行（受访问规则限制）
* **仅当确实需要**绕过限制时使用 `sudo()`；注意审计（`create_uid` 等将变为 sudo 用户）

### 3.4 多公司（Multi-company）

* 当前激活公司集（右上角勾选）会影响读写
* 要确保按记录公司执行，典型用法：

  ```python
  for rec in recs.sudo():
      rec = rec.with_company(rec.company_id)
      # 后续对 rec 的操作在其公司环境中执行
  ```

### 3.5 不建议在代码里 `import`

* 代码通过 `safe_eval` 执行，不鼓励任意 `import`
* 常用工具（`datetime`、`relativedelta`）已放入上下文
* 复杂逻辑建议写到**自定义模块**的 Python 方法里，然后在 Server Action 里调用 `env['your.model'].method()`。

### 3.6 返回值

* 代码可以 `return action_dict` 打开一个窗口/报表，比如：

  ```python
  return {
      'type': 'ir.actions.act_window',
      'name': 'Metal Prices',
      'res_model': 'metal.pricelist',
      'view_mode': 'tree,form',
      'target': 'current',
  }
  ```

---

# 4. 实操实例（可直接用）

## 实例 A：批量把产品设为“在 POS 可售”

**模型**：`product.template`
**代码**：

```python
# 取勾选记录，或用 active_ids 兜底
pts = records or env['product.template'].browse(env.context.get('active_ids') or [])
pts.write({'available_in_pos': True})
log(f"已设置 {len(pts)} 个产品在 POS 可售。")
```

**绑定**到 `product.template` 列表（Binding Type=Action，View=List），勾选多条 → 动作 → 执行。

> 进阶：顺带把追踪方式改为序列号、加 POS 分类

```python
pts = records or env['product.template'].browse(env.context.get('active_ids') or [])
pts.write({'tracking': 'serial', 'available_in_pos': True})
cat = env['pos.category'].search([('name','=','黄金')], limit=1)
if cat:
    for pt in pts:
        pt.pos_categ_ids = [(4, cat.id)]   # 追加分类
```

---

## 实例 B：强制关闭 POS 会话（你之前用过的增强版）

**模型**：`pos.session`
**代码**：

```python
sessions = records or env['pos.session'].browse(env.context.get('active_ids') or [])

closed, forced = 0, 0
for s in sessions.sudo():
    s = s.with_company(s.company_id)
    # 推进状态机
    if s.state == 'opening_control':
        s.action_pos_session_open()
    if s.state == 'opened':
        s.action_pos_session_closing_control()
    try:
        s.action_pos_session_validate()  # 正常关班&过账
        closed += 1
    except Exception as e:
        s.write({'state': 'closed'})     # 兜底强关（可能留尾巴）
        forced += 1

log(f"正常关闭: {closed} 条；强制关闭: {forced} 条。")
```

**注意**：强关可能留下未过账差异，后续要检查会计/库存。

---

## 实例 C：把选中的“序列号 lot”统一改工费（示例）

**模型**：`stock.production.lot`
**代码**：

```python
lots = records or env['stock.production.lot'].browse(env.context.get('active_ids') or [])
for lot in lots.sudo():
    lot = lot.with_company(lot.company_id)
lots.write({'wage_type': 'per_piece', 'wage_value': 120.0})
log(f"已更新 {len(lots)} 个序列号工费。")
```

---

## 实例 D：执行后直接打开一个窗口（返回 action）

**模型不限**（比如 `metal.pricelist`）
**代码**：

```python
# 做点事情……
# 然后打开金价列表
action = env.ref('pos_gold_pricing.action_metal_pricelist').read()[0]
return action
```

---

## 实例 E：作为“自动化动作”（记录创建/更新触发）

**入口**：设置 → 技术 → **自动化动作（Automated Actions / base.automation）**

* **触发器**：On Creation / On Update
* **模型**：比如 `stock.production.lot`
* **要执行的动作**：选择“执行服务器动作”（选你建好的 Server Action），或者直接在自动化动作的“动作”页签里写 Python 代码

**示例**：当 lot 的净金重变化时，写入一个“需复核”标记

```python
for lot in records:
    if 'net_gold_weight' in lot._origin and lot.net_gold_weight != lot._origin.net_gold_weight:
        lot.message_post(body="净金重已被修改，请复核。")
```

---

# 5. 调试与排错

* **日志/提示**：在 Server Action 里用 `log("文本")`，执行结果弹窗会显示；服务器日志也能看到异常堆栈
* **先小批量测试**：列表里先勾 1\~2 条跑，确认无误再扩大范围
* **多公司**：如果看到 `Journal multi-company` 等权限问题，右上角**激活记录所属公司**；或使用 `with_company()`
* **POS 缓存**：改完产品/lot 等，**重开会话/同步** 才会下发到前台
* **权限**：若代码必须越权，使用 `sudo()`，但要知道它会绕开访问规则（请谨慎）

---

# 6. 最佳实践小抄

* **更新用 `write` 批量化**；避免循环里 `search`；先收集 ID 再一次性处理
* **动作原子性**：出错会整体回滚；可在代码里分段 try/except，记录到 `log()` 并继续
* **不要乱删业务单据**（生产环境优先“存档”）；删除只在测试库
* **复杂逻辑放模块**：把算法和规则写在自定义模块的 Python 方法里，Server Action 只负责“调入口”

---

需要我把“某个动作”**绑定到具体列表**（比如产品列表/会话列表）或把你的一段业务规则**改写成可直接粘贴的 Server Action**，告诉我目标模型和你想干什么，我给你成品代码和绑定指引。




  
  
  

# #############################################################################################################


# 直接落地的 **Server Actions（服务器动作）**，用于在 **产品列表**里一键把选中的产品批量**生效到 POS**（勾上 *Available in POS*）或批量**失效**（取消勾选）。我把**创建、绑定到“动作”菜单、执行与验证**一步步写清楚；如果你看不到“Action Bindings（动作绑定）”菜单，也给了替代路径。

---

# 目标

* 动作 A：**批量设为 POS 可售**（`available_in_pos = True`）
True of available_in_pos 
model：Product Template Attribute Line
* 动作 B：**批量取消 POS 可售**（`available_in_pos = False`）
False of available_in_pos
model：Product Template Attribute Line
> 作用对象：**Product Template (`product.template`)**。
> 注意：*Available in POS* 是**模板级**字段；请在“产品（Product）”的模板列表上执行。

---

## 一、开启开发者模式

* 右上角头像 → **关于/调试** → **启用开发者模式**（或 URL 加 `?debug=1`）。

---

## 二、创建两个 Server Actions

路径：**设置 → 技术 → 动作 → 服务器动作 → 新建**

### 1) 动作 A：批量设为 POS 可售

* **模型（Model）**：`Product Template (product.template)`
* **动作类型（State）**：执行 Python 代码
* **代码（Code）**：

```python
# 取勾选的模板；若从其他入口触发，用 active_ids 兜底
pts = records or env['product.template'].browse(env.context.get('active_ids') or [])
# 写入：在 POS 可售
pts.write({'available_in_pos': True})
log(f"已设置 {len(pts)} 个产品为 POS 可售。")
```

* 保存，命名如：**批量设为 POS 可售**

### 2) 动作 B：批量取消 POS 可售

* **模型**：`Product Template (product.template)`
* **动作类型**：执行 Python 代码
* **代码**：

```python
pts = records or env['product.template'].browse(env.context.get('active_ids') or [])
# 写入：取消在 POS 可售
pts.write({'available_in_pos': False})
log(f"已取消 {len(pts)} 个产品的 POS 可售。")
```

* 保存，命名如：**批量取消 POS 可售**

---

## 三、把动作挂到产品列表的“动作(Action)”菜单

### 方式 1（有菜单时，推荐）

路径：**设置 → 技术 → 用户界面 → Action Bindings（动作绑定） → 新建**

* **名称**：与上面动作名一致（便于识别）
* **动作（Action）**：选择对应的服务器动作（A 或 B）
* **模型（Model）**：`product.template`
* **绑定类型（Binding Type）**：`Action`
* **绑定视图类型（Binding View Types）**：勾 **List**（可再勾 Form）
* **Active**：勾选
* 保存
  （对两条动作分别新建一条绑定）

### 方式 2（看不到“Action Bindings”菜单时）

* 路径：**设置 → 技术 → 数据库结构 → 模型（Models）**
* 搜索并打开模型 **`ir.actions.binding`** → 进入后点击页面上方的 **“View Records / 记录”** 智能按钮
* 在该记录列表中 **新建**，按上面同样的字段填写并保存（各做一条）

---

## 四、使用与验证

1. 进入 **销售/库存 → 产品 → 产品**（切到**列表视图**）
2. （可选）用筛选器挑出需要的产品（比如某分类/标签/公司）
3. 勾选多条产品 → 顶部 **动作（Action）** → 选择：

   * **批量设为 POS 可售**（动作 A），或
   * **批量取消 POS 可售**（动作 B）
4. 弹窗会显示 `log(...)` 的执行结果；执行完成

> 变更后要让 POS 前台生效：**关闭并重新打开 POS 会话**（或在前台点“同步/刷新”）。POS 有前端缓存，不刷新看不到变化。

---

## 五、常见问题 & 快速排错

* **动作菜单里只有“导出”**

  * 你可能没绑定动作到列表；按“三、绑定”步骤做
  * 或者**没有勾选任何记录**；先勾选再点“动作”
  * 确认在**列表视图**（kanban/看板视图通常没“动作”）
* **我只看到变体页面，找不到模板列表**

  * 切换到“产品（Product）→ 产品（Product）”的模板列表（列里有“变体数”的就是模板）
* **执行后前台无变化**

  * 记得**重开 POS 会话**或“同步”
  * 多公司：右上角**激活**产品所属公司；产品公司与 POS 公司需一致
* **权限不够/按钮灰**

  * 用具有“设置/技术”权限的管理员创建动作与绑定

---

## 六、可选增强（一次性完成更多设置）

如果你希望在“设为 POS 可售”的同时，顺便把追踪方式改为**序列号**，并给产品追加一个 POS 分类（比如“黄金”），可把动作 A 的代码换成：

```python
pts = records or env['product.template'].browse(env.context.get('active_ids') or [])
# 1) POS 可售 + 一码一物（序列号）
pts.write({'available_in_pos': True, 'tracking': 'serial'})
# 2) 追加一个 POS 分类（按名字找；改成按外部ID更稳）
cat = env['pos.category'].search([('name', '=', '黄金')], limit=1)
if cat:
    for pt in pts:
        pt.pos_categ_ids = [(4, cat.id)]  # 追加，不覆盖
log(f"已设置 {len(pts)} 个产品：POS 可售 + 序列号跟踪，并追加分类。")
```

> 覆盖全部 POS 分类请用：`pt.pos_categ_ids = [(6, 0, [cat.id, ...])]`

---

## 七、不绑定也能运行（“手动运行”）

在服务器动作表单上点 **Run Manually / 手动运行**：

* 填 Domain（筛选条件），例如

  * 只打开现在不在 POS 的：`[('available_in_pos', '=', False)]`
  * 只关闭目前在 POS 的：`[('available_in_pos', '=', True)]`
* 确认运行

---

用这两条 Server Actions，你就可以在产品列表里一键**批量生效/失效**到 POS。如果你告诉我产品筛选条件（比如“黄金大类”“某公司”），我可以把动作改成**只对特定条件的产品**生效，并且帮你绑定好菜单名字（中/英文）以便你团队识别。

  
  
  

# #############################################################################################################


没问题。我给你三套**可执行**的路径，把你已经建好的两个 Server Actions“挂到产品列表的【动作】菜单”里。优先用方案 1；如果你那边菜单隐藏，用方案 2；都不方便就用方案 3（命令行直接创建绑定记录）。

---

# 方案 1（推荐）：打开“动作绑定”菜单，正常新建绑定

**前提**：你要有“设置管理员”权限 + 开启开发者模式

* 设置 → 用户与公司 → 用户 → 打开你的账号

  * Administration/管理：选 **Settings**（不是 Access Rights）→ 保存
* 右上角开启**开发者模式**（或 URL 加 `?debug=1`）

**步骤**

1. 进入：**设置 → 技术 → 用户界面 → Action Bindings（动作绑定）**
2. 点 **新建**，为第一个 Server Action（“批量设为 POS 可售”）填写：

   * **Name/名称**：批量设为 POS 可售（随意）
   * **Action/动作**：选择你刚建好的“批量设为 POS 可售”的 Server Action
   * **Model/模型**：`Product Template (product.template)`
   * **Binding Type/绑定类型**：**Action**（上下文动作）
   * **Binding View Types/绑定视图类型**：**勾选 List**（也可勾 Form，让它也出现在表单页的“动作”里）
   * **Active**：勾选
   * 保存
3. 再建一条绑定，选第二个 Server Action（“批量取消 POS 可售”），其余同上。
4. 使用：**销售/库存 → 产品 → 产品**（注意这是**模板列表**），切到**列表视图** → 勾选若干产品 → 顶部 **动作** 下拉里能看到这两条动作 → 点击执行。

> 看不到“动作”菜单？请先**勾选至少一条记录**；看板视图没有“动作”，切到**列表视图**。

---

# 方案 2：菜单看不到？从“模型 → 记录”入口创建绑定（100% 有）

即使“Action Bindings”菜单被隐藏，也能通过模型进到它的记录表：

1. **设置 → 技术 → 数据库结构 → 模型（Models）**
2. 搜索并打开模型 **`ir.actions.binding`**
3. 进入该模型后，点击页面上方的 **“View Records / 记录”** 智能按钮
4. 在出现的列表中 **新建**两条记录（分别对应你两个 Server Action），字段同方案 1：

   * 名称、动作（选你的 Server Action）、模型= `product.template`、绑定类型= **Action**、绑定视图类型= **List**、Active=勾选
5. 回到 **产品 → 产品** 列表，勾选记录 → **动作** 下拉即可看到并使用。

> 如果连“数据库结构 → 模型”都看不到，说明权限不够：把**Administration=Settings** 开起来，再开开发者模式。

---

# 方案 3（应急）：命令行直接创建绑定记录

如果你熟悉 Shell，可直接创建 `ir.actions.binding`，省去找菜单的麻烦：

```bash
odoo shell -d <你的库名>
```

```python
# 1) 找到两个 Server Action
act_set = env['ir.actions.server'].search([
    ('name', '=', '批量设为 POS 可售'),
    ('model_id.model', '=', 'product.template')
], limit=1)

act_unset = env['ir.actions.server'].search([
    ('name', '=', '批量取消 POS 可售'),
    ('model_id.model', '=', 'product.template')
], limit=1)

# 2) 找到 product.template 的 ir.model
mdl = env['ir.model'].search([('model', '=', 'product.template')], limit=1)

# 3) 创建两条绑定（绑定到列表视图）
env['ir.actions.binding'].create({
    'name': '批量设为 POS 可售',
    'action_id': act_set.id,
    'model_id': mdl.id,
    'binding_type': 'action',
    'binding_view_types': 'list',  # 也可用 'list,form'（若你的环境支持多选）
    'active': True,
})
env['ir.actions.binding'].create({
    'name': '批量取消 POS 可售',
    'action_id': act_unset.id,
    'model_id': mdl.id,
    'binding_type': 'action',
    'binding_view_types': 'list',
    'active': True,
})
```

完成后，刷新浏览器，去产品模板**列表**勾选记录，就能在**动作**里看到这两条。

---

## 使用与验证小抄

* 路径：销售/库存 → 产品 → **产品（模板列表）** → **列表视图**
* 勾选若干产品 → **动作** → 执行“批量设为 POS 可售”或“批量取消 POS 可售”
* 弹窗会显示 `log(...)` 的结果
* **POS 前台要同步**：执行后，**关闭并重新打开 POS 会话**或前台点“同步/刷新”，前端缓存才会拿到新状态。

---

## 常见问题速排

* **动作菜单只剩“导出”**：没勾选记录；或绑定没建对（模型应为 `product.template`，视图类型要含 List）；或权限不够。
* **在变体页执行没效果**：字段在**模板**上，要到“产品 → 产品”的模板列表执行。
* **执行成功但前台没变**：POS 有缓存，**重开会话/同步**。
* **多公司**：与 POS 使用的公司一致；必要时右上角激活该公司。

如果你告诉我两个 Server Action 的**名字**（你实际填的中文/英文）以及你当前**看得到的技术菜单列表**，我可以判断你适合用哪个方案，并给你更精确的字段名/按钮位置。


明白了：你在 **User Interface** 里看不到 **Action Bindings（动作绑定）** 菜单。不过没关系，下面给你三条“肯定能成功”的路径，把你已经建好的两个 *Server Actions* 挂到 **产品列表 → 动作** 菜单里。

---

# 0) 先确认两个前提（很重要）

* 你的账号在 **设置 → 用户 → 你的账号** 里，**Administration = Settings**（设置管理员）。
* **开发者模式**已开启（右上角甲虫/URL 含 `?debug=1`）。
* 右上角激活了**正确公司**（多公司环境）。

---

# 1) 路径 A（不依赖菜单）：用“直达 URL”打开绑定列表

即使左侧菜单没有“Action Bindings”，直接打开它的列表页也可以：

把下面 URL 中的域名和端口换成你的，再在浏览器输入打开：

```
http://<你的域名或IP>:<端口>/web#model=ir.actions.binding&view_type=list
```

进入列表后，点 **New / 新建**，分别为你那两条 Server Action 建两条绑定：

**第一条（批量设为 POS 可售）**

* **Name**：批量设为 POS 可售
* **Action**：选择你创建的那条 *Server Action*（模型是 `product.template`）
* **Model**：选择 **Product Template**（技术名 `product.template`）
* **Binding Type**：`action`
* **Binding View Types**：`list`（如果是多选框界面就勾 **List**；有的环境是文本框，就填 `list` 或 `list,form`）
* **Active**：勾选
* 保存

**第二条（批量取消 POS 可售）**
同上，Action 选你第二条 *Server Action*，其他字段一致，保存。

完成后，去 **销售/库存 → 产品 → 产品**（**模板列表**，不是变体），切到**列表视图**，**勾选至少一条记录** → 顶部 **动作** 下拉里就能看到这两条动作。

> 只看到“导出”？请确认你在**列表视图**且**勾选了记录**，并且绑定的 **Model=product.template**、**View Types** 含 **list**。

---

# 2) 路径 B（菜单仍不可见时）：从“模型 → 记录”入口创建绑定（必有）

1. 进 **设置 → 技术 → 数据库结构 → 模型（Models）**
2. 搜索并打开模型 **`ir.actions.binding`**
3. 页面顶部点 **View Records / 记录**
4. 在列表中 **新建**两条记录，字段同“路径 A”

完成后同样去产品模板列表验证。

> 如果连“数据库结构 → 模型”也看不到，说明权限还不够：把 **Administration=Settings** 打开，再启用开发者模式。

---

# 3) 路径 C（不进界面，命令行直接创建绑定）

如果你熟悉 Shell，可以直接创建绑定记录：

```bash
odoo shell -d <你的库名>
```

```python
# 找到两条 Server Action（按名称 & 模型）
act_set = env['ir.actions.server'].search([
    ('name', '=', '批量设为 POS 可售'),
    ('model_id.model', '=', 'product.template'),
], limit=1)
act_unset = env['ir.actions.server'].search([
    ('name', '=', '批量取消 POS 可售'),
    ('model_id.model', '=', 'product.template'),
], limit=1)
mdl = env['ir.model'].search([('model', '=', 'product.template')], limit=1)

# 若已存在同名绑定就先不重复创建
def ensure_binding(name, action):
    b = env['ir.actions.binding'].search([
        ('name', '=', name),
        ('model_id', '=', mdl.id),
        ('action_id', '=', action.id),
        ('binding_type', '=', 'action'),
    ], limit=1)
    if not b:
        env['ir.actions.binding'].create({
            'name': name,
            'action_id': action.id,
            'model_id': mdl.id,
            'binding_type': 'action',
            'binding_view_types': 'list',  # 或 'list,form'，视你环境而定
            'active': True,
        })

ensure_binding('批量设为 POS 可售', act_set)
ensure_binding('批量取消 POS 可售', act_unset)
```

刷新浏览器 → 产品模板列表勾选记录 → 动作菜单里出现两条操作。

---

## 使用与验证（统一）

1. **销售/库存 → 产品 → 产品**（模板列表）
2. 切到**列表视图**，**勾选**需要处理的产品
3. **动作 → 执行**“批量设为 POS 可售”或“批量取消 POS 可售”
4. 弹窗会显示日志条数（来自 `log()`）
5. **POS 前台同步**：关闭并重新打开 POS 会话或点“同步/刷新”

---

## 常见问题速排

* **动作菜单仍不显示**：确保在**列表视图**，且**至少勾选一条**。确认绑定的 `Model=product.template`、`binding_type=action`、`binding_view_types` 包含 `list`。
* **在变体页执行无效**：字段在**模板**上，请到“产品 → 产品”的**模板列表**执行。
* **执行成功前台没变化**：POS 前端有缓存，必须**重开会话/同步**。
* **权限/多公司**：把 **Administration=Settings** 给自己；并在右上角激活该产品所属公司。

如果你把两条 *Server Action* 的**实际名字**发我，我可以帮你给出一条“复制即用”的 `odoo shell` 脚本，直接把绑定创建好。

你这步已经走到关键点了。现在之所以在“产品列表 → 动作”里看不到你的动作，**根因是你把 Server Action 的 Model 设成了 “Product Variant（product.product）”，而代码却在改 `product.template` 的字段**。绑定会挂到**变体列表**，而你去**模板列表**里找，自然看不到；就算在变体列表里点它，`records` 也是 `product.product`，你的代码也没对上模型。

下面给你两种“正确挂载”的做法，任选其一：

---

## 方案 A（推荐）：挂到“产品模板（Products）”列表

**适用**：你希望在“产品 → 产品（模板列表）”的【动作】里看到并执行它。
**怎么改**

1. 打开这条 Server Action（你截图的这条）。
2. 把 **Model** 改为 **Product Template (`product.template`)**。
3. （可选）把名称改成友好的，比如“批量取消 POS 可售”。
4. **保存**，然后点击 **Create Contextual Action**（只点一次）。这会自动创建绑定到 `product.template` 列表/表单的上下文动作。
5. 去 **销售/库存 → 产品 → 产品**（注意是**模板**），切换到**列表视图**，**勾选**至少一行 → 顶部 **动作** 下拉里就能看到这条动作（名字就是你在 Server Action 的 Name）。

> 提醒：若动作里仍只有“导出”，通常是没勾选记录或不在列表视图。

你的代码保持不变即可：

```python
pts = records or env['product.template'].browse(env.context.get('active_ids') or [])
pts.write({'available_in_pos': False})
log(f"已取消 {len(pts)} 个产品的 POS 可售。")
```

---

## 方案 B：挂到“产品变体（Product Variants）”列表

**适用**：你更习惯在“产品 → 产品变体”列表里点动作。
**怎么改**

1. 保持 **Model = Product Variant (`product.product`)**。
2. 把代码改为先取变体，再映射到模板写入：

```python
prods = records or env['product.product'].browse(env.context.get('active_ids') or [])
templates = prods.mapped('product_tmpl_id')
templates.write({'available_in_pos': False})
log(f"已取消 {len(templates)} 个产品模板的 POS 可售。")
```

3. **保存** → 点击 **Create Contextual Action**（只点一次）。
4. 去 **产品 → 产品变体** 列表，**列表视图**勾选记录 → **动作** 下拉里就能看到并使用。

---

## 必要检查（看不到时逐条核对）

* **Allowed Groups**：你把组限定为 *Point of Sale / Administrator*。确保你这个用户在该组里；否则你自己也看不到。

  * 不想限权限：可暂时清空 *Allowed Groups*，或加上 *Settings* 管理员组。
* **只点一次 “Create Contextual Action”**：重复点击会生成多个绑定，菜单会出现重复项。若点多了，可到 `ir.actions.binding` 列表删除多余绑定。
* **生效位置**：绑定到哪个模型，就去**那个模型的列表视图**找（模板 vs 变体不要混）。
* **要勾选记录**：很多页面未勾选时“动作”只剩“导出”。
* **刷新/清缓存**：保存绑定后刷新页面。
* **多公司**：右上角激活与产品同一公司，否则看不到或执行报权限。

---

## 小建议

* 把这两条动作分别做成：

  * **Model = product.template**，名字 “批量设为 POS 可售 / 批量取消 POS 可售”
  * 代码里只操作 `product.template`，最直观也最不易踩坑。
* 做完后，到“产品 → 产品（模板）”列表里验证；执行后别忘了**重开/同步 POS 会话**，前端缓存才会拿到变化。

需要的话你把当前这条动作的 **Model** 改成 `Product Template` 后点一次 **Create Contextual Action**，再去产品模板列表勾几条看下；如果还没出现，把“Allowed Groups”也发我一下，我帮你判断是不是组限制挡住了显示。


  
  
  

# #############################################################################################################

# 执行actions'False of available_in_pos'时，提示'invalid operation':'You must first remove this product from the T-shirt Combo combo'。

你点动作报错：

> invalid operation: **You must first remove this product from the T-shirt Combo combo**

含义很直接：**该产品被用作 POS 组合（Combo）的组成项**。在 Odoo 18 里，只要某产品还被任何 Combo 引用，就**不允许**把它“从 POS 下架”（`available_in_pos=False`）或存档。先把它从所有 Combo 里移除/停用，才可以执行你的 Server Action。

下面两种做法，任选其一。

---

## 方式一（界面操作，最安全）

1. 进入：**POS → Products（或 Configuration）→ Combos（组合）**。
2. 打开提示里的 **T-shirt Combo**（以及其它可能引用该产品的组合）。
3. 在 **Components/Lines** 里把这个产品删除（或用同类替换），保存。
4. 再回到 **产品 → 产品（模板列表）**，勾选目标产品，执行你的 **“批量取消 POS 可售”**。

> 如果你不再使用该组合，直接**存档/停用**这个 Combo 也可以。

---

## 方式二（批量清理后再下架：给“批量取消”动作加一段代码）

把你“批量取消 POS 可售”的 Server Action 改成先**清理所有引用该产品的 Combo 行**，再写 `available_in_pos=False`。
（模型仍选 **Product Template**；下面代码会兼容常见的组合行模型/字段名）

```python
# 1) 取到被勾选的产品模板
templates = records or env['product.template'].browse(env.context.get('active_ids') or [])

removed = 0
def _clear_combo_lines():
    global removed
    combo_models = [
        # (模型名, 产品字段候选, 上级组合字段候选)
        ('pos.combo.line',   ['product_tmpl_id','product_id'], ['combo_id','pos_combo_id']),
        ('pos.combo.item',   ['product_tmpl_id','product_id'], ['combo_id','pos_combo_id']),
        ('pos.combo.product',['product_tmpl_id','product_id'], ['combo_id','pos_combo_id']),
    ]
    for model_name, prod_fields, parent_fields in combo_models:
        try:
            model = env[model_name]
        except KeyError:
            continue
        # 找到可用的产品字段
        prod_field = next((f for f in prod_fields if f in model._fields), None)
        if not prod_field:
            continue
        lines = model.search([(prod_field, 'in', templates.ids)])
        if not lines:
            continue
        removed += len(lines)
        lines.unlink()  # 解除与组合的绑定（直接删行）
        
_clear_combo_lines()

# 2) 现在可以下架（使其在 POS 不可售）
templates.write({'available_in_pos': False})

log(f"已从组合中移除 {removed} 条行，并将 {len(templates)} 个产品设置为非 POS 可售。")
```

> 说明
>
> * 代码会尝试三种常见的组合行模型（不同安装可能字段名略有差异），找到就删除对应行。
> * 如果你们环境的组合模型名字不同，改一下 `combo_models` 即可。
> * 这会**改变组合配置**：请确认业务允许把这些项移出组合。

---

## 小提示

* 执行成功后，**POS 前台需要“同步/重开会话”** 才会看到变化。
* 如果“Allowed Groups”限制了可见性，请确保你在该组内或临时去掉组限制。
* 在**模板列表**执行这些动作（`product.template`），不要在“产品变体”列表上点。

需要我把你这条动作直接改成“先清 Combo 再下架”的最终版脚本，也可以把你们环境里的**组合模型/字段**发我（或报错全文），我给你量身定制一份不报错的代码。
  
  
  

# #############################################################################################################

# odoo18中,pos应用中，products菜单下的三个选项，prodeucts、products variants和Combo Choices分别的业务定义功能，以及区别是什么

好的！这 3 个菜单在 POS 里的“业务定义、功能与区别”可以按下面理解：

---

# 1) Products（产品 = `product.template`）

**是什么**

* 产品“模板/母体”，代表一类商品（例如“金戒指 A 款”）。
* 大部分 POS 相关设置都在模板上完成：**Available in POS**、POS 分类、税、计量单位、是否序列号跟踪、基础售价等。

**在 POS 中怎么体现**

* 前台商品卡片通常对应模板；如果该模板有多个变体（颜色/尺码…），收银点到该商品会弹出变体选择。
* 你批量开/关 POS 可售，应该作用在 **产品模板** 上。

**典型用途**

* 建品类、挂 POS 分类，控制是否能在 POS 销售。
* 对黄金业务：把“一码一物/序列号跟踪”设在模板上（tracking=serial）。

---

# 2) Product Variants（产品变体 = `product.product`）

**是什么**

* 由模板 + 属性值组合生成的**具体 SKU**（例如“金戒指 A 款 / 16 号 / 金色”）。
* 变体有各自的条码、内部参考、库存数量；价格一般继承模板，**差价**可由属性值配置（Price Extra）或价目表实现。

**在 POS 中怎么体现**

* 收银员点“模板卡片”后，如果存在多个变体，会弹出**变体选择弹窗**；扫码时可直接识别具体变体条码。
* 变体页上的“Available in POS”并不是主字段（主字段在模板）。因此你把 **Server Action** 挂到变体列表时，要在代码里映射到模板再写入。

**典型用途**

* 管理不同尺码/颜色/款式的库存、条码；首饰如果有“号数”且要独立库存，可以做成变体。

---

# 3) Combo Choices（组合选项/可选项组，POS 组合）

**是什么**

* **POS 组合（Combo）** 的“选项组”配置。
* 你可以先定义一组“选择规则”（比如：主菜 1 份、配菜 2 份、饮料 1 份，允许的商品列表、是否必选、最小/最大数量、可否加价升级等），再把这些**选项组**挂到某个“组合产品（Combo Product）”上。

**在 POS 中怎么体现**

* 前台点击一个 **Combo 产品** 时，会弹出组合选择界面：按“选项组”的规则从候选商品中挑选；最终价格=**组合基础价** ± **各选项加价**（如果设置了升级加价）。
* **被选为组合组件的商品必须是 “Available in POS=True”**，否则在组合里无法挑选；这也是你刚才执行批量下架时看到报错的原因：

  > *“You must first remove this product from the T-shirt Combo combo”*
  > 说明该商品仍被某个 Combo 引用，必须先在 **Combo Choices/Combo 产品**里把它移除，才允许下架或存档。

**常见设置点**

* 在 **Products → Combo Choices** 定义选项组（名称、必选/最小/最大数量、候选商品/类别、是否允许加价）。
* 在一个“组合产品（通常设为 Service）”上勾选 **Combo** 并添加这些选项组，设置组合基础价。
* 组件商品在库存/价格上按普通商品处理；POS 下单时会把被选的组件作为行项目加入订单（是否产生库存拣货取决于你的 POS–库存联动设置）。

---

## 三者的关系与使用边界

| 项                | 数据对象               | 面向谁     | 主要作用                       | 典型操作                                          |
| ---------------- | ------------------ | ------- | -------------------------- | --------------------------------------------- |
| Products         | `product.template` | 业务/配置人员 | 定义一类商品、POS 可售、税、单位、分类、跟踪方式 | 勾/取消 **Available in POS**、设 POS 分类、设 tracking |
| Product Variants | `product.product`  | 库存/条码管理 | 管理 SKU、条码、库存；从模板继承设置       | 维护条码/参考；（需要时）映射到模板做批量动作                       |
| Combo Choices    | （POS 组合模型及其行）      | 营销/前台体验 | 定义“套餐/组合”的可选项与规则           | 先建“选项组”，再在“组合产品”上挂这些组、定价；组件必须可售               |

---

## 常见问答

* **为什么我把一个组件商品设置为“不可售”，系统报错？**
  因为它被某个 Combo 作为候选项/默认项使用。请在 **POS → Products → Combo Choices / Combo 产品** 中把该商品移除或停用该组合，再下架。

* **库存怎么扣？扣 Combo 还是扣组件？**
  组合产品通常做成 **Service**（自身不扣库存），在 POS 下单时把**选中的组件**作为行项目加入、据设置扣减组件的库存（你需要在 POS 配置里启用与库存的拣货/库存同步）。

* **首饰行业需要 Combo 吗？**
  常见是礼盒/赠品包（如“清洁布+礼盒+贺卡”）或“套装”（戒指+项链）；如果只是单件定价和属性较多，主要用 **Products/Variants + Lot/Serial**，Combo 不是必需。

---

## 操作提示

* **批量开/关 POS 可售**：对 **产品模板列表** 做动作最稳（你的 server actions 就是这个场景）。
* **想在“产品变体”列表触发同样效果**：代码要 `mapped('product_tmpl_id')` 后再写 `available_in_pos`。
* **删除/下架组件前先清 Combo**：到 **Combo Choices / Combo 产品** 里把组件移除，否则会阻止操作。
* **POS 前端缓存**：任何改动完成后，记得在前台 **同步/重开会话**。

如果你想，我可以给你一个“检查某商品被哪些 Combo 引用并一键移除”的小型 Server Action，点一下就清掉引用，然后再批量下架。


  
  
  

# #############################################################################################################

# 最终店面操作员的POS销售终端页面，展现的产品列表，是prodeucts呢，还是products variants，中的内容。

  结论先说：

* **POS 前台网格默认展示的是“产品模板（Products = `product.template`）的卡片”。**
* 但**实际加入订单的一定是“产品变体（Product Variants = `product.product`）”**。
* 如果该模板有多个变体，**点卡片会弹出“变体选择”面板**；或者你**直接扫某个变体的条码**，会直接把那一条变体加入订单（不弹选择）。

再细说一下你在前台会看到/能做的事：

1. **只有勾了 “Available in POS” 的模板**会出现在前台商品网格里（且未归档、在当期 POS 分类可见）。
2. **有变体的模板**：

   * 点卡片 → 出现“尺寸/颜色/号数…”的变体选择窗口，选择后落到具体 **product.product**；
   * 直接扫变体条码 → 直接把该 **product.product** 加入订单；
   * 没变体时，模板与变体是一体的（1:1）。
3. **是否能把每个变体都单独显示成卡片？**

   * 某些版本/部署在 POS 配置里提供“将变体单独显示/Display variants as separate items”或“产品配置器/Product configurator”等选项；打开后，前台可以把**每个变体当成一张独立卡片**显示（具体名称因安装/语言略有差异）。
   * 如果你的界面没有这个开关，就保持**模板卡片 + 变体弹窗**的默认体验；需要的话可通过小型前端扩展实现“每个变体一张卡片”的展示方式。
4. **组合（Combo）** 是单独的概念：前台会显示“组合产品”的卡片；点开后按组合规则选择“组件商品”。被作为组件的商品必须仍然 **Available in POS=True**，否则不能被选。

小贴士：

* 想“让某个变体不在 POS 可卖”，但保留模板：可以**归档该变体（product.product.active=False）**，或在库存/规则里限制它；模板仍可售、其它变体仍可选。
* 每次改完商品/变体/分类后，**前台需要同步或重开会话** 才会看到最新内容。

所以，店面操作员在网格上**看到的是 Products（模板）**；但真正结算的是 **Product Variants（变体）**。

  
  
# ******************************************************************************************************************************

# #############################################################################################################

# 就黄金类产品，可能有1000个产品品种，有可能重量不同，就是一个具体的产品，那么，对于，某一个具体的产品，具有下面这些属性值的话，如何合理应用prodeucts和products variants呢，如何分配属性值内容，具体的的操作方法。是需要手动来配置呢，还是编写一个模块用代码来实现。
```
一码一物还是一码多件
计件/计重
商品ID 必填
商品条码 必填
商品名称 必填
商品大类 黄金，K金，镶嵌，玉石		 必填
商品成色 空白 18k 足金  99.99% 	 必填
商品类别 戒指 手镯	 必填
商品主石（可空） 颜色，净度（写规格里）	 非必填
商品规格 自定义的	 非必填
商品工艺 硬金 3D 5D 5G 珐琅	 非必填
净金重 数值型	 必填
总重 数值型	 必填
石重 数值型 克拉ct 非必填
配件重 数值型 非必填
证书号 非必填
商品销售工费 数值型 非必填
克工费还是件工费 选择 非必填
商品成本 数值型	 必填 默认为0
商品标价 数值型	 必填 默认为0
商品批发价 数值型 	 必填 默认为0
商品性质（正品，特价，赠品，物料，配件，活动款）	 必填
商品备注	 非必填
```

太棒的问题！黄金首饰“**一件一重**、**一物一证**”的特点，决定了：

* \*\*前台展示=产品模板（Products / `product.template`）\*\*为主；
* **真正成交=产品变体（Product Variants / `product.product`）**；
* \*\*每件的差异数据=序列号（Lots/Serials / `stock.production.lot`）\*\*承载。

下面给你一套能直接落地的建模与操作路线：**哪些放模板/变体/序列号**、**如何批量导入**、**手工 vs 写模块**各怎么做。

---

# 1) 放哪里？——字段归属总表（黄金场景建议）

| 业务字段                  | 放哪                                                      | 原因/说明（POS 影响）                                                |
| --------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| 一码一物/一码多件             | **product.template.tracking**（`serial`/`none`/`lot`）    | 黄金零售建议：**serial（一物一码）**；配件可用 `none`。POS 里会强制选/扫序列号。          |
| 计件/计重                 | **product.template.uom\_id**（件/克） + lot 上的 **净金重**      | 首饰多为“按件售、按金重计价”，建议用 **件** 做销售单位，**净金重在 lot**。散金条/裸料可用 IoT 秤。 |
| 商品ID/条码/名称            | **product.product**（变体级）/ **product.template**（模板级）     | 扫码通常扫**变体**/序列号条码；模板有默认条码也可。                                 |
| 商品大类（黄金/K金/镶/玉）       | **pos.category**（顶层）                                    | 影响前台分类浏览。                                                    |
| 商品类别（戒指/手镯…）          | **pos.category**（子层）                                    | 影响前台分类浏览。                                                    |
| 成色（18K/足金/9999…）      | 常见做法①：**模板默认值**（或属性**不生成变体**）；做法②：确需同款多成色时 → **属性生成变体** | 成色会影响计价；若同款既有 18K 又有 9999，才做成变体，否则放模板默认值更简洁。                 |
| 主石（颜色/净度）             | **lot**                                                 | 每件不同，打印到小票/证书。                                               |
| 规格（自定义）               | 多为 **lot**（每件不同）                                        | 也可做模板/属性“仅描述”。                                               |
| 工艺（硬金/3D/5D/珐琅…）      | ①模板字段/属性（**不生成变体**）+ ②**lot**（如每件略有差异）                  | 若工艺直接影响价，可放 lot 并参与计价。                                       |
| 净金重/总重/石重/配件重         | **lot**                                                 | 每件不同，计价核心。                                                   |
| 证书号                   | **lot**                                                 | 一物一证。                                                        |
| 销售工费、工费类型（克/件）        | **lot**（模板可做默认）                                         | 不同件工费不同常见。                                                   |
| 成本                    | 模板 `standard_price`（会计）+（可选）**lot 参考成本字段**              | 实际会计成本走库存估价（FIFO/实时），lot 字段仅作参考。                             |
| 标价/批发价                | 模板 `list_price` + **Pricelist**（批发）                     | 动态金价时由公式覆盖。                                                  |
| 商品性质（正品/特价/赠品/配件/活动款） | **模板选择字段**或标签                                           | 用于促销与报表分组。                                                   |
| 备注                    | 模板或 lot                                                 | 业务需要即可。                                                      |

**关键理念**：

* **模板/变体放“稳定、可复用”的信息**；
* **lot 放“一件一份”的真实差异**（重量、证书、工费……）；
* 需要多 SKU（如戒指号）→ 才用 **变体**；否则别让变体爆炸。

---

# 2) 两种典型建模方案

## 方案 A（最稳健，推荐）

* **模板**：一个款式=一条 `product.template`；

  * `tracking=serial`、`Available in POS=True`、挂 `pos.category`；
  * 成色、工艺等作为模板字段/属性（**No Variant 不生成变体**）；
* **变体**：**仅在必须时**（如戒指号）生成；否则 1:1；
* **序列号 lot**：为每件创建，写入**净金重/总重/石重/证书/工费/工艺/成色**等，条码印在标签上；
* **计价**：POS 选择 lot → 用 “净金重×当日金价×成色系数 + 工费” 算 **unit price**（可用我给你的 `pos_gold_pricing` 模块直接实现）。

## 方案 B（更简单，适合快速上）

* **模板**：同上；
* **不做变体**（即使有号数，也先放到 lot 的 `ring_size` 字段作为描述）；
* **lot**：承载所有差异；
* **计价**：过渡期用**带价条码**（Barcode Nomenclature：Price），或每天后台批量写入 `list_price`；随后再切换为自动计价。

---

# 3) 具体操作（手动配置版）

1. **建 POS 分类**

   * POS → 配置 → 分类：顶层=大类（黄金/K金/镶/玉），子层=类别（戒指/手镯…）。

2. **建属性（可选）**

   * 设置 → 产品 → 属性：

     * 成色/工艺/材质等 → **生成策略设为 “不生成变体（No Variant）”**；
     * **只有戒指号等必须独立库存**的，才设为“生成变体”。

3. **建产品模板**

   * 销售/库存 → 产品 → 产品：

     * 勾 **Available in POS**、`tracking=serial`；
     * 挂 `pos.category`；
     * 若做变体：在“属性与变体”页签加上“戒指号”等属性；
     * 设置默认税、单位（**件**）等。

4. **为每件创建序列号（lot）**

   * 库存 → 产品 → 序列号/批次 → 新建：

     * `product` 选你的模板/变体，填 **净金重、总重、证书号、工费、工艺、成色**、条码等；
   * POS 配置勾 **Lots/Serials**，前台出售会弹序列号。

5. **计价**

   * 快速期：**带价条码**或手改价；
   * 正式期：安装我给你的 **pos\_gold\_pricing** 模块（你已拿到 ZIP），在菜单 **Metal Pricing** 维护当日金价，前台选 lot 自动定价。

> 任何改动后，**重开/同步 POS 会话** 生效。

---

# 4) 批量导入（上千条的正确姿势）

### A. 导入模板（`product.template`）

最小列：

```
id,name,default_code,barcode,available_in_pos,pos_categ_ids/id,tracking,type,uom_id/id,list_price,standard_price
pt_gold_ring_a,黄金戒指A,GR-A,690000000001,1,"pc_gold,pc_gold_ring",serial,product,uom.unit,0,0
```

### B. 导入变体（如需要戒指号）

* 先在属性里建“戒指号”及其值；
* 再导入 **模板属性行** 或在 UI 上给模板添加属性并“生成变体”；
* 也可直接导入 `product.product` 并指定 `product_tmpl_id/id` 与 `attribute_value_ids/id`（相对复杂，建议先 UI 生成）。

### C. 导入序列号（`stock.production.lot`）

```
name,product_id/id,company_id/id,metal_type,net_gold_weight,gross_weight,stone_weight_ct,wage_type,wage_value,process_technique,certificate_no,barcode
SN-GR-A-0001,pt_gold_ring_a,base.main_company,au_9999,3.56,3.70,0.10,per_piece,120.00,hard,CERT-0001,9900000000017
SN-GR-A-0002,pt_gold_ring_a,base.main_company,au_9999,3.48,3.60,0.00,per_g,10.00,3d,CERT-0002,9900000000024
```

> 批量化建议：先导入 **分类 → 模板 →（可选）变体 → 序列号**。每批导入后，立刻抽测 POS 前台。

---

# 5) 手动 vs 写模块：如何选择？

| 需求强度               | 建议                                                                                                                                                                   |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **先跑通**（少量数据/概念验证） | **手工+导入** 即可：建分类/模板；lot 导入净重+证书；带价条码或手改价                                                                                                                             |
| **正式上线**（上千件、每天新货） | 安装/开发模块：<br>① 在 `stock.production.lot` 扩展字段（净金重/证书/工费/工艺/成色…）；<br>② 新建 `metal.pricelist` 维护当日金价与成色系数；<br>③ POS 前端在选 lot 后自动算价；<br>④ 提供批量导入模板与校验；<br>⑤（可选）生成/打印序列号与条码 |
| **自定义报表/打印**       | 模块里加收据模板、价签模板、证书打印等                                                                                                                                                  |

> 你已经拿到的 **pos\_gold\_pricing.zip** 正是这套最小可用模块（含字段与自动定价、CSV 样例）。把它安装后，lot 一选就能算价，适配黄金零售。

---

# 6) 两个实战贴士

1. **不要滥用变体**：号数/成色确实要分 SKU 才做变体；其它差异放 **lot**，否则 1000 款 × 多属性组合会“变体爆炸”，POS 变慢。
2. **Combo 限制**：被 POS 组合引用的商品不能下架（你已遇到）。批量取消 POS 可售前，先清除组合引用或在脚本里自动解除。

---

# 7) 为你准备的“自动化样板”

* **批量把选中模板设为“在 POS 可售 + 序列号跟踪 + 追加分类”**（Server Action）

```python
pts = records or env['product.template'].browse(env.context.get('active_ids') or [])
pts.write({'available_in_pos': True, 'tracking': 'serial'})
cat = env['pos.category'].search([('name','=','黄金')], limit=1)
if cat:
    for pt in pts:
        pt.pos_categ_ids = [(4, cat.id)]  # 追加，不覆盖
log(f"处理 {len(pts)} 条。")
```

* **从 CSV 批量创建 lot**（Server Action 思路）

  * 将 CSV 上传为附件（`ir.attachment`），代码里读取解析后 `env['stock.production.lot'].create({...})`；
  * 或直接用 Odoo 导入器按上面的列模板导入。

---

**结论**

* **模板**承载“款式层”的可售/分类/跟踪等；
* **变体**只在必须时使用（如号数成 SKU）；
* **lot**是黄金业务的核心（净重、证书、工费…），POS 选 lot → 自动计价。
* 前期用手工/导入，规模化后用模块（你已有模块脚手架，直接安装即可）。

如果你愿意，我可以按你们实际“戒指号规则/是否多成色同款”的情况，再给一份\*\*“是否生成变体”的决定树\*\*，帮你把 1000 款精简到最小变体数量。


# deepseek

你提出的这个问题，是关于在 Odoo（特别是 Odoo 18） 中，如何合理地使用 Product（产品） 和 Product Variants（产品变体），来管理 黄金类、K金、镶嵌、玉石等珠宝类商品，尤其是当：

• 你面对的是 1000个品种的黄金类产品

• 每个产品可能 重量不同

• 每个产品具有 非常多的属性（如成色、主石、工艺、克重、工费、价格等）

• 你关心的是 一码一物 vs 一码多件

• 你关心的是 计件 vs 计重

• 你关心的是 如何配置属性、如何分配属性值、是手动配置还是通过代码实现

一、先理解 Odoo 中 Product 和 Product Variants 的基本概念

1. Product（产品模板，Product Template）

• 是商品的 “抽象模板”，定义了 一类商品共有的属性，比如：

  • 商品名称（如：“足金戒指”）

  • 商品大类（如：“黄金”）

  • 成色（如：“足金”）

  • 商品类别（如：“戒指”）

  • 商品工艺（如：“硬金”）

  • 商品销售工费、成本价、标价、批发价等 默认值

  • 是否计件/计重（这个一般不由 Variant 决定，而由模板或业务逻辑控制）

  • 商品性质（正品/赠品/特价等）

  • 以及其他 公共属性

• 一个 Product（模板）可以有 0 个、1 个或多个 Product Variants（变体）

2. Product Variant（产品变体，Product Product）

• 是 具体的、可售卖的单品，比如：

  • “足金戒指，成色：足金999，主石：无，净重：3.5克，总重：3.8克，工费：200元，条码：1234567890123”

• 每个变体可以拥有 自己独有的属性值组合，比如不同的：

  • 重量（净重、总重、石重）

  • 条码（一码一物）

  • 工费

  • 价格

  • 证书号

  • 配件

• 变体才是实际库存、扫码、销售、POS 中使用的对象

二、你的业务场景分析

你管理的商品是：

属性类别 是否多值（是否需要变体） 说明

商品大类（黄金/K金/镶嵌/玉石） ❌ 模板属性 是类别，不是变体维度

商品成色（18k / 足金 / 99.99%） ✅ 可能是变体属性 如果不同成色的同一款式算不同商品，可以作为变体属性

商品类别（戒指/手镯） ❌ 模板属性 是类别，不是变体维度

商品主石（颜色/净度） ✅ 可能是变体属性 如果主石不同，可作为变体区分

商品规格（自定义） ✅ 可能是变体属性 如果规格不同，比如不同设计，可作为变体

商品工艺（硬金/3D/5D等） ✅ 可能是变体属性 如果工艺影响价格或区分商品，可作为变体

净金重 / 总重 / 石重 / 配件重 ✅ 必须为变体属性 每个商品重量都可能不同，是核心变体属性

商品条码（必填） ✅ 一码一物，强烈建议绑定到变体 一码对应一个具体的商品实物

商品销售工费 / 克工费 or 件工费 ✅ 可能是变体属性 不同商品工费可能不同

商品成本 / 标价 / 批发价 ✅ 可能是变体属性 每个商品可能定价不同

商品性质（正品/特价/赠品等） ✅ 可能是变体属性 不同性质可能对应不同售价或库存策略

商品备注 ❌ 非关键，非变体属性 可放在变体或模板的备注中

三、一码一物 vs 一码多件

✅ 你提到：“一码一物”

• 意味着 每一个实物商品都有唯一的条码（如：1234567890123）

• 每个条码对应 一个具体的商品实例：比如 3.5克足金戒指，主石无，证书号xxx，工费200元

• 这种情况 强烈建议使用 Product Variants（变体）

  • 每个变体绑定一个唯一条码

  • 每个变体有自己的一套属性：重量、工费、价格、证书等

  • 每个变体是实际销售、盘点、出库的对象

❌ 一码多件（如：所有 3.5克足金戒指共用一个条码）

• 不推荐，除非你真的可以接受 多个实物商品共享一个条码，不区分细节

• 这样无法精确管理 每个商品的真实重量、工费、价格、证书号

• 不利于 POS 销售、库存精准管理、以及财务核算

四、计件 vs 计重

• 计件： 按 个数 卖，比如一个戒指卖一份，不管多重

• 计重： 按 克重 卖，比如黄金按实际称重计价

在 Odoo 中：

• 计件 or 计重 不是直接由 Variant 决定的，而是由销售规则、价格计算方式、POS 配置等控制

• 你可以：

  • 在 Product（模板）上设置一个字段，标识它是“计件”还是“计重”

  • 或者通过 不同的 Product Category（商品类别） 区分计件/计重逻辑

  • 或者通过 销售模块的价格规则（Pricelist Rules） 实现动态计价（比如按克重 × 单价 + 工费）

✅ 建议：你可以在 Product 模板或变体上增加自定义字段，如：is_weight_based（是否计重），然后在业务逻辑（比如 POS、销售订单、报表）中根据该字段做不同处理。

五、如何合理使用 Product 和 Variants（操作方案）

✅ 推荐方案：使用 Product Template（产品模板） + Product Variants（产品变体）

1. Product Template（模板）——定义公用属性

适合放 所有产品共性的、不会因单个商品而变化的属性，比如：

字段 建议放在 Template 还是 Variant 说明

商品名称（如：足金戒指） ✅ Template 公用

商品大类（黄金/K金/镶嵌/玉石） ✅ Template 公用，可做筛选分类

商品类别（戒指/手镯） ✅ Template 公用

商品工艺（硬金/3D/5D） ✅ 可放 Template 或 Variant 若工艺影响价格区分，放 Variant 更好

商品销售工费（默认） ✅ Template 可设置默认值，变体可覆盖

商品成本（默认 0） ✅ Template 可设置默认，变体可覆盖

商品标价（默认 0） ✅ Template 可设置默认，变体可覆盖

商品批发价（默认 0） ✅ Template 可设置默认，变体可覆盖

商品性质（正品/特价/赠品） ✅ 可放 Template 或 Variant 若每个商品不同，放 Variant

商品备注 ✅ 可放 Template 或 Variant 非关键

2. Product Variants（变体）——定义具体商品属性

适合放 每个商品独有的属性，尤其是会影响到销售、条码、库存、价格的属性，比如：

字段 建议放在 Variant 说明

商品条码（必填，一码一物） ✅ Variant 每个商品唯一

净金重 / 总重 / 石重 / 配件重 ✅ Variant 每个商品不同

成色（如：足金999、18k） ✅ Variant 若不同成色是不同商品，放 Variant

主石（颜色/净度） ✅ Variant 若主石不同，放 Variant

商品规格（自定义） ✅ Variant 若规格影响区分，放 Variant

工费（销售工费） ✅ Variant 每个商品可能不同

克工费 or 件工费 ✅ Variant 不同商品可能选择不同

证书号 ✅ Variant 每个商品可能不同

商品性质（正品/特价等） ✅ Variant 若每个商品性质不同

商品备注 ✅ Variant 可放

六、具体操作方法：手动 or 开发模块？

✅ 情况1：商品种类多（1000种）、属性多、重量不同 → 强烈建议通过模块开发实现

原因：

• 手动为每个商品（尤其有不同重量、条码、工费、价格）创建变体，工作量极大，易出错

• 你需要为每个商品设置：条码、净重、总重、工费、价格、成色、主石、工艺等

• 你需要让 条码唯一、且与实物一一对应

推荐方案：开发一个导入模块 或 后台管理界面，支持：

• 批量导入商品模板 + 变体（CSV/Excel）

• 为每个变体自动/手动设置条码、重量、工费、价格等

• 支持条码扫描、一码一物绑定

• 支持按重量计价、动态计算售价（比如：净重×金价 + 工费）

• 支持商品分类、成色、主石等筛选

如果你商品数量庞大、属性复杂，强烈建议 不要纯手工配置，而是通过开发实现：数据模型扩展 + 批量导入 + 自动变体生成

✅ 情况2：商品种类较少（几十个）、属性变化少 → 可以手动配置

• 通过 Odoo 后台：Products → Products

• 创建 Product Template（模板），设置公用属性

• 然后点击 "Variants" 标签页，手动创建不同的变体，为每个变体设置：

  • 条码

  • 重量

  • 价格

  • 工费

  • 成色等

但此方式 不适合你这种 1000+ 品种、重量各异、条码唯一的情况。

七、总结与推荐

问题 推荐方案

一码一物？ ✅ 必须使用 Product Variants，每个变体绑定唯一条码

计件 or 计重？ ✅ 通过变体字段区分，或通过业务逻辑控制，建议变体记录净重/总重，支持按重计价

商品属性多、重量不同、条码唯一？ ✅ 使用 Product Template + Variants，变体承载所有差异化属性

1000个品种，每个重量不同？ ❌ 不建议纯手工配置，强烈建议通过模块开发 + 批量导入实现

商品属性如何分配？ - 模板：放公用属性（名称、类别、工艺大类、默认价格等）<br>- 变体：放差异化属性（条码、重量、工费、价格、证书、主石等）

如何操作？ - 手动：仅适合极少量商品<br>- 开发模块：适合你这种业务复杂、数据量大的情况，支持批量导入、条码管理、动态计价等

🧩 如果你希望，我可以进一步为你提供：

1. 推荐的数据模型设计（Template & Variant 字段规划）
2. 批量导入模板（Excel/CSV 结构）
3. Odoo 模块开发思路：如何批量生成变体、如何绑定条码、如何实现按克重计价
4. POS 如何支持这些变体、如何显示条码、如何按重量销售

如你有更明确的诉求（比如：是否已有数据、是否需要对接电子秤、是否需要 POS 界面优化等），欢迎继续提问，我可以为你定制更落地的实施方案！  
  
# kimi

先把结论说在前面：  
1. 黄金珠宝这种“**同款多克重**”场景，**必须**用 **Product Template + Variants** 模式，否则 1000 个 SKU 会爆炸成 1000 个 Template，后期维护、库存、报价全是灾难。  
2. 只有“**真正会变、且影响库存/价格/条码**”的字段才做成 **Variant Attribute**；其余全部放在 Template 或 Variant 的 **普通字段** 里即可。  
3. 初始化可以**一次性用 Excel+CSV 导入**（Odoo 原生支持），日常新品用**小脚本**或**二次开发模块**自动创建，**无需手工一条条点**。

下面给出可直接落地的“**字段分配表 + 操作步骤 + 自动化思路**”，照着抄即可。

------------------------------------------------
一、字段分配表（Odoo 18 实体层面）

| 业务字段 | 放到哪 | 是否做成 Attribute | 理由 |
|-----------|--------|--------------------|------|
| 商品ID（内部编码） | `product.product`（Variant）默认字段 `default_code` | ❌ | 一码一物，系统自带 |
| 商品条码 | `product.product.barcode` | ❌ | 一码一物，系统自带 |
| 计件/计重 | Template 上新增 `x_fees_type` 选择 | ❌ | 同款下所有 Variant 共用 |
| 商品大类（黄金/K金/镶嵌/玉石） | Template 上新增 `x_category1` | ❌ | 同款同类 |
| 商品成色（18K/足金/99.99%） | Template 上新增 `x_purity` | ✅ 做成 Attribute | 影响工费/回收价 |
| 商品类别（戒指/手镯） | Template 上新增 `x_category2` | ❌ | 同款同类 |
| 商品主石（颜色/净度） | Variant 上新增 `x_stone_info` Char | ❌ | 非结构化文本即可 |
| 商品工艺（硬金/3D/5D/5G/珐琅） | Template 上新增 `x_craft` | ✅ 做成 Attribute | 影响克重区间 |
| 净金重 | Variant 上新增 `x_net_gold` Float | ❌ | 每克重即一个 Variant |
| 总重 | Variant 上新增 `x_total_weight` Float | ❌ | 库存以 Variant 维度 |
| 石重/配件重 | Variant 上新增 `x_stone_weight`/`x_part_weight` Float | ❌ | 同上 |
| 证书号 | Variant 上新增 `x_cert` Char | ❌ | 一物一号 |
| 销售工费/克工费/件工费 | Template 上新增 `x_fee_mode` + Variant 上 `x_fee_amount` | ❌ | 工费模式同款统一，金额因克重不同 |
| 成本/标价/批发价 | Variant 上新增 `x_cost`/`x_list_price`/`x_wholesale` Float | ❌ | 每克重价格不同 |
| 商品性质（正品/特价/赠品…） | Template 上新增 `x_nature` 选择 | ❌ | 同款同性质 |
| 商品备注 | Template 上新增 `x_note` Text | ❌ | 同款同说明 |

**Attribute 只留 3 个：**  
1. 成色（18K, 足金, 99.99%）  
2. 工艺（硬金, 3D, 5D, 5G, 珐琅）  
3. 克重（1g, 2g, 3g … 实际值用范围 0.01-200g，步长 0.01）  

------------------------------------------------
二、手工创建流程（一次性样板）

1. 开启开发者模式  
2. 销售 → 配置 → 属性 → 新建上述 3 个属性，勾选 **“快速创建”** 并录入所有值。  
3. 销售 → 产品 → 新建 **Template**  
   - 名称：足金硬金光圈戒指  
   - 产品类型：可储存  
   - 类别：黄金  
   - 勾选 **“可变异”**  
   - 在 **Variant Attributes** 页签添加 3 个属性 → 保存  
   - 系统会弹出 **“生成变体”** 向导 → 选 **“所有组合”** → 生成（如 3 成色 × 5 工艺 × 80 克重 = 1200 个 Variant）  
4. 用 **Variant 列表 → 导出** 拿到 ID 与 `default_code` 空白行 → Excel 填好条码、净金重、价格等 → 再 **导入** 即可。  
   一次样板做完，后续直接复制 Template 改名字即可。

------------------------------------------------
三、自动化方案（日常上新）

**思路：**  
- 只维护一张 **Excel 模板**（或上游 ERP 视图）→ 每晚/实时调用 Odoo API →  
  1. 若 Template 不存在 → 先 `create({‘name’:xxx, ‘attribute_line_ids’:[…]})`  
  2. 再 `create_variant_ids` 生成 Variant  
  3. 对 Variant `write({'x_net_gold':…, 'barcode':…, 'x_cost':…})`  

**核心代码片段（Odoo 18 API）**  
```python
# 1. 创建 Template 并一次性生成所有克重变体
template = env['product.template'].create({
    'name': '足金5D光圈手镯',
    'categ_id': gold_categ_id,
    'type': 'product',
    'x_craft': '5D',
    'x_purity': '99.99%',
    'x_fee_mode': 'gram',
    'attribute_line_ids': [
        (0, 0, {'attribute_id': attr_purity_id, 'value_ids': [(4, purity_99_id)]}),
        (0, 0, {'attribute_id': attr_craft_id,   'value_ids': [(4, craft_5d_id)]}),
        (0, 0, {'attribute_id': attr_weight_id,
                'value_ids': [(4, v) for v in weight_value_ids]})  # 0.01g-200g
    ]
})
# 2. 批量回写 Variant 级别字段
for var in template.product_variant_ids:
    net = var.product_template_attribute_value_ids.filtered(lambda a: a.attribute_id == attr_weight_id).name
    var.write({
        'default_code': f'GD5D-{net}g-{var.id}',
        'barcode':      f'695123{net.zfill(5)}{var.id}',
        'x_net_gold':   float(net),
        'x_total_weight': float(net) * 1.02,  # 工艺损耗
        'x_cost':       float(net) * 450 + 120,  # 当日金价+工费
    })
```
把这段放到 **Odoo Shell** 或 **计划任务** 里，即可**一键从上游视图生成几千个 Variant**，无需手工点界面。

------------------------------------------------
四、总结一句话

- **Template 管“款”**（名称、大类、工艺、工费模式）  
- **Attribute 只留“会变且影响库存/价格”的维度**（成色、工艺、克重）  
- **Variant 管“一物”**（条码、净金重、总重、价格、证书号）  
- 初始化用 **Excel 导入**；日常上新用 **API 脚本** 5 秒跑完 1000 SKU，**无需手工一条条建**。
  

# #############################################################################################################

# prodeucts，products variants，lot三者是什么关系，具有什么业务意义

下面把 **Products（product.template）**、**Product Variants（product.product）**、**Lots/Serials（stock.production.lot）** 三者的**结构关系**、**业务意义**与在 **POS/库存** 中的作用一次讲清：

---

# 一、三者的层级关系（谁管谁）

```
产品模板 (product.template)    1  ──►  N   产品变体 (product.product)   1  ──►  N   批次/序列号 (stock.production.lot)
      「款式/母体」                             「SKU/具体规格」                          「每一件或每一批的唯一编号」
```

* **Template → Variant（1\:N）**
  一个“款式”（模板）可以生成多个“SKU”（变体），例如“金戒指A款”有 15/16/17 号。
* **Variant → Lot/Serial（1\:N）**
  一个 SKU 可以对应多条批次/序列号记录：

  * **lot**：一码多件的“批次号”
  * **serial**：**一码一物**的“序列号”（黄金首饰强烈建议）

---

# 二、各自“业务定位”与你该把什么放哪里

## 1) Products = `product.template`（“款式/母体”）

**管什么**：共性、策略、在 POS 是否可售
**典型字段/设置**

* 是否在 POS 可售：`available_in_pos`（前台能否出现卡片）
* 跟踪方式：`tracking = serial/lot/none`（决定是否必须选序列号/批次）
* POS 分类：`pos.category`（决定前台分类浏览）
* 税、计量单位（计件/计重的销售单位）、默认售价/成本（策略基线）

**业务意义**

* 作为“目录项/卡片”出现在 POS 网格
* 定义一个款式的通用规则（黄金 / K金 / 镶嵌 / 玉石，大类、类别、是否一码一物……）

> 黄金场景建议：
> 模板上设 **`tracking = serial`（一码一物）**；把“是否在 POS 可售”“前台分类”“默认成色/工艺（仅描述）”放模板。

---

## 2) Product Variants = `product.product`（“SKU/具体规格”）

**管什么**：可实物管理的 SKU、条码、库存
**典型字段**

* 条码、内部参考（扫描、对账用）
* 由属性值（如戒指号）决定的具体规格
* 库存、补货、成本核算都以 **变体** 为粒度

**业务意义**

* **真正加入订单/出入库的实体**就是变体
* 需要“独立库存”的规格才做成变体（如戒指号数确实按号管理）

> 黄金场景建议：
> 只有 **“必须独立为 SKU”** 的差异（如戒指号）才生成变体；其他每件差异（重量、证书）**不要**做成变体，放“序列号”去承载，避免“变体爆炸”。

---

## 3) Lots/Serials = `stock.production.lot`（“每件/每批的唯一编号”）

**管什么**：**每一件**（或每一批）的**唯一标识与差异数据**
**典型字段（黄金建议扩展）**

* 标准：`name`（码）、`product_id`（指向变体）、`company_id`、有效期等
* 黄金建议扩展：**净金重、总重、石重、证书号、工艺、工费（按克/按件）、成色**……

**业务意义**

* **一码一物**：每件首饰一条 **Serial**；扫码即可唯一定位这件商品
* **承载每件差异**（重量、证书、工费…），用于 **动态计价** 与 **合规追溯**（售后、换退、抽检）

> 黄金场景建议：
> 把**净金重/证书/工费**等全部放到 **serial**；POS 选中序列号后即可按“净金重×当日金价×成色系数 + 工费”计算售价。

---

# 三、在 POS / 库存 / 会计 里的具体表现

* **POS 展示**：默认展示 **模板卡片**；若模板有多个变体，点卡片会先选变体。
  **加入订单**时记录的是 **变体**；若模板 `tracking=serial/lot`，会弹窗让你选 **序列号/批次**。
* **扫码**：

  * 扫 **变体条码** → 直接把该变体加入订单
  * 扫 **序列号条码**（若支持）→ 直接定位到那一件并绑定到行
* **库存**：按 **变体** 计量、拣货；若跟踪启用，拣货上会记录 **lot/serial**；报表可追溯到每件。
* **价格/策略**：

  * 模板/变体决定“是否可售/分类/税/基本价目表”；
  * **最终价**可由 **序列号数据 + 当日金价** 计算（你已安装的模块即可实现）。
* **合规/售后**：序列号提供“一物一证”的追溯链（买后退换、抽检监管都有据可查）。

---

# 四、黄金类最佳实践（避免踩坑）

* **少用变体，多用序列号**：
  “戒指号”若必须独立库存才做变体；重量/证书/工艺细节**放序列号**。
  否则 1000 款 × 多属性 = 变体爆炸，POS 加载慢、维护困难。
* **模板决定 POS 是否可售**：
  批量上下架 POS，用 **模板字段 `available_in_pos`**；你已做的 Server Actions 就是正确姿势。
* **组合（Combo）限制**：
  被 Combo 引用的商品不能直接下架；先从 **Combo Choices/组合** 中移除它。
* **改完要同步**：
  POS 前端有缓存，后台改数据后需 **同步/重开会话** 才生效。

---

# 五、一个“金戒指A”售卖流程的串起来示例

1. **模板**：Gold Ring A（`tracking=serial`、在 POS 可售、分类=黄金/戒指）
2. **变体**：Size 16（如需按号管理就生成，否则 1:1）
3. **序列号**：SN-GR-A-0001（净金重 3.56g、证书 CERT-0001、工费 120、工艺 3D、成色 Au999.9）
4. POS 前台：点“Gold Ring A” →（可能选择变体 “Size 16”）→ 选择/扫码 “SN-GR-A-0001”
5. 系统：用序列号上的净金重 + 当日金价 + 工费 计算单价 → 加入订单 → 出库时拣货记录该 serial

---

**一句话总括**

* **产品模板（Products）**：定义“能不能卖、怎么分类、是否一码一物”等“**款式层**规则”；
* **产品变体（Variants）**：落到“**SKU**”层面，真正出入库的单位；
* **序列号/批次（Lots/Serials）**：承载“**每件/每批真实差异与追溯**”，黄金行业的定价与合规核心。

  
  
  

# #############################################################################################################


# 再详细说明一下pos_gold_pricing 模块的具体业务功能，和在products、，products variants，lot页面中手动添加数据有什么具体的区别，只是使用配置界面是否能实现pos_gold_pricing 模块的所有功能，手动和建立模块代码区别在哪里。

下面把 **pos\_gold\_pricing** 的“它到底帮你多做了什么”、跟“只用配置界面（手工/导入）”的能力边界，和 **Products / Product Variants / Lots** 录入时有什么区别，讲清楚。最后给一张对照表+选型建议。

---

## 一、pos\_gold\_pricing 模块具体做了什么（业务功能）

1. **在序列号（lot）上建“黄金专用字段”**

   * 净金重、总重、石重、证书号、工艺、工费（克/件）、成色（金种）等。
   * 这些是“**一物一档**”的数据载体，避免把每件差异做成变体引发“变体爆炸”。

2. **新增“每日金价”模型（metal.pricelist）**

   * 金种、公司、日期、元/克、成色系数；自动取“**当日（<=今天最近一条）**”有效金价。
   * 多公司隔离（company\_id）。

3. **POS 前端自动定价（选 lot → 自动算单价）**

   * 公式（可改）：**净金重 × 当日金价 × 成色系数 + 工费（克/件）**。
   * 通过 POS 的 JS 补丁在**选择序列号**后调用后端 RPC 计算，然后 `setUnitPrice()`。
   * 收银员不用心算、不用改价；过程可配经理 PIN 保护（Odoo 自带）。

4. **菜单/视图 & CSV 模板**

   * 菜单：POS→Metal Pricing→Daily Metal Prices；lot 表单增加“Jewelry”页签。
   * 自带 3 份样例 CSV（分类/产品/lot）支持**批量导入**。

> 一句话：把“**一物一证** + **当日金价** + **工费**”三者打通到 POS 前台，**自动出单价**。

---

## 二、只用配置界面（不装模块）能做到哪些？

✅ **完全能做**（无需写代码）

* POS 分类、是否可售（Available in POS）、跟踪=序列号、选择 lot；
* 价目表（按产品/类别/日期做阶梯/折扣，**但不认 lot 的净重**）；
* **带价条码**（Barcode Nomenclature：Price），扫条码直接把“最终价”带入；
* IoT 秤（称重类商品）。

⚠️ **做不到/很费劲**（UI-only 的边界）

* **基于“lot 的净金重 + 当日金价 + 成色系数 + 工费”的自动单价**；
* 在**选中序列号时**自动改价（前端没这个钩子，需要自定义 JS 或 Studio 也做不到）；
* “当日金价”的**结构化维护与按公司/日期自动取价**；
* 让 **lot 字段**“参与 POS 定价公式”；原生价目表不会读 lot 字段。

👉 **不用代码的替代**：

* 打印**带价条码**（每件价签上已是“最终价”）→ 扫码即价；
* 或每天跑一个**脚本/自动动作**去**批量写死 list\_price**（按净重\*金价+工费算出模板/变体价）。
  代价：**不再是一物一价**（价格写在产品而非 lot 上），且每日要重算全量。

---

## 三、手工/导入 vs 模块：录入体验 & 数据落点的区别

| 场景          | 只用配置（手工/导入）                                                    | pos\_gold\_pricing（装模块）                     |
| ----------- | -------------------------------------------------------------- | ------------------------------------------- |
| **字段载体**    | 模板/变体能用的字段有限；lot 几乎无“黄金字段”，可用 Odoo Studio 临时加，但**不会驱动 POS 定价** | lot 上有**净金重/证书/工费/工艺/成色**等字段；被 POS 自动计算直接使用 |
| **当日金价**    | 无模型；用价目表“近似”或手工更新价签/产品价                                        | **metal.pricelist** 模型，按公司/日期取最近有效价         |
| **定价触发**    | 收银员手改；或用**带价条码**                                               | 收银员选 lot → **自动算价**；可叠加经理授权                 |
| **准确性/一致性** | 人工易错；多店同步靠流程                                                   | 公式固化、统一计算；改一次金价全店生效                         |
| **变体规模**    | 往往为了“每件不同”被迫做成变体，**爆炸**                                        | **严格一物一码**，差异放 lot，**极大减变体量**               |
| **批量导入**    | 你自己设计 CSV；多字段容易对不齐                                             | 模块自带 3 类 CSV 模板，列名匹配，导入即用                   |
| **可审计性**    | 价从何来难追溯                                                        | lot 字段 + 金价记录，**算价可复现**                     |
| **上线速度**    | 快，但靠操作纪律                                                       | 稍多一步安装+配置，之后更省事、更稳                          |

---

## 四、结论：配置能否“等价替代”模块？

* 你可以用**带价条码**把 POS 先跑起来（**无代码**），但那是“**后台或外部系统**先把价算好并印到条码”，POS 只是录价；
* **要在 POS 里“选 lot 就自动算价”**，且支持“当日金价/多公司/成色系数”，就**必须有自定义逻辑**（JS 钩子 + 后端计算）——也就是 **pos\_gold\_pricing** 的核心价值。

---

## 五、什么时候只用配置，什么时候用模块？

* **小规模/过渡期**：

  * SKU ≤ 数百，价签系统到位 → **带价条码** + 手工/导入即可。
* **标准化/规模化/多门店**：

  * 每天调价、上千款、追溯/审计要求高 → **pos\_gold\_pricing**（或等价定制）更合适。

---

## 六、和 Products / Variants / Lots 的配合

* **Products（模板）**：是否 POS 可售、tracking=serial、POS 分类、税/UoM；
* **Variants（变体）**：只在**必须独立库存**（如戒指号）时才生成；
* **Lots（序列号）**：录入净金重/证书/工费/工艺/成色等；**本模块从这里取数并算价**。

> 手工/导入与装模块**并不冲突**：
>
> * 你仍然用 UI 或 CSV 导入“分类/模板/变体/lot”；
> * **区别在于**：装了模块后，**lot 字段立刻“有用武之地”**（驱动定价），不再只是摆设/描述。

---

## 七、潜在扩展（模块能继续做的事）

* 经理 PIN 控制“手工改价/折扣”；
* 含税/不含税口径、现金舍入；
* 票据/价签模板（打印净金重/证书）；
* 批量校验器（导入时检查“净金重>总重”等逻辑）；
* 与 IoT 秤融合（以序列号净重为主，秤为校验）。

---

### 一句话总结

* **配置界面**可把 POS 先跑起来（分类、lot、带价条码）；
* **pos\_gold\_pricing** 把“**一物一证 + 当日金价 + 自动定价**”真正落在 POS 上，**减少人工、避免出错、可追溯**；
* 两者的差别不是“能不能录入数据”，而是“**这些数据是否被 POS 自动、稳定地用起来**”。

  
  
  

# #############################################################################################################

# Product Template 、Variants 、Variant Attribute，这三个业务意义分别是什么

下面用 Odoo 术语把三者的**业务意义**说清楚，并点明它们之间的关系与常见用法/坑位。

---

## 1) Product Template（产品模板，`product.template`）

**业务定位**：一“款”商品的**母体/蓝本**。
**承载**：对这款商品**共同**且**稳定**的属性与策略——是否可在 POS 销售（Available in POS）、计量单位（件/克）、税、产品类型（库存/消耗/服务）、跟踪方式（不跟踪/批次/序列号）、POS 分类、基础标价/成本等。
**作用**：

* POS 前台默认显示**模板**卡片（点击后选变体）。
* 模板上挂“变体属性线”（见下条）决定会生成哪些变体。
* 批量上下架 POS、设置追踪方式、归类等，都在模板层完成。

> 比喻：模板 = “iPhone 15 这款机型”的定义，不含具体颜色/容量。

---

## 2) Product Variants（产品变体，`product.product`）

**业务定位**：可入库/出库/计数的**具体 SKU**。
**来源**：由“模板 + 变体属性值组合”**自动派生**。
**承载**：条码、内部参考、实际库存、补货与成本核算都在**变体**颗粒度进行；价格可继承模板，也可由属性值附加“价差”。
**作用**：

* **真正加入订单/拣货/盘点**的是变体（不是模板）。
* POS 扫变体条码直接加行；若从模板卡片进入会先弹变体选择。
* 只有**确需独立库存**的规格（如尺码、容量、戒指号）才应做成变体，避免“变体爆炸”。

> 比喻：变体 = “iPhone 15 / 黑色 / 256GB” 这条 SKU。

---

## 3) Variant Attribute（变体属性）

> 由几个相关对象构成：`product.attribute`（属性，如颜色/尺码）、`product.attribute.value`（属性值，如黑/白、S/M/L），以及模板上的 `product.template.attribute.line`（模板选择了哪些属性及其允许的值、是否生成变体）。

**业务定位**：定义**哪些维度**会把同一款商品拆分成多个 SKU；或仅作为**描述/搜索字段**存在。
**关键点**：

* **生成策略**（在“属性与变体”页签）：

  * **Generate variants**（生成变体）：不同取值会产生不同的 `product.product`。
  * **No variant**（不生成变体）：仅用于展示/搜索/过滤，不创建新 SKU。
* **价差（Price Extra）**：可在属性值上设置对标价的加价/减价（如 256GB +300）。
* **排除规则**（Exclusion，可选）：禁止不合逻辑的组合。

**作用**：

* 决定**有多少个变体**、每个变体的**属性标签**、可能的**价差**。
* 典型做法：把“必须独立库存”的维度（尺码/容量/戒指号）设为**生成变体**；把“仅用于描述/搜索”的（成色/工艺等）设为 **No Variant**。

> 比喻：属性=“颜色/容量”，属性值=“黑/白”“128/256”。

---

## 三者关系一图懂

```
Product Template（款式）
  └─ Attribute Lines（本款使用的属性+值+生成策略）
        ├─ 属性A：值a1、a2 …（是否生成变体？价差？）
        └─ 属性B：值b1、b2 …
  └─ 自动派生 → 多个 Product Variants（SKU：a1+b1、a1+b2、…）
```

---

## 常见实践（以黄金首饰为例）

* **模板**：定义“黄金戒指A 款”，POS 可售、`tracking=serial`（一码一物）、POS 分类=黄金/戒指。
* **变体**：\*\*只有“戒指号”\*\*需要独立管理时才生成变体（如 15/16/17 号）。
* **变体属性**：

  * 戒指号：**生成变体**
  * 成色/工艺：通常设为 **No Variant**（仅描述）；每件差异（净金重、证书号、工费…）放**序列号 lot**上，由定制模块参与计价。

> 小贴士：一切“每件都不同”的信息（重量、证书）不要做成变体，放 lot；否则 SKU 会指数膨胀，POS 变慢、维护困难。

---

## 常见坑

* **把所有维度都设成生成变体** → 组合爆炸、维护困难。
* 在**变体**页面改“在 POS 可售”无效：该勾选在**模板**层（`available_in_pos`）。
* 忽视 `tracking`：贵金饰不设 `serial` 会丢失“一物一证”的追溯与定价依据。

---

## 快速决策原则

* “是否能卖、如何分类、是否一码一物” → **模板**
* “库存与条码的最小单位（必须独立管理）” → **变体**
* “会不会把款式拆成多个 SKU/是否仅作描述与价差” → **变体属性（及其值）**

需要的话，我可以给你一张“你的字段清单 → 放模板/变体/lot/属性”的映射表（已在前面多次给过黄金场景版），或按你的真实商品数据生成**最小变体集合**的建议方案。
  
  
  

# #############################################################################################################

# 按chatgpt的设计方案，黄金类产品适合用products+lot来定义产品，只有少量的需要采用products variants，而你这边的建议是products+products variants，没有考虑lot，请对比两种方案的优劣。

# 按deepseek的设计方案，黄金类产品适合用products+products variants来定义产品，，没有考虑lot，而你这边的建议是products+lot，请对比两种方案的优劣。

# deepseek
这是一个非常重要且实际的问题，特别是在 黄金、珠宝、玉石等贵重、多规格、多批次、一码一物类行业 的 Odoo 商品管理设计中。

你提到了两个主流的 Odoo 商品管理建模思路：

🔁 两种主流方案对比

方案 核心组成 适用商品类型 你的提问中的表述

方案 A（你提到的 ChatGPT 推荐） Product（产品） + Lot/Serial Number（批次/序列号） 强调以“批次/唯一码”管理商品，适合 一物一码、强调追溯、重量不作为变体区分维度 的场景 “黄金类产品适合用 Products + Lot 来定义产品，只有少量需要采用 Product Variants”

方案 B（我的推荐） Product Template（产品模板） + Product Variants（产品变体） 强调以“变体”管理不同规格/属性组合的商品，适合 规格多样、属性复杂（如成色、重量、工艺）、一码一物 的场景 “建议使用 Product + Product Variants，每个变体绑定唯一条码/重量/属性”

接下来，我会从多个维度，深入对比这两种方案在 黄金、K金、珠宝、玉石行业 的实际应用中的：

• 业务适配性

• 系统实现难度

• 管理效率

• 条码/追溯/库存管理

• 价格/成本管理

• 适用场景范围

一、先明确两个方案的本质

✅ 方案 A：Product（产品模板） + Lot/Serial Number（批次/序列号）

• 核心思想：

  • 你只定义 一个或少数几个 Product（产品模板），比如 “足金产品”、“K金戒指”；

  • 每个实际的商品（不同重量、条码、成色）不创建 独立变体，而是通过 Lot（批次）或 Serial（序列号） 来区分；

  • 每个实物商品（比如一根 3.5g 的足金项链）对应一个 唯一的 Lot 或 Serial Number（一码一物）；

  • 商品的属性（如重量、成色、主石）通过 附加字段、Lot 信息、外部表或关联模型 记录。

• 通俗理解：

  • 你卖的是 “足金产品” 这个品类，至于具体是 3.5g 还是 4.0g，是通过 Lot 号/序列号 + 外部信息 区分，而不是通过 Odoo 的变体机制。

✅ 方案 B：Product Template + Product Variants

• 核心思想：

  • 你为每一种 实际可售卖的商品组合（规格/属性） 创建一个 独立的变体（Product Variant）；

  • 每个变体可以拥有 自己独立的条码、重量、成色、价格、工费等；

  • 每个变体是一个 具体的 SKU（库存单位），是实际销售、盘点、出库的对象；

  • 通过 变体机制天然支持一码一物（条码唯一）、属性组合、精准库存管理。

• 通俗理解：

  • 你卖的不只是 “足金戒指”，而是 “足金戒指 3.5g 足金 成色999 戒指款 刻字” 这么一个具体的商品，它是一个独立 SKU。

二、核心维度对比

维度 方案 A：Product + Lot 方案 B：Product + Variants 适用性结论

1. 一码一物（条码唯一性） ✅ 支持，通过 Lot 或 Serial Number 绑定唯一条码 ✅ 更直接，每个变体天然可绑定唯一条码 两者都支持，但 变体更直观、更贴合 SKU 管理

2. 商品属性多（成色、重量、工艺、主石等） ⚠️ 属性不放在变体上，需通过 Lot/额外字段/外部表记录，查询困难 ✅ 属性可直接作为变体属性或变体字段，查询直观、筛选方便 变体胜出：属性管理更结构化

3. 重量不同（如 3.5g / 4.0g） ⚠️ 重量通常不作为变体区分依据，需通过 Lot 或额外字段记录 ✅ 推荐将重量作为变体字段或属性，每个变体可不同 变体胜出：重量是重要售卖和计价维度，应结构化管理

4. 商品种类极多（1000+ 品种，每个重量/成色不同） ❌ 管理复杂，依赖大量 Lot，难以结构化查询与分析 ✅ 每个商品组合对应一个变体，结构清晰，易于管理、分析、销售 变体胜出：适合海量 SKU 管理

5. 是否需要用户选择规格（如成色、重量）来购买 ⚠️ 用户无法直接选择“成色/重量”，需通过业务逻辑控制 ✅ 用户可在前端选择不同成色/重量/规格的变体，体验更友好 变体胜出：适合需要规格选择的销售场景（如电商/POS）

6. 计件 or 计重 ⚠️ 需通过额外逻辑判断，比如通过 Lot 记录重量，再计算价格 ✅ 可通过变体字段记录重量，灵活支持计件或计重逻辑 两者皆可，但变体更直观

7. 条码管理（扫码销售、盘点） ✅ 可通过 Lot + 条码实现，但需额外配置 ✅ 变体天然支持条码，可直接绑定、扫码、销售 变体更直接，适合 POS / WMS / 扫码场景

8. 价格管理（不同商品不同价格） ⚠️ 不同重量的商品价格差异需通过 Lot 或外部表管理 ✅ 每个变体可设置独立价格，管理清晰 变体胜出：价格与 SKU 绑定更直观

9. 成本核算（不同商品成本不同） ⚠️ 需通过 Lot 或额外字段记录成本 ✅ 每个变体可设置独立成本，适合精细核算 变体胜出

10. 实现难度 / 配置复杂度 ✅ 只需创建少量产品模板，通过 Lot 区分实物，配置简单 ⚠️ 若商品种类极多，手动创建变体工作量大，推荐通过模块/导入实现 方案 A 更简单，方案 B 更精准但需开发支撑

11. 适合场景 - 商品种类少<br>- 规格变化少<br>- 强调批次追溯（如黄金原料）<br>- 不需要用户前端选择规格 - 商品种类多<br>- 每个商品重量/成色/工艺不同<br>- 需要用户选择规格<br>- 需要精准 SKU 管理、条码、价格、成本 黄金珠宝行业通常更适合方案 B（变体），除非是原料/大克重金条等可批次管理

三、重点补充：Lot（批次/序列号）的本质与局限

✅ Lot（批次号）或 Serial（序列号） 是什么？

• 是 Odoo 提供的用于 追踪实物唯一性或生产批次 的机制；

• 你可以为 每一个入库的商品（哪怕是同一个模板）绑定一个唯一的 Lot 或 Serial；

• 适用于：

  • 追溯生产批次

  • 管理保质期（食品、药品）

  • 管理贵金属原料（如金条，不区分具体克重售卖）

  • 管理设备、零件等

⚠️ 但在黄金珠宝零售/POS场景中的 局限性：

问题 说明

无法直接区分商品属性 比如 3.5g 足金戒指 和 4.0g 足金戒指，如果只用 Lot，无法在前端让用户选择“我要 3.5g 的”

不适用于结构化 SKU 管理 每个重量/成色/工艺都不同，用 Lot 管理会使得销售、库存、价格管理变得复杂

不适合 POS 场景 用户在门店不可能说：“我要那个 Lot 号是 123 的金戒指”，而是说：“我要 3.5g 足金戒指，刻字的”

不利于价格差异化 不同重量的商品价格不同，用 Lot 管理会导致价格逻辑分散、难以维护

四、综合结论：哪种方案更适合你？（黄金珠宝类商品）

✅ 推荐使用 方案 B：Product + Product Variants（产品模板 + 变体），如果：

• 你销售的是 具体规格的商品（如 3.5g 足金戒指、4.0g K金项链）

• 每个商品有 不同的条码、重量、成色、工艺、价格、工费

• 你希望用户在 POS 或电商中可以选择具体规格

• 你希望做到 一码一物（条码精准绑定实物）

• 你有 1000+ 不同组合的商品，需要结构化、可筛选、可管理

🔧 实现建议：
• 用 Product Template 定义公用属性（如：足金戒指、K金、商品类别）

• 用 Product Variants 定义具体商品（如：3.5g 足金 戒指 刻字 证书号xxx）

• 每个变体绑定 唯一条码、净重、总重、价格、工费、证书号

• 通过 模块/导入工具 批量生成变体，避免手工创建

✅ 可考虑使用 方案 A：Product + Lot（适用于特殊情况），如果：

• 你管理的是 黄金原料、金条、回收料，它们 按批次/重量范围管理，而不是按每个具体克重售卖

• 你更关注 批次追溯、入库批次、保质期、原料流向，而不是前端用户选择具体规格

• 商品种类少、规格单一、不需要用户选择成色/重量/工艺

五、最终结论（精简版）

你要管理什么样的黄金商品？ 推荐方案

具体规格商品（3.5g足金戒指、带证书、有工费、条码唯一），有 1000+ 品种，需精准销售、条码、价格管理 ✅ Product + Product Variants（推荐）

原料类、金条、大克重、按批次管理，不区分具体规格售卖 ✅ Product + Lot / Serial（可接受）

你想让用户在前端选择成色/重量/款式，精准购买 ✅ 变体（Variants）

你只关心入库批次、简单追溯，不关心具体规格售卖 ✅ Lot

✅ 如果你希望，我可以进一步为你：

1. 提供 Odoo 变体属性的最佳实践设计（哪些放模板，哪些放变体）
2. 设计 黄金珠宝行业的变体字段结构（重量、成色、工费、价格等）
3. 提供 批量变体生成 / 导入方案（Excel/CSV/模块）
4. 帮助你设计 POS、销售、库存、条码、计价等配套流程

欢迎继续深入交流！





  
  

# #############################################################################################################

# 在odoo18中，product.template和product.product以及pos.category分别代表什么意思，当这些出现的时候，是指数据库表吗，还是分类，当提到这些的时候，我该如何操作。

下面把 **product.template**、**product.product**、**pos.category** 在 Odoo 18 里的含义、它们是不是“数据库表”、以及你在界面里该怎么操作，讲清楚；再补上常用字段与导入要点，避免和其它“分类”混淆。

---

# 它们分别是什么？

## 1) `product.template`（产品模板）

* **业务意义**：一款商品的“母体/款式”。用来定义对整款通用且稳定的设置：
  是否在 POS 可售（`available_in_pos`）、计量单位（件/kg）、是否称重（`to_weight`）、税、产品类型（库存/消耗/服务）、POS 分类、基础标价/成本、跟踪方式（不跟踪/批次/序列号）等。
* **技术上**：这是一个**模型（Model）**，技术名是 `product.template`，底层数据库表是 **`product_template`**。
* **关系**：1 个模板可以派生出 **多个变体**（见下一条）。

## 2) `product.product`（产品变体 / SKU）

* **业务意义**：真正进入库存/出库/盘点/结算的 **具体 SKU**（例如“戒指A / 16号”）。
  具体条码、实际库存、补货、会计成本核算都在变体粒度进行。
* **技术上**：模型 `product.product`，底层数据库表 **`product_product`**。
* **来源**：由“模板 + 变体属性（如尺码/颜色/号数）的取值”自动派生。

> 简单记：**模板=款式**，**变体=SKU**。POS 前台默认显示模板卡片，但加入订单的一定是变体。

## 3) `pos.category`（POS 分类）

* **业务意义**：**POS 前台的左侧分类树**（“黄金/戒指/手镯…”）。它只影响 POS 前台的分组和浏览，不等于会计/库存分类。
* **技术上**：模型 `pos.category`，底层数据库表 **`pos_category`**。
* **别混淆**：还有一个 `product.category`（产品类别），那是会计/库存用的后台分类，**不会**控制 POS 前台左侧分类。

---

# 这是“数据库表”还是“分类”？我该怎么理解？

* 当你看到 **`product.template` / `product.product` / `pos.category`** 这种带点号的名字，通常指的是 **Odoo 的“模型（Model）”**（也就是 ORM 抽象）。

  * 在数据库里对应的表名是把点号换成下划线：`product_template`、`product_product`、`pos_category`。
* 在日常沟通里，大家说“到 `product.template` 勾 Available in POS”，意思是：**去“产品（模板）”界面**操作这个模型的字段，而不是让你去敲 SQL。

---

# 在界面中我该怎么操作？

> 先打开 **开发者模式**（右上角 → 关于 → 启用开发者模式），能看到技术名、更方便导入。

## A. 产品模板（`product.template`）

* 路径：**销售/库存 → 产品 → 产品**（这是模板列表）
* 常用操作：

  * 勾 **Available in POS**（在 POS 可售）
  * 设 **计量单位**（件/kg），是否称重（`To Weigh`）
  * 设 **POS 分类**（`pos.category`）
  * 设 **跟踪方式**（不跟踪/批次/序列号）
  * 添加“属性与变体”（决定是否生成变体）
* 适用：统一配置整款商品的策略与默认值。

## B. 产品变体（`product.product`）

* 路径：**销售/库存 → 产品 → 产品变体**
* 常用操作：

  * 填写 **条码**、内部参考
  * 查看/调整 **库存数量**、补货规则
  * 若用 CSV 直接落 SKU，也可以在此导入
* 适用：SKU 级别的库存/条码/定价微调（价格一般继承模板，可用价目表叠加）。

## C. POS 分类（`pos.category`）

* 路径：**POS → 配置 → 产品分类（或 Products → Product Categories）**
* 常用操作：

  * 维护**分类树**（父子关系）
  * 在产品模板上勾选对应的 POS 分类（可多选）
* 作用：决定 POS 前台左侧的分类与网格分组。

---

# 常用字段速查（导入时最常用）

**product.template（CSV 列）**

* `name`（名称）、`default_code`（款号）、`barcode`（可选）、`available_in_pos`（1/0）
* `type`（`product` 库存商品/`consu` 消耗品/`service` 服务）
* `uom_id/id`（单位：件=`uom.unit`；kg=`uom.kg` 等）
* `to_weight`（计重=1；计件=0）
* `pos_categ_ids/id`（POS 分类可多选，逗号分隔）
* `list_price`（标价）、`standard_price`（成本）

**product.product（CSV 列）**

* `product_tmpl_id/id`（指向模板）
* `attribute_value_ids/id`（属性值外部ID，逗号分隔）
* `default_code`、`barcode`、`list_price`

**pos.category（CSV 列）**

* `name`、`parent_id/id`（建树用）
* 例：`pc_gold` 顶层；`pc_gold_ring` 的 `parent_id/id=pc_gold`

---

# 模板、变体、POS 分类：如何配合？

1. 先建 **POS 分类** 树（`pos.category`）。
2. 建 **模板**（`product.template`）：

   * 是否在 POS 可售、计件/计重（单位/称重）、POS 分类、税等。
   * 有需要的“变体维度”（如戒指号）→ 在“属性与变体”页签配置是否生成变体。
3. （需要时）生成或导入 **变体**（`product.product`）：每个 SKU 的条码、库存、价目表。
4. POS 前台默认显示 **模板卡片**；若模板有多个变体，点击会先弹 **变体选择**；扫码变体条码可直接加行。

---

# 遇到“技术名”时如何定位到界面？

* **方法 1：全局搜索**：右上角搜索“产品”“变体”，进入对应菜单。
* **方法 2：开发者模式 → “查看元数据/字段”**：在任何表单右上角（虫子图标菜单）可看到当前模型名（比如 `product.template`）。
* **方法 3：导入/导出向导**：进入列表 → 导入/导出时，字段的“技术名”会显示，便于对齐 CSV 列名。

---

# 易错点提醒

* **`pos.category` vs `product.category`**：前者控制 POS 左侧分类；后者用于会计/成本/库存分组，**两者不是同一个**。
* **在“变体”页勾 POS 可售无效**：`available_in_pos` 是**模板字段**，到模板页去勾。
* **不在列表视图/没勾记录时看不到“动作”**：很多批量动作只在**列表视图**且**勾选行**后才出现。
* **多公司**：右上角切到正确公司；产品/分类/会话要同一公司才看得到/能操作。
* **导入时的外部 ID**：`/id` 列指“外部ID”（而不是显示名），要先在上游 CSV 定义过才可引用。

---

## 小结（如何理解 & 怎么做）

* 看到 `product.template` / `product.product` / `pos.category`：把它们理解为 **模型（可在界面里操作的业务对象）**；
  若你在写脚本/导入，它们也对应**数据库表**（`product_template`/`product_product`/`pos_category`）。
* 操作路径：

  * 模板：**销售/库存 → 产品 → 产品**
  * 变体：**销售/库存 → 产品 → 产品变体**
  * POS 分类：**POS → 配置 → 产品分类**
* 做初始化：按“先分类 → 再模板 → 再（可选）变体”的顺序，使用 CSV 导入；模板层设置 POS 可售、计量单位/称重、分类、税；变体层设置条码与库存。

如果你愿意，我可以给你三张**空白 CSV 模板**（带好常用列，含外部ID示例），你把 10 行样例数据填上来，我再检查一下列映射是否完全吻合你库的字段与语言环境。





  
  

# #############################################################################################################

# #############################################################################################################

# #############################################################################################################

下面给你一份**可落地的初始化方案**（Odoo 18），按你指定的**Product Template + Product Variants**（不用 lot）的建模思路来做，覆盖：数据建模、配置与导入模板、POS/库存联动、以及“只用配置”和“加少量代码/Studio”的取舍与差异。

---

# 0) 建模总纲（不使用 lot 的前提）

* **模板（product.template）**：决定是否在 POS 可售、产品类型/税、**计量单位（件 或 重量）**、POS 分类（大类/类别）、基础价格（固定价）。
* **变体（product.product）**：真正的 SKU（可入库/出库/盘点/定价对象），用来表达**戒指号等必须独立库存**的离散维度。
* **属性（Variant Attribute）**：

  * “戒指号”这类 → **生成变体**；
  * “成色/工艺/主石”等用于**分类/检索** → 建议 **No Variant（不生成变体）**，避免变体爆炸。
* **计件 vs 计重（互斥）**：

  * 计件：产品 UoM=“件”（`uom.unit`），`to_weight=False`，`list_price` 为**每件固定价**。
  * 计重：产品 UoM 用**重量类**（建议“公斤”系），勾 **To Weigh**（POS称重或手输重量），`list_price` 维护为**每公斤价**（当班克价×1000），收银时可**手改单价**（经理 PIN 控制）。

  > 说明：POS 称重按**数量×单价**计费，数量是**kg**（可用 IoT 秤或手输），单价是**元/kg**。若你的克价是 680 元/克，则 `list_price = 680 * 1000 = 680000 元/kg`，收银时也可直接改成当班价。

---

# 1) 基础配置（一次性）

1. **计量单位（UoM）**

   * 确认存在：**件（Units）**、**公斤（kg，重量类基准）**、**克（g）**（可选，仅用于显示/换算）。
   * 计重商品建议把销售单位设为**公斤**（POS秤量/手输数量是 kg，更顺畅），显示给收银员的标签可写“按克计价（自动换算）”。

2. **POS 分类（pos.category）**

   * 按你给的分类做两级树：**大类**（黄金/K金/镶嵌/玉石） → **类别**（戒指/手镯…）。
   * 前台商品网格依此分组。

3. **产品属性（product.attribute）**

   * **戒指号**：设为 **Generate Variants（生成变体）**。
   * **成色/工艺/主石**：设为 **No Variant**（只作描述/搜索、报表维度）。

4. **POS 设置**

   * 启用 **允许改价/折扣**（可配经理 PIN）。
   * 若有秤：启用 **IoT Scale**，计重商品勾 **To Weigh**。
   * 打印/报表按需启用。

---

# 2) 初始化与批量导入（CSV 模板）

> **导入顺序**：`pos.category` → `product.attribute`/`product.attribute.value` → `product.template` → `product.product`（可选，若你要生成具体变体行）。

### (A) POS 分类 `pos.category`

```csv
id,name,parent_id/id
pc_gold,黄金,
pc_gold_ring,戒指,pc_gold
pc_k,K金,
pc_k_ring,戒指,pc_k
```

### (B) 属性与取值

**属性（product.attribute）**

```csv
id,name,display_type
attr_ring_size,戒指号,radio
attr_fineness,成色,select
attr_process,工艺,select
attr_mainstone,主石,select
```

**属性值（product.attribute.value）**

```csv
id,name,attribute_id/id
v_size_15,15,attr_ring_size
v_size_16,16,attr_ring_size
v_fineness_au9999,Au 999.9,attr_fineness
v_fineness_18k,18K,attr_fineness
v_proc_3d,3D,attr_process
v_proc_hard,硬金,attr_process
v_stone_none,无,attr_mainstone
v_stone_diamond,钻石,attr_mainstone
```

> UI 上把 **戒指号**设为“生成变体”，其余设为 “No Variant”。若你坚持用 CSV 生成属性线，可导 `product.template.attribute.line`，但初次建议在模板表单里点选更稳。

### (C) 产品模板 `product.template`

* **计件商品**（固定价、按件卖）

```csv
id,name,default_code,barcode,available_in_pos,type,uom_id/id,to_weight,pos_categ_ids/id,list_price,standard_price
pt_ringA,黄金戒指A,GR-A,690000000001,1,product,uom.unit,0,"pc_gold,pc_gold_ring",2988,1500
```

* **计重商品**（按克卖、POS称重或手输重量；单价=元/kg）

```csv
id,name,default_code,barcode,available_in_pos,type,uom_id/id,to_weight,pos_categ_ids/id,list_price,standard_price
pt_gold_bulk,足金散件,AU-BULK,690000000100,1,product,uom.kg,1,"pc_gold",680000,0
```

> 字段说明：
>
> * `available_in_pos`：是否在 POS 可售；
> * `uom_id/id`：计件→`uom.unit`，计重→`uom.kg`；
> * `to_weight`：计重商品 **1**（启用称重）；
> * `list_price`：计件=单件价；计重=**元/kg**（克价×1000）。

### (D) 生成变体（两种方式，任选一种）

**方式 1（推荐）**：在模板表单 “属性与变体”页签，

* 添加 **戒指号** 属性，选中允许的值（15/16/…），选择 **Generate Variants** → 保存 → 系统自动生成变体。

**方式 2（CSV 导入 product.product）**：直接建立具体 SKU（适合你已有 SKU 清单）

```csv
id,product_tmpl_id/id,attribute_value_ids/id,default_code,barcode,list_price,standard_price
pp_ringA_15,pt_ringA,"v_size_15",GR-A-15,690000000015,2988,1500
pp_ringA_16,pt_ringA,"v_size_16",GR-A-16,690000000016,2988,1500
```

> `attribute_value_ids/id` 多值用逗号分隔（如同款多属性组合）。

---

# 3) 业务流对接（入库 / POS 销售 / 盘点报表）

* **入库**：按**变体**收货、上架；计重商品用 **kg** 数量（如 0.123 kg）。
* **POS 销售**：

  * 计件：点商品直接加行，按 `list_price`。
  * 计重：商品勾 “To Weigh” → 秤读取**kg数量** 或手输重量；**单价**用 `list_price`（元/kg），也可**手改**（建议经理 PIN）。
  * 若“当班克价”变动：可在 POS 里**手改单价**，或用**服务器动作**批量把 `list_price` 更新为“新克价×1000”。
* **盘点/报表**：

  * 库存以**变体**粒度；计重商品按 kg 统计。
  * 属性（成色/工艺/主石）作为报表的分组/过滤维度（因为设为 No Variant）。

---

# 4) 互斥校验 & 常用自动化（可选，强烈建议）

> **纯配置**能跑，但无法“拦错/自动算价”。下面两种做法二选一：

* **无代码（易上手）**：靠流程规范 + 服务器动作

  * “批量设为计重（to\_weight=1，UoM=kg）/计件（to\_weight=0，UoM=件）”
  * “把克价×1000写入 list\_price（元/kg）”

  ```python
  # 模型：product.template（服务器动作）
  pts = records or env['product.template'].browse(env.context.get('active_ids') or [])
  # 例：把这些模板设为计重商品，并刷新单价=克价×1000
  gram_price = float(env.context.get('gram_price', 680))  # 可在界面提供参数
  pts.write({'to_weight': True, 'uom_id': env.ref('uom.product_uom_kgm').id, 'list_price': gram_price * 1000})
  log(f"已更新 {len(pts)} 条（计重，{gram_price} 元/克）。")
  ```

  * “互斥校验”靠人工（或导出检查）：

    * 计件商品 `to_weight` 必须为 0，UoM=件；计重商品 `to_weight`=1，UoM=kg。
* **轻量定制（推荐）**：加一小模块或 Odoo Studio 字段 + 约束

  * 新增 `pricing_mode`（`per_piece` / `per_gram`），自动联动 `to_weight` 与 UoM；
  * 加 SQL/ORM 约束：禁止同时“per\_gram 且 UoM=件”等；
  * 提供后台“本日克价”字段，一键批量刷新计重商品 `list_price=克价×1000`。

  > 好处：避免错误数据，培训成本低；坏处：需要一次性小改动（很快）。

---

# 5) 你字段清单的**落点建议**（Variants 方案）

> 仅用配置，无法为“每件”存独立重量/证书——这些放**lot**才完美。但在“Variants-only”前提下，建议如下：

| 字段            | 放置建议（无代码/轻代码）                                                                                      |
| ------------- | -------------------------------------------------------------------------------------------------- |
| 一码一物/一码多件     | 用 **tracking=none**（不做 lot）；若监管要求强，可后续再启用 serial（那时会用 lot）                                         |
| 计件/计重         | 模板 UoM + `to_weight`（互斥）；可加 `pricing_mode` 字段自动联动                                                  |
| 产品ID、条码、名称    | 变体（`default_code`/`barcode`），模板有总名                                                                 |
| 大类/类别         | `pos.category` 两级；`product.category` 做会计分类                                                         |
| 成色/工艺/主石/规格   | **属性（No Variant）** 或模板自定义字段（用于报表/过滤）                                                               |
| 净金重/总重/石重/配件重 | **建议未来上 lot 后承载**；在 variants-only 阶段：可暂存在**变体说明**（description），或用 **Studio 给 product.product 加字段** |
| 证书号           | 同上（Studio 字段存于 `product.product`），但严格“一物一证”建议以后切换 lot                                              |
| 销售工费/工费类型     | 可存模板或变体自定义字段（Studio）；计价由收银员手改单价体现                                                                  |
| 成本、标价、批发价     | 模板/变体的 `standard_price / list_price` + 价目表（批发）                                                     |
| 性质（正品/特价/赠品…） | 模板选择字段或产品标签                                                                                        |
| 备注            | 模板/变体 `description`/`description_sale`                                                             |

---

# 6) 使用与培训要点（计重场景）

* 收银员流程：选择计重商品 → POS 自动读秤（或手输**kg**数量）→ 单价默认为“当班 kg 价”（或手改成当班克价×1000）→ 结账。
* 班前操作：经理用**服务器动作**批量刷新计重商品 `list_price = 当班克价×1000`。
* 报表：库存/销售汇总按**变体**；按属性（成色/工艺/主石）做分组。

---

## 7) 只用配置 vs 加少量代码（或 Studio）的**差异总结**

| 能力      | 只用配置（Variants-only） | 加少量代码/Studio                                 |
| ------- | ------------------- | -------------------------------------------- |
| 初始化速度   | 快                   | 略慢（一次性）                                      |
| 计件/计重互斥 | 依靠人工规范              | 字段/约束自动校验                                    |
| 当班克价更新  | 手改或服务器动作            | 一键动作、留痕                                      |
| 每件重量/证书 | **不支持结构化**（仅描述）     | 给 `product.product` 加字段可导入/报表；**最佳仍是改用 lot** |
| POS 定价  | 固定价/手改；计重=kg价×kg数量  | 同左，但可加更多自动化（比如输入克价自动换算 kg 价）                 |
| 监管/追溯   | 弱（缺一物一证）            | 仍弱；**要强追溯需切换 lot**                           |

> 你的前提是 **Product Template + Variants**，我们就按此落地；将来若要**一物一证**与“按净重精算”，推荐把“每件差异”（重量/证书/工费）迁到 **lot**，并可启用我给你的 `pos_gold_pricing` 自动定价模块。

---

## 8) 我可以直接给你的东西

* 一份**可导入的 CSV 模板包**（分类/属性/模板/变体），按你字段命名；
* 两个**服务器动作**：

  1. 批量设为计重（UoM=kg、to\_weight=1）并把克价×1000写入 `list_price`；
  2. 批量设为计件（UoM=件、to\_weight=0）。
* （可选）一个**极轻量模块/Studio**：加 `pricing_mode` 字段+约束，避免计件/计重混用，附“当班克价更新”按钮。

如果你愿意，发我一小段你们的**示例数据（10 行）**，我立刻替你生成四张 CSV，并给出两条服务器动作的可复制代码（含“当班克价”参数输入）。







  
  

# #############################################################################################################


下面给你一份 **Odoo 18 批量导入的实操手册**，严格按照你要的顺序做：
**`pos.category` → `product.attribute`/`product.attribute.value` → `product.template` → `product.product`**。
每一步都包含：进入哪个列表、CSV 必备列、示例、映射与常见坑。

> 预备：先**启用开发者模式**（右上角 → 关于 → 启用开发者模式），这样导入时能看到字段技术名和外部 ID。

---

# 0) 通用导入规则（强烈建议看一遍）

* **外部 ID（external id）**：在 CSV 里用列名 `id` 自定义一个稳定唯一的字符串（如 `pc_gold`、`pt_ringA`）。
  之后在别的 CSV 里，用 `xxx/id` 来引用它（比如 `parent_id/id`, `product_tmpl_id/id`）。
* **多对多/多选字段**：用列名 `field_name/id`，多个值用逗号分隔并用引号包住：
  例：`"pc_gold,pc_gold_ring"`
* **多对一（Many2one）字段**：也用 `field_name/id`，值就是对方的外部 ID，只有一个。
* **布尔**：`1/0` 或 `True/False` 均可（建议 `1/0`）。
* **数值**：十进制点 `.`；编码 **UTF-8**；首行是表头；无合并单元格。
* **测试导入**：在向导中先点 **“测试”**（Test）再 **“导入”**（Import）。
* **多公司**：有多公司时，建议在 CSV 加 `company_id/id`（如 `base.main_company`），确保数据落到正确公司。

---

# 1) 导入 POS 分类（`pos.category`）

**路径**：POS → 配置 → 产品分类（或 Products → Product Categories）→ 列表视图 → **导入**
**CSV 必备列**：`id`, `name`, `parent_id/id`（可空）
**示例**：

```csv
id,name,parent_id/id
pc_gold,黄金,
pc_gold_ring,戒指,pc_gold
pc_k,K金,
pc_k_ring,戒指,pc_k
```

**常见坑**

* 父分类必须已存在或**同一批 CSV 的更早行**里定义。
* 不要和后台会计分类 `product.category` 混淆；这里是 `pos.category`。

---

# 2) 导入产品属性与取值

> 目的：定义“戒指号”等变体属性；“成色/工艺/主石”等只做描述可设为 **不生成变体**。

## 2.1 属性（`product.attribute`）

**路径**：销售/库存 → 配置 → 产品属性 → 列表 → 导入
**CSV 列**：`id`, `name`, `create_variant`（可选：`always`=生成变体；`no_variant`=不生成变体）
**示例**：

```csv
id,name,create_variant
attr_ring_size,戒指号,always
attr_fineness,成色,no_variant
attr_process,工艺,no_variant
attr_mainstone,主石,no_variant
```

## 2.2 属性值（`product.attribute.value`）

**路径**：同上进入“属性值”列表（或在开发者模式下搜索模型）→ 导入
**CSV 列**：`id`, `name`, `attribute_id/id`
**示例**：

```csv
id,name,attribute_id/id
v_size_15,15,attr_ring_size
v_size_16,16,attr_ring_size
v_fineness_au9999,Au 999.9,attr_fineness
v_fineness_18k,18K,attr_fineness
v_proc_3d,3D,attr_process
v_proc_hard,硬金,attr_process
v_stone_none,无,attr_mainstone
v_stone_diamond,钻石,attr_mainstone
```

**常见坑**

* 先导入属性，再导入属性值；`attribute_id/id` 必须指向已存在的属性外部 ID。
* “是否生成变体”是**属性级**的（`create_variant`），不是值级。

---

# 3) 导入产品模板（`product.template`）

**路径**：销售/库存 → 产品 → 产品（这是**模板**列表）→ 导入
**关键字段含义**

* **是否在 POS 可售**：`available_in_pos`（1/0）
* **计件/计重（互斥）**：

  * 计件：`uom_id/id = uom.product_uom_unit`，`to_weight = 0`
  * 计重：`uom_id/id = uom.product_uom_kgm`（kg），`to_weight = 1`（POS 称重或手输重量；单价为“元/kg”）
* **类型**：`type` = `product`（库存商品）/ `consu`（消耗）/ `service`（服务）
* **POS 分类**（多选）：`pos_categ_ids/id`

**CSV 列（最小集合）**
`id, name, default_code, barcode, available_in_pos, type, uom_id/id, to_weight, pos_categ_ids/id, list_price, standard_price`

**计件示例**

```csv
id,name,default_code,barcode,available_in_pos,type,uom_id/id,to_weight,pos_categ_ids/id,list_price,standard_price
pt_ringA,黄金戒指A,GR-A,690000000001,1,product,uom.product_uom_unit,0,"pc_gold,pc_gold_ring",2988,1500
```

**计重示例（克价=680 元/克 ⇒ list\_price=680000 元/kg）**

```csv
id,name,default_code,barcode,available_in_pos,type,uom_id/id,to_weight,pos_categ_ids/id,list_price,standard_price
pt_gold_bulk,足金散件,AU-BULK,690000000100,1,product,uom.product_uom_kgm,1,"pc_gold",680000,0
```

**常见坑**

* `uom_id/id` 建议用**XML 外部 ID**（如 `uom.product_uom_unit`、`uom.product_uom_kgm`）；若你库自定义过单位，请在单位表“查看元数据”确认 XML ID。
* `pos_categ_ids/id` 多值要用引号包住并用逗号分隔外部 ID。
* 条码必须全局唯一（模板或变体），重复会被拒。

---

# 3A) （可选）导入“模板的属性行”以自动生成变体

> 如果你想**不写 `product.product`**，而是通过模板的“属性行”批量指定允许的值，并让 Odoo 自动生成变体，可导入 `product.template.attribute.line`。

**路径**：开发者模式 → 在“模型”里搜索 `product.template.attribute.line` → 打开其列表 → 导入
**CSV 列**：`product_tmpl_id/id`, `attribute_id/id`, `value_ids/id`
**示例**：

```csv
product_tmpl_id/id,attribute_id/id,value_ids/id
pt_ringA,attr_ring_size,"v_size_15,v_size_16"
pt_ringA,attr_fineness,"v_fineness_au9999"
pt_ringA,attr_process,"v_proc_3d"
```

**导入后**：打开任一受影响的模板检查“属性与变体”，Odoo 会生成对应 SKU（如未生成，可点保存/更新变体）。
**注意**：把“仅描述”的属性（成色/工艺/主石）设为 `no_variant` 时，它仍可出现在此处作为描述值，不会生成 SKU。

---

# 4) 直接导入产品变体（`product.product`）（另一种做法）

> 如果你有明确的 SKU 清单（每条组合是哪几个属性值），直接导入变体更直观。

**路径**：销售/库存 → 产品 → 产品变体 → 导入
**CSV 列**：`id, product_tmpl_id/id, attribute_value_ids/id, default_code, barcode, list_price, standard_price`

* `attribute_value_ids/id`：填写**属性值**外部 ID（第 2 步导入的），多值用逗号分隔。
  **示例**：

```csv
id,product_tmpl_id/id,attribute_value_ids/id,default_code,barcode,list_price,standard_price
pp_ringA_15,pt_ringA,"v_size_15,v_fineness_au9999,v_proc_3d",GR-A-15,690000000015,2988,1500
pp_ringA_16,pt_ringA,"v_size_16,v_fineness_au9999,v_proc_3d",GR-A-16,690000000016,2988,1500
```

**常见坑**

* 变体的属性值集合必须与模板定义的属性相容，否则导入后会出现“孤儿属性值”或冲突。
* 条码仍需唯一。

---

# 5) 导入后的校验与发布

1. **抽样检查**：随机打开 5–10 个模板与变体，确认：

   * 模板勾了 **Available in POS**、计量单位/称重设置正确；
   * POS 分类已挂；
   * 变体条码/价格正确。
2. **POS 前台**：**关闭并重新打开会话**（或点“同步/刷新”）让商品下发缓存。
3. **报表/库存**：做一次**试算盘点**或测试收银单，确认计件/计重的金额逻辑符合预期。

---

# 6) 常见错误 & 快速处理

* **External ID not found**：你引用了一个还没导入的外部 ID → 检查导入顺序或拼写。
* **Many2many 列未识别**：列名必须 `field_name/id`，多值用引号包住，例如 `"pc_gold,pc_gold_ring"`。
* **条码重复**：在模板或变体层面，条码必须全局唯一。
* **单位 XML ID 错**：标准是 `uom.product_uom_unit`（件）、`uom.product_uom_kgm`（kg）；若你库不同，请在单位页面“查看元数据”获取真实 XML ID。
* **POS 不显示**：没勾 `available_in_pos`、没挂 `pos.category`、或 POS 缓存未刷新。

---

# 7) 计重日常运维（可选但实用）

* **当班克价**：

  * 不写代码的做法：使用**服务器动作**批量把 `list_price`（元/kg）更新为“克价×1000”。
  * 例（模型 `product.template`，批量把所有计重商品更新价）：

    ```python
    pts = records or env['product.template'].search([('to_weight','=',True)])
    gram_price = float(env.context.get('gram_price', 680))
    pts.write({'uom_id': env.ref('uom.product_uom_kgm').id,
               'list_price': gram_price * 1000})
    log(f"已更新 {len(pts)} 条：{gram_price} 元/克（{gram_price*1000} 元/kg）。")
    ```
* **变体维护**：新增戒指号时，要么给模板加一条新的属性值（自动生成 SKU），要么直接导入 `product.product` 一条对应变体。

---

如果你把 **你们的 10 行样例数据**（大类/类别/模板/戒指号等）给我，我可以按这个流程直接生成四张 CSV 模板（含正确的列名与外部 ID 填写示例），你只要导入并点“测试 → 导入”就能完成初始化。






  
  

# #############################################################################################################

# #############################################################################################################

太可以了。黄金零售最稳的做法就是把 **Products（模板）+ Product Variants（变体）+ Lots/Serials（批次/序列号）** 三层一起用，各司其职：

* **Template** 管“能不能卖、卖到哪、按件还是按重”等“款式层”策略；
* **Variant** 只承载“必须独立库存的离散规格”（如戒指号）；
* **Lot/Serial** 承载“一物一证”的**每件差异**（净金重、证书、工费、工艺…）并驱动定价与追溯。

下面给你**详细设计** + **可落地实施路径**（含初始化顺序、CSV 模板要点、POS 流程、定价、入库/盘点/报表、校验与自动化）。

---

# 一、数据建模：字段放哪一层最合适？

| 业务字段                      | 放置层级                                    | 说明/理由                                        |
| ------------------------- | --------------------------------------- | -------------------------------------------- |
| 一码一物/一码多件                 | **Template** `tracking=serial/lot/none` | 黄金零售建议 `serial`（一物一证），配件可 `none`             |
| 计件/计重（互斥）                 | **Template** `uom_id` + `to_weight`     | 计件：单位=件、`to_weight=0`；计重：单位=kg、`to_weight=1` |
| 产品ID/条码/名称                | **Variant**（也可模板）                       | 扫码通常扫 **变体** 或 **序列号**                       |
| 大类/类别（黄金/K金/镶嵌/玉石；戒指/手镯…） | **POS 分类** `pos.category`（多级）           | 控制 POS 左侧分类/网格分组                             |
| 成色（18K/9999…）             | Template 默认值 + **Lot 可覆盖**              | 成色影响计价，模板给默认，个别件差异放 Lot                      |
| 主石/颜色/净度、规格、工艺（硬金/3D/…）   | **Lot**（亦可模板“仅描述”）                      | 每件不同，放 Lot 做追溯与定价说明                          |
| 净金重、总重、石重、配件重             | **Lot**                                 | 连续值、每件不同，计价与合规核心                             |
| 证书号（标签绑定）                 | **Lot**                                 | 一物一证                                         |
| 销售工费、工费类型（克/件）            | **Lot**（模板可给默认）                         | 单件往往不同                                       |
| 成本、标价、批发价                 | Template/Variant + Pricelist            | 会计成本走库存估价；批发走价目表                             |
| 性质（正品/特价/赠品…）、备注          | Template 或 Lot                          | 报表分组/说明用                                     |

> 原则：**离散且需要独立库存**→ 变体；**每件差异 & 连续值**→ Lot；**策略/可售/前台显示**→ 模板。

---

# 二、定价策略（两种可选，任选其一或并行）

### A. **Lot 驱动的自动定价（推荐）**

* 公式：**净金重 × 当日金价 × 成色系数 + 工费（克/件）**
* 实现：安装我给你的模块 **`pos_gold_pricing`**（你已拿到 ZIP），包含：

  * `stock.production.lot` 扩展字段（净金重/工费/工艺/证书/成色…）
  * `metal.pricelist` 维护每日金价与成色系数（按公司/日期取最近有效）
  * POS 前端补丁：**选中序列号**后自动 RPC 计算并写入行价
* 优点：一致、可审计、自动化强；**适合所有门店**。

### B. **计重商品（kg）+ 当班克价（简化方案）**

* 模板设 `to_weight=1`、单位=kg，`list_price=克价×1000`（元/kg）
* POS 读秤或手输重量（kg），可手动改单价（经理 PIN 控制）
* 每班用**服务器动作**批量刷新所有计重商品 `list_price=新克价×1000`
* 优点：**无定制也能跑**；缺点：**不读 lot 的净重/证书**，追溯弱。

> 你也可以两者并行：计件类按 A（lot 自动价），散金/基础材料按 B（称重价）。

---

# 三、初始化与批量导入（**三层联合**）

**导入顺序**：`pos.category` → `product.attribute`/`product.attribute.value` → `product.template` → *(可选)* `product.template.attribute.line` → `product.product` → `stock.production.lot` → *(若用 A)* `metal.pricelist`

## 1) POS 分类 `pos.category`

* 列：`id,name,parent_id/id`
* 示例：`pc_gold` 顶层，`pc_gold_ring` 的 `parent_id/id=pc_gold`

## 2) 变体属性（必要的才“生成变体”）

* `product.attribute`：`id,name,create_variant`（`always`/`no_variant`）

  * **戒指号**：`always`（生成变体）
  * **成色/工艺/主石**：`no_variant`（仅描述）
* `product.attribute.value`：`id,name,attribute_id/id`

## 3) 产品模板 `product.template`（**关键**）

最小列：

```
id,name,default_code,barcode,available_in_pos,type,uom_id/id,to_weight,pos_categ_ids/id,list_price,standard_price,tracking
```

* 计件：`uom.product_uom_unit`, `to_weight=0`, `tracking=serial`
* 计重：`uom.product_uom_kgm`, `to_weight=1`（元/kg）
* 多 POS 分类：`"pc_gold,pc_gold_ring"`

## 4) （可选）模板属性行 `product.template.attribute.line`

* 列：`product_tmpl_id/id,attribute_id/id,value_ids/id`
* 功能：批量指定某模板允许的属性值集合，系统**自动生成变体**

## 5) 产品变体 `product.product`

* 列：`id,product_tmpl_id/id,attribute_value_ids/id,default_code,barcode,list_price,standard_price`
* `attribute_value_ids/id` 多值用逗号：`"v_size_15,v_fineness_au9999"`

## 6) 序列号/批次 `stock.production.lot`（**每件一条**）

> 使用 `pos_gold_pricing` 字段名（可根据你的库调整）

最小列建议：

```
name,product_id/id,company_id/id,barcode,
metal_type,net_gold_weight,gross_weight,stone_weight_ct,
wage_type,wage_value,process_technique,certificate_no
```

* `product_id/id` 填 **变体或模板** 的外部 ID（一般填变体更准确）
* 每件一个 `name`（也是序列号），建议打印为**可扫码条码**

## 7) 每日金价 `metal.pricelist`（若用 A）

```
name,company_id/id,metal_type,price_per_g,fineness_factor,effective_date,active
```

* 例：`Au9999`、`price_per_g=克价`、`fineness=1.0`；18K = 0.75 等

> **导入技巧**：所有 `/id` 列都用“外部 ID”；多对多要引号+逗号；导入前先点“测试”。

---

# 四、POS 前台操作体验（融合三层）

1. 左侧按 **pos.category** 分类浏览（或扫码进入）
2. 点商品卡片（**模板**）：

   * 有 **变体**（戒指号等）→ 先弹“变体选择”
   * 模板 `tracking=serial/lot` → 选/扫 **序列号**
3. **定价**：

   * 走 **A**：选了序列号即**自动算价**（取 lot 净重 + 金价 + 工费）
   * 走 **B**：计重商品按秤的 **kg 数量 × 元/kg 单价**（可手改单价）

> 任何后台变更后，**重开/同步 POS 会话** 才会生效。

---

# 五、入库/盘点/退换（管理与追溯）

* **入库**：按 **变体**收货；对 `tracking=serial` 的商品在入库时生成/指定 **序列号**（也可预先批量导入）。
* **盘点/报表**：库存与成本以 **变体** 粒度统计；选定跟踪商品可细化到 **序列号**。
* **退换/RMA**：凭小票序列号直接定位到**具体那一件**（证书、重量、工费全可追溯）。

---

# 六、互斥规则与自动化（强烈建议）

### 1) 计件/计重互斥约束（服务器动作/轻定制）

* **无代码**：靠流程 + 导出抽查（`to_weight` 与 `uom` 是否匹配）。
* **轻定制**：在 `product.template` 增加 `pricing_mode`（`per_piece`/`per_gram`），写约束：

  * `per_piece` ⇒ `uom=件`、`to_weight=0`
  * `per_gram` ⇒ `uom=kg`、`to_weight=1`

### 2) 当班克价一键更新（方案 B 必备）

服务器动作（模型：`product.template`）：

```python
pts = records or env['product.template'].search([('to_weight','=',True)])
gram_price = float(env.context.get('gram_price', 680))   # 在对话框传入
pts.write({
    'uom_id': env.ref('uom.product_uom_kgm').id,
    'list_price': gram_price * 1000,  # 元/kg
})
log(f"已更新 {len(pts)} 条计重商品：{gram_price} 元/克（= {gram_price*1000} 元/kg）。")
```

### 3) 下架前清理 Combo 引用（避免你遇到的报错）

服务器动作（模型：`product.template`），先删组合行再下架：

```python
templates = records or env['product.template'].browse(env.context.get('active_ids') or [])
# 清除 POS Combo 里的引用（不同安装模型名可能略异，按你库调整）
for model_name in ('pos.combo.line','pos.combo.item','pos.combo.product'):
    if model_name in env:
        lines = env[model_name].search([('product_tmpl_id','in',templates.ids)])
        lines.unlink()
templates.write({'available_in_pos': False})
log(f"已移除 Combo 引用并下架 {len(templates)} 个模板。")
```

---

# 七、条码与标签建议

* **变体条码**：唯一，适合直接扫码加行。
* **序列号条码**：唯一，建议在标签上打印（扫码即选中该件）。
* **带价条码**（可选，仅方案 B）：按 **Price** 规则编码，扫入即带最终价（但与 lot 关系变弱）。

---

# 八、上线步骤清单（一步步照做）

1. **配置**：UoM（件/kg）、税、POS 分类树
2. **属性**：戒指号=生成变体；成色/工艺/主石=不生成变体
3. **导入模板**：计件/计重、POS 可售、分类、tracking=serial
4. **生成变体**：模板属性行或直接导入 `product.product`
5. **导入序列号**：每件净重/证书/工费/工艺/成色（Lot）
6. **定价选型**：

   * A：安装 `pos_gold_pricing` → 维护 `metal.pricelist`（金价/成色系数）
   * B：建“当班克价”服务器动作，每日刷新 `list_price`（元/kg）
7. **POS 配置**：启用 **Lots/Serials**、（可选）IoT 秤、改价权限
8. **前台联测**：模板→变体→序列号→自动/称重定价→结账→拣货记录 serial
9. **培训与 SOP**：收银（选/扫序列号）、入库（指定序列号）、退换（查一物一证）、日价更新

---

## 结论

* **三层联合**（Template + Variant + Lot）是黄金零售的“长期稳态”方案：
  既保证 **POS 体验**、**库存效率**，又满足 **一物一证追溯** 与 **可审计定价**。
* 你可先按此方案完成初始化；若要**自动定价**，直接启用 `pos_gold_pricing`；若短期用称重/当班价，也能无缝兼容。
* 需要我把四/五张 **CSV 空模板**（分类/属性/模板/模板属性行/变体/lot/金价）按你的字段中文名生成出来吗？发我 5–10 条样例行，我就给你可直接导入的模板。

  
  

# #############################################################################################################

# 实操

下面是一份**可直接照做**的 Odoo 18「黄金类商品初始化 & 批量导入」实操手册。流程严格按你要的顺序组织，并区分了“必做/可选”，每一步都有：菜单路径 → 要导入的 CSV → 操作要点 → 验证 → 常见报错与解决。

> 你可以直接用我给你的模板包：
> **[下载 CSV 打包](sandbox:/mnt/data/odoo18_gold_init_templates.zip)**
> 单文件：pos\_category / product\_attribute / product\_attribute\_value / product\_template / product\_template\_attribute\_line（可选）/ product\_product（可选）/ stock\_production\_lot / metal\_pricelist（可选）

---

# 0. 预备与原则（一次性）

1. **开启开发者模式**：右上角头像 → 关于 → 启用开发者模式（或 URL 加 `?debug=1`）。
2. **切换到正确公司**：右上角“允许公司”勾选并激活你的目标公司（多公司环境很关键）。
3. **检查单位**：确保有
- 库存->setting

   * 件：`uom.product_uom_unit`
   * 公斤：`uom.product_uom_kgm`
     如果你用的是自定义单位，导入时 `uom_id/id` 填对应的 XML ID。
	 
- 实际：
uom.product_uom_unit
uom.product_uom_gram
4. **POS 基础设置**（稍后也可以再开）：

   * 启用 **Lots/Serials（批次/序列号）**（跟踪一物一证会用到）
   * 有秤则启用 **IoT Scale**；允许**改价/折扣**（可配经理 PIN）

> **导入小规则（务必遵守）**
>
> * CSV 编码：UTF-8，十进制点 `.`。
> * 布尔：`1/0`。
> * 多对一/多对多引用都用 `字段名/id`，值填**外部 ID**。多值用**英文逗号**分隔并用引号包起来：`"pc_gold,pc_gold_ring"`。
> * 每次导入向导，先点 **“测试”**，无错误再 **“导入”**。
> * 条码必须全局唯一（模板或变体任一层）。

---

# 1. 导入 POS 分类（`pos.category`）— 必做

**菜单**：POS → 配置 → 产品分类（或 Products → Product Categories）→ 列表 → **导入**

**CSV**：`pos_category.csv`
必备列：`id`, `name`, `parent_id/id`（根类留空）

**操作**：上传 → 字段自动映射 → **测试** → **导入**。

**验证**：分类树中能看到“黄金/戒指”“K金/戒指”等层级。

**常见报错**

* *外部 ID 未找到*：父类的 `parent_id/id` 写错或父类未先导入 → 修正顺序或拼写。
* 写成了 `product.category`（会计分类） → 走错菜单了，退回。

---

# 2. 导入产品属性与取值 — 必做

> 原则：**戒指号**等“必须独立库存”的维度 → 设为**生成变体**；**成色/工艺/主石**等仅用于描述/检索 → 设为**不生成变体**。

## 2.1 属性（`product.attribute`）

**菜单**：销售/库存 → 配置 → 产品 → 属性 → 列表 → **导入**

**CSV**：`product_attribute.csv`
列：`id, name, create_variant`（`always`=生成变体；`no_variant`=不生成变体）

**验证**：打开任一属性，确认“生成策略”正确。

**报错**：值非法 → 统一用 `always` / `no_variant`。

## 2.2 属性值（`product.attribute.value`）

**菜单**：属性值列表（同上模块内）→ **导入**

**CSV**：`product_attribute_value.csv`
列：`id, name, attribute_id/id`

**验证**：属性页签能看到对应的值集合。

**报错**：`attribute_id/id` 不存在 → 先导入属性或修正外部ID。

---

# 3. 导入产品模板（`product.template`）— 必做

**菜单**：销售/库存 → 产品 → **产品**（这是模板列表）→ **导入**

**CSV**：`product_template.csv`
常用列（示例已填好）：

* 基础：`id, name, default_code, barcode, available_in_pos, type`
* 计件/计重互斥：

  * 计件 → `uom_id/id = uom.product_uom_unit`, `to_weight=0`
  * 计重 → `uom_id/id = uom.product_uom_kgm`, `to_weight=1`（POS 读秤/手输 **kg** 数量；`list_price` 写 **元/kg**）
* POS 分类（多选）：`pos_categ_ids/id`（`"pc_gold,pc_gold_ring"`）
* 价格成本：`list_price`, `standard_price`
* 跟踪：`tracking`（建议 `serial` 一物一证）

**测试 → 导入**。

**验证**：打开某模板：

* “在 POS 可售”已勾；
* POS 分类已挂；
* 单位/是否称重正确；
* 跟踪方式如期（`serial`）。

**常见报错**

* 单位 XML ID 不识别 → 替换为你库里的 XML ID（在单位页面“查看元数据”可见）。
* POS 分类外部 ID 拼写错 → 对照第 1 步 CSV 修正。

---

# 4. 生成变体：两条路二选一（**只选其中一种**，避免重复）

### 4A. 通过模板属性行“自动生成变体” — 常用

**用途**：你只想声明“这款允许哪些戒指号/成色/工艺”，让 Odoo 自动生成 SKU。

**菜单**：设置 → 技术 → 数据库结构 → 模型 → 搜索 `product.template.attribute.line` → **查看记录** → 列表 → **导入**

**CSV**：`product_template_attribute_line.csv`
列：`product_tmpl_id/id, attribute_id/id, value_ids/id`（多值用引号+逗号）

**导入后**：回到模板表单点 **保存**（或刷新），系统自动生成变体。

**验证**：销售/库存 → 产品 → **产品变体**，能看到对应 SKU；模板上“变体数量”>0。

**常见报错**：属性未导/值未导 → 回第 2 步确认外部ID。

---

### 4B. 直接导入变体（`product.product`）— 你已有明确 SKU 清单时用

**菜单**：销售/库存 → 产品 → **产品变体** → **导入**

**CSV**：`product_product.csv`
列：`id, product_tmpl_id/id, attribute_value_ids/id, default_code, barcode, list_price, standard_price`

> `attribute_value_ids/id` 可多值（如“号+成色+工艺”），用引号+逗号。

**验证**：SKU 条数/条码/价一致；模板“变体数量”同步增加。

**常见报错**：

* 属性值与模板不相容 → 先确保模板允许这些属性值（可用 4A 先声明属性行）。
* 条码重复 → 改成唯一。

---

# 5. 导入序列号/批次（`stock.production.lot`）— 一物一证（**强烈建议**）

**菜单**：库存 → 产品 → **序列号/批次** → 列表 → **导入**

**CSV**：`stock_production_lot.csv`
常用列（随你模块字段而定）：

* 标准：`name`（序列号/唯一码）, `product_id/id`（建议指向**变体**外部ID）, `company_id/id`, `barcode`
* 黄金扩展（来自 `pos_gold_pricing` 模块）：`metal_type, net_gold_weight, gross_weight, stone_weight_ct, wage_type, wage_value, process_technique, certificate_no`

**测试 → 导入**。

**验证**：打开变体 → 智能按钮“序列号”能看到刚导入的每件数据；POS 配置已启用 Lots/Serials。

**常见报错**：

* `product_id/id` 指到了模板但你实操要按变体追溯 → 改填变体外部 ID；
* 数值小数点/编码问题 → CSV 保证 UTF-8，数字用`.`小数点。

---

# 6.（可选）导入“每日金价”（`metal.pricelist`，用于自动定价）

> 仅当你装了 **pos\_gold\_pricing**（或等价定制）时需要。

**菜单**：POS → Metal Pricing → Daily Metal Prices → 列表 → **导入**

**CSV**：`metal_pricelist.csv`
列：`name, company_id/id, metal_type, price_per_g, fineness_factor, effective_date, active`

**验证**：列表按日期显示最新一条；不同金种/公司取值正确。
**注意**：POS 中选择序列号时将用此处**最近有效**金价参与“净重×金价×系数+工费”的计算。

---

# 7. POS 刷新与联测（必做）

1. **POS 配置**检查：启用 **Lots/Serials**；（计重商品）启用秤并在模板上勾 **To Weigh**。
2. **重开/同步 会话**，让前台缓存刷新。
3. **联测用例**：

   * 点“黄金戒指A（模板卡片）”→ 选择“戒指号（变体）”→ 选择/扫码“序列号（每件）”。
   * 方案 A（自动定价）：价应由序列号的净重 + 当日金价 + 工费计算并落单。
   * 方案 B（称重价）：计重商品读秤（kg 数量）× 元/kg 单价（可手改）。

---

# 8. 日常维护（建议）

* **当班克价更新（方案 B）**：

  * 做一个“服务器动作”：批量把所有 `to_weight=1` 的模板 `list_price=克价×1000`。
* **批量上下架**（你已创建的 Server Actions）：

  * “批量设为 POS 可售/取消 POS 可售”挂到产品模板列表的【动作】菜单。
* **Combo 约束**：下架前若报“请先从 XX 组合移除”，先去 POS → Products → **Combos/Combo Choices** 中把组件移除，再执行下架动作。

---

# 9. 常见错误速查表

* **External ID not found**：上一环节的外部 ID 未导或拼写错 → 回去修正 CSV。
* **Many2many 未识别**：列名须 `xxx/id`；多值需用引号包起来：`"a,b"`。
* **条码重复**：在模板/变体层全局唯一。
* **单位 ID 不存在**：换成你库里的单位 XML ID（开发者模式 → 查看元数据）。
* **POS 前台看不到**：没勾 `available_in_pos`、没挂 `pos.category`、或会话没刷新。
* **多公司看不到**：右上角没切到该公司。
* **“动作”菜单只有导出**：不在**列表视图**或未勾选任何记录；或动作绑定没挂到 `product.template` 的 List 视图。

---

## 10. 建议的“首批上线清单”

1. 先在**测试库**跑全流程（导入→联测）。
2. 生产库按本文顺序导入，每步都“测试→导入”，每导完一类立刻抽查 5–10 条。
3. 导入完成 → 重开 POS 会话 → 门店联测 10 单（计件/计重各 5 单）。
4. 正式开放收银。

---

需要我把模板里的示例值换成你们真实“款号/条码/号数/净重/工费”的 10 行样例并回生成一份**投产版 ZIP**吗？给我样例数据就行，我这边直接把 CSV 调整好。







  
  

# #############################################################################################################

# 单位的设置

下面给你一套**可直接照做**的步骤，教你在 Odoo 18 里**检查/确认“件(Units)”与“公斤(kg)”两个计量单位**是否存在、外部ID是否可用；如果缺失，如何**新建/启用**并（可选）**补上外部ID**，以便你在 CSV 导入中用到：

---

## A. 打开“计量单位（UoM）”列表并检查是否存在

1. **启用开发者模式**
   右上角头像 → 关于 → **启用开发者模式**（或 URL 加 `?debug=1`）。

2. **进入单位列表**
   应用 **库存(Inventory)** → 配置( Configuration ) → **单位(Units of Measure)**。
   小贴士：如果左侧没有“Units of Measure”，去“库存 → 设置 → 产品 → 勾选 Units of Measure”。

3. **取消过滤器，显示所有**
   在列表右上角清掉“活动/归档”过滤器，确保能看到被归档的记录。

4. **搜索两条记录**

   * 搜索 **Unit(s)** 或 **件**（根据语言），打开它；
   * 搜索 **Kilogram** / **kg** / **公斤**，打开它。

5. **逐条核对关键字段**

   * **Unit(s)**（件）：

     * *类型(Type)*：Reference Unit（基准单位）
     * *类别(Category)*：Units（单位类，中文机构可能叫“单位”）
     * *精度(Rounding Precision)*：**1.0000**（整数件）
     * *Active*：勾选
   * **Kilogram (kg)**（公斤）：

     * *类型(Type)*：Reference Unit（基准单位）
     * *类别(Category)*：Weight（重量类/质量）
     * *精度(Rounding Precision)*：建议 **0.000001 kg**（= 0.001 g，满足黄金行业毫克级别需要；若只要 0.01 g，可填 0.00001）
     * *Active*：勾选

> 只要以上两条存在且“Active”，就可以在产品模板里直接用。

---

## B. 查看或确认“外部ID（XML ID）”，用于 CSV 中 `/id` 引用

> 我们的 CSV 模板使用了：
>
> * **件**：`uom.product_uom_unit`
> * **公斤**：`uom.product_uom_kgm`

1. 在打开的 Unit(s) 或 Kilogram 表单界面，右上角 **虫子图标(调试菜单)** → **查看元数据(View Metadata)**。
2. 在弹窗中查看 **External ID**：

   * Unit(s) 通常是 **`uom.product_uom_unit`**
   * Kilogram 通常是 **`uom.product_uom_kgm`**
3. 若能看到这两个 External ID，就可以在 CSV 中用 `uom_id/id = uom.product_uom_unit` 和 `uom.product_uom_kgm` 进行导入 **（最佳做法）**。

---

## C. 遇到的三种“缺失”情况以及修复

### 情况 1：单位存在但被“归档”

* 在列表中取消“Active”过滤，打开该单位 → 点击 **复原/Unarchive**。
* 重新检查外部ID（B 步骤）。

### 情况 2：单位缺失（少见）

1. 点击 **新建** 分别创建两条：

   * **Unit(s)**（件）

     * Name：Unit(s)（或件）
     * Type：**Reference Unit**
     * Category：**Units**（若无此分类，先新建类别“Units”）
     * Rounding Precision：**1.0000**
     * Active：勾
   * **Kilogram (kg)**（公斤）

     * Name：Kilogram
     * Type：**Reference Unit**
     * Category：**Weight**（若无，先建类别“Weight”）
     * Rounding Precision：**0.000001**（黄金建议）
     * Active：勾

2. **（可选）给新建单位补外部ID**

   * 菜单：设置( Settings ) → 技术( Technical ) → **数据库结构(Database Structure)** → **外部标识符(External Identifiers)**。
   * 新建两条：

     * **Model**：`uom.uom`
     * **Record**：选择你刚建的 Unit(s)/Kilogram
     * **External ID**：

       * 若你要沿用我提供的 CSV，**必须**分别填入：

         * `uom.product_uom_unit`
         * `uom.product_uom_kgm`
       * 或者你也可以自定义，比如 `x_uom.product_uom_unit`；**但要同时修改你的 CSV**（把 `/id` 的值改成这个新的外部ID）。
   * 保存后回到 B 步骤再核对一次。

> 注：给已有记录**新建外部ID**是合法的。为避免与官方模块将来升级冲突，更稳妥是用你自己的“模块名前缀”（如 `x_uom.`），并同步修改 CSV。

### 情况 3：你不想用外部ID引用（应急）

* 在导入向导里，把 `uom_id/id` **改成** `uom_id`（不带 `/id`），并把 CSV 里对应列的值换成**单位名称**（如 `Unit(s)` 或 `Kilogram`）。
* 前提：名称**唯一**且与你系统语言一致；否则会匹配失败。**不推荐长期用**，稳定性不如外部ID。

---

## D. 黄金行业的“精度/四舍五入”建议

* **Kilogram 精度**：

  * 推荐 **0.000001 kg**（= 0.001 g，毫克级别），确保称重/计价有足够精度。
  * 若称重设备只到 0.01 g，可设 0.00001 kg。
* **计件 Unit(s) 精度**：1.0000（按件销售，不允许小数）。
* 修改精度后，**重新打开**相关产品以刷新前端缓存；**POS 会话重开/同步**让设置生效。

---

## E. 快速自检小抄

* [ ] “Unit(s)”存在，Type=Reference，Category=Units，Rounding=1.0000，Active；External ID= `uom.product_uom_unit`
* [ ] “Kilogram (kg)”存在，Type=Reference，Category=Weight，Rounding=0.000001，Active；External ID= `uom.product_uom_kgm`
* [ ] CSV 中 `uom_id/id` 正确引用对应 External ID
* [ ] POS 会话**重开/同步**后，计件/计重商品能正常下单/称重/改价

---

如果你愿意，我可以把你当前库里这两条 UoM 的 **External ID** 名称确认一下（你发一张“查看元数据”的截图给我），或者我给你准备两条**服务器动作/odoo shell**脚本：自动创建/修正 UoM 并补外部ID，避免手工点错。


# #################################################################################################################################################

# #################################################################################################################################################


下面给你一套\*\*“只用 Products（模板）+ Product Variants（变体），不使用 lot/serial”\*\* 的黄金类 POS 建模与落地方案。你的前提是**重量基本单位为 g（克）**，因此我们把 **产品 UoM 设为 g**，POS 的秤读 **kg** 也能自动换算（同一类别内按换算系数转换即可）。

---

# 一、总体设计（不用 lot 的取舍）

* **模板（product.template）**：决定是否在 POS 可售、计量单位（g/件）、是否称重（to\_weight）、税、POS 分类、基础价、跟踪（这里选 *不跟踪*）。
* **变体（product.product）**：只承载**必须独立库存**的离散规格（如戒指号/尺寸/款式变体等），并保存条码。
* **不使用 lot** 的影响：不做“一物一证”追溯；每件的**净重/证书**不会逐件保存，计价以\*\*称重数量（g）× 单价（元/克）\*\*为准。

> 适用场景：门店只需**按克销售 + 固定件价**的效率优先方案；不做逐件追溯（监管或售后需要一物一证时再考虑切换 lot）。

---

# 二、计量与精度（以 g 为基准）

1. **UoM 类别：Weight**

   * **参考单位（Reference）**：**Gram (g)**（基准 = 1）
   * **Kilogram (kg)**：Type = Bigger than reference，**Ratio = 1000**（1 kg = 1000 g）
   * **Rounding Precision**：g 的精度建议 **0.001 g**（即 0.001 的整数倍，对应 kg 的精度为 0.000001）。
2. **件数类别：Units**

   * 参考单位：Unit(s)（件），Rounding = 1.0000。

> POS 的秤通常回传 **kg**，Odoo 会把 **kg 自动换算成 g** 后参与金额计算（同一类别下自动换算）。

---

# 三、属性与变体设计

* **生成变体（Generate variants）**：只给必须独立库存的维度（如**戒指号**）。
* **不生成变体（No variant）**：成色/工艺/主石等仅用于描述/筛选的维度，不产生 SKU。
* **条码**：放在变体层（扫码即落到该 SKU），也可用模板条码（但不推荐）。

---

# 四、价格与计价策略（无 lot）

### 1) 计件（固定价）

* 模板 UoM = **件**，`to_weight = 0`，`list_price` = **单件价（元/件）**。

### 2) 计重（按克）

* 模板 UoM = **g**，`to_weight = 1`（启用称重/手输重量），`list_price` = **元/克**。
* 前台流程：秤读 **kg** → 自动换算为 **g 数量** → 金额 = **数量（g） × 单价（元/克）**。
* **当班克价**：

  * 简单做法：班前**批量把所有计重商品的 `list_price` 改为当班克价（元/克）**。
  * 方式：后台手改 / 导入 / 或用下文“服务器动作”一键更新。

> 可选：启用**改价需经理 PIN**，在 POS 允许收银员临时修改单价（防错）。

---

# 五、落地实施步骤（一步步操作）

## 步骤 1｜计量单位（已设 g 为基准时可略过）

* Inventory → Configuration → Units of Measure

  * 确认 **Gram** Type=Reference，Ratio=1，Rounding=0.001（或更细）；
  * **Kilogram** Type=Bigger than reference，**Ratio=1000**，Rounding=0.000001。
* Developer mode → View Metadata 查看 External ID（用于导入）：

  * g：`uom.product_uom_gram`
  * kg：`uom.product_uom_kgm`
  * 件：`uom.product_uom_unit`

## 步骤 2｜POS 分类（前台左侧树）

* POS → Configuration → Product Categories
* 维护两级树（如：黄金/戒指、K金/戒指…）。
* 导入时字段：`id,name,parent_id/id`（外部ID 互相引用）。

## 步骤 3｜属性与取值

* Sales/Inventory → Configuration → Products → Attributes

  * **戒指号**：Create variants=**always**；取值如 15/16/17……
  * **成色/工艺/主石**：Create variants=**no\_variant**；仅描述。
* 导入字段：

  * `product.attribute`: `id,name,create_variant`
  * `product.attribute.value`: `id,name,attribute_id/id`

## 步骤 4｜产品模板（product.template）

* Sales/Inventory → Products → **Products（模板）**
* 填写关键字段：

  * `available_in_pos=1`（POS 可售）
  * **计件**：`uom_id/id = uom.product_uom_unit`，`to_weight=0`，`list_price=元/件`
  * **计重**：`uom_id/id = uom.product_uom_gram`，`to_weight=1`，`list_price=元/克`
  * `pos_categ_ids/id`（多选，挂到 POS 分类）
  * `type=product`；**跟踪（tracking）= none**（不使用 lot）
* 按需在“属性与变体”页签添加：

  * 戒指号（生成变体）、成色/工艺/主石（不生成）。

## 步骤 5｜变体（两种方式二选一）

* **方式 A（推荐）**：在模板“属性与变体”里选好允许的值，**保存后自动生成**变体。
* **方式 B（CSV 导入）**：到 Products → **Product Variants** 直接导入 `product.product`：

  * `product_tmpl_id/id` 指向模板外部ID
  * `attribute_value_ids/id` 写属性值外部ID（多值用引号+逗号）
  * `default_code`、`barcode`、必要时 `list_price`

## 步骤 6｜POS 配置

* POS → Configuration → **Point of Sale**（每个店铺）：

  * **IoT Scale/称重**（有秤就开）；
  * **Price control**（允许改价/折扣；可配经理 PIN）；
  * *（不勾 Lots/Serials，因为本方案不用 lot）。*
* 保存后**重开/同步**会话。

## 步骤 7｜导入（CSV 列示例）

> **导入顺序**：`pos.category` → `product.attribute` → `product.attribute.value` → `product.template` → `product.template.attribute.line(可选)` → `product.product(可选)`

**A. pos.category**

```
id,name,parent_id/id
pc_gold,黄金,
pc_gold_ring,戒指,pc_gold
```

**B. product.attribute**

```
id,name,create_variant
attr_ring_size,戒指号,always
attr_fineness,成色,no_variant
attr_process,工艺,no_variant
attr_mainstone,主石,no_variant
```

**C. product.attribute.value**

```
id,name,attribute_id/id
v_size_15,15,attr_ring_size
v_size_16,16,attr_ring_size
v_fineness_au9999,Au 999.9,attr_fineness
v_proc_3d,3D,attr_process
```

**D. product.template（计件 & 计重）**

```
id,name,default_code,barcode,available_in_pos,type,uom_id/id,to_weight,pos_categ_ids/id,list_price,standard_price,tracking
pt_ringA,黄金戒指A,GR-A,690000000001,1,product,uom.product_uom_unit,0,"pc_gold,pc_gold_ring",2988,1500,none
pt_gold_bulk,足金散件,AU-BULK,690000000100,1,product,uom.product_uom_gram,1,"pc_gold",680,0,none
```

> `pt_gold_bulk.list_price=680` 表示 **680 元/克**。

**E. product.template.attribute.line（可选，自动生成变体）**

```
product_tmpl_id/id,attribute_id/id,value_ids/id
pt_ringA,attr_ring_size,"v_size_15,v_size_16"
pt_ringA,attr_fineness,"v_fineness_au9999"
pt_ringA,attr_process,"v_proc_3d"
```

**F. product.product（直接指定 SKU，二选一与 E）**

```
id,product_tmpl_id/id,attribute_value_ids/id,default_code,barcode,list_price,standard_price
pp_ringA_15,pt_ringA,"v_size_15,v_fineness_au9999,v_proc_3d",GR-A-15,690000000015,2988,1500
```

---

# 六、门店实际操作（POS 前台）

* **计件**：点商品卡片（模板→变体），直接加行，按 `list_price`（元/件）结算。
* **计重**：点计重商品 → 称重（**kg**）或手输重量 → 系统换算成 **g** 数量 → 金额 = g × （元/克）。
* **改价**：需要时手改（可启用经理 PIN）。
* **扫码**：扫**变体**条码（或模板条码）直接加行。

---

# 七、入库/盘点/报表（无 lot）

* **入库/调拨/盘点**：按**变体**与 **g/件** 数量操作。计重商品以 **g** 为库存单位。
* **报表**：按变体与属性（成色/工艺等设为 *no\_variant* 也可在模板层做自定义字段）分组。
* **限制**：无一物一证追溯；证书/单件重量无法逐件留档（若将来需要可增加自定义字段存到变体层，但仍非逐件）。

---

# 八、常用自动化（可选）

> 用“服务器动作（Server Actions）”，挂到“产品模板”列表的【动作】菜单，便于日常操作。

**1) 批量设为计重（g）并更新当班克价**

* **模型**：`product.template`
* **代码**：

```python
pts = records or env['product.template'].search([])
gram_price = float(env.context.get('gram_price', 680))  # 在执行对话框传入
g = env.ref('uom.product_uom_gram')
pts_to_update = pts.filtered(lambda r: r.to_weight or r.uom_id == g)
pts_to_update.write({
    'uom_id': g.id,
    'to_weight': True,
    'list_price': gram_price,  # 元/克
    'tracking': 'none',
})
log(f"已更新 {len(pts_to_update)} 条为计重（g），单价 {gram_price} 元/克。")
```

**2) 批量设为计件（固定价）**

```python
pts = records or env['product.template'].browse(env.context.get('active_ids') or [])
unit = env.ref('uom.product_uom_unit')
pts.write({'uom_id': unit.id, 'to_weight': False, 'tracking': 'none'})
log(f"已设置 {len(pts)} 条为计件商品（元/件）。")
```

> 绑定到产品列表“动作”菜单的方法：在该 Server Action 表单点 **Create Contextual Action**（Odoo 18 可见）。确保 **Model=product.template**。

---

# 九、风险与边界（务必知悉）

* **无逐件追溯**：不使用 lot 就没有“一物一证”（证书号、单件净重）级别记录。
* **重量差异**：同款不同件的重量差只能通过**称重数量**体现，不能存档于商品主数据。
* **合规/售后**：若日后需要逐件证书与回溯，必须引入 **lot/serial** 或定制每件记录的机制。

---

## 结论

* 以上方案完全满足“**不使用 lot，只用模板+变体，按克/按件销售**”的门店收银与库存管理。
* 重点是：**UoM=克、to\_weight=1、list\_price=元/克、秤为 kg、同类换算自动完成**。
* 如果你需要，我可以把**不含 lot 的 CSV 模板**（pos.category / attribute / attribute.value / template / template.attribute.line / product.product）单独打包给你，直接导入即可。


已帮你把\*\*仅用 Products+Variants（不含 lot）\*\*的导入模板打包好了，按“以克(g)为基准”的方案配置：

**一键下载：**

* [odoo18\_variants\_only\_templates.zip](sandbox:/mnt/data/odoo18_variants_only_templates.zip)

**如需单独下载：**

* [pos\_category.csv](sandbox:/mnt/data/odoo18_variants_only_templates/pos_category.csv)
* [product\_attribute.csv](sandbox:/mnt/data/odoo18_variants_only_templates/product_attribute.csv)
* [product\_attribute\_value.csv](sandbox:/mnt/data/odoo18_variants_only_templates/product_attribute_value.csv)
* [product\_template.csv](sandbox:/mnt/data/odoo18_variants_only_templates/product_template.csv)
* [product\_template\_attribute\_line.csv](sandbox:/mnt/data/odoo18_variants_only_templates/product_template_attribute_line.csv)（可选，用于自动生成变体）
* [product\_product.csv](sandbox:/mnt/data/odoo18_variants_only_templates/product_product.csv)（可选，直接指定具体 SKU）
* [README.txt](sandbox:/mnt/data/odoo18_variants_only_templates/README.txt)

### 关键点回顾

* 重量基准单位 = **g**，计重商品：`uom_id/id = uom.product_uom_gram`，`to_weight = 1`，`list_price = 元/克`。
* 计件商品：`uom_id/id = uom.product_uom_unit`，`to_weight = 0`，`list_price = 元/件`。
* **不使用 lot**：`tracking = none`。
* 导入顺序：`pos.category → product.attribute → product.attribute.value → product.template → (template.attribute.line 或 product.product)`
* 导入前开启**开发者模式**，导入向导先点“测试”，成功后再“导入”。
* 导入后**刷新/重开 POS 会话**让前台生效。

需要我把这些 CSV 里的示例值替换成你们的真实“款号/条码/戒指号/价格”等数据吗？发我 5–10 条样例，我立刻生成一份“可直接投产”的版本。


# 详细步骤
没问题！下面把 **每一个 CSV 的导入流程**都细化成「进去哪里 → 怎么上传 → 字段怎么识别与映射 → 如何验证 → 常见报错怎么处理」。
（本手册对应你已下载的 `odoo18_variants_only_templates.zip`；方案为**仅用 Products + Variants、不用 lot**，重量基准单位为 **g**。）

> 预备通用规则（一次性读完很有用）
>
> * 开启**开发者模式**：右上角头像 → 关于 → 启用开发者模式（或 URL 后加 `?debug=1`）。
> * 确认**当前公司**正确（右上角 Allowed Companies/当前公司切换）。
> * CSV 要用 **UTF-8**，小数点用 `.`，不要千分位逗号。
> * 导入向导中，**先点“测试”(Test)**，没有错误再点“导入”(Import)。
> * 列名带 `/id` 的列表示**外部 ID**引用，多个值要用**英文逗号**分隔并**整段加引号**（如 `"pc_gold,pc_gold_ring"`）。
> * **条码全局唯一**（模板或变体层都不能重复）。
> * 导入后，**刷新/重开 POS 会话**让前台生效。

---

# 1) POS 分类 `pos_category.csv`（pos.category）

**去哪里**
POS → Configuration → Product Categories（产品分类）→ 列表右上角 **Import**

**上传并映射**

* 上传 `pos_category.csv`。
* 字段会自动匹配：`id`, `name`, `parent_id/id`。
* `parent_id/id` 若为空表示顶层分类；子分类引用父分类的 **外部ID**。

**验证**

* 导入完成后，列表应出现分层结构（例如：黄金 ▶ 戒指）。
* 在“产品模板”里选择 POS 分类时能看到这些分类。

**常见报错 & 处理**

* “External ID not found” → `parent_id/id` 拼写错或父类未先导 → 修正 CSV 或先建父类。
* 误把 `product.category` 当成了 `pos.category` → 走错菜单，回到 POS 分类再导。

---

# 2) 产品属性 `product_attribute.csv`（product.attribute）

**去哪里**
Sales 或 Inventory → Configuration → Products → Attributes（属性）→ 列表 **Import**

Attribute	Variant Creation	Display Type	Values/alue

---

# 4) 产品模板 `product_template.csv`（product.template）

**去哪里**
Sales 或 Inventory → Products → **Products**（这是模板列表）→ **Import**

**上传并映射（重点字段解释）**

* 上传 `product_template.csv`。
* 常用列（模板里已给好）：

  * `id`：外部 ID
  * `name`、`default_code`、`barcode`（条码可留给变体层使用）
  * `available_in_pos`：1=POS 可售
  * `type`：`product`（库存商品）
  * **计件 vs 计重（互斥）**

    * 计件：`uom_id/id = uom.product_uom_unit`，`to_weight = 0`，`list_price = 元/件`
    * 计重：`uom_id/id = uom.product_uom_gram`，`to_weight = 1`，`list_price = 元/克`
    * ※ 你已选择**以 g 为基准**，所以用 `uom.product_uom_gram`。
  * `pos_categ_ids/id`：多选，示例为 `"pc_gold,pc_gold_ring"`
  * `standard_price`：成本价（不填也可；会计核算建议维护）
  * `tracking`：`none`（本方案不使用 lot）

**验证**

* 打开随机几条模板：

  * “在 POS 可售”勾上；
  * POS 分类已挂；
  * 计件/计重、单位、`to_weight`、`list_price` 符合预期；
  * `tracking=none`。

**常见报错 & 处理**

* 单位外部 ID 不存在 → 进入单位表单（Units of Measure），**View Metadata** 找真实 External ID；或你自定义了单位，要替换成你的 External ID。
* `pos_categ_ids/id` 未识别多选 → 确保用双引号包住逗号拼接的多个外部 ID。
* 条码重复 → 修改为唯一。

---

# 5) 模板属性行（可选）`product_template_attribute_line.csv`（product.template.attribute.line）

> 用于“让 Odoo **自动生成变体**”：声明某模板允许的属性及其取值集合。

**去哪里**
Settings → Technical → **Database Structure → Models** → 搜索 `product.template.attribute.line` → 进入 **View Records**（记录列表）→ **Import**
（或在任意模板下方的“属性与变体”手工添加，不想手工就按本 CSV 导）

**上传并映射**

* 上传 `product_template_attribute_line.csv`。
* 列：

  * `product_tmpl_id/id`：模板外部 ID（如 `pt_ringA`）
  * `attribute_id/id`：属性外部 ID（如 `attr_ring_size`）
  * `value_ids/id`：多个属性值外部 ID，**用引号包住**，用逗号分隔（如 `"v_size_15,v_size_16"`）

**导入后**

* 回到对应模板页面，点击 **保存**（或刷新）→ 系统自动生成变体。

**验证**

* Sales/Inventory → Products → **Product Variants** 列表，能见到新生成的 SKU；
* 模板页“变体数量”>0；点击可跳到变体列表。

**常见报错 & 处理**

* 属性或属性值外部 ID 未导入 → 回到步骤 2/3 补齐。
* 值与属性不匹配（写错）→ 修正 CSV。

---

# 6) 直接导入变体（可选，4A 的替代）`product_product.csv`（product.product）

> 当你手头有明确的 SKU 清单（每条 SKU 使用哪些属性值）时，用此法直接建立变体。

**去哪里**
Sales 或 Inventory → Products → **Product Variants**（产品变体）→ **Import**

**上传并映射**

* 上传 `product_product.csv`。
* 列：

  * `id`：外部 ID（便于下次更新）
  * `product_tmpl_id/id`：模板外部 ID
  * `attribute_value_ids/id`：**该 SKU 的属性值集合**，多值用引号+逗号
  * `default_code`（内部参考/款号）、`barcode`（SKU 条码）、`list_price`/`standard_price`（如要覆盖模板价）

**验证**

* 变体列表出现新 SKU；条码能扫码；模板“变体数量”同步增加。
* 打开该模板“属性与变体”，能看到这些 SKU 的属性组合。

**常见报错 & 处理**

* 属性值与模板不相容（模板没声明这个属性/值） → 建议先用第 5 步导入模板属性行，声明允许的值。
* 条码重复 → 改唯一条码。

---

## 导入后统一验证（强烈建议做）

1. **随机抽查 5–10 个模板**：

   * POS 可售、POS 分类、计件/计重、单位与 `to_weight`、`tracking=none`。
2. **随机抽查 5–10 个变体**：

   * 条码、内部参考、价格；用条码在 POS 搜索能否匹配到 SKU。
3. **POS 会话**：关闭并重新打开（或点“同步/刷新”），验证：

   * 计件商品：直接加行、金额=元/件。
   * 计重商品：秤读或手输**kg** → 系统换算为 **g 数量** → 金额=（g × 元/克）。
4. **库存**：对计重商品做一次收货/盘点，确保以 **g** 为库存单位、数量精度满足（g 精度建议 0.001g）。

---

## 常见“卡点”速排清单

* 看不到“导入”按钮 → 列表视图里才有；进入对应列表再找右上角 Import。
* “只能看到名称看不到 External ID” → 打开记录 → 调试菜单 **View Metadata**。
* “字段对不上/中文环境名称不一致” → 用**技术字段名**（你 CSV 已经用技术名，无需另配）。
* 多公司下数据“看不见” → 切换到正确公司；外部 ID 跨公司也应可引用，但记录本身的 `company_id` 要符合你期望。
* 导入很多行很慢 → 拆分成几批导入；每批后立即抽查验证。

---

## 进阶：日更“当班克价”的两种简单方法

**方法 A：在模板列表批量编辑（少量商品）**
**方法 B：服务器动作一键更新（推荐）**

* 模型：`product.template`
* 代码（把所有 `to_weight=1` 的模板价格设为 `gram_price` 元/克）：

```python
pts = records or env['product.template'].search([('to_weight','=',True)])
gram_price = float(env.context.get('gram_price', 680))  # 执行时在对话框传入
pts.write({
    'uom_id': env.ref('uom.product_uom_gram').id,
    'to_weight': True,
    'list_price': gram_price,  # 元/克
    'tracking': 'none',
})
log(f"已更新 {len(pts)} 条计重商品：{gram_price} 元/克。")
```

* 在 Server Action 表单点 **Create Contextual Action**，就能出现在产品模板列表的【动作】菜单里。

---

如果你愿意，把你们**真实的 10 行产品样例**（分类/模板/戒指号/条码/价格）给我，我可以直接把上面的 CSV 内容替换成你们的值，再发你一份“**直接导入可投产**”的包。


  
  

# #############################################################################################################

# 产品属性值的导入

下面把 **“属性值（product.attribute.value）” 的 CSV 导入**写成一步步可操作的小抄；我给你 3 条进入方式，任选其一，最后导入向导里怎么映射、怎么验证、常见报错怎么排。

---

# 进入“属性值”列表的 3 种方法

### 方法 A（常规，有此菜单就用它）

1. 打开 **销售** 或 **库存** 应用。
2. 菜单：**配置 → 产品 → 属性（Attributes）**。
3. 打开任意一个属性（比如“戒指号”），在表单上找到 **“值（Values）/属性值”** 一栏。
4. 点击这栏右上角的 **小列表图标** 或 **智能按钮 “值 / Values”**（如果有），进入 **属性值的列表视图**。
5. 在列表视图右上角应看到 **导入（Import）** 按钮。

> 注：有的界面在属性表单中的一对多子表不直接显示“导入”。这时用 **方法 B** 更稳。

### 方法 B（万能法，开发者模式）

1. 右上角头像 → **关于** → **启用开发者模式**。
2. 菜单：**设置 → 技术 → 数据库结构 → 模型**。
3. 搜索并打开模型 **`product.attribute.value`**。
4. 点击 **“查看记录（View Records）”**，进入该模型的 **列表视图**。
5. 右上角就有 **导入（Import）** 按钮。

### 方法 C（直接 URL）

在浏览器地址栏打开：

```
/web#model=product.attribute.value&view_type=list
```

进入后同样在右上角用 **Import**。

---

# 导入向导里的操作（逐步）

1. 点击 **Import（导入）**，将你的文件 **`product_attribute_value.csv`** 拖进去或“加载文件”。

2. 映射检查（系统通常会自动识别列）：

   * `id` →（外部 ID，必填，一行一个唯一字符串，如 `v_size_15`）
   * `name` →（属性值名称，如 `15`、`Au 999.9`、`3D`）
   * `attribute_id/id` →（指向**属性**的外部 ID，如 `attr_ring_size`、`attr_fineness`）

   > 说明：`attribute_id/id` 必须引用**你在“属性（product.attribute）导入时用的外部 ID”**。

3. 勾选/确认：

   * 第一行是表头（默认勾选）。
   * 如需“覆盖同名外部 ID 的记录以更新名称”，可勾 **Update records**（仅在你想改名、而不是新增时使用）。

4. 点击 **Test（测试）** → 无红色错误后点击 **Import（导入）**。

---

# 导入后如何验证

* 回到 **属性（Attributes）** 列表，打开如“戒指号”“成色”等属性表单：

  * 在 **“值（Values）/属性值”** 一栏能看到你刚导入的值（如 15、16、Au 999.9、3D…）。
* 后续在 **产品模板 → 属性与变体** 页签里，选择该属性时，就能勾选这些取值。
* 若属性被设置为 **No Variant（不生成变体）**，它的值只用于描述/筛选，不会生成 SKU；若为 **Always（生成变体）**，这些值会参与 SKU 组合。

---

# 常见报错 & 处理

* **External ID not found: attribute\_id/id**
  说明：你填的 `attribute_id/id` 在系统里不存在。
  处理：先导入 **product.attribute**，并确认外部 ID 拼写一致（例如你在属性 CSV 用的是 `attr_ring_size`，这里也必须写 `attr_ring_size`）。

* **Duplicated External ID**
  同一个 `id` 已存在。
  处理：如果是**想更新**名称，勾 **Update records** 再导入；如果是新增，就改 `id` 为唯一值。

* **中文界面看不到“导入”**
  说明还在属性表单内的一对多子表里，没有列表动作。
  处理：用上面的 **方法 B（模型→查看记录）** 进入“属性值”的**全局列表**再导入。

* **导入后属性值归到错误的属性下**
  处理：检查 CSV 的 `attribute_id/id` 是否填错；必要时删除记录（或修正）、重新导。

---

# 你可以直接用的 CSV 列示例

```csv
id,name,attribute_id/id
v_size_15,15,attr_ring_size
v_size_16,16,attr_ring_size
v_size_17,17,attr_ring_size
v_fineness_au9999,Au 999.9,attr_fineness
v_proc_3d,3D,attr_process
```

> 提醒：**先导入属性（product.attribute）**，比如：
>
> ```
> id,name,create_variant
> attr_ring_size,戒指号,always
> attr_fineness,成色,no_variant
> attr_process,工艺,no_variant
> ```
>
> 然后再导入上面的 **属性值**，`attribute_id/id` 就能正确引用到这些外部 ID。

---

需要我远程帮你确认一下你库里 **`product.attribute` 的外部 ID** 列表吗？你把“属性”那张表导出（包含 External ID 字段）给我，我就能帮你核对 `attribute_id/id` 的写法是否 100% 对得上。







  
  

# #############################################################################################################

结论先说在前：
**这四个“数值型重量/克拉”字段（净金重、总重、石重ct、配件重）本质是“连续值、每件都可能不同”。在不用 lot/serial 的前提下，**它们**不适合做“生成变体”的属性**（会导致 SKU 爆炸，也不精确）。一般做法是：

* **产品模板（product.template）**：放“款式级”的**标称/参考值**（便于标签、搜索、报表分组）。
* **产品变体（product.product）**：只有当“不同重量档位本身就是不同 SKU”时，才放到变体（或做成离散档位属性→生成变体）。否则不放。

下面给你一份判断表 + 实施建议。

---

## 放哪一层？——决策表

| 字段          | 典型含义         | 放到 template（模板） 的时机    | 放到 variant（变体） 的时机                                      | 不要做“生成变体属性”的情况                                         |
| ----------- | ------------ | ---------------------- | ------------------------------------------------------- | ------------------------------------------------------ |
| **净金重 (g)** | 去除镶嵌/配件后的金净重 | 仅作**标称/参考**，用于标签/检索/报表 | 你们把不同净重**定为不同 SKU**销售（例如“净重 3.50g 款”和“净重 3.80g 款”各一张价签） | 每件都略有不同、且 POS 以**称重**为准时（`to_weight=1`，UoM=g），不要用它生成变体 |
| **总重 (g)**  | 成品实称总重       | 同上（参考值）                | 同上（以“总重档位”定 SKU 时）                                      | 同上                                                     |
| **石重 (ct)** | 主石克拉数        | 仅用于说明/标签               | 若不同克拉**就是不同 SKU 定价**（例如 0.30ct 与 0.50ct 两个 SKU）         | 每件石重离散但很多，且不想爆 SKU 时                                   |
| **配件重 (g)** | 非主材金属/辅件     | 仅用于说明/标签               | 极少；通常不单独定 SKU                                           | 同上                                                     |

> 简化心法：**连续值、每件可能不同 → 不生成变体**。若它“决定了不同 SKU”，才放到变体；否则放模板作参考值即可。
> 真正结算时，**计重类**商品应靠 `to_weight=1 + UoM=g` 的\*\*称重数量 ×（元/克）\*\*来算价，**不依赖主数据里的重量字段**。

---

## “只用 Products + Variants”时的落地做法

### 方案 A（推荐）：模板放“参考值”，POS 以称重为准

* **计重商品**：模板上 `uom_id = g（uom.product_uom_gram）`，`to_weight=1`，`list_price=元/克`。
  POS 读秤（kg）→ 自动换算为 g 数量 → 金额 = g ×（元/克）。
* **把重量/克拉做成模板或变体上的**自定义 **Float** 字段（不参与生成变体）：

  * `x_net_gold_weight_ref`、`x_gross_weight_ref`、`x_stone_weight_ct_ref`、`x_accessory_weight_ref`
  * 用途：标签打印、检索、统计维度。
  * 好处：**不扩大 SKU**、导入维护简单；缺点：它们是**参考值**，不自动参与 POS 计价（计价靠称重）。

### 方案 B（需要“不同重量=不同 SKU”时）

* 定义一个**离散档位属性**（如“净金重档位：3.5g、3.8g、4.0g …”）→ **Generate variants**。
* 每个档位就是一个变体 SKU，手工维护 `list_price` 或价目表。
* 适合：确实按档位贴价签、销售数据需要到 SKU 粒度。
* 风险：**SKU 数量爆炸**、维护成本高；不适合重量细碎、变化多的门店。

> 提醒：Odoo 的“产品属性值”本质上是**枚举**，不是连续数值。用它来表达重量会逼你“离散化”为档位，因此要谨慎。

---

## 实操建议（不用 lot 的前提）

### 1) 在模板/变体上增加数值字段（两种方式）

* **无代码（Studio）**：

  * 打开产品模板表单 → **Studio** → 添加 **Float** 字段（单位写在标签里，例如“净金重(g)”）。
  * 如需变体也可见/可独立维护，同步在 `product.product` 增同名字段。
* **轻模块**（技术性强一点、可导入）：

  * 在 `product.template` / `product.product` 上定义 `fields.Float` 字段；
  * 在表单视图增加字段；
  * 这样 CSV 就能直接列 `x_net_gold_weight_ref` 等列导入。

### 2) CSV 导入（举例）

* **模板导入**（`product.template`）在原有列基础上，加你自定义列：

  ```
  id,name,uom_id/id,to_weight,list_price,...,x_net_gold_weight_ref,x_gross_weight_ref,x_stone_weight_ct_ref,x_accessory_weight_ref
  pt_ringA,黄金戒指A,uom.product_uom_unit,0,2988,...,3.60,3.75,0.10,0.05
  pt_gold_bulk,足金散件,uom.product_uom_gram,1,680,...,3.50,3.62,,0.03
  ```
* **变体导入**（`product.product`）同理可加：

  ```
  id,product_tmpl_id/id,attribute_value_ids/id,barcode,...,x_net_gold_weight_ref
  pp_ringA_15,pt_ringA,"v_size_15",690000000015,...,3.58
  ```

### 3) 报表/筛选

* 用这些 Float 字段做**自定义筛选**、**分组**，或在列表里展示；标签打印时也可引用。

---

## 什么时候必须考虑 lot（给你把边界说清楚）

* 监管/售后需要**一物一证**（证书号、单件净重留档可回溯）；
* “每件重量/克拉差异**决定价格**”，且你不想每个档位都变成 SKU；
* 需要退换/维修时精确定位“哪一件”。

> 上面这些要求用 Products+Variants 很难长期维护，这才是 lot/serial 的价值所在。

---

### 一句话总结

* **常规**：把“净金重/总重/石重/配件重”当作**参考数值**放**产品模板**（或必要时变体），**不要用它们生成变体**；计价靠 **称重（UoM=g, to\_weight=1）× 元/克**。
* **真的把重量当 SKU**才放变体（或做离散档位属性），否则以后会被 SKU 量反噬。

如果你愿意，我可以给你一份 **Studio 字段清单 + CSV 列模板**（product.template / product.product 各一套），直接按你现有库导入即可。





# #############################################################################################################################

# *****************************************************************************************************************************

你的目标：**先把产品模板建好、挂上属性和值，但不要立刻生成一堆变体**；只有当真的有“某个组合”的实物要入库/销售时，才让那个组合的 **Product Variant** 出现并在 POS 可售。你已经把属性的 **Variant Creation= DYNAMically** 设好了，下面给你三条可落地的做法（首选采购/销售单据触发），再给你一套“自动化收口”的小动作，让流程更顺滑。

---

# 方案一（首选）：用采购（或销售）单据按需生成变体

> **动态生成**的标准用法：在业务单（采购/销售）里选模板 → 选择属性组合 → **确认**时自动创建该组合的变体。

### 一次性准备

1. **产品模板**

   * 销售/库存 → 产品 → **产品**（模板）→ 新建/打开你的模板（例：黄金戒指）。
   * 勾 **Available in POS**（先可不勾，见“自动化收口”）。
   * 计量与计价：

     * 计件：`uom = Unit(s)`，`to_weight = 0`，`list_price = 元/件`
     * 计重：`uom = Gram (g)`，`to_weight = 1`，`list_price = 元/克`
   * POS 分类：挂上 `pos.category`。
   * **Attributes & Variants** 页签：添加 **成色/主石/规格/工艺**，勾选**允许的值集合**（可以一次性把将来可能用到的都勾上；**Dynamically** 不会立刻生成变体）。
2. **确认 “Dynamic” 可用**

   * 你已能把属性设成 *Dynamically*，说明相关配置器模块已可用（如 *sale\_product\_configurator*）。如果后续发现“销售单不弹配置器”，需要安装对应模块。

### 当“真的有货”时

A) **采购触发（推荐）**

* 采购 → 订单 → 新建 → 供应商
* 添加行：**产品**选择你的模板（不是变体）
* 弹出 **属性配置器**，选中真实成色/主石/规格/工艺组合，**确认**
* 确认采购单 → 收货
* 结果：系统**自动创建该组合的变体**（SKU），并入库有存货

B) **销售触发**

* 销售 → 报价单 → 新建
* 产品选模板 → 弹出配置器选组合 → 确认
* 结果：同样会自动创建该变体

> 一旦这个变体被创建：
>
> * 在 **产品 → 产品变体** 列表能看到它；
> * POS 前台（同步/重开会话后）点击该模板，就会出现这个**真实组合**可卖。
> * 建议给这个变体补上 **Barcode / Default Code**（条码/款号）。

---

# 方案二（不走单据）：后台“按需创建一个组合”按钮

> 用一个小的**服务器动作**，只为你指定的属性组合创建/取回变体（不会生成其它组合）。

### 一次性创建服务器动作

* 设置 → 技术 → **自动化 → 服务器动作** → 新建

  * **模型**：`product.template`
  * **动作类型**：Execute Python Code
  * **代码**（可直接用）：

    ```python
    tmpl = records[:1] or env['product.template'].browse(env.context.get('active_id'))
    if not tmpl:
        raise UserError("请在产品模板上运行该动作。")

    # 在“上下文”传入 attr_xml_ids，例如：v_fineness_au9999,v_proc_3d,v_spec_16
    xml_ids = (env.context.get('attr_xml_ids') or "").split(",")
    xml_ids = [x.strip() for x in xml_ids if x.strip()]
    if not xml_ids:
        raise UserError("请在上下文传入 attr_xml_ids，例如：v_fineness_au9999,v_proc_3d,v_spec_16")

    # 找到这些属性值（product.attribute.value）
    vals = []
    for xid in xml_ids:
        try:
            vals.append(env.ref(xid))
        except ValueError:
            raise UserError(f"未找到属性值 External ID: {xid}")

    # 确保模板允许这些值
    PTAL = env['product.template.attribute.line']
    for v in vals:
        line = PTAL.search([('product_tmpl_id','=',tmpl.id), ('attribute_id','=',v.attribute_id.id)], limit=1)
        if not line:
            line = PTAL.create({'product_tmpl_id': tmpl.id, 'attribute_id': v.attribute_id.id, 'value_ids': [(4, v.id)]})
        elif v.id not in line.value_ids.ids:
            line.write({'value_ids': [(4, v.id)]})

    # 将 product.attribute.value 映射到当前模板的 PTAV
    ptav = env['product.template.attribute.value'].search([
        ('product_tmpl_id','=',tmpl.id),
        ('product_attribute_value_id','in',[v.id for v in vals])
    ])

    # 只创建/获取这个组合的变体
    product = tmpl._get_variant_for_combination(ptav)
    product.active = True
    log(f"已创建/激活变体：{product.display_name}（ID: {product.id}）。")
    ```
  * 保存后点 **Create Contextual Action**（创建上下文动作），这样它会出现在产品模板列表的“动作(Action)”里。

### 使用

* 产品 → 产品（模板）→ 勾选目标模板 → **动作** → 选该服务器动作
* 在弹窗的 **Context** 输入：

  ```
  {"attr_xml_ids":"v_fineness_au9999,v_proc_3d,v_spec_16"}
  ```
* 执行后只会创建这一个组合的变体。

---

# 方案三：让模板先不进 POS，等有真实变体再放行（可选增强）

> 避免模板先在 POS 里被误点：**先不让模板“Available in POS”**；当第一条真实变体出现时，**自动**开放给 POS，并归档“空白变体”。

### 自动化 1：新变体创建时自动“放行 POS & 收口空白变体”

* 设置 → 技术 → **自动化 → 自动化动作（Automated Actions）** → 新建

  * **模型**：`product.product`（产品变体）
  * **触发**：On Creation
  * **域**（可选）：`[['product_template_attribute_value_ids','!=',False]]`（只对“有属性值”的新变体生效）
  * **动作类型**：执行 Python 代码
  * **代码**：

    ```python
    prod = records[:1]
    if not prod:
        return

    tmpl = prod.product_tmpl_id

    # 1) 模板未对 POS 开放则开放
    if hasattr(tmpl, 'available_in_pos') and not tmpl.available_in_pos:
        tmpl.write({'available_in_pos': True})

    # 2) 如果模板下还有“空白变体”（无属性值的默认变体），则把它归档
    blank_variants = tmpl.product_variant_ids.filtered(lambda p: not p.product_template_attribute_value_ids and p.id != prod.id)
    if blank_variants:
        blank_variants.write({'active': False})
    ```
* 作用：当你通过采购/销售/服务器动作**第一次**生成“真实组合”的变体时：

  1. 自动把模板 **Available in POS** 设为 True；
  2. 把“没有任何属性值的默认空变体”**归档**，避免 POS 加到那个“空 SKU”。

> 如果你一开始就希望模板显示在 POS，可以不建这个动作；但务必防止前台售卖到“空白变体”。

### 自动化 2：新变体自动分配条码（可选）

* 在 `product.product` 上再建一个自动化动作，On Creation：

  * 如果 `barcode` 为空，按你的条码序列自动生成（可用 ir.sequence 或自定义前缀+ID）。

---

# POS 侧注意

* 每次新增/归档变体后，**POS 会话要“同步/重开”**，前台才能看到最新可售组合。
* POS 前台点击模板卡片时会弹出 **变体选择器**；只有你“已创建”的那些动态变体会出现。
* 若你启用了“禁止无库存销售”，确保有实际库存（通过采购收货或盘盈入库到 POS 库位）。

---

# 总结推荐路径

* **日常**：用 **采购单**（或销售单）选模板→配置器选组合→确认 → 自动创建该变体。
* **需要时**：用“**按需创建组合**”服务器动作，后台一键生成指定 SKU。
* **防误售**：用自动化动作在“第一条真实变体”出现时**放行 POS**并**归档空白变体**。

如果你把“成色/主石/规格/工艺”的 **属性值 External ID 列表**发给我（或给 3–5 个你准备先落地的真实组合），我可以把第二方案的服务器动作调用参数写死到按钮里，点一下就生成这些 SKU，并顺手给它们分配条码。


  
  

# #############################################################################################################

# 新增Product 计件计重处理

下面给你一套**可直接照做**的步骤，教你在 Odoo 18 里为“新建产品模板”设置**计量与计价**（同时涵盖“按件卖”和“按克卖”两种场景）。你之前已决定**以 g 为重量基准**，我也按这个口径写。

---

## 0) 预备检查（只做一次）

* **计量单位**：Inventory → Configuration → Units of Measure

  * **Gram (g)**：Type=Reference Unit，Ratio=1（或你已把 g 设为参考）；
  * **Kilogram (kg)**：Type=Bigger than reference，Ratio=1000；
  * **Unit(s)**（件）：在 Units 类别里，Rounding=1.0000。
* **POS（若要称重）**：POS → Configuration → Point of Sale → 打开你的店铺

  * 勾 **IoT/Scale**（如果你用电子秤；不用秤也可手输重量）。

---

## 1) 新建产品模板（共同步骤）

路径：Sales 或 Inventory → Products → **Products（产品）** → **New**

必填与常用字段：

* **Product Name**：产品名称（例如“足金散件”“黄金戒指A”）
* **Product Type**：选择 **Storable Product**（可库存）
* **Available in POS**：勾选（要在 POS 前台售卖）
* **POS Category**：挂到你的 POS 分类（便于前台分组）
* **Customer Taxes**：选对应的销项税（与你的 POS 税设定一致）
* **Cost**（标准成本）：填写成本（用 FIFO/AVCO 的话由入库形成）

下面分两种计量与计价方式设置：

---

## 2) 计件销售（按件固定价）

**适用**：成品按件卖，如固定标价戒指/手镯。

在产品表单：

* **Unit of Measure**：选 **Unit(s)**（件）
* **Purchase UoM**：也选 Unit(s)（或供应商按件交付）
* **Sales Price**：填写 **元/件** 的价格
* **To Weigh with Scale**：**不勾**（或字段名 `To Weight` 置为 False）
* 保存

> POS 前台：点击商品即按 “元/件” 加入；如需改价，可在 POS 配置启用“价格控制/经理 PIN”。

---

## 3) 计重销售（按克定价）

**适用**：金料、按克定价的商品。

在产品表单：

* **Unit of Measure**：选 **Gram (g)**
* **Purchase UoM**：

  * 若供应商按 **kg** 供货，可选 **Kilogram (kg)**（系统会按 1000g=1kg 自动换算入库）；
  * 也可直接选 Gram。
* **Sales Price**：填写 **元/克**（例如 680）
* **To Weigh with Scale**（或 `To Weight`）：**勾选**（True）
* 保存

> POS 前台：
>
> * 有秤时读数是 **kg**，系统会自动换算为 **g 数量**；金额 = g ×（元/克）；
> * 无秤也可手输**重量**（输入 kg 或 g 取决于 POS 前端控件，系统会按 UoM 处理）。

---

## 4) 可选：属性与变体（不影响计量设定）

* 进入 **Attributes & Variants** 页签添加属性（如“成色/主石/规格/工艺”）。
* 你已把 **Variant Creation = Dynamically**，勾选好允许的值即可；**不会立刻生成变体**。
* 以后通过 **采购/销售单确认**或**服务器动作**按需生成真实 SKU。

---

## 5) 示例（照抄可用）

### A) 计件戒指（固定价）

* Unit of Measure = **Unit(s)**
* Purchase UoM = Unit(s)
* Sales Price = **2988**（元/件）
* To Weight = **False**

### B) 足金散件（按克）

* Unit of Measure = **Gram (g)**
* Purchase UoM = **Kilogram (kg)**（若供应商按 kg 供货）
* Sales Price = **680**（元/克）
* To Weight = **True**

---

## 6) 常见问题与排查

* **POS 不弹重量框**：该产品 **To Weight** 未勾；或 POS 会话未刷新（前台右上角 **Sync** / 重开会话）。
* **秤读 kg 但金额不对**：检查 UoM 是否 **Gram**，以及重量类别换算（kg=1000g）是否正确。
* **税额不对**：产品的 **Customer Taxes** 与 POS 的税/税映射不一致；统一口径（含税/不含税）并同步会话。
* **采购按 kg、销售按 g**：这正是 UoM 的用途——**Purchase UoM=kg**、**销售 UoM=g**，系统自动换算。
* **价格每天变**（克价）：

  * 简单：每天批量更新 **按克商品**的 `Sales Price`；
  * 可建 **Server Action** 一键把所有 `to_weight=True` 的模板价格改为当班克价。

---

## 7)（可选）CSV 批量导入对应列

* 计件：`uom_id/id = uom.product_uom_unit`，`to_weight = 0`，`list_price = 元/件`
* 计重：`uom_id/id = uom.product_uom_gram`，`to_weight = 1`，`list_price = 元/克`
* 其它：`available_in_pos`、`pos_categ_ids/id`、`standard_price`、`taxes_id/id` 等按需填。

---

### 一页小抄

* **计件**：UoM = Unit(s)，`to_weight=False`，`Sales Price=元/件`。
* **计重**：UoM = Gram，`to_weight=True`，`Sales Price=元/克`；秤读 kg 自动换算。
* **采购与销售 UoM 可不同**（kg 进、g 出），Odoo 自动换算。
* 动态变体：属性设 Dynamically，在业务单/动作里按需落地 SKU。

需要的话，你发我一个具体产品的截图（基本信息页 + POS 区块），我可以直接指出你应该勾/填的具体位置，或者我帮你写一个\*\*“一键更新克价”的服务器动作\*\*。



# #############################################################################################################


结论先说：
**可以**把所有属性都下沉到“批次/序列号（Lot/Serial）”，入库时逐件填写；系统也能跑通。但不**建议**把“成色/主石/规格/工艺”这类\*\*“型号/类目级”\*\*属性也全部搬到 Lot，因为你会失去很多“按变体管理”的能力（报价/价目表、网站/筛选、BOM 与工艺路由、补货与预测等）。

# 怎么分层更稳（推荐做法）

* **放在“产品/变体”上的（Catalog 级；Variant Creation 可设 Dynamically）：**
  成色（K 数/材质）、品类/款式（戒指/项链/…）、规格（戒围号/链长等）、工艺（抛光/镶嵌工艺…）

  * 作用：决定定价规则、网站筛选、BOM/工艺路线、补货与预测。
  * 优点：销售/网站能直接按变体选型、价目表可按属性计算；动态生成避免变体爆炸。
* **放在“Lot/Serial（序列号）”上的（每件实物唯一）：**
  净金重(g)（必填）、总重(g)（必填）、石重(ct)、配件重(g)、证书号、（这件）销售工费、备注等

  * 作用：入库时逐件确认；后续溯源/售后/标签打印/盘点统计都以**实物**为准。

> 简单记忆：**“型号/工艺/可复用的规格 → 变体”， “每件才知道/每件不同 → Lot”**。

# 如果“全部放 Lot”会有什么影响

* ✅ 减少变体数量、入库时一次性定案；POS 扫序列号很好用。
* ❌ 销售/网站端无法用“属性”来选型和定价（因为属性变成了Lot字段，报价前看不到）。
* ❌ 价目表/折扣公式很难按属性生效；补货/预测只能按“同一个产品”聚合，看不到“按成色/规格”的维度。
* ❌ MRP/BOM/工艺切换通常靠变体属性驱动，搬到 Lot 后就失去天然联动，需要定制。

# 落地细节（混合方案要点）

1. 产品启用**按唯一序列号**追踪。
2. 在 `stock.production.lot` 上建：净金重、总重（必填）、石重、配件重、证书号、工费、备注等字段。
3. 在收货明细（`stock.move.line`）上把这些 Lot 字段拉出来，设“入库必填/可见”。
4. （可选）在 Lot 上做**默认值联动**：新建序列号时自动带出该变体的成色/规格/工艺到只读展示字段，便于打印与搜索（避免重复维护）。
5. 标签/小票/收货单模板里读取 Lot 字段；报表做“按变体 + Lot 维度”透视即可。

# 快速决策表

* 需要在**下单/网站**按“成色/规格/工艺”选择并定价 → 这些属性留在**变体**。
* 仅在**入库/验收**才能确定（称重/检测后才知道）的 → 放**Lot**。
* 既要避免变体爆炸、又要有变体管理能力 → 变体属性设为 **Dynamically**，其余放 Lot。

如果你确定业务完全走“入库称重→POS 扫码售卖”，没有网站/报价按属性选型、也不做 MRP/补货分层，那么**全部放 Lot**也能行；只是要接受“销售前看不到属性/无法按属性定价”的取舍。需要的话，我可以给你一份最小模块，把上述 Lot 字段、入库必填和默认带出都配置好，直接安装即可。





# **********************************************************************************************************************************************
# **********************************************************************************************************************************************
# **********************************************************************************************************************************************
# **********************************************************************************************************************************************

太好了，这就把你列出的属性按“进货渠道（供应商）默认/政策”、“产品模板（含变体）”、“序列号/批次（Lot/Serial，入库逐件录入）”三层划清楚，并给出**为什么**这么放、**怎么操作**一步步来。目标是：入库称重→生成序列号→POS 扫码售卖，既不让变体爆炸，又保留按“成色/规格/工艺/类别”的管理与定价能力。

# 一、属性归属与理由（总表）

| 属性                     | 放在哪里                                      | 理由与使用时机                                                                 |
| ---------------------- | ----------------------------------------- | ----------------------------------------------------------------------- |
| 一码一物 / 一码多件            | **产品模板（Tracking）**，供应商处做**默认**            | 是否“序列号管理”是**产品固有属性**（珠宝=一码一物）。渠道只提供默认建议。POS/库存要依赖它来强制逐件录入。              |
| 计件 / 计重                | **产品模板（计量单位/UoM）**，供应商处做**默认**            | 影响库存单位与定价逻辑（计重用 g，计件用 Unit）。渠道可给默认（该供应商大多是计重）。                          |
| ID                     | **产品模板（Internal Reference）**              | 产品目录唯一编号，供采购/POS/报表用。                                                   |
| 条码                     | **产品模板**（商品条码） + **序列号**（每件的序列号/标签条码）     | 商品条码用于找商品；序列号条码用于找**那一件**。POS 可启用“扫描序列号”直接定位。                           |
| 名称                     | **产品模板**                                  | 基础展示字段。                                                                 |
| 大类（黄金/K金/镶嵌/玉石）        | **产品分类（product.category）**                | 用分层分类（父类=大类），会计核算、报表、POS 分类都受益。                                         |
| 类别（戒指/手镯…）             | **产品分类二级** 或 **变体属性（类别）**                 | 若“类别”决定不同款型/定价→做**变体属性**；若只是展示/统计→用二级分类即可。                              |
| 成色（18K/足金/99.99%…）     | **变体属性（动态生成）**                            | 这是**选型与定价关键**，应做成变体以便销售/网站筛选和价目表规则。                                     |
| 主石（颜色/净度）              | 视业务：**若用于选型**→**变体属性**；**若仅验收记录**→**序列号** | 可混合：变体放“是否有主石/主石类型”，颜色/净度放 Lot（验收时才知道）。                                 |
| 规格（戒围/链长/镶口等）          | **变体属性（动态生成）**                            | 常用于选型与价差。避免把“只在每件不同”的自定义文本放变体。                                          |
| 工艺（硬金/3D/5D/5G/珐琅）     | **变体属性**（推荐）或 **序列号**（若仅做记录）              | 若工艺影响价格/工艺路线/展示→放变体；若只是这件的说明→放 Lot。                                     |
| 净金重（必填）                | **序列号**                                   | **件级差异**，收货称重才能确定，必须入库时逐件填。                                             |
| 总重（必填）                 | **序列号**                                   | 同上。                                                                     |
| 石重（ct，选填）              | **序列号**                                   | 仅部分款有。                                                                  |
| 配件重（选填）                | **序列号**                                   | 件级差异。                                                                   |
| 证书号（选填）                | **序列号** + 渠道**是否必需**做**默认策略**             | 与标签/那一件绑定；有的渠道要求必须有证书。                                                  |
| 产品销售工费（选填）             | **序列号**（值），产品模板**工费类型默认**                 | 多为件级或批次级差异，入库时落到该件；模板上放“默认工费类型”。                                        |
| 克工费/件工费（选填）            | **产品模板（默认）** + **序列号（可覆盖值）**              | 用模板给定计价逻辑；具体那件可在 Lot 上定值（比如某件加工复杂）。                                     |
| 成本（必填=0 默认）            | **供应商信息/采购价**（渠道）→**存货估价**；模板仅作初始值        | 成本应来自**采购价/入库估价**而不是手填属性。让系统按 FIFO/AVCO 记成本，模板的 standard\_price 只是初始参考。 |
| 标价（必填=0 默认）            | **销售价目表（Pricelists）**                     | POS 价格来自价目表，支持零售价/活动价/会员价。不要把“标价/批发价”塞到属性或 Lot。                         |
| 批发价（必填=0 默认）           | **销售价目表（另一个Pricelist）**                   | 给批发客户或指定价目表使用。                                                          |
| 性质（正品/特价/赠品/物料/配件/活动款） | **产品模板选择字段**（可辅以 POS 分类/标签）               | 用于业务规则：赠品默认为 0 价、物料/配件不追踪序列号、特价/活动款走特定价目表。                              |
| 备注（选填）                 | **序列号备注**（件级） + **产品模板销售/采购描述**（通用）       | 既要有件级备注用于售后/标签，也要有模板级描述用于下单与标签默认。                                       |

> 记忆口诀：**选型/定价维度 → 变体/分类；件级差异/入库称重 → 序列号；价格规则 → 价目表；成本 → 采购与库存估价；渠道是“默认与约束”的来源。**

---

# 二、实际操作步骤（Odoo 18 中文界面）

## A. 进货渠道（供应商）默认与政策

1. 进入【联系人】新建/打开供应商：

   * 用 **Studio** 在 `res.partner` 上增几个**默认字段**（可选）：

     * 默认计价方式（计件/计重）
     * 默认工费类型（克工费/件工费）
     * 是否要求证书（是/否）
     * 默认是否一码一物（是，建议用于黄金类）
   * 这些字段仅作**默认/校验**，真正生效的是产品或入库（见下文）。
2. 在【库存 › 产品】打开某产品 → 页签【采购】→ **供应商**：

   * 添加该供应商的“采购价/币种/最小数量/交期”。
   * 采购单价将进入**存货估价**，成为成本来源。

> 进阶（可选）：用 Studio 做一个**自动化动作**：当创建收货单且供应商勾选“要求证书”，则在收货明细上把“证书号”设为必填。

## B. 产品目录建模（模板/变体/分类）

1. 分类树：

   * 【库存 › 配置 › 产品分类】建立层级：

     * 父类 = 大类（黄金/K 金/镶嵌/玉石）
     * 子类 = 类别（戒指/手镯/项链/吊坠…）
   * POS 分类也按需建立，便于前台筛选。
2. 变体属性：

   * 【库存 › 配置 › 属性】创建：

     * 成色（动态生成变体）
     * 规格（例如戒围#10/#11…，动态）
     * 工艺（硬金/3D/5D/珐琅…，动态）
     * （可选）主石类型（若用于选型/价差）
   * 在**产品模板**上勾选这些属性；“Variant Creation = **Dynamically**”。
3. 计件/计重与单位：

   * 计重：把**计量单位**设为 g（克），同类单位用“重量”类别。
   * 计件：单位设为 Unit(s)。
   * 可在模板自定义布尔“按重量定价”供价目表规则引用（需要轻度定制时用）。
4. 一码一物：

   * 模板字段 **追踪方式（Tracking）= 按唯一序列号**（黄金类）。
   * 配件/耗材可设为“无追踪”。
5. 基础字段：

   * 名称 / 内部参考（ID）/ 条码：在模板的基本信息里维护。
   * 性质：用 Studio 在 `product.template` 增加选择字段（正品/特价/赠品/物料/配件/活动款），用于报表或价目表过滤。
6. 售价/批发价：

   * 【销售 › 配置 › 价目表】开启多价目表：

     * 建“零售价（标价）”“批发价”两套价目表；POS 配置里选择可用价目表并允许前台切换（或按客户群自动应用）。
   * 若有“按克金价 + 工费”的规则，可用**公式/折扣**或定制计算（见“增强建议”）。

## C. 序列号（Lot/Serial）字段（入库逐件录入）

1. 启用并进入【库存 › 主数据 › 批次/序列号】。
2. 用 **Studio** 在 `stock.production.lot` 上新增字段：

   * 净金重（必填）、总重（必填）、石重（ct）、配件重、证书号、销售工费（数值）、工费类型（选择：克/件，默认来自模板）、备注。
3. 在收货明细行展示与必填：

   * 打开任一**收货单** → 列表“操作明细（拣货行）”→ 用 Studio 在 `stock.move.line` 树视图**把上述 Lot 字段作为 related 列拉出来**，并设置：

     * 当 `picking_type_code == 'incoming'` 时**可编辑/必填**（净金重、总重）。
     * 若供应商“要求证书”= 是，则证书号也设为必填（使用显示/必填条件）。
4. 条码与序列号：

   * 每件生成一个**序列号**，可在序列号上放“序列号条码”（lot\_name 同步到条码或自定义 x\_barcode）。
   * 标签模板里打印该条码，POS 扫码即可定位到**该件**。

## D. 入库流程（从采购到入库）

1. 【采购】下单 → 确认 → 在【库存】里看到相应**收货单**。
2. 打开收货单：

   * 逐行**创建序列号**（每件一条 move line），录入：净金重、总重、（石重/配件重/证书号/销售工费/工费类型）。
   * 若该产品 Tracking=序列号，系统会强制你逐件填；**没填必填项无法验证**。
3. 验证收货：

   * 成本来自采购价 → 过账后进入库存估价（若开了自动估价/FIFO）。
   * 每件的重量/证书/工费等信息已与**序列号**绑定。

## E. POS 销售配置

1. 【POS › 配置】

   * 启用“价目表”，选择“零售价/批发价”等。
   * 启用“批次/序列号”扫描（或使用条码规则让 POS 识别序列号条码）。
   * 前台类目用 POS 分类（与产品分类对齐）。
2. 前台售卖两种常见方式：

   * **方式 1（推荐）**：店员**扫描序列号条码**→ POS 自动定位到对应商品与那一件（重量/证书信息不直接显示但在后台有记录）。
   * **方式 2**：先选商品，再从可用序列号中选择那一件（开箱即用的 Odoo 需要轻度定制/扩展来弹选序列号明细）。
3. 价格来源：

   * 默认来自价目表（零售价/批发价/活动价）。
   * 若要“按克金价+工费”的**实时价**，见下方“增强建议”。

## F. 报表/标签与售后

* **标签模板**（QWeb）：把 Lot 上的“净金重/证书号/工艺/成色/序列号条码”打印出来。
* **销售/库存报表**：按产品分类/变体维度做汇总，按序列号字段做明细统计（净金重区间、证书追溯、某工艺销量等）。
* 售后换修/盘点：直接按**序列号**定位实物。

---

# 三、价格与成本的两条落地路线（择一或并行）

## 路线 A（快落地，标准功能）

* **标价/批发价**：全部放**价目表**；按“类别/成色/规格/工艺”设规则或导入价目数据。
* **成本**：来自采购价/入库估价（FIFO/AVCO），无需手填“成本属性”。
* **销售工费**：录在序列号用于报表与标签；实际**售价**仍以价目表为准。

## 路线 B（黄金专用，按金价 + 工费）

* 在公司参数或自定义模型里维护**当日金价**。
* POS/销售价格计算：`售价 = 净金重 * 当日金价 + （克工费*净金重 或 件工费）`
* 实施方式：

  1. 在序列号已有净金重/工费/工费类型；
  2. 通过轻度定制，在 POS 扫描序列号时**动态计算行价**并写入；
  3. 保留价目表作为“上限/下限/活动价”覆盖（可选）。
* 成本仍来自采购与估价。

---

# 四、几个关键“坑位”与建议

* **不要**把“标价/批发价”做成 Lot 字段：POS/价目表不会自动读它。
* **主石颜色/净度**：如果客户会按此筛选/报价 → 做变体；否则放 Lot。
* **类别（戒指/手镯）**：若你要在 POS 里筛选、并且不同类别经常有**不同工艺/规格**，用**分类树**最稳；需要价差才加变体。
* **性质（赠品/特价/配件）**：用模板选择字段 + 价目表/折扣规则联动；“配件”多为**不追踪序列号**。
* **一码一物**：黄金类务必在模板上设“**按唯一序列号**”，否则入库环节就无法逐件录入重量/证书。

---

如果你愿意，我可以在下一步把：

* 需要的 Studio 字段清单（模型/字段类型/显示规则）、
* 视图上该放到哪、
* 以及一个可直接安装的极简模块骨架（Lot 字段 + 收货行必填 + 标签模板字段）

整理成一份“实施检查清单 + 最小可用包”的交付版，照着勾就能落地。

  
  
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

# #############################################################################################################

太好了。下面给你“三套落地方案”，分别满足你提到的约束：

* 方案一：**纯应用页面手动配置（不使用 Studio、不写代码）**
* 方案二：**在完成“手动配置”的前提下，用导入模板做**批量录入/批量维护\*\*
* 方案三：**通过创建自定义模块（写代码）实现“件级字段 + 入库必填 + POS可用”**

我会把你列出的“全量属性”逐一映射到可实现的位置，并给出操作路径与注意事项。
（说明：不使用 Studio 的前提下，**无法给序列号/收货行增加新字段**；因此方案一会采用“可替代”的方式；方案三则提供真正的件级字段。）

---

# 方案一｜纯应用页面手动配置（无 Studio、无代码）

## 目标与取舍

* 目标：从采购→入库→POS 售卖，全流程打通；按**变体**管理“选型/定价”维度，按**序列号**区分“每件实物”。
* 取舍：像“净金重/总重/石重/配件重/工费/证书号”等**件级字段**，在不写代码和不使用 Studio 的情况下，无法直接存到序列号字段里。可采用以下折中：

  1. **证书号 = 序列号名**（让操作员把证书号直接作为序列号输入，后续可扫码定位该件）。
  2. **重量/工费记录方式**：

     * A. 使用 **质量(Quality)** 应用的“进货质检表”记录（无代码、UI 配置即可，记录与收货/序列号关联）；
     * B. 或使用**标签/附件**方式记录（适合轻量场景；统计弱）。
  3. **POS 价格**走价目表（标价/批发价/活动价）；若要“金价+工费”，不写代码时只能走“**手工组合**”法（见下文）。

> 提示：如果你**必须**把“净金重/总重/工费/证书号”等变成真正的字段并在入库时必填，请直接看文末的“方案三（模块实现）”。

---

## 一）系统准备（一次性设置）

1. 【应用】安装：**库存、采购、销售、POS、价目表（启用）、（可选）质量Quality**。
2. 【库存 › 配置 › 设置】

   * 勾选 **批次/序列号**；（必要时）勾选 **有效期**（如果用到）。
   * 勾选 **计量单位**；确认有“重量（g）”单位（如没有就添加一个“克(g)”）。
3. 【销售 › 配置 › 设置】启用 **价目表**。
4. 【POS › 配置】

   * 启用 **价目表**；把“零售价/批发价/活动价”等加入可用列表。
   * 启用“**允许使用批次/序列号**”（不同版本在 POS 配置或产品追踪中体现；核心是产品追踪=序列号即可在 POS 选择/扫描序列号）。

---

## 二）主数据建模（分类/属性/模板/追踪/价目表）

### 1. 分类（大类/类别）

* 【库存 › 配置 › 产品分类】

  * 建立父级分类=**大类**：黄金 / K金 / 镶嵌 / 玉石（对应“必填：大类”）。
  * 在各大类下新建子类=**类别**：戒指 / 手镯 / 项链 / …（对应“必填：类别”）。
* POS 分类（前台分组展示）：【POS › 配置 › POS 分类】按同样层级建立（可与产品分类一致）。

### 2. 变体属性（用于选型/定价）

* 【库存 › 配置 › 属性】创建以下属性，**Create Variants = Dynamically**：

  * **成色**（18K/足金/99.99%…，必填）
  * **规格**（如戒围 10/11…、链长…，非必填）
  * **工艺**（硬金/3D/5D/5G/珐琅…，非必填）
  * **主石类型**（是否镶嵌/主石类别…，若用于选型/价差则做属性；若只做记录，后续走质量/标签）

> 理由：这些是“**选型/定价**维度”，在销售/网站/POS 上要能筛选和定价，对应**变体**最合适；避免把它们全部放成件级记录而失去前端可选能力。

### 3. 产品模板（一码一物/计件计重/ID/条码/价格）

* 【库存 › 产品】新建产品模板（例如“足金戒指基础款”）：

  * **名称/ID/条码**：对应“必填：名称/ID/条码”。
  * **产品类型**：可库存产品。
  * **产品分类**：选“大类/类别”。
  * **追踪方式（Tracking）**：

    * “**按唯一序列号**”= 一码一物；
    * “**按批次**”= 一码多件；
  * **计量单位（UoM）**：

    * 计件：单位（Unit(s)）；
    * 计重：克（g）（如需 POS 电子秤，可勾“按重量称重/To Weigh With Scale”，不同版本名称略有差异）。
  * **属性**：勾选成色/规格/工艺（与上一步创建的属性对应）。
  * **成本/标价/批发价**：

    * **成本**建议来自采购/库存估价（FIFO/AVCO）。模板的“成本”字段可置 0（系统会以后续估价为准）。
    * **标价/批发价**通过**价目表**管理（见下一小节）。
  * **性质（正品/特价/赠品/物料/配件/活动款）**：

    * 不写代码时，推荐用**产品分类/子分类或 POS 分类**来代表“性质”分组；
    * 例如建“活动款/赠品/配件”子分类或 POS 分类，供报表/价目表规则使用。

### 4. 价目表（标价/批发价/活动价）

* 【销售 › 配置 › 价目表】

  * 建“**零售价**”“**批发价**”“**活动价**”等；
  * 规则维度可按\*\*产品/产品分类/属性（通过指定变体）\*\*定价；
  * POS 中关联可用价目表，并按客户或前台选择应用。

> 若你想“金价+工费”自动计算，纯 UI 很难无代码完成（需要读取**净金重**等件级字段）。纯 UI 的替代做法见“POS 结算小技巧”。

---

## 三）入库流程（证书号=序列号；记录重量的两种法）

### 1. 收货前置（操作类型）

* 【库存 › 配置 › 操作类型】打开“**收货(Receipts)**”：

  * 勾选“**允许创建新序列号**”“**允许使用现有序列号**”（不同版本措辞略有差异）；
  * 保存。
```
Inventory->Configuration->Operations Types->Receipts
LOTS/SERIAL NUMBERS
Create New ?v
```

### 2. 采购→收货（证书号=序列号）

* 【采购】创建采购订单→确认→【库存】打开对应**收货单**。
* 在收货明细里，对每件实物：

  * 点“**序列号**”或“标识”按钮，**创建序列号**；
  * \*\*将“证书号”直接作为该条的“序列号名称”\*\*录入（这样后续标签/扫码即=证书号）。
  * 验证收货。
  
```实操
没问题。下面给你**一步步**把“证书号=序列号”落到采购收货里（Odoo 18，按你当前菜单）。

---

# A. 一次性检查（只做一次）

1. **开启序列号功能**
   Inventory → Configuration → **Settings** → 勾选 **Lots & Serial Numbers** → Save。
2. **把需要一物一证的产品设为按序列号追踪**
   Inventory → Products → **Products** → 打开目标产品 → **Inventory** 页签 → **Tracking = By Serial Number** → Save。

   > 若是新产品模板，先这样设，后续所有变体都会按序列号收货。

（可选）3) **允许在收货时创建新序列号**
Inventory → Configuration → **Operation Types** → 打开 **Receipts**（收货）→ 勾选

* *Use existing Lots/Serial numbers*（使用已有）
* *Create New Lots/Serial numbers*（允许新建）
  → Save。

> 这样收货时会有“创建序列号”按钮/向导。

---

# B. 采购单 → 打开对应收货单

1. Purchase → **Orders → Requests for Quotation / RFQs** → **New**

   * Vendor 选供应商，添加上面那个**按序列号**的产品和数量。
2. **Confirm Order**（确认订单）。
3. 打开**收货单**（二选一）：

   * 在 PO 顶部智能按钮点 **Receipts（收货）**；
   * 或 Inventory → **Operations → Receipts**，按 **Origin**（来源=PO编号）或 **Vendor** 搜索打开该单（形如 **WH/IN/xxxxx**）。

---

# C. 在收货单里把“证书号”录为“序列号”

> 目标：N 件实物，就产生 N 条序列号（每条=证书号）。

到 **收货单（WH/IN/…）** 页面后，做下面其一：

### 方法 1｜一键向导批量录（适合一次收很多件）

1. 在产品行右侧，点 **⚙️/Serial Numbers/标识**（按钮名称可能略有差异）。
2. 在弹出的**Assign/创建序列号**向导里：

   * 选择 **Create New**（创建新的序列号）；
   * 在列表里**逐行输入“证书号”**；或把证书号**一行一个**粘贴进去（N 行对应 N 件）；
   * 确认 **Quantity Done** 会自动等于输入的序列号条数。
3. **Confirm / Save** 返回收货单。

### 方法 2｜在“详细作业（Detailed Operations）”里逐行录（适合少量或要挑批次）

1. 滑到 **Operations / 详细作业** 区域（有时需点**📝 Details/详细**才展开）。
2. **Add a line / 新增一行**：

   * **Done** = 1；
   * **Lot/Serial Number** 里输入**证书号**；
   * Location Dest 维持默认（WH/Stock）。
3. 重复添加 N 行（每行 1 件、1 个证书号）。
4. 完成后回到上方主表。

> 无论哪种方法，**序列号字段里填的就是你的“证书号”**。收货后系统会把这些值创建为该产品的 SN 记录。

---

# D. 验证并过账收货

1. 回到收货单顶部 → **Validate / 验证**。

   * 如果弹窗提示“你处理的数量与预期不同”，点 **Apply**（按已录的序列号数量为准）。
2. 成功后状态变 **Done**。

---

# E. 结果查看 & 打印

* **查看序列号台账**：Inventory → **Products → Lots/Serial Numbers** → 搜该产品或直接搜你的**证书号**，能看到刚创建的 SN（名称=证书号）。
* **打印标签**：

  * 在收货单上：**Print → Lot/Serial Number Labels**（名称/条码会用 SN，也就是你的证书号）；
  * 或 Lots/Serial Numbers 列表勾选若干 → **Print**。
* **后续扫码**：在出库/销售/POS 里，扫码这个证书号=选择对应**序列号**。

---

## 常见卡点（对照排查）

* 看不到“序列号/标识”按钮：先确认产品 **Tracking=By Serial Number**；且 Receipts 操作类型允许 **Create New Lots/Serial numbers**。
* 无法保存：确认“Done 数量”与序列号条数一致；序列号**不允许重复**（同产品下每个 SN 必须唯一）。
* 从 Moves History 进去看不到按钮：请在\*\*拣货单（WH/IN/…）\*\*页面操作，而不是单条 move。

需要我给你一张“证书号=SN”的**收货向导截图位置信息**（中文/英文界面对照）也可以，你回我现在界面语言即可。

```  

### 3. 记录重量/工费（无 Studio 的两种可行法）

**法 A｜用质量(Quality)应用做“进货质检表”**（推荐，无代码）

1. 【质量 › 配置 › 控制点】新建“**收货质检**”控制点：

   * 适用：操作类型=收货；产品=（可空/指定类目）；
   * 步骤中加入：

     * **测量**项：净金重(g)、总重(g)、石重(ct)、配件重(g)；
     * **文本**项：工费、工费类型（克/件）、备注（这些是文本/数字框，供操作员填）。
2. 收货时系统会弹出质检：

   * 逐件输入上述值，质检记录将绑定该次收货/行/序列号（能追溯和报表）。
3. 报表查看：

   * 在【质量】里按控制点/产品/日期统计；
   * 或在【库存】里通过“序列号 → 质量检查”关联查看。

**法 B｜用标签/附件记录**（轻量）

* 在收货后打印**标签**，把“序列号（=证书号）”“成色/规格/工艺”“重量”等印上（重量手工录入到标签模板的“可编辑文本”——仅作为打印信息，不入库到结构化字段）；
* 或在序列号/收货单上附加 PDF/图片（称重单/证书照）。
* 适合门店现场快速操作，但后期统计弱。

> 无 Studio/代码时，**无法把净金重等作为“结构化字段”存入序列号**。你仍可追溯证书号＝序列号，也能在质量记录/附件/标签里留痕。

---

## 四）POS 销售（两种“工费+金价”的纯手工玩法）

> 目标：不写代码前提下，尽量贴近“金价+工费”的实际结算。

**方式 1｜秤重 + 工费为单独产品**

1. 建两个服务产品：

   * `工费-计克`（UoM=克，标价=每克工费，POS 可输入**数量=净金重**）；
   * `工费-计件`（UoM=件，标价=每件工费）。
2. 计重商品（黄金克卖）：

   * 商品本体设“**按秤称重**”（POS 连接电子秤或手工输入重量=数量）；
   * **金价**：直接把“黄金原料金价（每克）”做成一个商品 `黄金基价-克`，前台输入**数量=净金重**；或用价目表动态改价。
   * **工费**：根据选择加上 `工费-计克` 或 `工费-计件`。
3. 缺点：操作员要把“净金重”手动敲两次（或秤/复制），但**不写代码只能如此**。

**方式 2｜一口价（价目表管控）**

* 把每个“款+成色+规格+工艺”变体在价目表里**定一口价**（活动时改价）；
* 适合“政策价/标签价”为准、对重量不强依赖的商品。

---

# 方案二｜手动配置后的“批量模板导入/维护”方案

> 思路：先用 UI 建**少量样例**（类别/属性/模板/价目表/供应商价等），然后**导出**示例 CSV，看列名与关系字段；接着按此结构**批量导入**。

## 可批量导入的主对象与建议列

1. **产品分类**（`product.category`）

   * 列：名称、父分类
2. **属性与属性值**（`product.attribute` / `product.attribute.value`）

   * 列：属性名、创建变体=动态；属性值（多行）
3. **产品模板**（`product.template`）

   * 列：名称、内部参考(ID)、条码、类型、分类、追踪方式（序列号/批次/无）、计量单位等
4. **产品变体**（`product.product`）

   * 方式 A：直接导入变体，使用列名 `Attribute: 成色`、`Attribute: 规格`、`Attribute: 工艺` 来指定属性值；
   * 方式 B：导入“模板属性行”（`product.template.attribute.line`），再让系统生成变体。
5. **供应商价**（`product.supplierinfo`）

   * 列：产品、供应商、采购价、币种、最小起订量、交期等
6. **价目表与价目表项**（`product.pricelist` / `product.pricelist.item`）

   * 列：价目表名称、币种；规则项：适用范围（产品/分类/全部）、计算方式（固定价/折扣/公式）、价格/折扣等
7. **序列号（期初/历史）**（`stock.production.lot`）

   * 列：名称（建议=证书号）、产品、公司（如多公司）；**注意**：此模型**没有**你要的“净金重”等字段（无 Studio/代码做不到）。

## 操作步骤（通用）

1. 进入目标列表视图（例：产品），点击右上角 **导入** → **下载示例模板**。
2. 用示例模板填充数据（名称要与系统中已有对象一致，或使用外部 ID）。
3. 导入前可先 **导出**一条你手工建好的记录，作为模板对照（能看到字段技术名与数据格式）。
4. 导入后，在 UI 检查：分类树、属性、变体是否正确生成，价目表是否生效。
5. 如果需要大规模更新，用“**外部 ID**”保证幂等（再次导入会更新而不是重复创建）。

---

# 方案三｜创建自定义模块（推荐从长期角度）

> 目标：把“净金重、总重、石重、配件重、证书号、销售工费、工费类型、备注”等做成**序列号上的真实字段**，并在**收货（incoming）**时**逐件必填**；同时给产品模板增加“性质”等字段，满足你提出的“全量属性”落地。

## 1）模块结构（示例）

```
product_jewelry_specs/
├─ __manifest__.py
├─ security/
│   └─ ir.model.access.csv
├─ models/
│   ├─ stock_production_lot.py
│   ├─ stock_move_line.py
│   ├─ product_template.py
│   └─ res_partner.py
└─ views/
    ├─ stock_production_lot_views.xml
    ├─ stock_picking_views.xml
    ├─ product_template_views.xml
    └─ res_partner_views.xml
```

### `__manifest__.py`

```python
{
    "name": "Jewelry Specs for Lots",
    "version": "18.0.1.0.0",
    "depends": ["stock", "purchase", "sale", "point_of_sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/stock_production_lot_views.xml",
        "views/stock_picking_views.xml",
        "views/product_template_views.xml",
        "views/res_partner_views.xml",
    ],
    "license": "OEEL-1",
}
```

### `security/ir.model.access.csv`

（为扩展的模型赋读写权限）

```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_lot,access_lot,model_stock_production_lot,,1,1,1,1
access_move_line,access_move_line,model_stock_move_line,,1,1,1,1
access_product_template,access_product_template,model_product_template,,1,1,1,1
access_res_partner,access_res_partner,model_res_partner,,1,1,1,1
```

### `models/stock_production_lot.py`

```python
from odoo import api, fields, models

class StockProductionLot(models.Model):
    _inherit = "stock.production.lot"

    x_net_gold_weight_g   = fields.Float("净金重(g)", digits=(12, 3))
    x_total_weight_g      = fields.Float("总重(g)", digits=(12, 3))
    x_stone_weight_ct     = fields.Float("石重(ct)", digits=(12, 3))
    x_accessory_weight_g  = fields.Float("配件重(g)", digits=(12, 3))
    x_certificate_no      = fields.Char("证书号")
    x_labor_fee           = fields.Monetary("销售工费")
    x_labor_fee_type      = fields.Selection([("by_gram","克工费"), ("by_piece","件工费")], string="工费类型")
    x_note                = fields.Char("备注")
    currency_id           = fields.Many2one("res.currency", default=lambda s: s.env.company.currency_id, string="货币")
```

### `models/stock_move_line.py`

```python
from odoo import api, models
from odoo.exceptions import ValidationError

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    @api.constrains('lot_id', 'picking_id', 'qty_done')
    def _check_required_lot_fields_on_incoming(self):
        for line in self:
            if not line.picking_id or line.picking_id.picking_type_id.code != 'incoming':
                continue
            lot = line.lot_id
            # 只有追踪=序列号/批次的产品才校验
            if line.product_id.tracking != 'none':
                if not lot:
                    raise ValidationError("入库需要逐件/逐批登记序列号。")
                # 必填：净金重、总重；证书号可选看你需求（也可改为必填）
                if not lot.x_net_gold_weight_g or not lot.x_total_weight_g:
                    raise ValidationError("收货必须填写：净金重与总重（在序列号上）。")
```

### `models/product_template.py`

```python
from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_nature = fields.Selection([
        ("normal","正品"),
        ("special","特价"),
        ("gift","赠品"),
        ("material","物料"),
        ("part","配件"),
        ("campaign","活动款"),
    ], string="性质", default="normal")

    x_default_labor_fee_type = fields.Selection([
        ("by_gram","克工费"),
        ("by_piece","件工费"),
    ], string="默认工费类型")
```

### `models/res_partner.py`（可选：供应商策略）

```python
from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    x_require_certificate = fields.Boolean("进货要求证书号")
```

### `views/stock_production_lot_views.xml`

```xml
<odoo>
  <record id="view_stock_production_lot_form_jewelry" model="ir.ui.view">
    <field name="name">stock.production.lot.form.jewelry</field>
    <field name="model">stock.production.lot</field>
    <field name="inherit_id" ref="stock.view_production_lot_form"/>
    <field name="arch" type="xml">
      <xpath expr="//sheet/notebook" position="inside">
        <page string="珠宝属性">
          <group>
            <field name="x_certificate_no"/>
            <field name="x_net_gold_weight_g"/>
            <field name="x_total_weight_g"/>
            <field name="x_stone_weight_ct"/>
            <field name="x_accessory_weight_g"/>
            <field name="x_labor_fee"/>
            <field name="x_labor_fee_type"/>
            <field name="x_note"/>
          </group>
        </page>
      </xpath>
    </field>
  </record>
</odoo>
```

### `views/stock_picking_views.xml`（在收货明细就地编辑 Lot 字段）

```xml
<odoo>
  <record id="view_move_line_tree_inherit_jewelry" model="ir.ui.view">
    <field name="name">stock.move.line.tree.jewelry</field>
    <field name="model">stock.move.line</field>
    <field name="inherit_id" ref="stock.view_move_line_tree"/>
    <field name="arch" type="xml">
      <xpath expr="//tree/field[@name='lot_id']" position="after">
        <field name="lot_id.x_certificate_no" string="证书号"/>
        <field name="lot_id.x_net_gold_weight_g" string="净金重(g)"/>
        <field name="lot_id.x_total_weight_g" string="总重(g)"/>
        <field name="lot_id.x_stone_weight_ct" string="石重(ct)"/>
        <field name="lot_id.x_accessory_weight_g" string="配件重(g)"/>
        <field name="lot_id.x_labor_fee_type" string="工费类型"/>
        <field name="lot_id.x_labor_fee" string="销售工费"/>
      </xpath>
    </field>
  </record>
</odoo>
```

### `views/product_template_views.xml`

```xml
<odoo>
  <record id="view_product_template_form_inherit_jewelry" model="ir.ui.view">
    <field name="name">product.template.form.jewelry</field>
    <field name="model">product.template</field>
    <field name="inherit_id" ref="product.product_template_only_form_view"/>
    <field name="arch" type="xml">
      <xpath expr="//sheet/group/group" position="after">
        <group string="珠宝配置">
          <field name="tracking"/> <!-- 一码一物/一码多件 -->
          <field name="uom_id"/>  <!-- 计件/计重 -->
          <field name="x_nature"/>
          <field name="x_default_labor_fee_type"/>
        </group>
      </xpath>
    </field>
  </record>
</odoo>
```

### `views/res_partner_views.xml`（可选）

```xml
<odoo>
  <record id="view_partner_form_inherit_jewelry" model="ir.ui.view">
    <field name="name">res.partner.form.jewelry</field>
    <field name="model">res.partner</field>
    <field name="inherit_id" ref="base.view_partner_form"/>
    <field name="arch" type="xml">
      <xpath expr="//sheet/notebook/page[@name='sales_purchases']" position="inside">
        <group string="珠宝进货策略">
          <field name="x_require_certificate"/>
        </group>
      </xpath>
    </field>
  </record>
</odoo>
```

> 说明
>
> * **必填校验**通过 Python `@api.constrains` 在“收货（incoming）”强制：净金重、总重未填不可过账。
> * 证书号是否必填可按需加逻辑（例如供应商勾“要求证书”则强制）。
> * 上述视图把 Lot 字段拉到**收货明细列表**，操作员**就地录入**，无需逐个打开 Lot 表单。
> * POS 侧：你可以把“证书号”打印到标签并生成条码（若要标签模板，我可以再给 QWeb 模版示例）。

---

# 最后给你一张“属性落位清单”（方便核对）

| 属性            | 方案一（纯 UI）          | 方案二（导入模板）      | 方案三（模块）                |
| ------------- | ------------------ | -------------- | ---------------------- |
| 一码一物/一码多件     | 产品模板·Tracking      | 模板 CSV 字段      | 模板字段                   |
| 计件/计重         | 模板·UoM（Unit/g）     | 模板 CSV 字段      | 模板字段                   |
| ID/条码/名称      | 模板基本字段             | 模板/变体 CSV      | 模板/变体字段                |
| 大类/类别         | 产品分类（父/子）          | 分类 CSV         | 同左                     |
| 成色/规格/工艺      | 属性（动态生成变体）         | 属性/变体 CSV      | 同左                     |
| 主石            | 若选型→属性；否则留给质检/标签   | 同左             | 也可做 Lot 字段（扩展）         |
| 净金重/总重/石重/配件重 | 质量检查/标签文本          | 质量控制点 CSV（仅配置） | **Lot 真字段 + 入库必填**     |
| 证书号           | **= 序列号名**         | 导入 Lot 时用“名称”  | **Lot 字段（也可同步到 name）** |
| 销售工费/工费类型     | 质量记录/或 POS 作为独立产品行 | 不适用            | **Lot 真字段（类型+数值）**     |
| 成本            | 采购价 + 估价           | 供应商价 CSV       | 同左                     |
| 标价/批发价        | 价目表                | 价目表/规则 CSV     | 同左                     |
| 性质（正品/特价/赠品…） | 用分类/POS 分类表示       | 分类 CSV         | **模板选择字段**             |
| 备注            | 质量备注/附件/标签         | 不适用            | **Lot 备注字段**           |

---

如果你要继续推进，我可以按你当前 Odoo 18 的部署方式，基于“方案三”的代码骨架补齐：

* 增加 **QWeb 标签模板**（把证书号/净金重等打印出来）；
* （可选）POS 行价计算 hook（“金价+工费”自动算价）；
* （可选）把供应商策略（证书必填、默认工费类型）自动带入入库。

你更偏向哪条路线？我就按那条给你“可直接用的清单/或代码包”。







  
  

# #############################################################################################################

# #############################################################################################################
  
# #############################################################################################################

好的，我直接给你一套“可安装的模块 + 批量导入模板”，并配上一步步使用说明。你拿去放进 Odoo 18 的 `addons` 目录，更新应用列表即可安装使用。

# 交付物

* 模块压缩包（含源码、视图、向导、权限、README、示例模板）
  [下载模块：jewelry\_lot\_intake.zip](sandbox:/mnt/data/jewelry_lot_intake.zip)

# 模块做了什么

* 在\*\*序列号/批次（stock.production.lot）\*\*上新增字段：净金重、总重、石重(ct)、配件重、证书号、销售工费、工费类型（克/件）、备注。
* 在\*\*收货明细列表（stock.move.line）\*\*上就地展示这些 Lot 字段，方便入库时查看/微调。
* 增加“性质（正品/特价/赠品/物料/配件/活动款）”“默认工费类型”等**产品模板**字段（可选用）。
* 提供一个**批量导入收货向导**：上传 CSV → 自动创建收货单、创建/匹配 Lot、写入上述字段、设置数量与单价（cost）→ 自动确认并过账（可选）。

# 安装步骤

1. 将压缩包解压后的 `jewelry_lot_intake/` 放到服务器的自定义 addons 目录（例如 `/odoo/custom/addons/`）。
2. 登录 Odoo，进入【应用】，点击“更新应用列表”，搜索 **Jewelry Lot Intake** 并安装。
3. 确保已安装：库存、采购、销售、POS（模块已声明依赖）。

# 使用步骤（一次性批量入库）

1. 预置产品：请先在【库存 › 产品】中建立商品（名称、条码、内部参考、变体属性、追踪方式=按唯一序列号或按批次、计量单位等）。
2. 打开菜单：**库存 › 珠宝导入 › 批量导入收货**。
3. 选择仓库（会自动带出该仓库的收货类型），勾选“自动验证过账”（可选）。
4. 上传 CSV 文件（UTF-8，默认逗号分隔）。

   * 模块内自带模板：`static/description/jewelry_lot_intake_template.csv`（也打包在压缩包里）。
5. 点击“开始导入”。系统会：

   * 创建一个收货单（Receipts）；
   * 每行匹配产品（条码 → 内部参考 → 名称），创建/找到对应 **Lot**（lot\_name），写入净金重/总重/石重/配件重/证书号/工费/备注等；
   * 为每行创建 stock move + move line，设置 `qty_done`，并在提供 `cost` 时用于估价；
   * 自动确认并过账（若勾选自动过账），并处理“即时过账/补货”向导。

# CSV 模板字段说明

表头（必须）：

```
product_barcode, product_code, product_name,
lot_name, certificate_no,
net_gold_weight_g, total_weight_g, stone_weight_ct, accessory_weight_g,
labor_fee_type, labor_fee, note,
qty, uom, cost
```

填写规则：

* **产品匹配优先级**：`product_barcode` → `product_code`（内部参考 default\_code）→ `product_name`。
* **lot\_name**：序列号或批次号。**序列号追踪的商品，qty 必须为 1 且 lot\_name 唯一**。
* **labor\_fee\_type**：`by_gram` 或 `by_piece`。
* **uom**：留空则用产品默认单位（如 `Unit` 或 `g`）。
* **cost**：本次入库的单位成本（用于无采购订单的估价，未填则回退到产品 `standard_price`）。

# 关键校验与业务逻辑

* 收货（incoming）过账前会强制检查：**Lot 上净金重 / 总重必填**。
* 对追踪产品未提供 lot\_name 会报错；对 **序列号**追踪且 `qty != 1` 会报错。
* 每行建一条 move + 一条 move line（简单直观，适合小批量；如需超大批量导入，可再做聚合优化）。

# 常见问题 & 提示

* **我还没有产品**：向导不会创建产品，请先建好产品模板/变体（含追踪方式）。
* **成本如何进账**：无采购订单时，使用 CSV 的 `cost` 作为入库单价参与估价；建议长期走 PO 以形成完整成本链。
* **POS 如何卖**：建议在标签里打印 `lot_name`（通常与证书号一致）做条码，POS 扫码直达那一件。
* **模板中的重量单位**：模块字段以 g / ct 计；请在称重后填入对应数值。
* **工费**：支持件工费与克工费两种记录，具体售价可配合价目表或定制 POS 价格计算规则（如后续你需要“金价+工费”自动算价，我可以在此模块基础上再加一个 POS 扩展）。

如果你想要我继续：

* 我可以帮你把 **标签(QWeb)** 模板补上（把证书号/序列号条码、成色、工艺、净金重等打印出来）；
* 或新增一个 **“按金价+工费自动计算 POS 行价”** 的小扩展（读取 lot 的净金重和工费类型/金额，结合当日金价计算）。


好了，给你加上了一个**58×40mm 热敏标签**的 QWeb 模板（带条码、成色/工艺/规格、净金/总重/石重、证书号等），直接绑定在“**批次/序列号（stock.production.lot）**”的打印菜单里。

* 更新后的模块包：
  [下载更新模块：jewelry\_lot\_intake.zip](sandbox:/mnt/data/jewelry_lot_intake.zip)

# 标签模板包含的内容

* 标题：产品变体名（含属性）
* 辅助信息：内部编码、产品分类路径
* 属性行：成色 / 工艺 / 规格（自动从变体属性读取）
* 重量行：净金重(g) / 总重(g) / 石重(ct)（从 lot 字段）
* 证书号：从 lot 的 `x_certificate_no`
* 条形码：**Code128**，编码为 lot 的 `name`（通常即序列号/证书号），下方有人可读文本

# 使用方法

1. 安装/升级模块后，进入任意**序列号**记录（库存 › 主数据 › 批次/序列号）。
2. 顶部【打印】下拉会出现“**Jewelry Lot Label**”。
3. 点打印即可生成 PDF；纸张为 **58×40mm**，适合窄幅热敏标签机。

# 可选定制点（我已经预留了样式位，后续调整很方便）

* 改纸张尺寸：在模块的 `report_jewelry_lot_label.xml` 里有 `report.paperformat`（`paperformat_label_58x40`），把 `page_width/page_height` 改为需要的 mm 尺寸即可。
* 条码类型：把 `<img src="/report/barcode?...type=Code128">` 的 `type=` 改为 `QR` 可输出二维码（若你希望标签扫证书用二维码）。
* 字段取值：目前“成色/工艺/规格”是从产品的属性值集合里**按属性名**筛选（`成色/工艺/规格`），你的属性名与此一致即可自动显示。

需要我再加一个**产品标签（product.product）**版本或把**标价/货号/门店简称**等一起印上吗？我可以继续把模板拓展成两列/三列排版（A4 批量打）或者 POS 票据风格的小票。





  
  

# #############################################################################################################

没问题，这里把 **“在 POS 启用价目表，并把‘零售价/批发价/活动价’加入可用列表”** 做成一步步的操作手册（Odoo 18，纯界面）：

# 步骤 1：在销售里开启价目表功能

1. 进入【销售 › 配置 › 设置】
2. 在“定价（Pricing）”区：勾选 **“价目表（Pricelists）”**

   * 推荐选择 **“多价格（Multiple prices per product）”** 或 **“高级价格规则（Advanced price rules）”**（后者能按分类、最小数量、时间窗口等做规则）。
3. 点击【保存】。

# 步骤 2：建三套价目表（零售价/批发价/活动价）

1. 到【销售 › 产品 › 价目表】→【新建】：

   * ① **零售价**（Retail）：币种=公司本位币；“折扣策略”建议选“显示折扣”（POS上可看到原价/折扣）。
   * ② **批发价**（Wholesale）：可在“价目表项”里新增规则，如“对全部商品打 9 折”或“按某分类打 8.5 折”。
   * ③ **活动价**（Promotion）：新增规则时设置**有效期**（起止日期），可对某些商品/分类**固定特价**或额外折扣。
2. 在每个价目表中，点【添加项目（Add Item）】定义规则：

   * 适用范围：全部产品 / 指定分类 / 指定产品
   * 计算：固定价 / 折扣 / 公式
   * 有效期：用于“活动价”自动生效/失效
   * 最小数量（可选）：用于批量价

> 小贴士：如果你只想把“零售价”=产品的销售价（List Price），零售价价目表可以不加任何规则，系统会直接用产品的“销售价”。

# 步骤 3：在 POS 配置里启用并选择价目表

1. 进入【POS › 配置 › 销售点】（不是“设置”页，而是“销售点列表”）
2. 打开你的门店 POS（例如“门店一”）
3. 在“**定价**/Pricing”区域：

   * 勾选 **“使用价目表（Use Pricelists）”**
   * **默认价目表（Default Pricelist）**：选 **零售价**
   * **可用价目表（Available Pricelists）**：多选 **零售价、批发价、活动价**
   * （可选）勾选 **“使用客户的价目表”**：收银员选中客户后，会自动切换到该客户卡片上配置的价目表
4. 点击【保存】。

```
快速对照
Flexible Pricelists ＝ 启用“使用价目表（Use Pricelists）”。开了它之后，页面会出现 Default Pricelist 和 Available Pricelists 两个下拉框。
Price Control ＝ 允许/限制手动改价（行单价）。
Line Discounts ＝ 行级折扣开关（每行可输入 % 折扣）。
Global Discounts ＝ 整单折扣按钮开关。
Pricer ＝（可选）在POS前台快速对比/切换价目表的侧边面板。
```

# 步骤 4：刷新 POS 前端缓存并验证

1. 回到【POS › 仪表板】
2. 如果该 POS 正在运行，先【关闭会话】并【过账】（或用右上角“…”的 **更新** 按钮）
3. 重新【开始会话】进入前端：

   * 右上角或结账区会出现 **“价目表/Price List”切换**（不同主题位置略有不同）
   * 切换到“批发价/活动价”，添加同一商品，应看到价格变化
   * 选择绑定有“批发价”的客户，系统应自动套用其价目表

# 常见卡点与排查

* **POS里没有“价目表”选项**：回检查【销售 › 设置】里“价目表”是否已开启并保存。
* **价目表切换了但价格不变**：

  * 该价目表是否有覆盖该商品/分类的“项目（规则）”？
  * POS 是否已刷新/重启会话以加载最新设置？
  * 价目表币种必须等于 POS 公司币种（或系统已启用多币种且汇率生效）。
* **客户自动套价无效**：客户卡片（【联系人】→打开客户→“销售与采购”）里是否指定了价目表？

# 进阶建议（可选）

* 想让 POS 前端显示“原价-现价-折扣”：在价目表设置里把“折扣策略”选成 **“显示折扣”**。
* 想做“满件/满额减、门店促销券”：可再启用 **优惠券与促销（Promotions & Coupons）** 模块配合使用（与价目表互补）。
* 如果你的黄金业务要“金价 + 工费”自动算价：价目表做固定价不够用，需要在我们刚给你的模块上再加 POS 扩展逻辑（读取 lot 的净金重/工费类型 + 当日金价）——随时可以帮你加。

需要我把“批发价=全店 9 折、活动价=某分类限时固定价”的**图文示例**或**CSV 批量导入模板**也给你吗？我可以按你的商品分类结构示范 3 条常用规则。



  

# #############################################################################################################

# odoo18的Product Images应用以及图片的储存机制是什么样的，我可以直接通过在模板、变体直接上传图片，但是我也看到批量上传模板可以使用base64编码上传。

下面把 \*\*Odoo 18 的 Product Images（产品图片）\*\*能做什么、图片放在哪里、底层如何存、批量导入怎么做、以及 POS/Website 的显示规则一次讲清。

# 能做什么（对象 & 场景）

* **主图**：放在产品模板 `product.template` 或产品变体 `product.product` 的 `image_1920` 字段。

  * **POS / 后台**默认展示主图。
  * 多变体时，**变体图优先于模板图**。
* **图库/多图**：模型 `product.image`（“Images/图片”“Extra Images/附加图片”页签/按钮），主要给 **Website 电商** 用（详情页轮播、按属性值显示不同图）。POS 仅取主图。

# 存储机制（你需要知道的底层）

* 字段类型：`fields.Image`（如 `image_1920`、`image_1024`、`image_256`、`image_128`）。

  * **`image_1920` 是原图**（建议≤1920px 边长）；其余是自动生成的缩略图，用于不同界面提速。
* 物理存储：并**不直接存到产品表**，而是生成一条 **ir.attachment** 附件记录（字段 `res_model`、`res_id`、`res_field=image_1920`）。

  * 文件数据默认落地到 **filestore**：`~/.local/share/Odoo/filestore/<db_name>/<hash_path>`（Linux 为例），附件表保存 `store_fname/sha1/mimetype/file_size` 等元数据。
  * 只有个别特殊配置才把二进制放数据库里。大多数部署=**磁盘文件 + 数据库元数据**。
* 访问与缓存：前端通过 **`/web/image/<model>/<id>/<field>`** 或 `/web/image/<attachment_id>` 路由读取，带 ETag/缓存；Odoo 会按需要下发相应尺寸。
* 备份要点：备份/迁移时务必同时备 **数据库** 和 **filestore**，两者缺一不可。

# 上传方式（手工 & 批量）

## 手工（单张）

* 打开产品表单 → **Edit** → 左上圆形图片框 **上传/拖拽/粘贴** → **Save**。
* 变体图：进入 **Variants** 打开某个变体，在变体表单左上上传。

## 批量（CSV 导入 base64）

> 导入时给字段 `image_1920` 赋值，导入后 Odoo 会把 base64 解码成附件并写入 filestore。

* 导入到 **产品模板**（`product.template`）或**产品变体**（`product.product`）均可；多变体且每个图不同→导到变体更合适。
* **CSV 最小字段示例**：

  ```
  default_code,image_1920
  PEND001,data:image/jpeg;base64,/9j/4AAQSkZJRgABAQ...
  PEND002,data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...
  ```

  * `default_code`：你用来匹配目标记录的唯一键（也可用外部ID `id`）。
  * `image_1920`：**带前缀**的 base64（`data:image/jpeg;base64,` 或 `data:image/png;base64,`）。
* 入口：对应列表视图（Products / Product Variants）右上 **Import** → 映射 → **Test** → Import。
* 体量建议：单图 0.3–1MB、800–1200px；更大也行，但导入慢、占空间多。

> 补充：默认 Import 不会“从 URL 抓图”。要从 URL 拉取需写小脚本/模块（Python `requests` 下载→写入 `image_1920`），或先离线转 base64。

# 放在模板还是变体？

* **无变体**：模板上设图即可。
* **有变体**：每个变体单独设图（POS、Website 体验更好）；没设才回退用模板图。

# POS / Website 显示规则

* **POS**：只读主图（优先变体），不读图库；更换图片后请到 **POS → Dashboard → … → Update/同步数据** 刷新前端缓存。
* **Website**：商品详情可显示**主图 + 图库**；图库里的图片还可按属性值过滤（如“成色=足金”显示对应图）。

# 维护与清理

* 删除产品/变体时，关联的字段型附件（`res_field=image_1920`）会随记录清理；图库 `product.image` 记录删除后也会清理对应附件。
* 批量替换图：再次给 `image_1920` 赋值即可覆盖；缩略图会自动重建。
* 多公司：图片归属取决于产品所属公司；切公司查看/编辑。

# 常见问题速答

* **为什么我导了 base64，库里看不到大字段？**
  因为**文件在 filestore**，产品表里只有指向附件的引用。
* **能只给图库、不改主图吗？**
  可以：在 `product.image` 里新增图片；主图仍在 `image_1920`。
* **POS 没显示新图？**
  90% 是没刷新 POS 数据；另外确认商品 **Available in POS** 且在对应 **POS Category**，必要时给 POS 使用的库位加库存或关闭 “Hide out-of-stock”。

---

如果你告诉我你准备用“模板统一图”还是“变体各自图”，我可以马上给你一份对应的 **CSV 模板**（含 1 行演示），照着改就能导。还可以给你一个 5 行的 PowerShell/Python 小脚本，把本地图片批量转成 base64 CSV。

# 
Product Images这个应用主要的作用是做什么的，怎么用





  
  

# #############################################################################################################

# 在pos店铺里销售商品后，会有receipt收据小票在页面右侧显示出来，这个小票如何按我需要的格式来编辑，给我两个方案，一个是手动编辑的，一个是代码模块方式的，之前我也有在销售应用模块里做了一个销售票据打印的热敏纸的模块，可以用于pos收据吗。


可以的，POS 收据（右侧的 ticket/receipt）可以按你需要的格式来改。给你两种落地方式：

---

# 方案 A｜“手动编辑”（不写代码，用后台视图继承）

前提：开启开发者模式（设置 → 激活开发者模式）。

1. 打开【设置 → 技术 → 用户界面 → 视图】
2. 搜索 View 类型=**QWeb**，关键字输入：`OrderReceipt` 或 `point_of_sale` `Receipt`

   * 目标模板一般叫 **`point_of_sale.OrderReceipt`**（Odoo 18 新 POS 的收据模板）。
3. 新建一条 **QWeb 继承视图**（重要：不是复制原视图，而是“继承”）：

   * 名称：随意（如 `POS Receipt Custom`）
   * 视图类型：**QWeb**
   * 继承自（inherit\_id）：选择 **point\_of\_sale.OrderReceipt**
   * 架构（XML）里写你的改动（示例：替换整张收据主体，并加上你关心的字段）

```xml
<template id="pos_receipt_custom_inherit" inherit_id="point_of_sale.OrderReceipt" name="POS Receipt Custom">
  <!-- 把整张收据主体替换为你的布局 -->
  <xpath expr="//div[@class='pos-receipt']" position="replace">
    <div class="pos-receipt my-receipt">
      <div class="hdr">
        <div class="shop"><t t-esc="receipt.company.name"/></div>
        <div class="row">
          <span>门店：</span><span t-esc="receipt.config_name"/>
          <span>单号：</span><span t-esc="receipt.name"/>
        </div>
        <div class="row">
          <span>收银员：</span><span t-esc="receipt.cashier or (receipt.employee and receipt.employee.name)"/>
          <span>时间：</span><span t-esc="receipt.date.localestring"/>
        </div>
        <t t-if="receipt.client">
          <div class="row"><span>客户：</span><span t-esc="receipt.client.name"/></div>
        </t>
      </div>

      <div class="cutline"></div>

      <div class="lines">
        <t t-foreach="receipt.orderlines" t-as="line">
          <div class="l">
            <div class="l1">
              <span class="name"><t t-esc="line.product_name"/></span>
              <span class="qtyprice"><t t-esc="line.quantity"/> × <t t-esc="line.unit_price"/></span>
            </div>
            <t t-if="line.discount and line.discount &gt; 0">
              <div class="discount">折扣：<t t-esc="line.discount"/>%</div>
            </t>
            <!-- 若你的 POS 启用序列号，默认导出里通常有 line.lots，可逐个显示 -->
            <t t-if="line.lots">
              <div class="lots">
                <t t-foreach="line.lots" t-as="lt">
                  <div class="lot">证书/序列：<t t-esc="lt.name"/></div>
                </t>
              </div>
            </t>
            <div class="sum"><span>小计：</span><b><t t-esc="line.price_with_tax"/></b></div>
          </div>
        </t>
      </div>

      <div class="cutline"></div>

      <div class="totals">
        <div><span>数量：</span><t t-esc="receipt.total_quantity"/></div>
        <div><span>合计（含税）：</span><b><t t-esc="receipt.total_with_tax"/></b></div>
        <t t-if="receipt.total_discount and receipt.total_discount &gt; 0">
          <div><span>总折扣：</span>-<t t-esc="receipt.total_discount"/></div>
        </t>
      </div>

      <div class="cutline"></div>

      <div class="payments">
        <t t-foreach="receipt.paymentlines" t-as="pl">
          <div><span t-esc="pl.name"/>：<b><t t-esc="pl.amount"/></b></div>
        </t>
        <t t-if="receipt.change and receipt.change &gt; 0">
          <div><span>找零：</span><b><t t-esc="receipt.change"/></b></div>
        </t>
      </div>

      <div class="cutline"></div>

      <div class="foot" style="text-align:center">
        <t t-if="receipt.barcode">
          <img t-att-src="'/report/barcode?type=Code128&amp;value=' + encodeURIComponent(receipt.barcode) + '&amp;width=450&amp;height=120'"/>
        </t>
        <div>谢谢惠顾 / THANK YOU</div>
      </div>
    </div>
  </xpath>

  <!-- 简单内联样式（热敏友好） -->
  <xpath expr="//head" position="inside">
    <style>
      .my-receipt { font-size:12px; line-height:1.2; font-family: Arial, sans-serif; }
      .my-receipt .shop { text-align:center; font-weight:700; font-size:14px; }
      .my-receipt .row { display:flex; gap:8px; justify-content:center; }
      .my-receipt .cutline { border-top:1px dashed #000; margin:6px 0; }
      .my-receipt .l1 { display:flex; justify-content:space-between; }
      .my-receipt .name { max-width:70%; overflow:hidden; text-overflow:ellipsis; }
      .my-receipt img { max-width:100%; height:auto; }
    </style>
  </xpath>
</template>
```

4. 保存视图。
5. 回【POS 仪表板】关闭当前会话并过账 → 重新开始会话，收据即按你的模板显示。

> 备注：POS 收据使用**前端 QWeb 模板**，这套方法就是“在后台创建一个继承 QWeb 的新视图”，不需要打包模块，也能立即生效。
> 想显示“序列号/证书号”，用 `line.lots` 循环（如上），无需额外 JS。如果你想显示更复杂的 lot 字段（比如净金重），就需要扩展 POS 的 JS 导出（见方案 B 的可选扩展）。

---

# 方案 B｜“代码模块”方式（推荐稳定部署）

我帮你打好了一个可安装模块，内置热敏友好的收据模板，安装即可用：

* 模块下载：**[jewelry\_pos\_receipt.zip](sandbox:/mnt/data/jewelry_pos_receipt.zip)**
  依赖：`point_of_sale`；安装后自动把模板注入到 POS 前端资源中（`point_of_sale.assets`）。

## 安装

1. 把 `jewelry_pos_receipt` 目录放到自定义 addons；更新应用列表并安装。
2. 关闭并过账当前 POS 会话 → 重新开启；新模板立即生效。

## 模块做了什么

* 通过 **assets** 将 `static/src/xml/pos_receipt.xml` 注入 POS 前端。
* 用 `t-extend="point_of_sale.OrderReceipt"` + `t-jquery` 替换默认 `.pos-receipt`，重排版头/行/合计/支付/条码。
* 默认支持显示 `line.lots`（有序列号时）。
* 样式按 58/80mm 热敏友好（行距、虚线分割、溢出省略）。

> 想把“净金重/证书号/工费”等 **lot 扩展字段**也显示到收据：
> 需要在 POS 的 `Orderline.export_for_printing()` 加一段小扩展，把 lot 上的字段并入 `line.lots`。若你用我之前提供的 `jewelry_lot_intake` 模块保存了这些字段，我可以再给你一个很小的 JS 补丁模块，把 `x_net_gold_weight_g / x_certificate_no ...` 添加到 `receipt.orderlines[*].lots[*]`，然后在模板里显示即可。

---

# 你现有的“销售模块热敏票据”能直接用于 POS 吗？

**不能直接用。**

* 销售模块的报表是 **服务端 QWeb（qweb-pdf/html）** 报表，触发点是销售订单/发票；
* POS 收据是 **前端 QWeb（assets）** 模板，由 POS 前端（浏览器/IoT）即时渲染并打印。

但**可以复用样式和版式**：把你销售报表的 HTML 结构/CSS 迁移到 POS 收据模板（方案 A/B 的模板）中；
或者你也可以在 POS 做“开票”，打印发票报表（那是另一条链路，不是右侧收据）。

---

# 常见问题

* **我改了模板但前台没变**：确保关闭会话并过账再开启新会话；若装了模块，清浏览器缓存（或换隐私窗口）。
* **看不到序列号**：确保 POS 产品启用了追踪（序列号/批次），并在售卖时选择/扫描了 lot；导出的 `line.lots` 才会有数据。
* **条码不显示**：`/report/barcode` 走服务端路由，离线模式下可能取图失败；IoT/在线时正常。可以退而求其次显示文本码。

如果你给我你想要的排版草图（示意图/字段位置），我可以直接把“净金重/证书号/工费”那一行也加进 POS 收据模板，并附上 JS 扩展把这些 Lot 字段带进收据。






  
  

# #############################################################################################################


非常好的问题 👍。
在 **Odoo 服务** 中，常见的两个端口号 —— **8069** 与 **8072** —— 虽然经常同时出现，但它们的作用完全不同。下面我给你详细拆解一下两者的区别与联系。

---

## 🌐 一、Odoo 的主要端口功能概览

| 端口       | 协议             | 默认用途      | 说明                                 |
| -------- | -------------- | --------- | ---------------------------------- |
| **8069** | HTTP           | Web 主服务端口 | 用于浏览器访问 Odoo 前端网页、HTTP JSON-RPC 接口 |
| **8072** | 长连接（websocket） | 实时通信通道    | 用于实时通知、聊天、POS 同步、IoT 通信等           |

---

## 🧩 二、端口 8069：Odoo 主 HTTP 服务端口

这是 **Odoo 的核心 Web 服务** 端口。
当你在浏览器访问

```
http://localhost:8069
```

或

```
http://your-server-ip:8069/web
```

实际上访问的就是 **Odoo 的 HTTP 服务器（Werkzeug / WSGI）**。

### 作用：

* 提供网页前端访问（Web UI）
* 提供 JSON-RPC / XML-RPC API 接口
  例如：`/web/dataset/call_kw`、`/jsonrpc` 等
* 所有模块的 HTTP 控制器（Controllers）都跑在这个端口上
  比如 `/shop`, `/web`, `/pos`, `/api`, `/mail`

### 举例：

```bash
curl http://127.0.0.1:8069
```

你会看到返回的 HTTP 头：

```
Server: Werkzeug/2.x Python/3.x
Location: /web/login
```

---

## ⚡ 三、端口 8072：Odoo 长连接服务（bus/websocket）

从 Odoo 13 开始（Odoo 18 当然包含），系统默认会启动一个 **长连接服务（Bus Service）**，用于“实时”推送消息。
该服务通常监听 **8072 端口**。

### 作用：

这是一个基于 **websocket / longpolling** 的异步通信服务。
它被用在以下功能中：

| 场景                            | 说明                       |
| ----------------------------- | ------------------------ |
| **即时消息（Discuss 模块）**          | 实时显示“对方正在输入…”、新消息即时推送    |
| **POS 前端与后端同步**               | 前端 POS 页面与 Odoo 后台保持实时通信 |
| **通知提醒（顶部铃铛）**                | 实时通知系统消息、任务提醒            |
| **IoT Box、Livechat、Mail Bus** | 需要双向通信的服务模块              |

### 工作原理：

Odoo 的主服务（8069）中有一个模块 `bus`，它会将实时消息放入 Redis 或内存队列；
而 8072 端口负责 WebSocket 长连接，将这些消息实时推送给前端浏览器。

---

## 🔧 四、查看实际配置（在 odoo.conf 中）

你可以在 Odoo 的配置文件（通常 `/etc/odoo/odoo.conf` 或 `/opt/odoo/odoo.conf`）中看到类似配置：

```ini
[options]
xmlrpc_port = 8069
longpolling_port = 8072
proxy_mode = True
```

这说明：

* `xmlrpc_port` → HTTP / JSON-RPC 主端口
* `longpolling_port` → 实时消息（bus）端口

---

## 🧠 五、在生产环境（如 nginx 代理）中两者的关系

在生产部署中，你常常会看到 nginx 反代配置如下：

```nginx
upstream odoo {
    server 127.0.0.1:8069;
}
upstream odoo-longpolling {
    server 127.0.0.1:8072;
}

server {
    listen 80;
    server_name myodoo.com;

    # 主页面请求
    location / {
        proxy_pass http://odoo;
    }

    # 实时通信请求
    location /longpolling {
        proxy_pass http://odoo-longpolling;
    }
}
```

👉 nginx 会将普通网页请求转发到 **8069**，
将实时通信请求 `/longpolling` 转发到 **8072**。

---

## ✅ 六、总结对比

| 项目     | 8069                    | 8072                          |
| ------ | ----------------------- | ----------------------------- |
| 服务类型   | 主 Web 服务                | 长连接 / Bus 服务                  |
| 协议     | HTTP/HTTPS              | WebSocket / Longpolling       |
| 提供功能   | 网页、API、控制器              | 实时通知、消息推送                     |
| 模块依赖   | 所有 Web 模块               | `bus`, `im_livechat`, `pos` 等 |
| 常见反代路径 | `/web`, `/api`, `/shop` | `/longpolling`                |
| 是否必须   | ✅ 必须                    | ⚙️ 可选（若使用实时功能则必须）             |

---

如果你只是想运行一个单机简化版 Odoo（不需要即时通信、POS、聊天等功能），
**8072 可以不开放或关闭 bus 模块**；
但如果你使用 POS 或消息模块，**必须同时运行 8072 端口**。

---

是否希望我再帮你画一张「Odoo 端口架构示意图」，标出 8069/8072 与 nginx/浏览器之间的通信流向？（会更直观）


  

# #############################################################################################################

短答：**是的**，最常见做法是把外部的 **80/443** 统一入口交给 Nginx，然后 **按路径把普通 HTTP 请求转到 8069、把长连接转到 8072**。WebSocket/长轮询也可以完全走 **80/443**（只要 Nginx 正确设置 Upgrade/Connection 头），无需再开公网 8072。

下面给你三种常见架构，按需选：

---

# 方案 A（推荐）：单域名单端口，按路径分流

* 外部只开放 **80/443**。
* 普通请求 → `127.0.0.1:8069`
* 长连接（/longpolling） → `127.0.0.1:8072`
* 好处：简单、安全（8072 不对公网暴露）、兼容公司/酒店/咖啡店网络（很多网络只放行 80/443）。

```nginx
upstream odoo {
    server 127.0.0.1:8069;
}
upstream odoo_longpolling {
    server 127.0.0.1:8072;
}

server {
    listen 80;
    server_name odoo.example.com;
    # 建议配合 443 + 证书，这里仅示意

    # Odoo 主站
    location / {
        proxy_pass http://odoo;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_read_timeout 300;
        proxy_send_timeout 300;
        proxy_buffering off;
    }

    # 长连接（bus/websocket/longpolling）
    location /longpolling {
        proxy_pass http://odoo_longpolling;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_read_timeout 720s;   # 长一点，避免误断
        proxy_send_timeout 720s;
        proxy_buffering off;
    }
}
```

Odoo 侧确保：

```ini
[options]
proxy_mode = True
xmlrpc_port = 8069
longpolling_port = 8072
```

---

# 方案 B：用不同端口对外区分（例如直接开放 8072）

* 外部开放 **80/443（HTTP）** + **8072（WebSocket）**。
* 好处：网络层面更直观地区分流量；某些防火墙/ACL 基于端口做策略时更方便。
* 风险：多一个公网入口需要加固；某些公司网络会拦截非常规端口（8072 可能被阻断）。

做法 1：**直出 8072**（不经 Nginx）
直接把服务器的 8072 暴露公网（不建议在生产用，难做统一限流/审计/证书）。

做法 2：**Nginx 再开一个对外监听端口转发到 8072**（更安全）：

```nginx
# 与方案A并存：额外开一个公网 8072
server {
    listen 8072;
    server_name odoo.example.com;

    location / {
        proxy_pass http://127.0.0.1:8072;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 720s;
        proxy_send_timeout 720s;
        proxy_buffering off;
    }
}
```

---

# 方案 C：用子域名分流（例如 ws.example.com 专管长连接）

* 外部仍然只用 **80/443**，但用 **不同域名**。
* 好处：清晰的 DNS/监控/证书/限流策略；CDN 或 WAF 也能独立配置。
* 例子：`odoo.example.com` → 8069，`ws.example.com/` → 8072

```nginx
# odoo.example.com → 8069
server {
    listen 443 ssl;
    server_name odoo.example.com;
    location / { proxy_pass http://127.0.0.1:8069; ...同上... }
}

# ws.example.com → 8072
server {
    listen 443 ssl;
    server_name ws.example.com;
    location / {
        proxy_pass http://127.0.0.1:8072;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 720s;
        proxy_send_timeout 720s;
        proxy_buffering off;
    }
}
```

---

## 关键细节与最佳实践

* **一定启用 `proxy_mode = True`**，并在反代时正确传递 `Host`/`X-Forwarded-Proto`，否则 Odoo 里生成的绝对 URL、回调、Cookies 可能异常。
* **WebSocket 必备头**：`Upgrade` 与 `Connection`；同时设置较长的 `proxy_read_timeout`。
* **强烈建议统一走 443（HTTPS）**：WebSocket 也可走 `wss://`，在办公网络/出海环境更稳。
* **不要把 8069/8072 直接暴露公网**（除非你清楚后果并做好了 WAF/ACL/限流/审计）。
* **POS/实时通知** 场景：更倾向 **方案 A 或 C**，兼容性最好。
* 若用云负载均衡（如阿里云 SLB / NLB）：确认 **支持 WebSocket**，并把 **空闲超时** 调大。

---

## 结论

* 你说的理解没错：**通过 Nginx，长连接完全可以走 80/443**，不必单独开放 8072。
* 如果你**确实想用端口区分**，可以采用 **方案 B** 或 **方案 C**；
  但从**安全性与可达性**综合考虑，**方案 A（单域名单端口路径分流）**通常是最佳选择。

需要我基于你的域名/证书/环境（HTTP 还是 HTTPS、是否有 WAF/CDN）给一份可直接粘贴上线的完整 Nginx 配置吗？



  

# #############################################################################################################

# 盘点 库存

好的！下面把 Odoo 18 里“库存查询统计”和“盘点（库存调整）”两块，按实际操作路径一步步讲清楚。你可以直接照着点。

# 一、库存查询与统计（日常查看）

## 1）看“在手/预计”数量与分布

* 路径：**库存 → 产品 → 产品/产品变体**

  * 打开某产品，页上方有 **在手** / **预测**（预计）按钮。
  * 点“在手”→ 进入“当前库存（Quants）”，看每个**库位**的数量分布。
  * 右上角用 **筛选/分组**：按“库位 / 批次 / 包裹 / 所有者 / 公司”等查看。

## 2）查看所有产品的当前库存（Quants 总表）

* 路径：**库存 → 报表 → 当前库存**（或“产品库存”）

  * 可筛选：产品、库位、公司；
  * **分组**：库位→产品，或产品→库位；
  * 显示的是“系统理论数”（理论库存），用于对账与找差异。

## 3）查看库存移动（哪来哪去）

* 路径：**库存 → 报表 → 库存移动**

  * 按日期、产品、拣货类型（收货/发货/内部调拨）筛选。
  * 常用“分组”：产品、来源位置、目标位置、拣货单状态、负责人员。

## 4）看预测库存（考虑未来收/发）

* 路径：**库存 → 报表 → 预测库存**

  * 选产品，能看到基于已确认但未完成的采购/销售/制造/调拨后的预计可用量。
  * 适合做补货与承诺发货判断。

## 5）按批次/序列号查询

* 先确保开启：**库存 → 配置 → 设置 → 启用“批次/序列号”**。
* 路径：**库存 → 产品 → 批次/序列号**

  * 搜索某批/序列 → 点进详情，看它在哪个库位、数量、入库/出库历史。

## 6）库存估值（给财务/成本）

* 路径：**库存 → 报表 → 库存估值**（需“永久盘存”并配置估值方法）

  * 支持按**产品、分类、库位**分组；
  * 与会计模块联动时，可核对存货科目余额。

> 小贴士
>
> * 多公司：右上角切换公司查看对应数据。
> * 多仓库/多步收发：看清 **WH/Input / WH/Quality / WH/Stock** 等位置；货未“上架”到 WH/Stock，不计在手。
> * 过滤器：报表有日期/状态过滤，查看异常先清空过滤器再看。

---

# 二、盘点（库存调整）——标准流程

目标：对“系统理论数（Quants）”做实物盘点，录入“实盘数”，生成**库存调整分录**（内部库存移动），使系统数=实物数。

## 0）准备（一次性配置）

* （可选）开启必需功能：**库存 → 配置 → 设置**

  * **存储位置**（Locations）
  * **批次/序列号**（如需按批/序列盘点）
  * **条码**（如用扫码枪/手机扫码盘点）
* （可选）制定周期盘点策略：

  * 路径：**库存 → 配置 → 位置** → 打开需要做循环盘点的库位，在“周期盘点”设置

    * **盘点频率**（如 30 天一次）
    * **下次盘点日期**（系统会在到期时把库位推到“需要盘点”）

## 1）创建盘点任务

* 路径：**库存 → 运营 → 盘点**（Inventory Adjustments）→ **新建**
  填写关键字段：

  * **盘点参考**：如“2025-10-21_成品库月度盘点”
  * **公司**：选择对应公司
  * **盘点范围**（三选一或多条件组合）：

    * **按库位**：选择一个或多个库位（常用）；
    * **按产品/产品分类**：只盘这些；
    * **按批次/包裹/所有者**：有需要时限定。
  * **盘点日期**（Inventory Date）：建议选**盘点实操当天/时刻**；
  * **会计日期**（Accounting Date，可见于开启估值/会计时）：用于生成库存估值/会计分录的过账日期。
  * **包含为 0 的产品**（Include Exhausted Products）：勾选后，即使系统理论数为 0 的产品也会在明细中出现，便于录入“盘盈”。
  * **预填数量**（重要）：

    * **使用理论数量**：系统把“理论数”带入“盘点数量”列 → 你只改有差异的；
    * **预填为 0**：适合“清仓式盘点”，只把实物看到的数量逐一录入（没录的默认 0，容易造成大量“盘亏”，务必慎用）。

> 建议：多数企业用“使用理论数量”，降低工作量与遗漏风险。

## 2）发放盘点单/扫码作业（可选）

* 桌面录入：直接在本盘点单的明细里编辑“盘点数量”。
* 离线纸质：**打印 → 盘点清单**，线下填好后回录。
* 扫码：启用条码应用后，用**库存 → 操作 → 盘点**里的“**开始盘点**”在移动端/PC 扫描产品/批次/库位，系统逐行生成/更新明细。

## 3）录入实盘数

* 在盘点单的“**盘点行**”中：

  * 列：产品、批/序列（若启用）、库位、**理论数量**、**盘点数量**
  * 将**盘点数量**改为实数；
  * 若有新发现的批次/包裹，可新增一行或在扫码中录入。

## 4）校验差异与锁定

* 页签或列表右上角会显示**差异合计**。
* 确认无误后，点击 **验证/应用（Validate/Apply）**：

  * 系统自动**生成库存移动**（从“盘亏位置”到库存，或从库存到“盘盈位置”，内部特殊库位），使系统数=盘点数；
  * 若启用库存估值，会生成**库存估值层/会计分录**（按产品成本法：标准价/AVCO/FIFO）。

## 5）复核与追踪

* 查看：**库存 → 报表 → 库存移动**（筛选“来源/目标位置”为盘点用的“库存调整”位置）
* 查看产品的“**在手**”是否已更新为实盘数。
* 会计联动：在会计中核对相应存货/损益科目（如启用自动过账）。

---

# 三、常见盘点场景与技巧

### 场景 A：按库位循环盘点（Cycle Count）

* 给库位设置**盘点频率**与**下次盘点日期**（见“准备 0）”）；
* 到期时，盘点页面会出现“需要盘点”的库位，点进直接创建盘点；
* 好处：不必停工全仓清点，持续小批量维护数据准确。

### 场景 B：只盘一个产品（或一类产品）

* 在盘点单里把**范围限定为该产品/分类**；
* 勾选“包含为 0 的产品”以发现潜在盘盈。

### 场景 C：导入盘点数据（大量录入更快）

* 在盘点单打开后 → **导入**（顶部）

  * 模板列常见：`Location / Product / Lot / Package / Owner / Counted Quantity`
  * 导入后再“验证/应用”。

### 场景 D：按批次/序列盘点

* 先为产品启用**追踪方式**（产品 → 库存 → 追踪：批次/序列）；
* 盘点时每一行带批号/序列号；
* 若用扫码，按批/序列扫描即可生成/匹配。

### 场景 E：条码盘点（移动端）

* 启用条码 → 进入**条码应用**选择“盘点”流程；
* 扫库位→扫产品/批次→录数量→提交；
* 适合现场快速作业。

---

# 四、易犯错误与排查

* **做了盘点却没生效**：多数是**没点“验证/应用”**；盘点单仍是草稿状态。
* **差异很多**：可能用了“预填为 0”但漏录；或多仓/多公司切错上下文。
* **看不到需要盘点的库位**：库位未启用“周期盘点”或筛选条件挡住了。
* **实物在 WH/Input/Quality**：未做“上架”到 WH/Stock，导致与实盘对不上。
* **批次/序列不一致**：追踪设置与录入不一致，导致重复或遗漏。

---

# 五、给你的快速操作清单（可打印）

1. **日常看库存**：库存→报表→当前库存；分组=库位/产品。
2. **查移动**：库存→报表→库存移动；按日期/产品过滤。
3. **做盘点（整库位）**：库存→运营→盘点→新建

   * 盘点范围=库位（含下级）
   * 盘点日期=今日；会计日期=月末/今日（按财务要求）
   * 预填=使用理论数量；包含为 0 的产品=按需
   * 录入/导入实盘数 → 验证/应用
4. **复核**：产品页“在手”是否正确；库存移动是否生成；估值是否过账。

如果你告诉我：要盘的库位（如 WH/Stock）、是否启用批次、是否打算条码扫码，我可以给你一份“可直接导入的盘点模板列定义”和“你当前配置下的最佳勾选方案”。


# #############################################################################################################

# 销售
好嘞！给你一份 **Odoo 18 “从报价到收款”完整销售流程（标准仓配）** 的一键式操作手册。照着做就能把一张销售订单完整跑通，并且库存、发票、收款都闭环。

---

# 一、准备一次性配置（只做一次）

* 产品：**产品类型=可库存产品**（Consumable 不计库存），必要时启用**批次/序列号**。
* 税、价目表：需要开票含/不含税、折扣、价目表的先在**会计/销售设置**里打开。
* 仓库流程：默认**一步发货**（WH/Stock→Customers）。若启用两步/三步，交付时会多出“拣货/打包/出库”。

---

# 二、业务执行（从销售到收款）

## 1) 新建报价（Quotation）

路径：**销售 → 订单 → 报价单 → 新建**

* 选择**客户**。
* 添加**产品**与**数量**（需要库存在手或可采购/生产）。
* 可选：折扣、价目表、税、交货日期（承诺日期）。
* 添加备注/条款（可关联模板）。
* 点 **发送报价/打印**（可邮件给客户）。

> 小贴士：若有**订金**需求，先在发票部分做“**开具订金**”，系统会自动生成订金发票与收款（见下文扩展）。

## 2) 确认订单（Confirm）

* 报价页点击 **确认**，报价变 **销售订单（SO）**。
* 系统自动创建**交货单（Delivery，WH/OUT/…）**。

## 3) 备货与出库（交货）

路径一：在 SO 右上角点击 **交货** → 打开交货单
路径二：**库存 → 运营 → 调拨** 搜索对应 **WH/OUT/…**

在交货单页面：

* 点击 **检查可用**（Check Availability）→ 变为“就绪”。
* 若启用**批次/序列**：点击“按批/序列指定”（或扫描），把要出的批/序列录入行上。
* 若启用**两步/三步出库**：先做“拣货/打包”，最后在 Delivery 单上 **验证**。
* 数量不足：

  * 选择**部分交货** → 自动生成 **Backorder（欠交单）**；等补货后再发。
* 全部准备好后点击 **验证**（Validate/Apply）→ 出库完成。

> 结果：库存从 **WH/Stock → Customers**，在手数量减少。SO 的“已交付数量”更新。

## 4) 开具发票（Invoice）

从 SO 或交货单进入 **发票**：

* SO 页面 → 智能按钮 **发票** → **创建发票**
* **发票类型**：

  * **按订购开票**（Ordered Quantities）：按 SO 行数量开；
  * **按交付开票**（Delivered Quantities）：按已交付数量开（多数仓配企业推荐）。
* 检查发票行（税、金额、折扣）。
* 点击 **确认**（Post / 确认过账）。

> 若之前收过订金，创建“最终发票”时会**自动抵扣**订金行。

## 5) 收款（Register Payment）

在发票页面：

* 点击 **登记付款** → 选择**收款方式**（银行、现金等）、**收款金额/日期** → **确认**。
* 完成后：发票状态为 **支付**，应收账款减少。
* 若使用银行对账：导入银行对账单 → 在**对账**界面把收款与该发票匹配即可。

> 结果：**销售完成**；SO/发票/出库/收款闭环。

---

# 三、执行完成后的核对点

* **SO**：状态“已开票/已交付”（或显示余额明细）。
* **交货单**：状态“已完成”，无未处理 Backorder。
* **库存**：当前库存（Quants）中该产品在 WH/Stock 的数量减少。
* **发票**：状态“已过账 + 已支付”（或应收余额为 0）。
* **会计**：相关收入、税额、应收、库存估值（若永久盘存）都已入账。

---

# 四、常见分支与变体

### 1) 部分发货（欠交）

* 在交货时输入小于订单量 → 系统询问 **创建 Backorder**；
* 后续到货后，在 Backorder 单上继续 **检查可用 → 验证**。

### 2) 退货（销退）

* 打开原 **Delivery** → 点击 **退回**；
* 选择产品/数量/原因，**验证**退货入库；
* 会计上在原发票开**贷项凭证**（部分/全额退款），登记退款或与原收款核销。

### 3) 直运（Dropship）

* 在 SO 行选择**直运路线**，确认后系统创建 **供应商→客户** 的直发流程；
* 此流程通常不占用你仓库库存；开票依据合同约定（多用订购数量）。

### 4) 生产/组装（MRP/BOM）

* 若产品需生产：确认 SO → 触发**制造单**（或补货规则）→ 完工入库 → 出库。
* KIT/套装：可以用 BOM（不做制造），交货时按组件出库或按虚拟包销。

### 5) 订金与尾款

* SO 上点 **创建订金发票**（按固定额或百分比）→ 收款；
* 发货后 **创建最终发票** 自动抵扣订金 → 收尾款。

### 6) 序列号/保修卡

* 产品启用 **按序列追踪**；
* 出库时逐件录入序列 → 后续售后/保修可按序列追踪。

---

# 五、常见问题与排错

* **交货单“验证”灰色**：未“检查可用”或无可用库存；先补货或改“部分交货”。
* **SO 无法开票**：开票策略与“已交付数量”不匹配（例如按交付开票但未交付）；或权限不足。
* **库存没变**：交货单没“验证”；或在两/三步仓下货停在 **WH/Packing/Output**，未完成最后一步。
* **价格/税不对**：价目表或客户税设置与发票默认不同；在 SO/发票行修正或调整默认规则。
* **负库存**：曾“强制可用/立即转移”；尽快用收货/退货/盘点把 WH/Stock 拉回非负，避免估值扭曲。

---

## 一页速查卡（可打印）

1. **销售 → 报价 → 新建 → 确认**
2. **库存 → 调拨（或 SO → 交货） → 检查可用 →（批/序列）→ 验证**
3. **SO → 发票 → 创建发票（按交付）→ 确认**
4. **发票 → 登记付款 / 银行对账核销**
5. 核对 **SO/交货/库存/发票/收款** 全部完成

---

如果你把“想跑通的一张真实 SO 编号”发我（以及你仓库是一/两/三步出库），我可以按你的配置给出**你那台系统上具体要点的按钮与页面路径**，确保一次就跑通。





# #############################################################################################################





# 销退处理

没问题！下面把 **Odoo 18 的销售退货（销退）**从业务到按钮，完整说清楚。分三块：**A. 退货入库**（回到库存）、**B. 开具红字发票/退款单**（会计退款）、**C. 常见变体与排错**。按这个顺序做，最稳。

---

# A. 退货入库（把客户退回的货收进来）

> 适用：客户把货实物退回，需要回库，影响库存数量与成本。

**前提**

* 原销售的**交货单（Delivery，WH/OUT/…）已经“验证/完成”**。
* 若启用**批次/序列号**，退货时要按原批/序列退回。

**步骤**

1. 进入销售单或直接找交货单

* 路径1：**销售 → 订单 → 销售订单** → 打开该 SO → 右上角“交货”进入 **WH/OUT/xxxx**
* 路径2：**库存 → 运营 → 调拨**，搜索对应 **WH/OUT/xxxx**

2. 在交货单上点 **“退回”（Return）**

* 弹窗里：

  * 选择要退的 **产品、数量**（不能超过已交付数）
  * **退货原因**（可维护字典，便于统计）
  * 若启用**批/序列**，逐行填入要退回的批/序列
  * 目标库位（默认 **Customers → WH/Stock**；若仓库有两/三步收货，可能先回到 **WH/Input/Quality**，等会再“上架”）

3. 生成的退货单（通常类型是 Returns / Receipts）→ **验证**

* 路径：退货单页面点击 **“验证”**。
* 如果仓库是多步流程：

  * 退货单验证后，货会先到 **WH/Input/Quality**，再做一张**内部调拨**上架到 **WH/Stock**。
* 成功后：**库存数量增加**，成本按你的估值方法（标准价/加权平均/先进先出）自动处理。

> 小贴士
>
> * **直运（Dropship）**销售：原来是 Vendor→Customer 不经过你仓库。退货时弹窗会提供不同目标库位：
>
>   * 退回到你的仓（变成你持有）
>   * 或退回到供应商（跟原路线闭环）——按你的实际业务选。
> * 如果按钮“退回”不可见，通常是**原交货没完成**或你权限不足。

---

# B. 会计退款（开具红字发票 / 贷项通知）

> 适用：客户应收需要冲减（退货退款、价格折让、部分退款等）。
> 先做**A.退货入库**再做**B.退款**，能让库存与会计一致。若只是价格补偿且不退货，可只做 **B**。

**步骤**

1. 找到原发票

* 路径：**会计 → 客户 → 发票**（或在销售订单页面 → 智能按钮“发票”进入）

2. 打开发票，点击 **“新增贷项凭证 / Add Credit Note”**（或“退款”）

* 弹窗关键项：

  * **退款类型**：

    * **全额退款**（Full Refund）：按原发票明细全额红冲
    * **部分退款**（Partial Refund）：只退部分数量/金额
    * **取消并退款**（Cancel & Refund / Reversal with Cancel）：在某些版本会把原发票作废并开红字
  * **退款日期/会计日期**：会计过账用的日期
  * **原因**：写上“客户退货/价格折让”等，便于追溯
  * （有的版本）**复制明细**与否：一般保留，便于改数量/金额
* 点 **创建** → 生成一张**发票状态为草稿**的贷项凭证

3. 编辑并 **确认** 贷项凭证

* 若是**部分退款**：把行数量或单价改成需要退的部分
* 确认后，发票状态变“**已过账**”

4. 打款退款或与原收款核销

* 若之前有**收款**，在贷项凭证上点击 **登记付款（Register Payment）** 或与原收款 **对账**
* 如果使用**银行对账单**，把客户退款与贷项凭证匹配勾对即可

> 小贴士
>
> * **只退钱不退货**：跳过 A，直接做贷项凭证（部分退款）。
> * **加收/扣除运费、整备费**：在贷项凭证上新增一行“费用”正/负值即可（正值=向客户收，负值=退给客户）。
> * **换货**：做退货（A）+ 贷项（B），同时给客户下**新销售单**开新发票。

---

# C. 常见变体 & 排错

**1) 看不到“退回”按钮**

* 原交货单未“验证/完成”；或你看的是**拣货波次**而不是具体交货；或权限不足。

**2) 退货生成到奇怪库位**

* 仓库启用了**两/三步收货**，退货默认去 **WH/Input/Quality**。

  * 去 **库存 → 运营 → 调拨** 把内部调拨“**上架**”到 **WH/Stock** 才会计入“在手”。
* 直运销售：根据选择可能去供应商/你仓库。

**3) 批次/序列退不进去**

* 该产品启用了追踪，退货时必须录入**同一规则的批/序列**。
* 数量不符/批号不匹配会被拒绝。

**4) 库存数量没变**

* 退货单仍在草稿/就绪状态，**尚未“验证”**；
* 或货停在 **Input/Quality** 未“上架”。
* 打开**当前库存（Quants）**按库位展开看分布就能定位。

**5) 退款金额与库存成本不一致**

* 库存估值与会计是两条线：**数量与成本**走库存估值，**应收应付**走发票。
* 确保：退货入库（A）与贷项凭证（B）对应同一业务范围。加权平均/FIFO 情况下，退货越晚成本可能与原发出时不同，这是正常会计现象。

**6) 负库存**

* 如果先发货后补收货，可能出现 **WH/Stock 负数**。
* 退货时优先把**实物回库**并纠正负库存，再做贷项。

---

## 一页流程卡（可打印）

* **实物退回** → 销售原交货单 → **退回** → 选择产品、数量、原因（批/序列）→ **验证**
* （多步仓）必要时 **上架** 到 WH/Stock
* **退款** → 会计→客户→发票→原发票→**新增贷项凭证** → 选择全额/部分、日期、原因 → **确认**
* **登记退款/对账**（与原收款核销）
* 如需换货：再开新 SO。

---

如果你把一个真实案例（SO 号/交货单号/发票号）发我，我可以直接告诉你：在哪个页面点哪个按钮、哪几行要填什么，确保“数量、成本、应收应付”三线对齐。


  

# #############################################################################################################

# POS销退

没问题！把 **Odoo 18 的 POS 销售退货（销退）**分成三块讲清楚：**A. 前置设置** → **B. 前台（POS 界面）退货操作** → **C. 后台（POS 订单/会计/库存）联动与常见问题**。照着做即可把 POS 的退货从前台到库存/会计完整闭环。

---

# A. 前置设置（一次性）

1. 打开 POS 配置
   路径：销售点 → 配置 → 销售点 → 进入你的门店（Shop / POS）。
   重点检查：

* **库存位置**：POS 使用的“仓库/库位”，退货会回到这里（通常是 `WH/Stock` 或门店专用库位）。
* **发票**（若 POS 允许开发票）：启用后，**退货时会自动生成贷项凭证**（原单已开发票的场景）。
* **条码设置**（可选）：启用“扫描小票/条码”以便用“退款（Refund）”直接扫码原小票。
* **支付方式**：至少有一种能用于**退款**（现金/原路径），必要时在“支付方式”里勾选允许退款。

> 小提示
>
> * 多仓/多步收发企业通常给 POS 配一条**一步出入**的运营类型，退货才会直接回到可售库位。
> * 没有“允许退款/退回”专门开关，退款是以**负数订单**+**负支付**实现的。

---

# B. 前台（POS 界面）退货操作

## 方式一：用“退款（Refund）”按钮（推荐）

适合：顾客带着**原小票**来退货（全退/部分退都行）。

1. 打开 POS 收银界面，点击 **Refund（退款）**
2. **扫描原小票**（或输入小票号 / 从列表选择原 POS 订单）
3. POS 自动把原单的行带出来，**默认数量为负数**

   * 需要**部分退**：把要退的行/数量改成需要的负数（例如 -1）
   * 有**批次/序列**的商品：按提示选择/录入原序列号或批号
4. 右上角点 **支付**：选择**退款方式**（通常退到现金，或原支付通道）
5. **验证/完成**订单

   * 完成后，这张“负订单”就代表退货；库存会**回库**，会计在**关闭/过账 POS 会话**时统一入账

## 方式二：手动建一张“负数量”的订单

适合：找不到原小票，但业务允许退（按门店政策）。

1. 新建 POS 订单，逐个把要退的商品**加入购物车**
2. 点击商品行上的 **数量键**，把数量改成 **负数**（例如 `-1`）

   * 或用 +/- 切换至负数
3. 结账 → 选择退款方式 → 完成
4. 同样会生成退货订单（负额），库存回库，会计在会话过账时入账

## 方式三：退货+换货（以差额结算）

1. 先按“Refund”把要退的旧商品变为**负行**
2. 再把要换的新商品**正行**加上
3. 去支付页：系统会自动算出**应收/应付差额**

   * 若负数更大 → 退顾客钱
   * 若正数更大 → 顾客补差价
4. 完成后，库存同时做**退入 + 发出**，会计在会话过账时汇总

> 常见细节
>
> * **部分退款**：只退部分行/数量即可。
> * **多支付方式**原单：退货时你可以只用一种方式退款（按门店政策），Odoo 不强制“原路退回”。
> * **已开发票的 POS 单**：如果你的 POS 启用了开发票，做退款会**自动生成贷项凭证**；若你只做负订单但不想要贷项，需在 POS 配置中**关闭自动开发票**或按会计政策处理。

---

# C. 后台联动 & 排错

## 1) 看 POS 订单与库存

* 路径：销售点 → 订单 → POS 订单

  * 退货单会显示**负金额**，行数量为负
* 库存移动

  * 完成退款后立即生成**Customers → POS 库位**的**入库**（数量为正，因为是退回）
  * 在**库存 → 报表 → 库存移动 / 当前库存（Quants）**可看到数量回库
  * 若你的 POS 库位是门店缓存库，还会有**内部调拨**把货从门店库位转到主库位（视配置）

## 2) 会计与结账

* POS 的**会计分录**在你点击“**关闭与过账**（Close & Post）”POS 会话时统一生成
* 退货订单的负额会**冲减当期营业额**，负支付会出现在相应的**支付日记账**里
* 若启用 POS 发票，退货会创建**贷项凭证**（与原发票关联），在会计里可直接对账

## 3) 批次/序列号

* 商品启用批/序列追踪：

  * 销售时出库记录了序列/批
  * 退货时必须录入**相容的批/序列**才能回库
  * 不匹配会被系统拒绝

## 4) 常见问题与解决

* **看不到 Refund 按钮**：

  * 检查你是否在 POS 主界面（不是后台），以及 POS 应用版本；多数版本“Refund”默认可见。如果是自定义 UI/权限，请在 POS 界面按钮权限或前端模块中启用。
* **退货做完库存没回**：

  * 先确认退货单**已完成**（不是挂单）
  * 多仓/多步时，可能回到了**门店库位**或 **WH/Input**，需要**内部调拨上架**到 WH/Stock
* **会计没变化**：

  * 你还没把 POS 会话 **Close & Post**（未过账）
* **想原路退回但无该支付方式**：

  * 在“销售点 → 配置 → 支付方式”中添加/允许该支付方式，并勾选门店可用
* **退货找不到原小票**：

  * 用方式二（建负单）；若门店政策要求必须匹配原票，先在“POS 订单”里搜原单，再用方式一

---

## 一页速查（可贴操作台）

* **全/部分退**：POS → **Refund** → 扫小票 → 调整负数量 → **支付（选择退款方式）** → 完成
* **无票退**：POS 新建单 → 加商品 → 数量改负数 → 支付 → 完成
* **退换同单**：负行（退） + 正行（新买） → 支付差额 → 完成
* **后台检查**：销售点→POS订单（负额）／库存→库存移动（回库）／会话→关闭与过账（生成会计分录）

---

如果你把“门店使用的仓库/库位、是否要开发票、是否强制原路退款”告诉我，我可以帮你给出**最贴合你门店政策的一套按钮和配置清单**（包括支付方式勾选、条码小票格式、退款凭证打印等）。


# #############################################################################################################

# 其他出库 除销售外’的功能，

好的，下面给你一份在 **Odoo 18** 里完成“**其他出库（非销售）**”的全流程指南。核心思路是：不通过销售订单发货，而是用**调拨（Transfers）**把货从**内部库位**转到**虚拟外部库位**（客户/供应商/损益/自定义），从而实现样品、赠品、借用、展会、内部消耗、报废、无单退供等场景。

---

# 一、准备与基础设置（一次性）

1. 打开多库位等功能
   路径：**库存 → 配置 → 设置**

* 勾选：**存储位置（Storage Locations）**
* 需要批次/序列号时：勾选 **批次/序列号**
* 需要称重/计重：勾选相应选项
  保存。

2)（可选）新建专用库位（更好分账/统计）

* 路径：**库存 → 配置 → 位置** → 新建
  常见做法（按场景建几个“虚拟外部库位”）：

  * **WH/Other Out – 非销售出库**（地点类型：客户）→ 用于样品/赠品/借用/展会等“流向外部但非销售”的出库
  * **WH/Internal Use – 内部消耗**（地点类型：库存损益）→ 内部使用/研究消耗
  * **WH/Scrap – 报废**（地点类型：库存损益）→ 报废
  * **Vendors/Return – 退供应商**（地点类型：供应商）→ 无采购单的退供

> 说明：地点类型决定会计含义。
>
> * **客户**：视同出库到外部客户，影响库存、产生出库成本。
> * **供应商**：视同退回供应商。
> * **库存损益**：视同盘亏/内部消耗/报废。
>   产品分类=自动计价时，会在验证时产生会计分录（按产品分类的科目）。

3)（推荐）新建“其他出库”操作类型（更易用、可上看板）

* 路径：**库存 → 配置 → 操作类型** → 新建

  * 名称：**其他出库（非销售）**
  * 代码：可选 `OUT`
  * 方向：**出库**
  * 默认来源位置：**WH/Stock**
  * 默认目的位置：**WH/Other Out – 非销售出库**（或你定义的目标库位）
  * 勾选 **显示在操作看板**（方便首页直接点）
    保存。

> 不建也行，直接用“杂项调拨”来做；建了以后更直观、可控默认库位。

---

# 二、标准操作流程（以“样品/赠品/借用”非销出库为例）

**路径 A（推荐）：通过自定义“其他出库（非销售）”操作类型**

1. 新建调拨
   **库存 → 操作 → 调拨** → **新建**

* **操作类型**：选择 **其他出库（非销售）**
* 计划日期、负责人：按需
* （可选）**所有者**、**备注**：写清用途（如“展会样品”）便于追踪
* **源位置** 自动= WH/Stock
* **目标位置** 自动= WH/Other Out – 非销售出库

2. 添加产品行

* 点击 **添加产品**
* 选择产品、数量（可分行多种产品）
* 若启用序列/批次：在产品行或**详细操作**里录入/扫描序列号或批次
* 若称重：输入实际出库重量

3. **检查可用性 / 预留**

* 点击 **检查可用性**（或直接 **标记为待处理** / **预留**，取决于配置）
* 确保数量变为可用

4. **验证**（出库生效）

* 点击 **验证**
* （若需要）打印 **送货单/拣货单**
* 结果：库存减少；若产品分类自动计价→生成会计分录（出库成本）。

**路径 B：直接用“杂项调拨”**

1. **库存 → 操作 → 调拨 → 新建**

* **操作类型**：选择 **杂项调拨**（Miscellaneous operation）
* 手动指定：**源位置= WH/Stock**；**目标位置= 你需要的虚拟外部库位**（如 WH/Other Out – 非销售出库 或 Vendors/Return 或 WH/Internal Use）

2. 后续与路径 A 相同：加产品 → 预留 → 验证 → 打印

---

# 三、常见“非销售出库”场景与目标库位选择

| 场景          | 推荐目标库位类型 | 如何建/选                                                   |
| ----------- | -------- | ------------------------------------------------------- |
| 样品/赠品/借用/展会 | 客户       | 建一个 **WH/Other Out – 非销售出库（客户）**；也可为每类单独建（样品、赠品、展会）以便统计 |
| 员工个人借用      | 客户       | 可再细化到“Employee/xxx 借用库位（客户）”，或在调拨备注中写清责任人               |
| 内部消耗/研发用    | 库存损益     | **WH/Internal Use（库存损益）**，出库计为损益                        |
| 报废/损坏       | 库存损益     | 用 **Scrap（报废）**功能或直接调拨到 **WH/Scrap（库存损益）**              |
| 无采购单的退供     | 供应商      | **Vendors/Return（供应商）**，表示退回供应商                         |
| 寄售到第三方      | 客户       | 可为寄售单位建独立客户库位，或绑定特定伙伴便于对账                               |

> 提示：若你希望**按对象/渠道统计**（比如“展会费用”、“员工借用成本”），可以：
>
> * **细分库位**（一个场景一个库位）；
> * 或者在调拨单头/明细加**分析账号/标签**（需在产品分类与会计中启用），便于报表分析。

---

# 四、报废（Scrap）与盘点（Inventory Adjustment）的区别

* **报废**：路径 **库存 → 操作 → 报废**，把货从**内部库位 → 报废库位（库存损益）**，有完整追踪记录；适合坏货、过期。
* **盘点**：路径 **库存 → 操作 → 实物盘点**，是**修正在手数**的专用流程（差异走损益）。用于盘盈盘亏校准，不强调去向、更多面向数量纠偏。
* 做“其他出库”更强调**去向**与**业务用途**，所以更推荐用 **调拨** 到**明确的目标库位**，而不是直接盘亏。

---

# 五、序列号/批次、包装、条码

* 若启用序列/批次：
  在调拨的 **详细操作** 中录入/扫描序列或批次，确保每件/每批的追踪链路完整。
* 若用条码：
  在 **条码**应用里也可新建/处理调拨（扫描源/目标库位、产品、序列、数量），提效一线操作。
* 包装/箱号：
  可在调拨中**打包**，便于物流追踪。

---

# 六、会计影响（自动计价时）

* 发生时点：**验证**调拨时产生库存估值层（SVL），并记账。
* 分录科目：来自**产品分类**的库存科目设置；方向取决于**源/目标库位类型**：

  * **内部 → 客户**：计为销售出库成本（但无收入），常用于样品/赠品/寄售；
  * **内部 → 供应商**：计为退供影响；
  * **内部 → 库存损益**：计为损益（内部消耗/报废）；
* 若你希望“非销售出库”走**特定费用科目**：

  * 方式一：为这类产品单独设 **产品分类**（不同费用科目）；
  * 方式二：借助**库存科目规则**或**分析账号**细分成本归集（需要会计模块配置）。

---

# 七、单据打印、追踪与报表

* 调拨单 → **打印**：送货单/拣货单/标签等。
* **库存 → 报表**：

  * 库存总览、移动明细、估值明细
  * 用**地点过滤**（WH/Other Out、Internal Use、Scrap 等）+ 时间范围，即可看到“其他出库”的量与成本。
* **产品 → 追溯**：序列/批次的上下游链路一目了然。

---

# 八、几个实战小技巧

* **看板直达**：在操作类型勾“显示在操作看板”，首页点“其他出库”一键新建。
* **模板化**：对重复场景（比如“展会出库”）可做**服务器动作**或**studio按钮**，自动带出默认库位/备注。
* **权限**：给仓库操作员/主管分配合适的访问与验证权限，避免误操作。
* **回收/归还**：样品/借用期满归还时，做相反方向调拨（从“客户库位”回到“WH/Stock”），或在**退回**功能里选择原调拨做“退回”。

---

需要我给你**按你的场景**（比如“样品、赠品、员工借用、展会、内部消耗、无单退供”）分别创建**库位与操作类型**的建议命名、会计归集方案、以及一步步的**截图式操作清单**吗？我可以直接列出你在 Odoo 18 里点哪一页、填什么字段的详细清单。




# #############################################################################################################

对于商品报废来说，会计信息科目中，库存估值科目(进货)和库存估值科目(出货)分别怎么选择

下面把“商品报废（Scrap）”这一场景下，Odoo 的三类关键科目怎么选、为什么这么选，讲清楚（以**自动库存估值**为前提；若是**手工/定期**估值则不会自动生成凭证）。

# 一、三类相关科目各自作用

* **库存估值科目（Stock Valuation Account）**
  资产类，反映“库内存货”的账面价值。所有入库/出库都会在这里增减。
* **库存估值科目(进货) / Stock Input（也叫：收货暂估、在途/GRNI）**
  采购收货时的对方科目，用来暂挂供应商入库尚未收票的金额；开供应商账单后与应付/成本结转冲销。
* **库存估值科目(出货) / Stock Output（也叫：发货暂估、成本结转）**
  销售发货时的对方科目，用来暂记发货形成的结转；开客户发票后与主营成本等科目配合结转。

> 注意：**报废不是采购也不是销售**，系统不会走 Input/Output 暂估清算的路径。报废对应的是**从库存（资产）转到损失（费用）**。

# 二、报废时应该怎么配置

报废会把货从“库内位置(Internal Location)”移到“报废/损耗位置(Scrap/Inventory Loss Location)”。会计分录的**借方**取自“报废位置的估值科目（Valuation Out Account）”，**贷方**恒为“库存估值科目”。

### 1）产品类别（Product Category）

路径：库存 → 配置 → 产品 → 产品类别

* **库存估值**：选择“自动/永久（Automated/Perpetual）”
* **库存估值科目（Stock Valuation Account）**：选**存货类资产科目**

  * 常见示例：

    * 中国会计：`1403 库存商品 / 原材料`（按你业务分开设更精细也可以）
    * 通用/IFRS/US GAAP：`Inventory`
* **库存估值科目(进货) / Stock Input**：选**收货暂估（GRNI）**类的**负债**或**暂挂**科目

  * 示例：`Goods Received Not Invoiced (GRNI)` / `应付暂估`
* **库存估值科目(出货) / Stock Output**：选**发货暂估/成本结转**类**成本或暂估**科目

  * 示例：`Interim COGS / 发货暂估`

> 这些 Input/Output 设置**主要用于采购入库、销售出库**。**报废不会用到这两个科目**，但仍需为采购/销售流程完备而正确设置。

### 2）报废位置（Scrap/Inventory Loss Location）

路径：库存 → 配置 → 位置 → 搜索“Scrap”或“报废/损耗”位置 → 打开

* **位置类型**：通常为“Inventory Loss / 库存损耗”
* 展开“会计/估值”部分，设置：

  * **Valuation In/Out Account（估值入/出科目）**：至少**设置“估值出科目（Valuation Out Account）”**为**库存报废损失/盘亏损失**等费用科目。

    * 中国会计常用：

      * `营业外支出-存货盘亏` 或
      * `管理费用-存货报废/损耗`（看你公司制度，是走营业外还是期间费用）
    * 通用：`Inventory Write-off / Shrinkage Expense`

> 有了这个配置，**报废出库**时分录为：
>
> * **借：报废损失（你在 Scrap 位置设置的 Valuation Out Account）**
> * **贷：库存估值科目（Stock Valuation Account）**

# 三、报废分录示例（加深印象）

假设某商品账面单价 100，数量 5，合计 500 报废：

* 借：`Inventory Write-off / 报废损失` … 500
* 贷：`Inventory / 库存估值科目` ………… 500

> 你会发现，这里**完全没用到**“库存估值科目(进货/出货)”两个暂估科目，因为没有涉及收票或开票的清算流程。

# 四、常见错误与排查

1. **把“库存估值科目(出货)”误认为报废要用的对方科目**
   → 报废不会走 Output；它走的是**位置的 Valuation Out Account**。
2. **Scrap 位置未配置会计科目**
   → 报废不出分录或挂错科目。请在位置上补齐**估值出科目**。
3. **产品类别没启用“自动库存估值”**
   → 报废只动数量不出会计分录。若希望自动记账，请开启自动估值并设好科目。

# 五、给你的“怎么选”结论（一句话版）

* **库存估值科目（Stock Valuation Account）**：选**存货资产**（如 `Inventory / 1403库存商品`）。
* **库存估值科目(进货) / Stock Input**：选**收货暂估（GRNI）**类科目（采购流程用，不用于报废）。
* **库存估值科目(出货) / Stock Output**：选**发货暂估/成本结转**类科目（销售流程用，不用于报废）。
* **报废真正用到的对方科目**：在**Scrap/报废位置**的“**估值出科目（Valuation Out Account）**”里，选**报废/盘亏损失**类费用科目。

如果你把贵司使用的**会计科目表编码**（例如用友/金蝶口径）发我，我可以按你的口径把上面几项一对一落到具体科目编号。




# #############################################################################################################

# odoo18中，如何操作进货是按计重来的，如何处理，对于同一件产品，第1件是50g，第2件是30g，同时有产品区分记录，如何操作，详述步骤

下面给你一套在 Odoo 18 里“按克计价/按重量入库”，且“同一产品分成两件分别 50g 与 30g，并保留产品区分记录（批次/序列号）”的标准做法。全流程一次走通即可复用。

# 一、准备与开关

1. 打开计量单位
   路径：库存 → 配置 → 设置 →（产品）勾选【计量单位】→ 保存。
   （若你系统语言是中文，开关名一般就是“计量单位”。）

2. 打开批次/序列号跟踪
   路径：库存 → 配置 → 设置 →（可追溯性）勾选【批次与序列号】；
   建议同时勾选【显示详细操作】（收货时能逐行拆分并填写批次/序列与各自重量）。→ 保存。

> 可选：若你做仓位管理，也勾【存储位置】；做包装管理则勾【包裹/包装】。

# 二、计量单位与产品设置

3. 检查“克(g)”这个计量单位
   路径：库存 → 配置 → 计量单位。
   在“重量（Weight）”类别下，确保有“g（克）”“kg（千克）”。
   如果没有“g”，新建一个：

* 名称：g
* 类别：重量（与 kg 同一类别很关键）
* 比率：相对 kg 的换算（通常 0.001 kg = 1 g）
* 精度：建议保留 0.01 或 0.001（便于称重精确到分克/毫克，取决于你的业务）

4. 新建/编辑产品（例如：“足金转运珠”或“Au999 金料”）
   路径：库存 → 产品 → 产品 → 新建/编辑

* 产品类型：可库存产品
* 计量单位（UoM）：g（克）
* 采购计量单位：g（克）
* 成本/销售价格：按“每克”填写（如采购价 ¥X / g，销售价 ¥Y / g）
* 跟踪：按批次（每件生成一个批次号）或按序列号均可；建议“按批次”。
* 估值/成本法（在会计或库存估值里）：按你公司要求（FIFO/加权平均、自动或手动估值）
  保存。

> 关键点：把该产品的“主计量单位”定为“g”。这样无论采购、入库、销售，数量都是“克数”，价格也是“每克”。

# 三、供应商价格（按克报价）

5. 在产品的“采购”页签里添加供应商价

* 供应商：选择你的供应商
* 计量单位：g
* 价格：按每克填写（如 ¥X/g）
  保存。

# 四、采购下单（示例：同一产品，两件分别 50g 与 30g）

有两种等效做法，二选一即可：

**做法 A：在采购订单上写总重量，收货时再拆分两件**
6A) 采购 → 询价单/采购订单 → 新建

* 供应商：XXX
* 行1：产品=（上面建好的）金料；数量=80（单位=g）；单价=按每克；税率按公司规则。
* 确认订单。

**做法 B：在采购订单上就直接拆成两行**
6B) 采购 → 询价单/采购订单 → 新建

* 行1：产品=金料；数量=50 g；
* 行2：产品=金料；数量=30 g；
* 确认订单。

> 默认情况下 Odoo 可能会合并相同产品行；若你想强制不合并，可以在两行的“描述”里写不同的备注（比如“第1件”“第2件”）或使用不同的“显示类型段落/备注辅助”，从而避免自动合并显示。实务上，用做法 A 更简洁，收货时拆分更直观。

# 五、收货时“按件拆分”，记录两件的重量与区分（批次/序列）

7. 从采购订单进入收货

* 在采购单右上角点【收货】，打开收货单（拣货单/入库单：类型一般是 Receipts）。

8. 打开“详细操作/批次序列录入”

* 在该产品行右侧，点击“详细操作”图标（或进入“操作/Operations”标签页）。
* 因为产品已设为“按批次/序列号跟踪”，系统会要求你为“已完成数量”录入批次/序列。

9. 拆分为两条操作行并分别填写

* 点击【添加一行（或“添加批次/序列”）】

  * 行1：批次/序列号（自定义，如 G20251023-001），已完成数量：50（g）
  * 再添加一行：行2：批次/序列号（如 G20251023-002），已完成数量：30（g）
* 确认两行合计=应收数量（80g）。
* （可选）如果你启用“存储位置”，可以把两行分别放到不同库位（如“金料库-托盘A/托盘B”）。
* 点击【验证/验证并应用】，完成入库。

> 这样系统会创建两个“产品区分记录”（本质是两条批次/序列明细），每条记录对应一件实物与其重量。以后你在销售/调拨时就可以选择具体哪一个批次（哪一件）。

# 六、供应商账单/发票

10. 从采购单创建供应商账单

* 采购单 → 创建账单（或从会计 → 供应商 → 账单 → 从订单引入）
* 金额=（50+30）×（每克单价）。
* 若供应商发票上两件分两行，你也可在采购订单阶段（做法 B）就分两行，这样账单会自然按两行带出。

# 七、如何查看“产品区分记录”（两件货的台账）

11. 查看批次/序列及库存

* 库存 → 产品 → 批次/序列号（或“可追溯性”视图）

  * 可看到 G20251023-001：在手=50 g
  * G20251023-002：在手=30 g
* 库存 → 报表 → 在手数量（过滤该产品、分组到“批次/序列”）

  * 你能按批次看到各自的在手克数。
* 后续销售/调拨：系统会要求选择批次（即挑选哪一件），同时“数量”依旧填克数（例如卖出 30 g，可以指定卖出 30 g 来自哪一个批次；若要整件卖出，就把相应批次的 50 g 或 30 g全数出库）。

# 八、常见问题与小技巧

* **为什么用 g 做主计量单位？**
  因为金料等按重量交易、核算与计价，用 g 做主 UoM 最顺手。这样单价就是“每克价”。
* **要不要用“序列号”而不是“批次”？**
  一件一号、严格一对一可选“序列号”；若只需区分每件，但不强调“唯一不可拆”，用“批次”更灵活（允许部分出库），珠宝/金料通常选“批次”。
* **要不要在采购单上就分两行？**
  业务+对账需要时可分两行；否则在收货“详细操作”里拆两条更自然。
* **打印标签**（可选）：
  若开启条码/标签模块，可给每个批次打印标签，贴到实物上，后续盘点/销售扫码选择该批次。
* **盘点**：
  盘点时也支持按批次/序列核对克数，差异自动生成库存调整分录。

---

如果你愿意，我可以按你现有产品的字段（成色/工费等）给一个更贴合珠宝行业的字段布局与打印模板建议（采购单、收货批次标签、销售单据里如何呈现“第1件50g、第2件30g”）。




# #############################################################################################################

odoo18中，将重量的基准单位从kg改为g，是否可行，如何该

可以，但**不一定有必要**。在 Odoo 里，只要把产品的“计量单位/采购计量单位”设为 g，系统就会按克计价与过账，**无需**把“重量”类别的基准单位从 kg 改成 g。
如果你确实想把“重量”类别的**参考单位（Reference）**改成 g，下面是可行且安全的做法与注意事项。

# 推荐做法（更安全省事）

* 直接把涉及金料/按重计价的产品：

  * **计量单位**：g
  * **采购计量单位**：g
  * 单价填写“每 g 价格”。
    这样采购/收货/销售全流程都会以“克”为数量单位，**无需**调整系统级“重量”类别的参考单位。

# 若必须把参考单位从 kg 改为 g（可行方案）

> 前提：开启开发者模式；操作前**完整备份数据库**，并在**测试环境**先演练一次。

## A. 变更前检查

1. 暂停业务：关闭进行中的收货/交货/盘点/MO/POS 会话，避免中途产生新单据。
2. 记录现有“重量”类别下各单位（kg、g、mg、lb、oz 等）的**换算**与**四舍五入精度**（Rounding）。

## B. 调整步骤（Inventory → Configuration → Units of Measure）

1. 进入：库存 → 配置 → **计量单位** → 列表视图 → 过滤“类别 = 重量（Weight）”。
2. 找到 **g（克）**并打开编辑：

   * **类别**：仍为“重量（Weight）”（务必不改类别）。
   * **类型（Type）**：改成 **Reference**（参考单位）。
   * **四舍五入精度**：按业务需要（例如 0.01 g 或 0.001 g）。
3. 打开 **kg（千克）**：

   * **类型**：选 **Bigger than the reference unit**（大于参考单位）。
   * **比率（Ratio）**：**1000**（表示 1 kg = 1000 g）。
4. 校正“重量”类别下其他单位的比率（都相对 **g** 这个新参考单位）：

   * **mg**：Smaller than reference，**0.001**（1 mg = 0.001 g）
   * **lb**：Bigger than reference，**453.59237**（1 lb ≈ 453.59237 g）
   * **oz**：Bigger than reference，**28.349523125**（1 oz ≈ 28.349523125 g）
   * 若还有 ton、ct（克拉，注意克拉是质量单位但常另设类别）等，按需补全。
5. 保存后，用一个测试产品做一次“收货 100 g / 销售 30 g”的往返，核对库存数量、成本和金额是否正确。

## C. 变更后核验

* **产品主计量单位**与**采购计量单位**仍可按 g 填写；历史单据不会丢，但要检查新旧单据的显示是否一致。
* 抽查以下报表：在手数量、估值层、移动明细，确认数量与金额逻辑一致。

## 风险与注意点

* **不必要的系统级改动**：参考单位的切换属于“系统级”，一旦设置不当，可能造成换算错误。若只为按克交易，改产品 UoM 即可，**更安全**。
* **Rounding（四舍五入）**决定最小增量：若需要精确到 0.01 g，请把 g 的 Rounding 设为 0.01；太粗会导致不能录入细分重量。
* **产品“重量/毛重/净重”字段**（用于物流运费）在 Odoo 中通常以 **kg** 显示，这与“计量单位类别”的参考单位是**两回事**。即便你把参考单位改为 g，产品表单里“重量(kg)”字段标签仍是 kg——这是正常的。
* **定制/接口**：若你有代码或接口写死了某个 UoM 的 ID/名称（如假定 kg 为参考单位），改动后需回归测试。
* **跨类别不可切换**：产品的计量单位只能在**同一类别**内切换；本方案未改“重量”类别本身，因此不触发限制。

---

如果你告诉我当前“重量”类别下的单位列表（名称、类型、比率、Rounding），我可以帮你核对一版“改 g 为参考单位”的**精确参数对照表**，以及一份**回滚步骤**（若需恢复为 kg 参考单位）。

好的，我给你把在 Odoo 18 里“批量清空当前预留”的**可操作步骤**写到位（收货、交货、内部调拨都一样的思路），再补充制造与 POS 常见占用点的处理。

# 一、库存拣货/交货/收货里清空预留（批量）

1. 进：**库存 → 操作 → 调拨（Transfers）**

   * 右上角切到**列表视图**（更适合批量勾选）。
2. 设筛选器（可保存为“清预留-待处理”方便重复用）：

   * **状态**：勾选【等待中】、【可用】（也就是未完成未取消的）
   * **可用性**：勾选【已分配】、【部分可用】
   * （可选）**操作类型**：分别筛【收货（WH/IN）】【交货（WH/OUT）】【内部调拨（WH/INT）】逐类处理更稳妥。
3. 批量全选：列表左上角方框 → 勾选当前页或【选择所有符合搜索条件的记录】。
4. 批量**取消预留**：

   * 列表上方【操作】下拉 → 找【取消预留】（Unreserve）。
   * 若你没看到“取消预留”，就改为逐单打开拣货单 → 顶部的【取消预留】按钮点一下（此按钮在“可用/部分可用”状态时出现）。
   * 提示：取消预留后，单据仍处于“等待中/可用”状态，只是物料不再被锁定。
5. 需要**彻底打回草稿**才继续（不一定必须）：

   * **逐单**打开拣货单 → 右上角【取消】→（取消后）右上角出现【重置为草稿】→ 点击。
   * 批量“重置为草稿”通常没有列表级动作；想批量只能逐单操作或做自定义 Server Action（不建议生产上随便开）。
   * 注意：取消/重置为草稿会影响与其关联的采购/销售流程，请确认业务允许。

> 常见按钮位置：
>
> * **取消预留**（Unreserve）：拣货单顶部按钮。
> * **取消**（Cancel）：拣货单顶部按钮。
> * **重置为草稿**（Reset to Draft）：拣货单被取消后出现（部分情形需开启开发者模式才看到）。

# 二、按类型分别处理（更稳）

为避免互相牵连，建议分三次操作：

* **收货（WH/IN）**：按上面步骤清空预留。
* **交货（WH/OUT）**：按上面步骤清空预留；若来自销售订单，取消预留不会取消SO，只是释放库存。
* **内部调拨（WH/INT）**：同上。

# 三、制造占用也要清

如果你启用了制造/拆装，这里也会“占用”组件：

1. 进：**制造 → 操作 → 制造订单**
2. 搜索筛选：**状态**= 待处理/进行中，且**组件可用性**= 已分配/部分可用
3. 打开每个 MO，在**组件**页签点击【取消预留】（或【释放】）
4. 若 MO 生成了拣货单（原料领料/成品入库），回到 **库存 → 调拨** 用上一节的方法再清一次。

# 四、POS 会话 & 条码也可能锁库存

* **POS**：未结账的 POS 订单会生成待处理的交货单（已分配）。

  * 进：**POS → 订单** 或 **库存 → 调拨（操作类型=交货）**，把对应交货单**取消预留/取消**。
  * 关闭未结的 POS 会话（POS → 会话 → 结束会话），避免新的预留继续产生。
* **条码**：若有人在条码界面开启了拣货并处于“已分配”未完成，也会锁。让执行人**完成或取消**该拣货。

# 五、如何目测确认“已清空”

* **库存 → 报表 → 在手数量**：相关产品“可用数量”应上升（释放锁定量）。
* **库存 → 操作 → 调拨**：用之前保存的筛选器，列表应为空或仅剩“未分配”的。
* 单个产品页 → **可用性**条 & **预留数量**字段（开发者模式可见）应趋近 0。

# 六、常见看不到按钮/动作的原因

* 权限不够：确保你是库存经理。
* 单据状态不对：只有在“可用/部分可用/等待”状态才会出现【取消预留】。
* 自定义视图/翻译差异：有时“取消预留”被翻译成“释放”、“解除保留”。
* 列表视图没有“取消预留”批量动作：请用逐单页面按钮。

# 七、操作建议（避免业务连锁反应）

* **优先只用【取消预留】**，少用“取消/重置为草稿”，这样不破坏上游订单，仅释放库存。
* 分批处理（先非关键订单，再关键订单），并与采购/销售同事打好招呼，避免他们在你释放期间又触发“检查可用性”把它们重新预留。
* 完成以上清理后，再去做你要的设置调整；必要时临时在**库存 → 配置 → 设置**里把**“预留策略”**从“下单时”改为“拣货时”，防止系统马上又自动预留（调整完再改回）。

如果你愿意，我可以根据你当前仓库的**操作类型名称（WH/IN、WH/OUT、自定义名）**和**具体产品**，给你一份可保存的**筛选器配置清单**（逐项点哪里、保存为哪种收藏搜索），这样你每次只需两三下点击就能把预留清干净。



# #############################################################################################################

短答：**不用上产品变体**。你这套“条码决定唯一性”的珠宝建模，更适合用**产品=款式/类别**，**序列号(批次)=具体那一件**来承载差异；把“成色/金重/石重/计重or计件/大类/品类/一物一码”等都落到**序列号（stock.production.lot）**层，而不是用变体来拆 SKU。

# 为什么不需要变体

* 你说“只要是这个条码的，都是这个产品”。在 Odoo 里，“条码”可以放在**序列号**上（每件珠宝一枚序列号=证书号/商品码），这本质上就已经是**最细的唯一标识**。
* 变体用于：同一款式按“尺寸/颜色/材质”等分成**多个独立 SKU 各自记库存/价格/条码**。但你是**每件**都有独立条码与重量/参数，用序列号即可一件一件管理，不必再拆出一堆变体。
* 计重/计件因条码而异：把“是否计重”“金重/石重”等做成**序列号级别字段**，就能让同一款式下不同条码分别按各自规则定价出库。

# 推荐建模（简洁稳定）

1. **产品（product.template / product.product）**

   * 作为“款式/SPU/业务产品”。
   * 售卖单位建议统一用“个（Unit）”，**定价公式**去读序列号的金重/石重（计重时用重量算价；计件时直接按标价/工费）。
   * 打开“按序列号追踪”（Inventory → 产品 → 追踪=By Unique Serial Numbers）。

2. **序列号（stock.production.lot）= 每件珠宝的“证书号/一物一码”**
   扩展以下字段（用 Studio 或自定义模块）：

   * `x_measure_type`（选择：计重/计件）
   * `x_fineness`（成色：足金/K18/K10…可选列表）
   * `x_gold_weight`（金重，g）
   * `x_stone_weight`（石重，ct 或 g）
   * `x_major_category`（大类）
   * `x_category`（品类）
   * （已有）`barcode`（把你的“一物一码”直接写到序列号条码字段）

   收货时创建序列号并填好上述参数；**库存、成本、出入库、销售**都跟着这枚序列号走。

3. **定价与开票**

   * POS/销售单上选择产品后，再扫描/选择序列号。
   * 定价策略读取序列号字段：

     * 若 `x_measure_type=计重` → 价格 = 金价×`x_gold_weight` + 工费（可按大类/成色/品类加成）。
     * 若 `x_measure_type=计件` → 直接用产品标价或序列号上的自定义价格字段。
   * 这可用价目表公式或一个轻量定制（onchange/compute）实现。

4. **“多物一码”的处理**

   * 从珠宝业务看，不建议“多物一码”（不同件的金重/石重不同）。
   * 若确实要“多物一码”，只能把重量等放**订单行自定义字段**而不是序列号（否则同一码无法表达多件不同参数）。但这会牺牲可追溯性。强烈建议**一物一码**。

# 什么时候才考虑“产品变体”

仅当下列之一成立才上变体（对你当前描述，大多不需要）：

* 确实要按“成色/尺码/圈口”等**预先分 SKU 各自记库存**（不是每件唯一条码的粒度）。
* 不同选项需要**不同价目或不同BOM**且**不以序列号划分**。
* 需要给每个选项**独立条码**用于批量上架/大规模零售，而不是件件唯一条码。

# 一次性配置步骤（速记）

1. 打开产品变体功能可不开启；但务必**开启“按序列号追踪”**。
2. 用 Studio（或模块）在 **stock.production.lot** 上增加：成色、计重/计件、金重、石重、大类、品类 等字段。
3. 产品上启用“追踪=序列号”，销售单位先用“个”。
4. 收货 → 创建序列号（=证书号/条码）→ 填字段。
5. 价目表/定价钩子读取序列号字段给单价。
6. POS/销售单扫描条码（匹配序列号） → 系统自动带出该件参数，完成销售/出库。

这样做的好处：

* 不会产生**变体组合爆炸**；
* **每件**都有清晰的可追溯参数（成色/重量/类别）；
* 计重/计件**可在序列号层切换**，不被产品的计量单位种类所限制；
* 符合珠宝行业“一物一码”的实际流程。

需要的话，我可以给你一段**Studio 字段清单**（精确到字段类型/标签/技术名）和一版**价目表计算公式示例**，直接照抄配置即可。



# #############################################################################################################


不需要。结论再明确一次：

* 你的建模走“序列号=一物一码”，核心是**启用序列号追踪**，而不是产品变体。
* **不用勾选**“产品变体（Attributes & Variants）”开关也完全能实现你的需求。

# 要勾/不要勾的开关

* 勾✅：Inventory → Settings → Traceability → **Lots & Serial Numbers**（按序列号追踪）
* 不必勾❌：Inventory → Settings → **Variants**（产品变体）

> 如果你已经误勾了 Variants：也没事，只要**不要**在产品上添加会“生成变体”的属性组合即可（18 里属性有“是否创建变体”的选项时，选“Never/不创建”也能避免 SKU 爆炸）。

# 把信息放哪

* 把“成色/计重or计件/金重/石重/大类/品类/条码”都放到**序列号（stock.production.lot）**自定义字段里（用 Studio 最快）。
* 产品（模板）只当“款式/SPU”，计量单位先用“个”，价格通过读取**被选择/扫描的序列号**来计算（计重走金重×金价+工费；计件走标价/序列号自定义价）。

# 价格 & 业务联动（简述）

* 标准价目表不会直接读“序列号字段”，常见做法是：

  * 在销售/POS 选择（或扫描）序列号后，**onchange** 把“按重计价”算出单价；或
  * 做一个轻量自定义定价钩子；或
  * 在 POS 里用自定义规则根据 lot 字段改行价。
* 这样你既保留“一物一码”的精细参数，又不产生多余变体。

一句话：**核心只开“序列号追踪”，变体功能可以不勾**。如果以后某些款式真的需要“预先分 SKU（比如圈口/尺寸固定组合）”，再单独给那类款式启用属性→生成变体即可。





# #############################################################################################################







# #############################################################################################################







# #############################################################################################################







# #############################################################################################################







# #############################################################################################################







# #############################################################################################################







# #############################################################################################################







# #############################################################################################################







# #############################################################################################################







# #############################################################################################################







# #############################################################################################################







# #############################################################################################################
































