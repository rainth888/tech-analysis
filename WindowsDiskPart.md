Windows DiskPart 是 Windows 自带的磁盘分区工具，适合处理 SD 卡、U 盘、硬盘的分区清理、格式化、恢复容量异常等问题。

下面按你前面说的 **SanDisk 读卡器 / SD 卡格式化** 场景来讲。

---

## 一、打开 DiskPart

先把 SD 卡插入 SanDisk 读卡器。

然后在 Windows 中：

1. 右键点击 **开始菜单**
2. 选择 **终端管理员 / Windows PowerShell 管理员 / 命令提示符管理员**
3. 输入：

```bat
diskpart
```

进入后会显示：

```bat
DISKPART>
```

---

## 二、查看磁盘列表

输入：

```bat
list disk
```

你会看到类似：

```bat
磁盘 ###  状态      大小
--------  --------  -----
磁盘 0    联机      512 GB
磁盘 1    联机      128 GB
磁盘 2    联机      29 GB
```

这里要根据容量判断哪一个是 SD 卡。

例如你的 SD 卡是 32GB，通常可能是：

```bat
磁盘 2    29 GB
```

注意：**一定不要选错磁盘。选错会清空电脑硬盘数据。**

---

## 三、选择 SD 卡磁盘

假设 SD 卡是磁盘 2，输入：

```bat
select disk 2
```

系统会提示：

```bat
磁盘 2 现在是所选磁盘。
```

再次确认一下：

```bat
detail disk
```

看容量、类型是否像你的 SD 卡。

---

## 四、清除 SD 卡分区表

如果你只是想恢复 SD 卡容量、清除乱分区、删除 Linux 镜像分区，输入：

```bat
clean
```

这一步会清除 SD 卡上的所有分区信息。

执行后会提示：

```bat
DiskPart 成功地清除了磁盘。
```

---

## 五、重新创建主分区

输入：

```bat
create partition primary
```

然后选中新分区：

```bat
select partition 1
```

激活分区一般 SD 卡不需要，但如果是某些老设备或启动卡，可以执行：

```bat
active
```

普通存储卡可以不执行 `active`。

---

## 六、格式化 SD 卡

### 1. 32GB 以内 SD 卡，推荐 FAT32

```bat
format fs=fat32 quick
```

### 2. 64GB 及以上 SD 卡，推荐 exFAT

```bat
format fs=exfat quick
```

### 3. 需要 NTFS 时

```bat
format fs=ntfs quick
```

不过 SD 卡通常不建议优先用 NTFS，除非你明确只在 Windows 设备上使用。

---

## 七、分配盘符

格式化完成后，输入：

```bat
assign
```

系统会自动给 SD 卡分配一个盘符，例如 E:、F:。

然后退出：

```bat
exit
```

再退出一次命令行即可。

---

# 常用完整命令示例

## 示例一：32GB SD 卡格式化为 FAT32

```bat
diskpart
list disk
select disk 2
detail disk
clean
create partition primary
format fs=fat32 quick
assign
exit
```

---

## 示例二：128GB SD 卡格式化为 exFAT

```bat
diskpart
list disk
select disk 2
detail disk
clean
create partition primary
format fs=exfat quick
assign
exit
```

---

## 示例三：只清除 SD 卡异常分区

如果 SD 卡被写过 Linux 镜像、树莓派镜像、OpenWrt 镜像，Windows 显示容量异常，可以这样做：

```bat
diskpart
list disk
select disk 2
clean
exit
```

然后再用：

```text
SD Memory Card Formatter
```

进行官方格式化。

这是比较稳妥的方式。

---

# 重要注意事项

## 1. `clean` 会清空整张卡

执行：

```bat
clean
```

后，SD 卡上的文件、分区都会被删除。

如果里面有重要数据，先备份。

---

## 2. 大于 32GB 的卡，DiskPart 通常不能格式化成 FAT32

例如 64GB、128GB、256GB 卡，如果执行：

```bat
format fs=fat32 quick
```

可能会失败。

这不是 SD 卡坏了，而是 Windows 的限制。

这种情况可以用：

```text
GUIFormat
Rufus
DiskGenius
```

强制格式化成 FAT32。

---

## 3. 老设备建议用 MBR + FAT32

如果 SD 卡是给老相机、老行车记录仪、老工控设备、老播放器用，建议：

```text
MBR 分区表
单个主分区
FAT32 文件系统
```

---

## 4. 新设备、大容量卡建议 exFAT

如果是 64GB 以上，且设备支持 SDXC，建议：

```text
exFAT
```

兼容性通常更好。

---

## 推荐你按这个流程操作

针对 SanDisk 读卡器 + SD 卡，我建议：

```text
DiskPart clean
↓
SD Memory Card Formatter 格式化
↓
目标设备中再格式化一次
```

这是兼容性最好的处理方式。
