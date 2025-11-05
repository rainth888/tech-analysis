
# 常用

**看容器环境变量**



我需要对postgresql的使用做一个tutorial式的分章节介绍，内容包括快速入门、常用基本命令、互联网常用镜像使用、与mysql比较、常见问题分析及解答。


# 🐘 PostgreSQL Tutorial 分章节教程

## 第 1 章：PostgreSQL 快速入门

### 1.1 什么是 PostgreSQL

* 一款开源的 **对象关系型数据库系统 (ORDBMS)**，被认为是最先进、最强大的开源数据库。
* 特点：

  * 支持 **复杂 SQL 查询**、**事务处理**、**并发控制**；
  * 提供 **JSON、GIS、全文搜索** 等扩展；
  * 高度可扩展（用户自定义函数、数据类型、插件）。

### 1.2 安装 PostgreSQL

* **Linux**：

  ```bash
  sudo apt install postgresql postgresql-contrib   # Debian/Ubuntu
  sudo yum install postgresql-server postgresql-contrib  # CentOS/RedHat
  ```
* **macOS**：

  ```bash
  brew install postgresql
  ```
* **Windows**：
  通过 [EnterpriseDB 安装器](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)。

### 1.3 启动与基本使用

```bash
# 启动服务
sudo service postgresql start   # systemctl start postgresql

# 登录数据库
sudo -u postgres psql

# 创建数据库用户和数据库
createuser myuser -P
createdb mydb -O myuser
```

---

## 第 2 章：常用基本命令

### 2.1 连接与退出

```sql
psql -U myuser -d mydb -h localhost -p 5432
\q    -- 退出
```

### 2.2 数据库与表

```sql
-- 创建数据库
CREATE DATABASE testdb;

-- 切换数据库
\c testdb;

-- 创建表
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

-- 插入数据
INSERT INTO users (name, age) VALUES ('Alice', 25);

-- 查询数据
SELECT * FROM users;
```

### 2.3 常用 psql 命令

```sql
\l     -- 列出所有数据库
\dt    -- 列出当前数据库的表
\d users  -- 查看表结构
\du    -- 查看用户列表
```

---

## 第 3 章：互联网常用镜像使用

### 3.1 Docker 镜像运行 PostgreSQL

```bash
# 拉取镜像
docker pull postgres

# 启动容器
docker run -d --name pgdb \
    -e POSTGRES_USER=myuser \
    -e POSTGRES_PASSWORD=mypass \
    -e POSTGRES_DB=mydb \
    -p 5432:5432 postgres:16
```

### 3.2 配合 pgAdmin（可视化管理）

```bash
docker run -d --name pgadmin \
    -e PGADMIN_DEFAULT_EMAIL=admin@test.com \
    -e PGADMIN_DEFAULT_PASSWORD=admin \
    -p 8080:80 dpage/pgadmin4
```

然后浏览器访问 `http://localhost:8080` 即可。

### 3.3 常用工具与生态

* **pgAdmin**：官方 GUI 管理工具
* **DBeaver**：通用数据库管理工具
* **PostGIS**：GIS 扩展
* **TimescaleDB**：时间序列扩展

---

## 第 4 章：与 MySQL 的比较

| 维度           | PostgreSQL        | MySQL           |
| ------------ | ----------------- | --------------- |
| **定位**       | 企业级、功能全面、复杂查询强    | 轻量、Web 应用广泛     |
| **SQL 标准支持** | 更严格、支持更多标准        | 较宽松             |
| **事务**       | MVCC 强大、并发支持优     | 支持（InnoDB），但细节弱 |
| **扩展性**      | 强（插件、数据类型、函数）     | 相对弱             |
| **NoSQL 支持** | 原生 JSONB、全文检索、GIS | JSON 支持较弱       |
| **性能**       | 复杂查询/写入型强         | 读多写少场景快         |
| **社区/生态**    | 稳定、学术和大企业爱用       | Web 开发者与中小企业多   |

总结：

* **MySQL** → 轻量级、Web 后端常见；
* **PostgreSQL** → 更适合金融、电信、GIS、大数据分析等复杂场景。

