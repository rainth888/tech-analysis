

#

docker exec -it mysql8 mysql -uroot -p

# WSL2 + Ubuntu 24.04 + Docker MySQL 8.0。 安装指南

---

## 一、整体环境说明

* 宿主机：Windows 11
* WSL：Ubuntu 24.04 (noble)，启用了 systemd
* Docker：Docker Engine - Community（在 WSL 里原生跑）
* 数据库：MySQL 8.0 官方镜像（`mysql:8.0`）
* 部署方式：Docker 容器，持久化到宿主目录 `/srv/mysql`
* 访问方式：

  * WSL 内：`127.0.0.1:3306`
  * Windows 客户端：`localhost:3306` 或 `WSL IP:3306`

---

## 二、Docker 安装与网络/代理（简版记录）

> 这部分你已经搞定了，这里只是归档一下思路，方便以后回顾。

1. 在 WSL2 中安装 Docker Engine（略去具体命令）：

   * 添加 Docker 官方仓库（`https://download.docker.com/linux/ubuntu noble stable`）。
   * 安装 `docker-ce docker-ce-cli containerd.io ...`。
   * 将当前用户加入 `docker` 组：`sudo usermod -aG docker $USER`。

2. 配置 Docker 守护进程走 Windows 上的代理（Clash 等）：

   在 WSL 中：

   ```bash
   sudo mkdir -p /etc/systemd/system/docker.service.d
   sudo tee /etc/systemd/system/docker.service.d/proxy.conf >/dev/null <<'EOF'
   [Service]
   Environment="HTTP_PROXY=http://<你的Windows网关IP>:7890"
   Environment="HTTPS_PROXY=http://<你的Windows网关IP>:7890"
   Environment="NO_PROXY=localhost,127.0.0.1,::1,.local,.wsl,host.docker.internal,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16"
   EOF

   sudo systemctl daemon-reload
   sudo systemctl restart docker
   ```

3. 让 Docker 用固定 DNS（防止奇怪的解析问题）：

   ```bash
   sudo mkdir -p /etc/docker
   sudo tee /etc/docker/daemon.json >/dev/null <<'EOF'
   {
     "dns": ["8.8.8.8", "1.1.1.1"]
   }
   EOF

   sudo systemctl restart docker
   ```

---

## 三、MySQL 8.0 容器安装与目录结构

### 1. 准备数据/配置/日志目录

```bash
sudo mkdir -p /srv/mysql/{data,conf,logs}
sudo chown -R $USER:$USER /srv/mysql
```

> 约定：
>
> * 数据：`/srv/mysql/data`
> * 自定义配置：`/srv/mysql/conf`
> * 日志：`/srv/mysql/logs`

### 2.（可选）写一个基础配置

```bash
cat > /srv/mysql/conf/my.cnf <<'EOF'
[mysqld]
# 全局字符集
character-set-server = utf8mb4
collation-server     = utf8mb4_0900_ai_ci

[client]
default-character-set = utf8mb4
EOF
```

如果你只在本地用，不强制旧客户端，可以先不改 `default_authentication_plugin`，保持 MySQL 8.0 默认的 `caching_sha2_password`，更安全。

### 3. 拉取 MySQL 8.0 镜像

```bash
docker pull mysql:8.0
```

### 4. 启动 MySQL 8.0 容器

```bash
export MYSQL_ROOT_PW='YourStrong!Root#Pass'
export MYSQL_APP_DB='appdb'
export MYSQL_APP_USER='appuser'
export MYSQL_APP_PW='YourStrong!App#Pass'

docker network create devnet || true

docker run -d \
  --name mysql80 \
  --restart unless-stopped \
  --network devnet \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD="$MYSQL_ROOT_PW" \
  -e MYSQL_DATABASE="$MYSQL_APP_DB" \
  -e MYSQL_USER="$MYSQL_APP_USER" \
  -e MYSQL_PASSWORD="$MYSQL_APP_PW" \
  -v /srv/mysql/data:/var/lib/mysql \
  -v /srv/mysql/conf:/etc/mysql/conf.d \
  -v /srv/mysql/logs:/var/log/mysql \
  mysql:8.0
```

说明一下几个关键点：

* `--restart unless-stopped`：WSL 里重启 Docker 后自动拉起 MySQL。
* `-p 3306:3306`：将容器 3306 映射到 WSL 的 3306。
* `-v /srv/mysql/data:/var/lib/mysql`：数据持久化，不随容器删除而丢。
* `-v /srv/mysql/conf:/etc/mysql/conf.d`：挂载你自定义配置。
* `-v /srv/mysql/logs:/var/log/mysql`：日志方便在宿主查看。

