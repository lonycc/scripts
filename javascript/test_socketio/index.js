const express = require('express');
const app = express();
const server = require('http').Server(app)
const io = require('socket.io')(server);

app.use(express.static(__dirname));

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

let onlineNum = 0;

io.on('connection', function (socket) {
    onlineNum++;
    socket.broadcast.emit('open', {num: onlineNum});
    socket.on('disconnect', function () {
        onlineNum--;
        socket.broadcast.emit('close', {num: onlineNum});
        io.emit('user disconnect');
    });
    socket.on('get_num', function (data) {  // 监听客户端的get_num事件
        socket.emit('set_num', {num: onlineNum});   // 向客户端推送set_num事件
    });

  socket.emit('news', { hello: 'world' });  // 向客户端推送news事件
  socket.on('my other event', function (data) {
    console.log(data);
  });

});

server.listen(1234, function () {
    console.log('连接成功');
});