---

## 第 5 章：常见问题分析及解答

### 5.1 连接失败

**问题**：`psql: could not connect to server`
**解决**：

* 检查服务是否启动：`systemctl status postgresql`
* 编辑 `pg_hba.conf` 确认客户端连接权限。
* 确认 `listen_addresses='*'` 并开放防火墙端口。

### 5.2 用户/密码错误

**解决**：在 `psql` 内执行：

```sql
ALTER USER myuser WITH PASSWORD 'newpass';
```

### 5.3 数据库性能慢

**解决**：

* 使用 `EXPLAIN ANALYZE` 查看执行计划。
* 建立索引（B-Tree/GIN/BRIN）。
* 调整 `work_mem`、`shared_buffers` 等参数。

### 5.4 容器数据丢失

**原因**：未挂载卷。
**解决**：

```bash
docker run -d --name pgdb \
  -v pgdata:/var/lib/postgresql/data \
  postgres
```

### 5.5 MySQL 转 PostgreSQL 难点

* **自增字段**：MySQL `AUTO_INCREMENT` → PostgreSQL `SERIAL` 或 `IDENTITY`。
* **时间戳**：Postgres `TIMESTAMP WITH TIME ZONE` 更标准。
* **大小写敏感**：Postgres 标识符区分大小写（需注意引号）。
* **工具**：`pgloader` 可用于迁移。

---

# ✅ 总结

这份教程结构包含：

1. 快速入门与安装使用
2. 常用命令
3. Docker 镜像和常见工具
4. 与 MySQL 对比
5. 常见问题与解决方案

---

要不要我帮你把这份教程整理成一个 **Markdown 或 PDF 教程文档**，方便你保存和分享？

# *****************************************************************************************************************************************

下面是一套 **“一条龙”** 操作指引，帮你用 Docker 在 Ubuntu 20.04 上运行 **PostgreSQL 17**，容器名 `pg170`，库内超级用户 `proot`。  
所有命令直接复制即可用；如遇权限问题，在前面加 `sudo`。

------------------------------------------------
1. 安装 Docker（若已装可跳过）
```bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl enable --now docker
sudo usermod -aG docker $USER   # 让自己不用 sudo 就能用 docker
newgrp docker                   # 立即生效
```

------------------------------------------------
2. 一键启动 PostgreSQL 17 容器
```bash
docker run -d \
  --name pg170 \
  -e POSTGRES_USER=proot \
  -e POSTGRES_PASSWORD=prootpass \
  -e POSTGRES_DB=postgres \
  -p 5432:5432 \
  -v $HOME/pg17-data:/var/lib/postgresql/data \
  postgres:17
```
说明  
- `proot` 是超级用户；密码自己改。  
- 端口 5432 映射到宿主机，方便外部工具连。  
- 数据卷 `$HOME/pg17-data` 持久化。

------------------------------------------------
3. 进入容器 / 连上数据库
```bash
# 进入容器 bash
docker exec -it pg170 bash

# 在容器里用 psql 连库
psql -U proot -d postgres      # 交互式
# 或一条命令直接执行 SQL
psql -U proot -d postgres -c "SELECT version();"
```

------------------------------------------------
4. 常用数据库 / 表 / 数据操作

4.1 创建新库、新用户
```sql
-- 在 psql 里
CREATE DATABASE mydb OWNER proot;
CREATE USER appuser WITH PASSWORD 'apppass';
GRANT ALL PRIVILEGES ON DATABASE mydb TO appuser;
```

4.2 建表 & 插入
```sql
\c mydb                       -- 切换到 mydb
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);
INSERT INTO users(name, email) VALUES ('Alice','alice@a.com'),('Bob','bob@b.com');
```

4.3 查询
```sql
SELECT * FROM users;
SELECT * FROM users WHERE id = 1;
```

4.4 备份 / 恢复（容器外执行）
```bash
# 备份 mydb 到宿主机
docker exec -t pg170 pg_dump -U proot mydb > $HOME/mydb.sql

# 恢复
cat $HOME/mydb.sql | docker exec -i pg170 psql -U proot -d mydb
```

