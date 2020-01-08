<?php

/**
 * 时间表述转化
 */
function transfer_time($time)
{
    $rtime = date("Y-m-d H:i",$time); //过去日期
    $htime = date("H:i",$time); //过去时间
    $time = time() - $time; //间隔秒数
    if ($time < 60)
    {
        $str = '刚刚';
    } elseif ($time < 60 * 60) {
        $min = floor($time/60);
        $str = $min.'分钟前';
    } elseif ($time < 60 * 60 * 24) {
        $h = floor($time/(60*60));
        $str = $h.'小时前 ';
    } elseif ($time < 60 * 60 * 24 * 30) {
        $d = floor($time/(60*60*24));
        if ($d == 1)
            $str = '昨天 ';
        elseif ($id==2)
            $str = '前天 ';
        else
           $str = $d.'天前';
    } elseif ($time < 60 * 60 * 24 * 365) {
        $m = floor($time/(60*60*24*30));
        $str = $m."个月前";
    } else {
        $str = floor($time/(60*60*24*365))."年前";
    }
    return $str;
}

/**
 * 各种hash算法的测试
 */
function testAlgos()
{
  $data = "hello";
  $file = "demo.php";
  foreach (hash_algos() as $v) {
    $r = hash($v, $data, false);
    $r1 = @hash_file($v, $file, false);
    $r2 = @hash_hmac($v, $data, 'key', false);
    $r3 = @hash_hmac_file($v, $file, 'key', false);
    printf("%-12s %3d %s<br/>", $v, strlen($r), $r3);
   }
}

/**
 * session 和 cookie 操作
 */
function operate_session_cookie()
{
  //setcookie("cookie[three]", "i am three");
  //setcookie("cookie[two]", "i am two");
  //setcookie("cookie[one]", "i am one");

  if ( isset($_COOKIE['cookie']) )
  {
    foreach ( $_COOKIE['cookie'] as $name => $value )
    {
      echo "{$name} : {$value} <br />\n";
    }
  }

  //setcookie("cookie[three]", "", time()-100);
  //echo $_COOKIE["cookie[one]"];
  $expires = date("1,d-m-y h:i:s",time()+100);
  //header("set-cookie: tracker=1;expires=$expires;");

  //PHPSESSIONID = hash_func(客户端IP + 当前时间（秒）+ 当前时间（微妙）+ PHP自带的随机数生产器)
  if (! session_id() )
  {
    session_start();
    $_SESSION['user'] = 'tony';
  }
  unset($_SESSION['user']);
  session_destroy();
  //setcookie(session_name(), '', time()-100, '/');
  session_unset();
}

/**
 * 生成若干个不重复的随机整数
 * @param $min 最小值
 * @param $max 最大值
 * @param $num 个数
 */
function unique_rand($min, $max, $num)
{
    $count = 0;
    $return = array();
    while ($count < $num) {
        $return[] = mt_rand($min, $max);  //随机整数
        $return = array_flip(array_flip($return));  //数组键、值转换,去掉重复
        $count = count($return);
    }
    shuffle($return); //数组key重新生成
    return $return;
}


/**
 * 字符串截取, 兼容各种编码字符
 */
function msubstr($str, $start=0, $length, $charset='utf-8', $suffix=true)
{
    if ( function_exists('mb_substr') )
        return mb_substr($str, $start, $length, $charset);
    elseif(function_exists('iconv_substr'))
        return iconv_substr($str, $start, $length, $charset);

    $re['utf-8']   = "/[\x01-\x7f]|[\xc2-\xdf][\x80-\xbf]|[\xe0-\xef][\x80-\xbf]{2}|[\xf0-\xff][\x80-\xbf]{3}/";
    $re['gb2312'] = "/[\x01-\x7f]|[\xb0-\xf7][\xa0-\xfe]/";
    $re['gbk']    = "/[\x01-\x7f]|[\x81-\xfe][\x40-\xfe]/";
    $re['big5']   = "/[\x01-\x7f]|[\x81-\xfe]([\x40-\x7e]|\xa1-\xfe])/";
    preg_match_all($re[$charset], $str, $match);
    $slice = join('', array_slice($match[0], $start, $length));
    if ( $suffix )
        return $slice.'…';
    return $slice;
}

/**
 * 字符串编码转换为utf-8
 */
function utf8($str, $encoding='gb2312')
{
    if ( function_exists('iconv') )
      return @iconv($encoding, 'UTF-8', $str);
    elseif ( MB_ENABLED === TRUE )
      return @mb_convert_encoding($str, 'UTF-8', $encoding);
    return FALSE;
}

/**
 * 逐行读取文件
 */
function get_count($fp)
{
	while ( ! feof($fp) )
	{
		$line = fgets($fp);
	}
	fclose($fp);
}