---

## 四、初次登录与账户配置

### 1. 在 WSL 中登录 MySQL（容器内）

```bash
docker exec -it mysql80 mysql -uroot -p
# 输入 $MYSQL_ROOT_PW
```

进入后可以检查：

```sql
SHOW DATABASES;
SELECT user, host, plugin FROM mysql.user;
```

### 2. 在 WSL 直接使用 mysql 客户端（可选）

如果要用宿主的 `mysql` 命令连：

```bash
sudo apt install -y mysql-client-core-8.0

mysql -h 127.0.0.1 -P 3306 -u root -p
```

---

## 五、Windows 11 客户端连接 MySQL 8.0

### 1. 选择 IP 地址

因为你用的是 `-p 3306:3306` 映射，情况比较简单：

* 多数情况下，Windows 上的客户端（Navicat、DBeaver、Workbench）可以直接用：

  * Host：`localhost`
  * Port：`3306`

如果有问题，可以在 WSL 中查实际 IP：

```bash
hostname -I
# 例如输出：172.26.48.120
```

然后在 Windows 客户端里尝试：

* Host：`172.26.48.120`
* Port：`3306`

### 2. 典型连接参数

以 Navicat/DBeaver 等为例：

* Host：`localhost` 或 `WSL IP`
* Port：`3306`
* User：`root` 或 `appuser`
* Password：启动时设置的密码
* Database：可选填 `appdb`，或者留空先连上再选库
* Charset：`utf8mb4`

### 3. 处理 2059 认证错误（老客户端）

如果某些老客户端/驱动报：

> 2059 - Authentication plugin 'caching_sha2_password' cannot be loaded

解决方案有两个：

#### 方案 A：升级客户端/驱动（推荐）

* 用较新的 Navicat/DBeaver。
* 用 MySQL Workbench 8.x。
* 代码中使用新版驱动（例如 Python 的 `mysql-connector-python`、Node.js 的 `mysql2` 等）。

#### 方案 B：把用户改为 `mysql_native_password`（MySQL 8.0 支持）

在 MySQL 8.0 容器内执行：

```sql
ALTER USER 'root'@'%'     IDENTIFIED WITH mysql_native_password BY 'YourStrong!Root#Pass';
ALTER USER 'appuser'@'%'  IDENTIFIED WITH mysql_native_password BY 'YourStrong!App#Pass';
FLUSH PRIVILEGES;

SELECT user,host,plugin FROM mysql.user;
```

看到 `plugin` 变成 `mysql_native_password` 后，老客户端也能正常登录。

> **注意**：你之前在 8.4 上试图启用 `mysql_native_password` 被卡住，就是因为那版编译时禁用了这个插件；改用 8.0 就解决了这个问题。

---

## 六、日常使用与管理命令（Docker 视角）

### 1. 状态查看

```bash
docker ps           # 看容器是否在跑
docker logs -f mysql80   # 实时看 MySQL 启动/运行日志
```

### 2. 启停/重启

```bash
docker stop mysql80
docker start mysql80
docker restart mysql80
```

### 3. 进入容器内部

```bash
docker exec -it mysql80 bash
# 或直接进 MySQL
docker exec -it mysql80 mysql -uroot -p
```

---

## 七、数据库层面的常用操作

### 1. 创建数据库与用户

```sql
CREATE DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

CREATE USER 'dev'@'%' IDENTIFIED WITH mysql_native_password BY 'DevStrong!Pass';
GRANT ALL PRIVILEGES ON mydb.* TO 'dev'@'%';
FLUSH PRIVILEGES;
```

### 2. 修改密码

```sql
ALTER USER 'dev'@'%' IDENTIFIED BY 'NewStrong!Pass';
FLUSH PRIVILEGES;
```

### 3. 查看当前连接/状态

```sql
SHOW PROCESSLIST;
SHOW VARIABLES LIKE 'character_set%';
SHOW VARIABLES LIKE 'collation%';
```

---

## 八、备份与恢复

### 1. 备份（导出 SQL 文件）

在 WSL 中：