------------------------------------------------
5. 用本地 GUI 工具连接
- **DBeaver / pgAdmin / DataGrip**  
  Host: `localhost`  
  Port: `5432`  
  Database: `postgres` 或 `mydb`  
  User: `proot` / `appuser`  
  Password: 对应密码

------------------------------------------------
6. 常用运维命令
```bash
# 查看日志
docker logs -f pg170

# 停止 / 启动 / 删除
docker stop pg170
docker start pg170
docker rm -f pg170          # 删除容器（数据卷还在）
```

至此，PostgreSQL 17 已在 Docker 中正常运行，库、表、查询、备份一条龙搞定。


# *****************************************************************************************************************************************

你的容器 **pg170（postgres:17）已经存在** 并且正常运行，所以 Docker 会提示 “Unable to find image …” 只是之前拉取时被打断，实际镜像已下载完成，容器也已启动。  
**无需再次 `docker run`**，直接按下面步骤使用即可：

------------------------------------------------
1. 确认容器状态  
```bash
docker ps -a 
# 输出应类似：
# 3ebca6a51cee postgres:17.0 Up About an hour 0.0.0.0:5432->5432/tcp pg170
```

2. 进入容器并连数据库  
```bash
# 进入容器 bash
docker exec -it pg170 bash

# 用 psql 登录
psql -U proot -d postgres
```
出现 `postgres=#` 提示符即成功。

3. 常用 SQL 示例  
```sql
-- 建库
CREATE DATABASE mydb OWNER proot;

-- 建表
\c mydb
CREATE TABLE users(id SERIAL PRIMARY KEY, name VARCHAR(50));
INSERT INTO users(name) VALUES ('Alice'),('Bob');

-- 查询
SELECT * FROM users;
```

4. 退出  
- `exit`  退出 psql  
- `exit`  退出容器 bash

------------------------------------------------
如果只是想 **重置或重新创建** 容器：

```bash
docker stop pg170
docker rm pg170
# 再执行你之前的 docker run 命令即可
```

当前容器已可用，无需再拉镜像。




# *****************************************************************************************************************************************

好的，我们就把 PostgreSQL（Odoo 默认数据库）从“零基础”到“安全、健壮”一步走全。以下步骤假设你的 Odoo 与 PostgreSQL 都在 Ubuntu 服务器上（root 或 sudo 权限），并面向 Odoo 18。

# 1) 基本盘点与最小暴露面

1. 确认数据库版本与状态

```bash
psql --version
sudo systemctl status postgresql
```

2. 如果 Odoo 和数据库在同一台服务器，**不要对外开放 PostgreSQL 端口**（默认 5432）：

* 仅监听本机：

  ```bash
  sudo -u postgres psql -c "SHOW listen_addresses;"
  # 若不是 'localhost' 或 '127.0.0.1'，编辑：
  sudo nano /etc/postgresql/*/main/postgresql.conf
  # 修改为：
  # listen_addresses = '127.0.0.1'
  sudo systemctl restart postgresql
  ```
* 防火墙（若必须远程访问，只放行你需要的固定来源 IP）：

  ```bash
  sudo ufw allow from <你的办公固定IP> to any port 5432
  sudo ufw deny 5432    # 若完全本机访问，可禁用对外
  ```

# 2) 开启强密码机制（SCRAM）、限制认证源

1. 启用更安全的密码存储：
   编辑 `postgresql.conf`：

   ```bash
   sudo nano /etc/postgresql/*/main/postgresql.conf
   # 确保：
   # password_encryption = scram-sha-256
   sudo systemctl restart postgresql
   ```

