下面给你一份「把 Odoo 放进 Docker」的**实战指引**。既适合你现在“源码开发”的场景（挂载本地代码、热重载），也包含“更偏生产”的方式（固定镜像、持久化数据、备份）。

---

# 方案 A：用官方 Odoo 镜像 + 本地源码/插件挂载（推荐起步）

## 目录结构（在 WSL2 的 Linux 路径里建，不要放在 /mnt/c… 以提升性能）

```
/home/you/odoo-docker/
├─ docker-compose.yml
├─ odoo.conf
├─ addons/                 # 你的自定义插件（源码）
├─ data/                   # Odoo 数据目录（filestore 等持久化）
└─ pgdata/                 # PostgreSQL 数据（持久化）
```

## odoo.conf（最小可用）

```ini
[options]
admin_passwd = superadmin123              ; 后台管理密码（创建数据库时用）
db_host = db
db_port = 5432
db_user = proot
db_password = proot
db_name = odoo                            ; 也可不写，登录页创建
addons_path = /usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons
logfile = /var/log/odoo/odoo.log
; http_port = 8069
; dev = reload                            ; 开发期热重载（可选）
```

> 说明
>
> * 我们不依赖环境变量，**用配置文件更稳**。
> * `addons_path` 把官方内置 + 你的自定义 `/mnt/extra-addons` 都包含进去。
> * `dev=reload` 仅开发使用，自动重载 Python/视图（改动即生效）。

## docker-compose.yml

```yaml
version: "3.9"

services:
  db:
    image: postgres:17
    container_name: odoo_db
    restart: unless-stopped
    environment:
      POSTGRES_USER: proot
      POSTGRES_PASSWORD: proot
      POSTGRES_DB: odoo
    volumes:
      - ./pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U proot -d odoo"]
      interval: 5s
      timeout: 3s
      retries: 30

  odoo:
    image: odoo:17
    container_name: odoo_app
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped
    ports:
      - "8069:8069"
    volumes:
      - ./odoo.conf:/etc/odoo/odoo.conf
      - ./addons:/mnt/extra-addons
      - ./data:/var/lib/odoo
    command: ["odoo", "-c", "/etc/odoo/odoo.conf"]
    # 开发期可打开自动重载（等价于在 conf 写 dev=reload）
    # command: ["odoo", "-c", "/etc/odoo/odoo.conf", "--dev=reload"]
```

> 如果你的自定义插件需要**额外 Python 依赖**，看下面“方案 B（自定义镜像）”。

## 启动/停止/日志

```bash
cd /home/you/odoo-docker
docker compose up -d
docker compose logs -f odoo
# 停止
docker compose down
```

浏览器打开：`http://localhost:8069`

* **首次创建数据库**会用到 `admin_passwd`（superadmin123）
* 数据、附件都在 `./data/` 和 `./pgdata/`，容器删掉也不会丢

---

# 方案 B：需要额外 Python 依赖 → 构建自定义 Odoo 镜像

如果你的自定义模块有 `requirements.txt`（如 `python-ldap`, `psycopg2`, `lxml` 等），建议在官方镜像基础上安装，避免每次容器启动都 pip：

**Dockerfile**

```dockerfile
FROM odoo:17

USER root
# 常见构建依赖（按需精简/扩展）
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev libxml2-dev libxslt1-dev \
    libjpeg-dev zlib1g-dev libfreetype6-dev \
    libldap2-dev libsasl2-dev libffi-dev libssl-dev \
  && rm -rf /var/lib/apt/lists/*

# 复制你的依赖清单（如果有）
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt || true

USER odoo
```

**compose 改为：**

```yaml
  odoo:
    build: .
    image: my-odoo:17-dev
    ...
```

> 你之前在 WSL2 手动安装依赖时遇到的那些编译错误（`pg_config`、`lber.h` 等），在这个 Dockerfile 里都统一解决了。

---

# 方案 C：继续用你**现有**的 Postgres 容器

如果你已经有在跑的 `pg170` 容器（端口映射到 5432）——可以让 Odoo 直接连它，不再在 compose 里再起一个 `db`：

* 删除 `services.db`，保留 `odoo`，把 `odoo.conf` 里的 `db_host` 改为 `127.0.0.1`（或你的 Postgres 容器 IP/服务名）。
* **但更推荐**把 Odoo 和 DB 放在**同一个 docker-compose** 里，自动服务发现，用 `db` 当主机名即可，部署/迁移更简单。

---

# 开发者日常：热重载与路径

* **热重载**

  * 在 `odoo.conf` 加 `dev = reload` 或 compose 的 command 里追加 `--dev=reload`。
  * Python/模板改动会自动重载；个别模型变更仍建议 `-u your_module` 更新模块。
* **插件路径**

  * 你的源码放 `./addons/`，容器里挂成 `/mnt/extra-addons`，`addons_path` 已包含了它。
* **日志**

  * 映射到容器内 `/var/log/odoo/odoo.log`（你可在 compose 里再挂载出来），也可 `docker compose logs -f odoo` 直接看。

---

# 备份/恢复（必须要有）

**备份数据库 + filestore：**

```bash
# DB
docker exec -t odoo_db pg_dump -U proot -d odoo | gzip > backup/odoo_$(date +%F).sql.gz
# Filestore（Odoo 附件）
tar czf backup/odoo_filestore_$(date +%F).tgz -C data filestore
```

**恢复：**

```bash
gunzip -c backup/odoo_2025-08-28.sql.gz | docker exec -i odoo_db psql -U proot -d odoo
tar xzf backup/odoo_filestore_2025-08-28.tgz -C data
```

---

# 常见问题与排查

* **8069 或 5432 端口被占用** → 改成 `"18069:8069"` / `"5433:5432"`，客户端连对应宿主端口。
* **Odoo 连不上 DB** → `docker compose logs db` 看健康检查是否 PASS；确认 `odoo.conf` 的 db\_\* 正确；容器在同一网络。
* **安装依赖失败（编译报错）** → 用“方案 B”的 Dockerfile 安装好构建依赖（`libpq-dev/libldap2-dev/...`）。
* **WSL2 I/O 慢** → 把项目放在 WSL 的 Linux 路径（`/home/you/...`），避免 `/mnt/c|d`。

---

# 一键启动脚本（可选）

在项目根建个脚本 `up.sh`：

```bash
#!/usr/bin/env bash
set -e
docker compose pull || true
docker compose up -d
docker compose logs -f odoo
```

给执行权限：`chmod +x up.sh`，以后 `./up.sh` 即可。

---

需要我帮你把**你现有仓库**的 `requirements.txt` 和自定义模块目录嵌入到 Dockerfile（方案 B）里吗？我可以直接给你贴合你项目的 Dockerfile 与 compose，确保第一次 `docker compose up -d` 就能开箱即跑。