```bash
# 备份单库
docker exec mysql80 sh -c 'exec mysqldump -uroot -p"$MYSQL_ROOT_PASSWORD" mydb' > ~/backup_mydb.sql

# 备份所有数据库
docker exec mysql80 sh -c 'exec mysqldump -uroot -p"$MYSQL_ROOT_PASSWORD" --all-databases' > ~/backup_all.sql
```

### 2. 恢复

```bash
# 恢复到目标库（需已存在 mydb）
mysql -h 127.0.0.1 -P 3306 -uroot -p mydb < ~/backup_mydb.sql

# 或用 docker exec 恢复
docker exec -i mysql80 mysql -uroot -p"$MYSQL_ROOT_PASSWORD" mydb < ~/backup_mydb.sql
```

---

## 九、升级/重建注意事项

* **版本升级**（例如 8.0.x → 8.0.y）：

  1. 备份数据（mysqldump）。
  2. 停容器：`docker stop mysql80`
  3. 拉新镜像：`docker pull mysql:8.0`
  4. 用同样的 `docker run` 参数创建新容器（挂载同一个 `/srv/mysql` 数据目录）。
  5. 验证无误后删除旧容器。

* **严禁** 用 MySQL 8.4 的 data 目录直接回退到 8.0 使用 —— 版本不兼容，会导致 InnoDB 报 “upgrade after downgrade not supported”。

* 实在出问题，可以这样重建（会清空数据）：

  ```bash
  docker stop mysql80
  docker rm mysql80
  sudo rm -rf /srv/mysql/data
  # 然后重新 docker run 初始化
  ```

---

## 十、小结（给未来的你看的）

1. **数据库是跑在 WSL 里的 Docker 容器**：`mysql80`，挂载到 `/srv/mysql`。
2. **Windows 连接方式**：

   * 优先用 `localhost:3306`；
   * 若不稳定，用 `hostname -I` 查 WSL IP，连 `WSL_IP:3306`。
3. **遇到认证 2059 错误**：

   * 优先升级客户端；
   * 或把用户改为 `mysql_native_password`。
4. **数据备份**：

   * 习惯用 `mysqldump`。
   * SQL 文件最好同步一份到 Windows 盘（防止 WSL 环境损坏）。
5. **容器删了数据还在**：

   * 真正的数据在 `/srv/mysql/data`，删除容器不会删库。

---

如果你愿意，下一个阶段我可以帮你：

* 写一个 **小 shell 脚本** 一键打印：

  * 当前 WSL IP
  * Windows 连接信息（`Host/Port/User/DB`）
* 再写一个 **每日自动备份 MySQL 的脚本 + crontab**，
  每天定时把 `mysqldump` 存到你指定的目录（比如 `/mnt/e/mysql_backup`），
  这样你的数据库就变成“想坏都很难”的状态了 😄



# 🐳 在 WSL2（Ubuntu 24.04）中运行 Docker + MySQL 8.4 完全指南

## 一、运行环境结构

| 项目        | 内容                             |
| --------- | ------------------------------ |
| 系统        | WSL2 Ubuntu 24.04 (noble)      |
| Docker 引擎 | Docker Engine 29.x (Community) |
| 网络模式      | bridge + 自建 network `devnet`   |
| MySQL 版本  | 8.4 LTS (官方 `mysql:8.4` 镜像)    |
| 数据持久化     | `/srv/mysql/data`              |
| 配置文件      | `/srv/mysql/conf/my.cnf`       |
| 日志目录      | `/srv/mysql/logs`              |
| 容器名       | `mysql8`                       |
| 宿主端口      | `3306`（可改）                     |

---

## 二、首次部署步骤回顾

```bash
# 1. 创建目录
sudo mkdir -p /srv/mysql/{data,conf,logs}
sudo chown -R $USER:$USER /srv/mysql

# 2. 写配置（可选）
cat > /srv/mysql/conf/my.cnf <<'EOF'
[mysqld]
character-set-server = utf8mb4
collation-server     = utf8mb4_0900_ai_ci

[client]
default-character-set = utf8mb4
EOF

# 3. 启动容器
export MYSQL_ROOT_PW='YourStrong!Root#Pass'
export MYSQL_APP_DB='appdb'
export MYSQL_APP_USER='appuser'
export MYSQL_APP_PW='YourStrong!App#Pass'

docker network create devnet || true

docker run -d \
  --name mysql8 \
  --restart unless-stopped \
  --network devnet \
  -p 3306:3306 \
  -e TZ=UTC \
  -e MYSQL_ROOT_PASSWORD="$MYSQL_ROOT_PW" \
  -e MYSQL_DATABASE="$MYSQL_APP_DB" \
  -e MYSQL_USER="$MYSQL_APP_USER" \
  -e MYSQL_PASSWORD="$MYSQL_APP_PW" \
  -v /srv/mysql/data:/var/lib/mysql \
  -v /srv/mysql/conf:/etc/mysql/conf.d \
  -v /srv/mysql/logs:/var/log/mysql \
  mysql:8.4
```