/**
 * 递归遍历目录
 */
function list_dir($start)
{
	$contents = scandir($start);
	foreach ( $contents as $item )
	{
		if ( is_dir("$start/$item") && (substr($item,0,1)!='.') )
		{
			list_dir("$start/$item");
		} else {
			if ( preg_match("/t2016\d{4}_\d{3,8}.htm$/i", $item) )
			{
				echo $start."/".$item;
			}
		}
	}
}

/**
 * 获取毫秒级的时间戳
 */
function getMillisecond()
{
	list($t1, $t2) = explode(' ', microtime());
	return $t2 . ceil(($t1 * 1000));
}

/**
 * 获取客户端ip地址
 */
function get_client_ip()
{
	foreach ( array('HTTP_CLIENT_IP','HTTP_X_FORWARDED_FOR','HTTP_X_FORWARDED','HTTP_X_CLUSTER_CLIENT_IP','HTTP_FORWARDED_FOR','HTTP_FORWARDED','REMOTE_ADDR') as $key )
	{
		if ( array_key_exists($key, $_SERVER) )
		{
			foreach ( explode(',', $_SERVER[$key]) as $ip )
			{
				$ip = trim($ip);
				//会过滤掉保留地址和私有地址段的IP，例如 127.0.0.1会被过滤
				//也可以修改成正则验证IP
				if ( (bool) filter_var($ip, FILTER_VALIDATE_IP,	FILTER_FLAG_IPV4 | FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE) )
				{
					return $ip;
				}
			}
		}
	}
	return null;
}

/**
 * 获取最近$interval天将过生日的人
 */
function getRecentDate($interval)
{
	$back_day = date('md', strtotime('-' + $interval + ' day'));
	$forward_day = date('md', strtotime('+ ' + $interval + ' day'));
	if ( $back_day < $forward_day )
	{
		return "select * from table_name where date_format(ptime,'%m%d') between $back_day and $forward_day";
	} else {
		return "select * from table_name where date_format(ptime,'%m%d') >= $back_day or date_format(ptime,'%m%d') <= $forward_day";
	}
}

/**
 * 判断执行环境是否cli
 */
function is_cli()
{
    return preg_match("/cli/i", php_sapi_name()) ? true : false;
    // return preg_match("/cli/i", PHP_SAPI) ? true : false;
}


/** basic realm
 * $_SERVER['PHP_AUTH_USER'];
 * $_SERVER['PHP_AUTH_PW'];
 * header('WWW-Authenticate: Basic realm="My Realm"');
 * header('HTTP/1.0 401 Unauthorized');
 */

/**
 * ip2long('127.0.0.1');  //将字符串ip转为长整数
 * long2ip('607649792');  //将长整数转为字符ip
 *
 * array('607649792', '608174079'), //36.56.0.0-36.63.255.255
 * array('1038614528', '1039007743'), //61.232.0.0-61.237.255.255
 * array('1783627776', '1784676351'), //106.80.0.0-106.95.255.255
 * array('2035023872', '2035154943'), //121.76.0.0-121.77.255.255
 * array('2078801920', '2079064063'), //123.232.0.0-123.235.255.255
 * array('-1950089216', '-1948778497'), //139.196.0.0-139.215.255.255
 * array('-1425539072', '-1425014785'), //171.8.0.0-171.15.255.25
 * array('-1236271104', '-1235419137'), //182.80.0.0-182.92.255.255
 * array('-770113536', '-768606209'), //210.25.0.0-210.47.255.255
 * array('-569376768', '-564133889'), //222.16.0.0-222.95.255.255
 */

base64_encode('this is my pm');
base64_decode('dGhpcyBpcyBteSBwbQ==');

`system(string $command [, int &$return_var ]) : string`   返回输出的最后一行, 前面的行打印在屏幕
`passthru(string $command [, int &$return_var ]) : void`  不返回, 输出内容打印在屏幕
`shell_exec(string $command) : string`  输出全部返回
`exec(string $command [, array $rs]) : string` 返回输出最后一行

// base64编码图片
$img_file = 'https://img.alicdn.com/bao/uploaded/TB1eaiELpXXXXcPXpXXSutbFXXX.jpg';
$img_info = getimagesize($img_file);
$img_src = "data:{$img_info['mime']};base64," . base64_encode(file_get_contents($img_file));
exit("<img src='{$img_src}' />");


// 解析网络xml资源
$xml = new DOMDocument();
$xml->load("http://www.domain.com/aaa.xml");
foreach($xml->getElementsByTagName('pic_item') as $pic)
{
    $pic->getElementsByTagName('url')->item(0)->nodeValue;
    $pic->getElementsByTagName('title')->item(0)->nodeValue;
}