2. 收紧 `pg_hba.conf`（认证策略）：

   ```bash
   sudo nano /etc/postgresql/*/main/pg_hba.conf
   ```

   推荐规则（示例，按需增减）：

   ```
   # 仅 postgres 系统管理员本地 peer 登录
   local   all             postgres                                peer

   # Odoo 应用用户仅允许本机 IPv4 通过 SCRAM
   host    all             odoo                                   127.0.0.1/32   scram-sha-256

   # 如需远程访问的特定管理账号（例：dba），只允许你的办公公网 IP
   host    all             dba                 <你的办公固定IP>/32  scram-sha-256

   # 拒绝其他来源
   host    all             all                 0.0.0.0/0           reject
   host    all             all                 ::/0                reject
   ```

   保存后：

   ```bash
   sudo systemctl reload postgresql
   ```

# 3) 角色与权限模型（最小权限）

1. 进入数据库控制台：

```bash
sudo -u postgres psql
```

2. 盘点现有角色与库：

```sql
\du
\l
```

3. 为 Odoo 创建**专用的最小权限角色**（若已存在就改密和权限）：

```sql
-- 建一个只用于应用连接的角色（不能创建数据库/新角色）
CREATE ROLE odoo WITH LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT;
ALTER ROLE odoo PASSWORD '替换为强密码';  -- 将来我们会把密码写进 odoo.conf
```

4. 为日常维护建一个 DBA 管理员（仅你自己使用，且限制远程源 IP）：

```sql
CREATE ROLE dba WITH LOGIN CREATEDB CREATEROLE INHERIT;
ALTER ROLE dba PASSWORD '另一个强密码';
```

5. 若已有 Odoo 数据库（例如 `odoo18_prod`），授予恰当权限（**不要给超级权限**）：

```sql
GRANT CONNECT ON DATABASE odoo18_prod TO odoo;
\c odoo18_prod
GRANT USAGE ON SCHEMA public TO odoo;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO odoo;
GRANT USAGE, SELECT, UPDATE ON ALL SEQUENCES IN SCHEMA public TO odoo;

-- 确保未来新表也自动给权限
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO odoo;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT, UPDATE ON SEQUENCES TO odoo;

-- 可选：收紧 PUBLIC 权限
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON DATABASE odoo18_prod FROM PUBLIC;
```

6. 若你打算**多环境隔离**（prod/test/dev），请**不同数据库 + 不同应用账号**（至少不同密码），并用 `dbfilter`（见第 5 节）隔离。

# 4) Odoo 应用侧安全点

1. Odoo 主配置文件（例如 `/etc/odoo/odoo.conf`）：

```ini
[options]
; 强烈建议：
admin_passwd = 生成一个强随机值
db_user = odoo
db_password = 上面设置的强密码
db_host = 127.0.0.1
db_port = 5432
; 仅允许匹配名称的数据库显示/访问（防止误连他库）
dbfilter = ^%d$
; 生产上不让随便列库：
list_db = False
; 其他性能与安全：
limit_time_cpu = 60
limit_time_real = 120
; workers、longpolling 等按你的部署方案配置
```

* `admin_passwd` 是 Odoo 的“数据库管理主密码（Master Password）”，**一定要强随机**并安全保存。
* `list_db = False` 可避免登录页枚举数据库。

2. **文件权限**：

   * 将 `odoo.conf` 所有权设置为 Odoo 运行用户（例如 `odoo`），并限制读写：

     ```bash
     sudo chown odoo:odoo /etc/odoo/odoo.conf
     sudo chmod 640 /etc/odoo/odoo.conf
     ```
   * 不要以 root 运行 Odoo 服务；使用独立系统用户（如 `odoo`）。

# 5) 如需多库/多实例

* **多数据库隔离**：为每个站点单独 DB（如 `chowta_prod`、`chowta_test`），配合 `dbfilter`，并**不同密码**。
* **多实例**（多 `odoo.conf` + 多 systemd 服务）时，每个实例连接自己的数据库与账号。

# 6) 传输加密（可选但推荐）

* 如果 Odoo 与 PostgreSQL 不在同一台机，建议：

  * **优先走内网专线/VPC 或 SSH 隧道**；
  * 或在 PostgreSQL 端启用 SSL（`postgresql.conf` 中 `ssl=on`，提供 `server.crt/server.key`，`chmod 600 server.key`），并在 `pg_hba.conf` 里要求 `hostssl`；
  * 防火墙**只允许**应用服务器的固定 IP 访问 5432。

