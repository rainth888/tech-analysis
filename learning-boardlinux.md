下面这份是面向“板载 Linux（裁剪版 BusyBox/Yocto/Buildroot 等）+ SoC（如 GK720x/Hi351x 等）”的工程化说明。尽量讲清楚 DTS 的作用、结构、你在后期加外设（I²C/SPI/UART 等）时的通用改造流程，以及是否必须“升级板级系统（BSP）”还是能通过更小的改动解决。

# 什么是 DTS（Device Tree Source）

* **Device Tree（设备树）**是一种**数据描述**，用来把“硬件拓扑与属性”告诉内核，而不是把这些信息硬编码在驱动里。
* **DTS** 是人类可读的源文件；编译成 **DTB**（Device Tree Blob，二进制）后，由 **U-Boot** 等引导程序传给内核，或被“内核中嵌入/附加”的方式随内核加载。
* 设备树把你的板子抽象成一棵树：SoC → 总线控制器（I²C/SPI/UART/SDIO/MIPI/…）→ 外设设备节点（传感器、触摸、GPIO-LED、按键、PMIC、Regulator……）。
* **驱动匹配**通过 `compatible` 字符串完成（驱动的 OF 匹配表里列出支持的 `compatible`）。
* DTS 常见要素：

  * `compatible`：设备标识，用来和驱动匹配
  * `reg`：寄存器地址/从地址（I²C/SPI 等挂载点地址）
  * `interrupts`：中断线描述
  * `clocks` / `clock-names`：时钟依赖
  * `reset-gpios` / `enable-gpios` / `pwdn-gpios`：控制管脚
  * `vdd-supply`、`avdd-supply`：电源轨（由 regulator 节点提供）
  * `pinctrl-0`、`pinctrl-names`：管脚复用（pinmux）与上下拉等
  * `status = "okay"`：启用该节点（`"disabled"` 为禁用）
  * `aliases`、`chosen`：全局辅助信息（如把 `serial0` 指到具体 UART 节点）
* DTS 组织：通常 `SoC.dtsi`（芯片通用）+ `Board.dts`（板级差异），`Board.dts` 里 `#include` 若干 `.dtsi`。

# 为什么 I²C/SPI/UART 常常**必须**改 DTS

* **USB/PCI** 这类**可枚举**总线能自发现设备；但 **I²C、SPI、UART** **不具备自枚举**能力，内核要“知道”你的外设挂在何处、占用哪个地址/片选/中断、用哪些 GPIO/电源/时钟，才能绑定相应驱动。因此：

  * 仅仅“`modprobe` 加载一个驱动模块”**并不会**自动实例化这些外设；
  * 必须通过 **DTS（或 DTS Overlay）** 来**声明设备节点**，驱动才会创建对应的 platform 设备并工作。
* 有些“原型/调试”方式可以临时**手动实例化**：

  * I²C：`echo <chipname> <addr> > /sys/bus/i2c/devices/i2c-<bus>/new_device`
  * SPI：用 `spidev` + 用户态访问（需要在 DTS 允许 `spidev`，或临时 new_device）
    但这两种都偏临时/不稳定（尤其是 SPI new_device），**发布/量产应回到 DTS**。

# 你加了外设之后，是否要“升级 BSP”？

不一定要“升级 BSP（重编内核、迁移大版本）”，更常见且工程化的做法是：

1. **确认内核已包含/可加载相应驱动**

* 查看目标外设的 Linux 驱动：是否已在你的 kernel 源里，`CONFIG_xxx` 是否开启（内建 `=y` 或模块 `=m`）。
* 如果你的板子采用“**DTB 与内核分离加载**”（U-Boot 从分区/文件系统各自加载），**只改 DTB 即可**；无需动内核。
* 若你的平台把 DTB **打包进内核镜像**（如 `zImage-dtb`），那改 DTS 后要**重新拼接/重打包镜像**（但仍不算“升级 BSP”，只是重打包）。

2. **修改/新增 DTS 或使用“DTS Overlay”**

* **直接改板级 DTS**：最直接可靠；改完 `make dtbs`，替换 DTB 文件，重启即可。
* **DTS Overlay（叠加层）**：把“新增外设/引脚/电源”等改动做成 overlay，在引导阶段“套上去”：

  * 需要 **CONFIG_OF_OVERLAY** 支持；
  * U-Boot 可在启动脚本里 `fdt apply` 叠加；
  * 也可在内核运行中用 configfs（`/sys/kernel/config/device-tree/overlays/...`）动态加载 overlay。
* **好处**：做不同外设组合（SKU）的弹性配置，不必每次重做主 DTB 或重编内核。

3. **只换“配置文件”能不能搞定？**

