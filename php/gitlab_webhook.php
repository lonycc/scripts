<?php

/**
 * gitlab的webhook,事件监控触发脚本
 */
$valid_token = 'd49dfa7622681425hjkmdd032eb2ca59498ce852';
$valid_ip = ['172.1.0.0','192.168.1.10','127.0.0.1'];

// webhooks token
$client_token = @$_SERVER['HTTP_X_GITLAB_TOKEN'];
// 事件
$client_event = @$_SERVER['HTTP_X_GITLAB_EVENT'];
$client_ip = @$_SERVER['REMOTE_ADDR'];
$fs = @fopen('./webhook.log', 'a');
@fwrite($fs, 'Request on ['.date("Y-m-d H:i:s").'] from ['.$client_ip.']'.PHP_EOL);

if ( $client_token !== $valid_token )
{
    echo "error 10001";
    @fwrite($fs, "Invalid token [{$client_token}]".PHP_EOL);
    exit(0);
}

if ( ! in_array($client_ip, $valid_ip) )
{
    echo "error 10002";
    @fwrite($fs, "Invalid ip [{$client_ip}]".PHP_EOL);
    exit(0);
}

$json = @file_get_contents('php://input');
$data = json_decode($json, true);
@fwrite($fs, 'Data: '.print_r($data, true).PHP_EOL);
@fwrite($fs, '======================================================================='.PHP_EOL);
fclose($fs);

@exec("/bin/bash /path/to/update.sh");
