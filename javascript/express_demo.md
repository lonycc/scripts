**[express 框架入门](http://www.expressjs.com.cn/guide/routing.html)**

- 安装

`npm i --save express`  #部署依赖

`npm i --save-dev express` #开发依赖

- hello world

```node.js
var express = require('express');
var app = express();

app.get('/', function (req, res) {
  res.send('Hello World!');
});

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});
```

- express生成器

`npm i -g express-generator` #全局安装

`express [option] [app_dir]`  #生成应用

`cd [app_dir]`

`npm install`

- 静态资源

`app.use(express.static('public'));` #public目录下的静态文件将可被访问

`app.use('/static', express.static('public'));` #public目录下的文件将有个虚拟路径/static/