$x = $xml->documentElement;
foreach ($x->childNodes as $item)
{
    echo $item->nodeName . " = " . $item->nodeValue . "<br />";
}

// 日期相关
date_default_timezone_set('PRC');
echo date('Y-m-d', strtotime('now')), '<br/>';
echo date('Y-m-d', strtotime('-1 week Monday')), '<br/>';
echo date('Y-m-d', strtotime('-1 week Sunday')), '<br/>';
echo date('Y-m-d', strtotime('+0 week Monday')), '<br/>';
echo date('Y-m-d', strtotime('+0 week Sunday')), '<br/>';


//date('n') 第几个月
//date('w') 本周周几
//date('t') 本月天数

echo '<br>上周:<br>';
echo date('Y-m-d H:i:s', mktime(0, 0 , 0, date('m'),date('d')-date('w')+1-7,date('Y'))),'<br/>';
echo date('Y-m-d H:i:s', mktime(23,59,59, date('m'),date('d')-date('w')+7-7,date('Y'))),'<br/>';
echo '<br>本周:<br>';
echo date('Y-m-d H:i:s', mktime(0, 0 , 0, date('m'),date('d')-date('w')+1,date('Y'))),'<br/>';
echo date('Y-m-d H:i:s', mktime(23, 59, 59, date('m'),date('d')-date('w')+7,date('Y'))),'<br/>';

echo '<br>上月:<br>';
echo date('Y-m-d H:i:s',mktime(0, 0 , 0, date('m')-1,1,date('Y'))),'<br/>';
echo date('Y-m-d H:i:s',mktime(23,59,59, date('m') ,0,date('Y'))),'<br/>';
echo '<br>本月:<br>';
echo date('Y-m-d H:i:s', mktime(0, 0 , 0, date('m'),1,date('Y'))),'<br/>';
echo date('Y-m-d H:i:s', mktime(23, 59, 59, date('m'),date('t'),date('Y'))),'<br/>';

$getMonthDays = date('t', mktime(0, 0 , 0, date('n')+(date('n')-1)%3,1,date('Y')));//本季度未最后一月天数
echo '<br>本季度:<br>';
echo date('Y-m-d H:i:s', mktime(0, 0, 0, date('n')-(date('n')-1)%3,1,date('Y'))),'<br/>';
echo date('Y-m-d H:i:s', mktime(23,59,59, date('n')+(date('n')-1)%3,$getMonthDays,date('Y'))),'<br/>';


if ($ext == 'docx') {
    //docx文件可以直接读取
    $contents = $this->extracttext($file);
} elseif($ext == 'doc') {
    //doc文件，需要安装antiword软件来读取
    $contents = shell_exec( "antiword -m UTF-8 $file" );
} else {
    $contents = file_get_contents($file);
}

// 字数统计, 兼容多字节字符
function _utf8_strlen($value = null)
{
	preg_match_all('/./us', $value, $match);
	return count($match[0]);
}

// 解析docx文档
function extracttext($filename)
{
	$ext = end(explode('.', $filename));
	if ( $ext == 'docx' )
		$dataFile = "word/document.xml";
	else
		$dataFile = "content.xml";
	$zip = new ZipArchive;
	if ( true === $zip->open($filename) )
	{
		if ( ($index = $zip->locateName($dataFile)) !== false )
		{
			$text = $zip->getFromIndex($index);
			$xml = DOMDocument::loadXML($text, LIBXML_NOENT | LIBXML_XINCLUDE | LIBXML_NOERROR | LIBXML_NOWARNING);
			return strip_tags($xml->saveXML());
		}
		$zip->close();
	}
	return false;
}

// 标准输入输出
$stdin = fopen('php://stdin', 'r');
$stdout = fopen('php://stdout', 'w');

echo "enter a number:";
$num = trim(fgets(STDIN));
echo "enter another number:";
$num1 = trim(fgets(STDIN));
echo "sum of two numbers above is:", $num + $num1;

fgets($stdin);
fread($stdin, 100);
fclose($stdin);

fwrite($stdout, 'php://stdout/n');
fclose($stdout);
fwrite(STDOUT, 'STDOUT/n');

// fsockopen()模拟socket通信
function check_url($url) {
	$url_slice = parse_url($url);
	$path = isset($url_slice['path']) ? $url_slice['path'] : '/';
	$port = isset($url_slice['port']) ? $url_slice['port'] : '80';
	$host = $url_slice['host'];
	if ( $fp = fsockopen($host, $port, $errno, $errstr, $timeout) ) {
		$msg = "HEAD {$path} HTTP/1.1\r\nHOST: {$host}\r\nCONNECTION: CLOSE\r\n\r\n";
		fwrite($fp, $msg);
		$data = fgets($fp, 128);
		flose($fp);
		return $data;
	}
	return $errstr;
}