# 7) 备份与恢复（务必做！）

1. **定时逻辑备份**（最实用）：

```bash
# 例：每天 03:10 备份到 /var/backups/odoo
sudo mkdir -p /var/backups/odoo && sudo chown postgres:postgres /var/backups/odoo

sudo -u postgres crontab -e
# 加入一行（替换库名与保留策略）
10 3 * * * pg_dump -Fc -d odoo18_prod > /var/backups/odoo/odoo18_prod-$(date +\%F).dump && find /var/backups/odoo -type f -mtime +14 -delete
```

* 恢复演示：

  ```bash
  sudo -u postgres createdb odoo18_restore
  sudo -u postgres pg_restore -d odoo18_restore /var/backups/odoo/odoo18_prod-2025-10-15.dump
  ```

2. **WAL/PITR（进阶）**：需要时开启归档，做到“任意时间点恢复”（Point-In-Time Recovery）。这是高可用/容灾的关键一环。

# 8) 自动维护与健壮性

1. **自动真空/重建统计**（默认启用）：检查是否运行、必要时微调：
   `postgresql.conf` 里相关 `autovacuum_*` 参数可适度加强（具体要看负载和表增长速度）。
2. **监控与日志**：

   * 打开 `log_line_prefix`、`log_min_duration_statement`（适度）帮助定位慢 SQL；
   * 安装 `pg_stat_statements` 扩展分析热点与慢查询：

     ```sql
     CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
     ```
3. **连接池**：用户 3 人 + 1000+ 产品一般无需，但若并发升高，考虑 `pgBouncer` 降低连接开销。
4. **按月审计**：

   * `\du`、`\l` 复核角色/数据库；
   * 轮换 Odoo 的 `db_password`、`admin_passwd`；
   * 检查防火墙与 `pg_hba.conf` 中是否有过期的来源 IP。

# 9) 升级与补丁

* 按发行版安全更新 PostgreSQL（Ubuntu 官方仓库），并定期 `apt update && apt upgrade`；
* 大版本升级用 `pg_upgrade` 或逻辑迁移（`pg_dump/pg_restore`），**先在测试库演练**。

# 10) 一键自检清单（可直接逐条核对）

* [ ] `listen_addresses='127.0.0.1'`（或仅内网 IP）
* [ ] `password_encryption='scram-sha-256'`
* [ ] `pg_hba.conf` 只允许必要来源，策略为 `scram-sha-256`，拒绝 0.0.0.0/0
* [ ] `ufw` 拒绝 5432 对外，或仅允许白名单
* [ ] Odoo 专用角色：`NOSUPERUSER NOCREATEROLE NOCREATEDB`
* [ ] Odoo 数据库最小权限授权 + 收紧 PUBLIC
* [ ] `odoo.conf`：强随机 `admin_passwd`、`list_db=False`、`dbfilter`、`db_user/db_password`
* [ ] `odoo.conf` 权限 640，属主为运行用户
* [ ] 定时逻辑备份 + 定期恢复演练
* [ ] （可选）SSL/隧道、`pg_stat_statements`、连接池、autovacuum 调优
* [ ] 月度审计与密码轮换

---

若你愿意，告诉我你目前的：

* `\du` 与 `\l` 输出（隐藏敏感库名亦可）、
* 现有 `pg_hba.conf` 片段（去掉真实 IP 也行）、
* `odoo.conf` 的数据库相关行（脱敏密码），
  我可以“对照你的实际情况”直接给出一份更贴身的 **最小改动补丁**（含需要执行的 SQL 和需要替换的配置片段）。另外，数据库安全稳住后，我们再回头查“静态页面加载”问题，按网络层（Nginx/代理/静态资源缓存）→ Odoo 配置（assets/longpolling/workers）→ 模块/自定义代码的顺序逐层定位。




# *****************************************************************************************************************************************






# *****************************************************************************************************************************************






# *****************************************************************************************************************************************



























