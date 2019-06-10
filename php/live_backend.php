<?php
$server = new swoole_websocket_server("0.0.0.0", 12450);

$server->on('open', function (swoole_websocket_server $server, $request) {
	echo "Request Room ID:" . $request->server['path_info'] . PHP_EOL;
	if ( $request->server['path_info'] !== '/push' ) {
		if ( $request->server['path_info'] !== '/play' ) {
			$server->push($request->fd, json_encode(['status' => 404, 'message' => 'Live Stream Not Found']));
			$server->close($request->fd);
		} else {
			echo "server: handshake success with fd{$request->fd}\n";
		}
	}
});
$server->on('message', function (swoole_websocket_server $server, $frame) {
	echo "receive from {$frame->fd}" . PHP_EOL;
	$data = $frame->data;
	foreach ( $server->connections as $fd ) {
		$server->push($fd, $data);
	}
	//$json = json_decode($data, true);
	// if ($json['type'] == 'owner' || $json['type'] == 'danmaku') {

	// }
});
$server->on('close', function ($ser, $fd) {
	echo "client {$fd} closed\n";
});
$server->start();
