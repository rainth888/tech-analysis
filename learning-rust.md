
# codex cli build
# Clone the repository and navigate to the root of the Cargo workspace.
git clone https://github.com/openai/codex.git
cd codex/codex-rs

# Install the Rust toolchain, if necessary.
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source "$HOME/.cargo/env"
rustup component add rustfmt
rustup component add clippy

# Build Codex.
cargo build

# Launch the TUI with a sample prompt.
cargo run --bin codex -- "explain this codebase to me"

# After making changes, ensure the code is clean.
cargo fmt -- --config imports_granularity=Item
cargo clippy --tests

# Run the tests.
cargo test


# Rust 快速入门（从 0 到能跑 Hello World）

下面这份速查式指南，帮你在 30 分钟内从背景 → 核心概念 → 语法速览 → 环境搭建 → 编译运行，一步到位。

---

## 一、Rust 是什么？简史与定位

* **起源**：2006 年 Graydon Hoare 发起，2010 年 Mozilla 赞助，2015 年发布 1.0 稳定版本。
* **目标**：在**不牺牲性能**（接近 C/C++）的前提下提供**内存安全**与**并发安全**。
* **核心卖点**：编译期通过**所有权/借用/生命周期**规则，杜绝空指针、悬垂引用、数据竞争等一大堆运行时问题。
* **生态**：包管理器 **Cargo** + 社区仓库 **crates.io**，开发体验优秀。

---

## 二、Rust 的三大核心概念（一定要懂）

1. **所有权（Ownership）**

   * 每个值有一个**唯一所有者**；所有者离开作用域时，值会被**自动释放（Drop）**，无需 GC。
2. **借用（Borrowing）**

   * 通过 `&T`（不可变借用）或 `&mut T`（可变借用）临时使用数据；编译器确保**同一时刻要么任意多个不可变借用，要么恰好一个可变借用**。
3. **生命周期（Lifetimes）**

   * 引用必须**比被引用对象活得更久**；大多数场景编译器可推断，复杂函数签名时用 `'a` 等标注。

额外关键：

* **零成本抽象**：泛型、迭代器等在编译期展开，不损失性能。
* **错误处理**：无异常；用 `Result<T, E>`/`Option<T>` 搭配 `?` 传播错误。
* **不可变默认**：`let` 默认不可变，需要改动时显式 `mut`。

---

## 三、语法速览（够用就好）

### 1) 变量与基本类型

```rust
let x = 42;          // 不可变
let mut y = 5;       // 可变
y += 1;

let pi: f64 = 3.14;
let ok: bool = true;
let ch: char = '中';

let tup: (i32, &str) = (7, "hi");
let arr: [i32; 3] = [1, 2, 3];
let slice: &[i32] = &arr[0..2];
```

### 2) 函数与控制流

```rust
fn add(a: i32, b: i32) -> i32 { a + b }

fn main() {
    for i in 0..3 { println!("{i}"); }
    let res = if add(1,2) > 2 { "big" } else { "small" };
    println!("{res}");
}
```

### 3) 结构体 / 枚举 / 模式匹配

```rust
struct User { name: String, age: u8 }

enum Shape {
    Circle(f64),
    Rect { w: f64, h: f64 },
}

impl Shape {
    fn area(&self) -> f64 {
        match self {
            Shape::Circle(r) => std::f64::consts::PI * r * r,
            Shape::Rect { w, h } => w * h,
        }
    }
}
```

### 4) 所有权/借用小例

```rust
fn takes(s: String) { println!("{s}"); }     // 取得所有权
fn borrows(s: &str) { println!("{s}"); }     // 借用（&String 可自动转换为 &str）

fn demo() {
    let s = String::from("hello");
    borrows(&s);        // 借用，不转移所有权
    takes(s);           // 所有权移动
    // println!("{s}"); // ❌ s 已被移动
}
```

### 5) 错误处理（Result + ?）

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_all(p: &str) -> io::Result<String> {
    let mut s = String::new();
    File::open(p)?.read_to_string(&mut s)?;  // 出错自动向上返回
    Ok(s)
}
```

### 6) 模块/包（crate）

* 包管理器 **Cargo** 组织项目：`Cargo.toml` + `src/`。
* 模块用 `mod` 声明，`pub` 导出；外部依赖写到 `Cargo.toml` 的 `[dependencies]`。

---

## 四、开发环境与工具链

### 1) 安装 Rust（跨平台统一用 rustup）

**Windows / macOS / Linux**：

```bash
# 官方推荐安装器
curl https://sh.rustup.rs -sSf | sh
# 或 Windows 直接运行 rustup-init.exe（官方安装器）
```

安装后：

```bash
rustc --version
cargo --version
```

**Windows 选择 MSVC 工具链**（默认）：
建议安装 *Visual Studio Build Tools*（勾选“C++ 桌面开发”）。
切换/检查：

```bash
rustup default stable-x86_64-pc-windows-msvc
rustup toolchain list
```

### 2) 推荐 IDE/编辑器

* **VS Code + rust-analyzer**（主流、轻量）：

  * 安装扩展 `rust-analyzer`、`Even Better TOML`、`CodeLLDB`（调试）。
* **JetBrains CLion/IntelliJ + Rust 插件**（强大、付费为主）。
* **Neovim**：`rust-analyzer` + `nvim-lspconfig` + `mason.nvim` + `dap`。

### 3) 常用工具

```bash
rustup component add rustfmt        # 代码格式化
rustup component add clippy         # 代码静态检查
cargo fmt                           # 格式化
cargo clippy                        # 运行 lint
cargo doc --open                    # 生成并打开文档
```

---

## 五、你的第一个项目：Hello World

### 方式 A：用 Cargo（推荐）

```bash
cargo new hello-rust
cd hello-rust
cargo run
```

会看到：

```
Hello, world!
```

项目结构：

```
hello-rust/
  Cargo.toml
  src/main.rs      // 入口
