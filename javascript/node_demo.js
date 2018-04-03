var port = 9091;

var projects = {
    mall: {
    },
    lib: {
    }
};

var db = {
    host: 'localhost',
    user: 'root',
    password: '123456',
    database: 'test'
};

module.exports = {
    projects: projects,
    port: port,
    db: db
};


/* 文件拷贝
const fs = require('fs');

function copy(src, dst) {
    fs.createReadStream(src).pipe(fs.createWriteStream(dst));
}

function main(argv) {
    copy(argv[0], argv[1]);
}
console.log(process.argv.slice(2));
*/


/* 拷贝大文件的原理
var rs = fs.createReadStream('/usr/local/bin/phantomjs');
var ws = fs.createWriteStream('phantomjs');

rs.on('data', function (chunk) {
    if (ws.write(chunk) === false) {
        rs.pause();
    }
});

rs.on('end', function () {
    ws.end();
});

ws.on('drain', function () {
    rs.resume();
});
*/

/* 异步方式读取
fs.readFile('/usr/local/bin/php', function (err, data) {
    if (err) {
        // Deal with error.
        throw err;
    } else {
        // Deal with data.
    }
});
*/

/* 同步方式读取
try {
    var data = fs.readFileSync('/usr/local/bin/php');
    // Deal with data.
} catch (err) {
    // Deal with error.
}
*/


/* 同步遍历目录
const path = require('path');
function travel(dir, callback) {
    fs.readdirSync(dir).forEach(function (file) {
        var pathname = path.join(dir, file);

        if (fs.statSync(pathname).isDirectory()) {
            travel(pathname, callback);
        } else {
            callback(pathname);
        }
    });
}

travel('/Users/work/Desktop/js/dhtCrawler', function(pathname) {
    console.log(pathname);
});
*/

/* 异步遍历目录
function travel(dir, callback, finish) {
    fs.readdir(dir, function (err, files) {
        (function next(i) {
            if (i < files.length) {
                var pathname = path.join(dir, files[i]);

                fs.stat(pathname, function (err, stats) {
                    if (stats.isDirectory()) {
                        travel(pathname, callback, function () {
                            next(i + 1);
                        });
                    } else {
                        callback(pathname, function () {
                            next(i + 1);
                        });
                    }
                });
            } else {
                finish && finish();
            }
        }(0));
    });
}
*/

/* 文件去bom头
function readText(pathname) {
    var bin = fs.readFileSync(pathname);
    if (bin[0] === 0xEF && bin[1] === 0xBB && bin[2] === 0xBF) {
        bin = bin.slice(3);
    }
    return bin.toString('utf-8');
}
*/

/* gbk转utf-8
var iconv = require('iconv-lite');
function readGBKText(pathname) {
    var bin = fs.readFileSync(pathname);
    return iconv.decode(bin, 'gbk');
}
*/

/* 单字节编码
function replace(pathname) {
    var str = fs.readFileSync(pathname, 'binary');
    str = str.replace('foo', 'bar');
    fs.writeFileSync(pathname, str, 'binary');
}
*/

/* http服务端模式
var http = require('http');
http.createServer(function(request, response) {
    //response.writeHead(200, {'Content-Type': 'text/plain'});
    //response.end('hello\n');
    var body = [];
    console.log(request.method);
    console.log(request.headers);
    request.on('data', function (chunk) {
        body.push(chunk);
        response.write(chunk);
    });

    request.on('end', function () {
        body = Buffer.concat(body);
        console.log(body.toString());
        response.end();
    });
}).listen(8080);
*/

/* http客户端模式
const http = require('http');
var options = {
  hostname: 'www.example.com',
  port: 80,
  path: '/upload',
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
};

var request = http.request(options, function (response) {});

request.write('Hello World');
request.end();

http.get('http://www.example.com/', function (response) {
    var body = [];
    console.log(response.statusCode);
    console.log(response.headers);

    response.on('data', function (chunk) {
        body.push(chunk);
    });

    response.on('end', function () {
        body = Buffer.concat(body);
        console.log(body.toString());
    });
});
*/

/* https
const https = require('https');
const fs = require('fs');
var options = {
    key: fs.readFileSync('./ssl/default.key'),
    cert: fs.readFileSync('./ssl/default.cer')
};

https.createServer(options, (req, res) => {
  res.writeHead(200);
  res.end('hello world\n');
}).listen(8000);
*/

/* 全局对象process, 提供当前node.js进程的信息查询和操作控制;
// exit事件
process.on('exit', (code) => {
  console.log(`About to exit with code: ${code}`);
});

process.abort(); //退出当前进程
process.arch; //处理器架构
process.argv;  //参数数组, 第一项是process.execPath; 第二项为被执行的脚本文件
process.argv0;  //如果process.execPath为/usr/local/bin/node, 则process.argv0为node;
process.channel; //对象, 仅当进程是由ipc通道产生时才存在
process.chdir('/tmp'); //切换目录
process.config;  //对象, 进程配置
process.connected;  //布尔值, 仅当进程是由ipc通道产生时才存在
process.cpuUsage({ user: 123176, system: 25168 })  //cpu使用情况, 参数可选
process.cwd(); //当前目录
process.debugPort; //调试端口, 可读可写;
process.disconnect(); //关闭ipc通道

*/