* /etc 下的 modprobe/udev 规则**只能影响模块加载顺序/参数**，**不能替代 DTS** 去“宣告一个挂在 I²C/SPI 的新设备”。
* 因此，“仅替换个别配置文件”通常**不够**。最小代价的正确姿势通常是**替换 DTB**（或加一个 DTS overlay），再配合加载对应驱动模块。

# 通用落地流程（以新增 I²C 设备为例）

> 假设你在原型板上新增了一个 I²C 传感器（地址 0x1A），挂在 I²C1，总线速率 400k，需一根中断 GPIO。

1. **勾选驱动**（一次性）

   * 在内核 `menuconfig` 里找到该传感器驱动，设为 `=m` 或 `=y`。
   * 若是 `=m`，最终在板上 `modprobe <driver>` 即可加载。

2. **配置引脚复用（pinctrl）**

   * 在 `pinctrl` 控制器下定义 I²C1 的 `scl/sda` 复用组，并为传感器中断定义 GPIO 复用/输入模式。
   * 把这些 pinctrl 节点引用到 I²C 控制器和设备节点上。

3. **开启 I²C 控制器节点**

   ```dts
   &i2c1 {
       status = "okay";
       clock-frequency = <400000>;
       pinctrl-names = "default";
       pinctrl-0 = <&i2c1_pins>;
   };
   ```

4. **新增外设子节点**

   ```dts
   &i2c1 {
       sensor@1a: my_sensor@1a {
           compatible = "vendor,model123";
           reg = <0x1a>;
           interrupt-parent = <&gpio2>;
           interrupts = <5 IRQ_TYPE_LEVEL_LOW>;   // 实际依 SoC 改
           vdd-supply = <&vdd_3v3>;
           pinctrl-names = "default";
           pinctrl-0 = <&sensor_int_pin>;
           status = "okay";
       };
   };
   ```

5. **编译 & 部署**

   * 交叉编译 `make dtbs`（或 vendor 提供的 `build.sh dtb`）。
   * 替换板上的 DTB 文件（通常在 boot 分区或 `/boot`/`/soc/` 之类）。
   * 若驱动是模块：`modprobe my_sensor`；否则开机会自动绑定。
   * `dmesg` 查看绑定日志，`/sys/bus/i2c/devices/`、`/sys/firmware/devicetree/base` 验证节点。

6. **用户态验证**

   * 若提供 `i2c-dev`：`CONFIG_I2C_CHARDEV=y`，可用 `i2cdetect/i2cget/i2cset` 做基本访问。
   * 驱动若导出 `sysfs`/`iio`/`input` 节点，按驱动说明验证。

# SPI 设备要点

* SPI 没有地址，靠 **片选线（CS）** 区分，从而在 DTS 中以 `reg = <cs>` 表示；需要声明 `spi-max-frequency`、模式（cpol/cpha），以及中断/供电/复位等。
* 示例：

  ```dts
  &spi0 {
      status = "okay";
      pinctrl-names = "default";
      pinctrl-0 = <&spi0_pins>;

      flash@0 {
          compatible = "jedec,spi-nor";
          reg = <0>;                        // CS0
          spi-max-frequency = <50000000>;
          status = "okay";
      };

      mytouch@1 {
          compatible = "vendor,mytouch";
          reg = <1>;                        // CS1
          interrupt-parent = <&gpio3>;
          interrupts = <12 IRQ_TYPE_EDGE_FALLING>;
          spi-max-frequency = <10000000>;
          vdd-supply = <&vdd_3v3>;
          status = "okay";
      };
  };
  ```
* **原型期**想先跑用户态可用 `spidev`：在从设备节点 `compatible = "spidev"`（或启用内核里对 spidev 的匹配），用户态通过 `/dev/spidevX.Y` 直接访问。但量产需换成**专用驱动**。

# UART 要点

* 大多数 SoC 的 UART 控制器节点在 `.dtsi` 已有，往往是 `status = "disabled"`。
* 使能并绑定到别名（`aliases { serial0 = &uart0; }`），并为 TX/RX/CTS/RTS 配 pinctrl。
* 若只是把 UART 暴露给用户态（不挂特殊外设协议），通常**无需写驱动**，启用后即有 `/dev/ttyS*`（或 `/dev/ttyAMA*`、`/dev/ttyPS*`）。
* 示例：

  ```dts
  &uart2 {
      status = "okay";
      pinctrl-names = "default";
      pinctrl-0 = <&uart2_pins>;
  };
  ```

# 必要时才需要“升级 BSP”

下面场景才更可能需要动 BSP/内核本体：