```

改 `src/main.rs`：

```rust
fn main() {
    println!("Hello, Rust! 🚀");
}
```

### 方式 B：单文件直接编译

```bash
cat > hello.rs <<'RS'
fn main() { println!("Hello, Rust!"); }
RS

rustc hello.rs
./hello
```

### 构建发布版（优化）

```bash
cargo build --release
# 可执行文件在 target/release/
```

---

## 六、引入第三方库（crates.io）

以 HTTP 客户端 `reqwest` 为例：

```toml
# Cargo.toml
[package]
name = "http-demo"
version = "0.1.0"
edition = "2021"

[dependencies]
reqwest = { version = "0.12", features = ["json"] }
tokio = { version = "1", features = ["full"] }
```

```rust
// src/main.rs
#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let text = reqwest::get("https://httpbin.org/get").await?.text().await?;
    println!("{text}");
    Ok(())
}
```

运行：

```bash
cargo run
```

---

## 七、测试与文档

### 单元测试

```rust
// src/lib.rs
pub fn add(a: i32, b: i32) -> i32 { a + b }

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn it_works() { assert_eq!(add(2, 3), 5); }
}
```

```bash
cargo test
```

### 生成文档

```bash
cargo doc --open
```

---

## 八、常见坑与小贴士

* **String vs \&str**：`String` 是可变堆字符串，`&str` 是切片（不可变视图）。函数参数尽量用 `&str`，兼容性更好。
* **可变借用唯一性**：同一可变引用的独占约束常会触发借用检查；用更小作用域或重构为不可变 + 新值返回。
* **生命周期报错**：先尝试让变量活得更久/减少引用交错；把数据**拥有权**上移，减少共享引用复杂度。
* **编译慢**：第一次拉依赖会慢；后续增量会快很多。生产用 `cargo build --release`。

---

## 九、下一步学习路径

1. 《The Rust Programming Language》（俗称 **TRPL**）
2. 练习：写 CLI（`clap`）、并发（`std::thread`/`tokio`）、序列化（`serde`）、数据库（`sqlx`/`diesel`）、Web（`axum`/`actix-web`）。
3. 读源码：`anyhow`、`thiserror`、`rayon`、`tokio` 等高质量crate。

---

### 一句话总结

装 **rustup** → 开 **Cargo 项目** → 写 `main()` 打印 → 通过小项目掌握所有权/借用/Result → 上手常用 crates。
到这一步，你已经可以自如地写出并运行 **Hello, Rust!** 了。


# ##############################

在 Rust 项目里，**`rustc`** 和 **`cargo`** 是两个核心工具，但各自扮演的角色不一样：

---

## 1. `rustc` —— Rust 编译器

* **作用**：把 `.rs` 源代码文件编译成目标文件（可执行文件、库文件等）。
* **用法**：

  ```bash
  rustc main.rs
  ```

  这样会直接把 `main.rs` 编译成一个二进制可执行文件（通常叫 `main` 或 `main.exe`）。
* **特点**：

  * 只能处理单个源文件（或需要手动管理依赖和编译参数）。
  * 更接近“底层”，类似 C 语言里的 `gcc` 或 `clang`。
  * 适合学习或写小型 demo 时快速编译运行。

---

## 2. `cargo` —— Rust 的构建和包管理工具

* **作用**：

  * 自动调用 `rustc` 进行编译，但同时管理整个项目、依赖和构建流程。
  * 相当于 `npm`（JavaScript）、`pip`（Python）、`maven`（Java）的角色。
* **主要功能**：

  1. **项目管理**：一键新建项目：

     ```bash
     cargo new my_project
     ```

     自动生成 `Cargo.toml` 配置文件和目录结构。
  2. **编译构建**：

     ```bash
     cargo build      # 编译项目（调试模式）
     cargo build --release   # 发布模式，开启优化
     ```
  3. **运行**：

     ```bash
     cargo run
     ```

     会先编译（如果需要），再运行。
  4. **依赖管理**：

     * 在 `Cargo.toml` 里声明依赖，比如：

       ```toml
       [dependencies]
       rand = "0.8"
       ```
     * 然后执行：

       ```bash
       cargo build
       ```

       会自动下载并编译依赖。
  5. **测试/文档**：

     ```bash
     cargo test
     cargo doc --open
     ```

---

## 3. 总结对比

| 工具      | 主要用途                                | 使用场景            |
| ------- | ----------------------------------- | --------------- |
| `rustc` | 编译单个 `.rs` 文件 → 可执行程序               | 学习、写 demo、实验性代码 |
| `cargo` | 项目管理 + 调用 `rustc` 编译 + 依赖管理 + 测试/发布 | 实际开发项目、团队协作     |

👉 可以理解为：

* **`rustc` 是发动机**，能让代码跑起来；
* **`cargo` 是整辆车**，有驾驶室、油箱、导航，帮你更方便地开车。

---

要不要我给你做一个 **实际示例**：同样是“Hello, world!”项目，用 `rustc` 和 `cargo` 各自怎么操作，让你直观对比两者区别？


