验证容器运行：

```bash
docker ps
```

---

## 三、MySQL 的基本操作

### 1. 登录容器内部数据库

```bash
docker exec -it mysql8 mysql -uroot -p
```

输入你设置的 root 密码。

### 2. 在宿主机（WSL）直接连接

Ubuntu 默认没装客户端，可先安装：

```bash
sudo apt install -y mysql-client-core-8.0
```

再执行：

```bash
mysql -h 127.0.0.1 -P 3306 -u root -p
```

### 3. 创建与管理数据库

```sql
CREATE DATABASE testdb CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
CREATE USER 'tester'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON testdb.* TO 'tester'@'%';
FLUSH PRIVILEGES;
```

---

## 四、常用 Docker 管理命令

| 操作     | 命令                                               |
| ------ | ------------------------------------------------ |
| 查看运行容器 | `docker ps`                                      |
| 查看日志   | `docker logs -f mysql8`                          |
| 进入容器   | `docker exec -it mysql8 bash`                    |
| 重启容器   | `docker restart mysql8`                          |
| 停止容器   | `docker stop mysql8`                             |
| 删除容器   | `docker rm -f mysql8`                            |
| 更新镜像   | `docker pull mysql:8.4 && docker restart mysql8` |

> 删除容器不会删除数据卷，`/srv/mysql` 会保留。

---

## 五、备份与恢复

### 1. 备份数据库

```bash
docker exec mysql8 sh -c 'exec mysqldump -uroot -p"$MYSQL_ROOT_PASSWORD" --all-databases' > ~/mysql_backup.sql
```

### 2. 恢复数据库

```bash
mysql -h 127.0.0.1 -P 3306 -uroot -p < ~/mysql_backup.sql
```

---

## 六、性能与配置要点

| 项    | 说明                                                         |
| ---- | ---------------------------------------------------------- |
| 字符集  | 推荐 `utf8mb4 / utf8mb4_0900_ai_ci`                          |
| 时区   | `TZ=UTC` 或 `Asia/Shanghai`                                 |
| 用户认证 | 默认 `caching_sha2_password`；旧客户端需改为 `mysql_native_password` |
| 存储路径 | `/srv/mysql/data`；删除容器不丢数据                                 |
| 自动重启 | `--restart unless-stopped` 保证 WSL 重启后自动拉起                  |

---

## 七、启动失败或无法访问排查

| 现象                             | 处理方式                                                   |
| ------------------------------ | ------------------------------------------------------ |
| `bind: address already in use` | 改端口：`-p 3307:3306`                                     |
| 登录报 “Access denied”            | 检查密码或 `ALTER USER` 重新设置                                |
| 远程客户端连不上                       | 确认防火墙、WSL IP、MySQL 用户 host='%'                         |
| 数据卷权限问题                        | `sudo chown -R 999:999 /srv/mysql/data`（MySQL UID/GID） |

---

## 八、可选：docker-compose 一键管理

`/srv/mysql/docker-compose.yml`

```yaml
version: '3.9'
services:
  mysql:
    image: mysql:8.4
    container_name: mysql8
    restart: unless-stopped
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: YourStrong!Root#Pass
      MYSQL_DATABASE: appdb
      MYSQL_USER: appuser
      MYSQL_PASSWORD: YourStrong!App#Pass
      TZ: UTC
    volumes:
      - ./data:/var/lib/mysql
      - ./conf:/etc/mysql/conf.d
      - ./logs:/var/log/mysql
```

使用：

```bash
docker compose up -d
docker compose down
```

---

## ✅ 总结

你当前环境已经具备：

* **Docker Engine 在 WSL2 Ubuntu 24.04 下完全运行；**
* **代理配置稳定（172.26.48.1:7890）；**
* **MySQL 8.4 容器正常启动并持久化数据；**
* 可以通过 `docker exec` 或 `mysql -h 127.0.0.1` 登录；
* 数据与配置均存于宿主 `/srv/mysql`，便于备份与迁移。