* **你的外设缺少内核驱动**：要新写/移植一个驱动（Kconfig/Makefile、probe、OF match），这通常需要重编内核或至少构建外部模块。
* **内核旧**导致缺少对应 bindings 或核心子系统特性（如新 I3C、复杂 MIPI 子系统、V4L2 async graph），这时升级到较新 LTS 才更省心。
* **DTB 与内核强绑定**：某些 vendor 固件把 DTB 内嵌并强依赖特定版本，抽离困难时，可能被迫重打包甚至同步升级。

# 工程最佳实践（针对你描述的“裁剪系统 + 后加外设”）

1. **尽量做到“内核/DTB 分离加载”**

   * 调整 U-Boot 脚本，从分区/文件系统单独加载 DTB（`fdt addr`, `fdt overlay apply`）。这样你后续加外设只需替换 **DTB 或 Overlay**，无需重编内核。

2. **把板级差异做成 Overlay**

   * 例如“同一主板 + 不同摄像头/传感器/屏幕”的 SKU，用不同 overlay；启动参数指定使用哪个 overlay，或引导脚本基于硬件 strap/EEPROM 自动选择。

3. **Pinmux 先行**

   * 任何 I²C/SPI/UART 先把管脚复用、上下拉、驱动能力配置对；很多“设备不工作”是 pinmux 或电源没配好。

4. **Regulator/Clock/Reset 依赖补全**

   * 外设供电/复位脚常被忽略，DTS 里给到 `vdd-supply`、`reset-gpios`，并在 board 的 regulator 节点定义输出轨（3V3/1V8）。

5. **驱动形态优先选择**

   * 快速验证：`i2c-dev`/`spidev` + 用户态测试；
   * 走向稳定：启用正式驱动（OF 匹配），完善 DTS bindings；
   * 性能/时序严格：进内核态驱动，减少用户态开销。

6. **验证清单**

   * `dmesg | grep -i of:` / 设备名，确认 OF 匹配成功；
   * `/proc/device-tree` 或 `/sys/firmware/devicetree/base` 查看生效的属性；
   * 总线枚举：`ls /sys/bus/i2c/devices/`、`ls /sys/bus/spi/devices/`；
   * 节点文件：`/dev/i2c-*`、`/dev/spidev*`、`/dev/ttyS*`；
   * 功能验证：读写寄存器、产生中断、测量吞吐。

---

## 结论（针对你的问题）

* **DTS 是“告诉内核你的硬件长什么样”的权威来源**。对 I²C/SPI/UART 这种**非自枚举**外设，**仅替换普通配置文件（如 /etc 下的 modprobe.conf、udev 规则）并不能让设备“被看见”**。
* **不必动整个 BSP**：多数情况下，你只需要：

  1. 确认驱动可用（内建或模块）；
  2. **修改或叠加 DTS/DT Overlay**（包含 pinmux、电源、中断、总线参数）；
  3. 重新部署 **DTB（或 overlay）** 与可能的**驱动模块**。
* 若 DTB 与内核分离：**只替换 DTB/Overlay 就能解决外设加载** —— 这是最“轻量”的方案。
* 若 DTB 被内核打包：需要重打包镜像（但仍不等于“升级 BSP”）。
* 只有当**缺驱动/内核太旧**时，才考虑真正升级 BSP。

---

**BSP** 是 **Board Support Package（板级支持包）** 的缩写。
在嵌入式 Linux 里，它通常指一整套让“特定主板/SoC 能正常启动并运行 Linux”的底层包，典型包含：

* **Bootloader**（如 U-Boot）及其板级配置、启动脚本
* **Linux 内核**（含该 SoC/主板相关的补丁、驱动、Kconfig/defconfig）
* **设备树**（.dts/.dtb 与可能的 overlay）
* **基础外设驱动与板级适配代码**（时钟/复位/电源/PinMux、I²C/SPI/UART 控制器等）
* **配套构建脚本/工具链/打包方式**（有时还含最小 rootfs 与发布说明）
* 厂商常把这些打成一个 **SDK** 或 **Yocto/Buildroot 层**，也会被笼统地称为 BSP

在那句话里，“**升级 BSP**”的意思是：
把整套板级底层环境升级到新的版本（例如换更高版本的内核/补丁、U-Boot、驱动与设备树框架，或迁移到更新的厂商 SDK/Yocto 层），而不仅仅是改一个配置文件。

多数“新增 I²C/SPI/UART 外设”的场景并**不需要整套升级 BSP**：
只要已有驱动可用，通常改（或叠加）**设备树/overlay** + 适当的 **内核配置/模块** 就能完成；只有当缺驱动、核心子系统太老或启动打包方式限制时，才考虑真正“升级 BSP”。
