**[node.js框架选型](http://cnodejs.org/topic/58caaec27dee71e5193a53ce)**


**centos系统安装node.js**

```
# 安装node.js
cd /usr/local/src
wget http://nodejs.org/dist/v8.11.3/node-v8.11.3-linux-x64.tar.xz
tar -xvf node-v8.11.3-linux-x64.tar.xz -C /usr/local

# node环境配置
vim /etc/profile

加入以下几行
export NODE_HOME=/usr/local/node-v8.11.3-linux-x64
export PATH=$PATH:$NODE_HOME/bin
export NODE_PATH=$NODE_HOME/lib/node_modules

# 立即生效使用配置
source /etc/profile

# 检查是否正常
node -v
npm -v
```

## 利用anyproxy做代理抓包分析

`anyproxy --root` # 生成证书

`anyproxy --intercept` # 明文解析https

`anyproxy --clear`  # 清除证书

## pm2相关

`pm2 start anyproxy -x -- -i`  #  pm2环境下运行

`pm2 logs anyproxy [--lines 10]`

`pm2 delete anyproxy` # 关闭服务

`pm2 restart anyproxy`

`pm2 monit`  # 监控内存占用

`pm2 list`  # 监控运行状态

## nodemon, 热更新

`npm i -g nodemon`

```
nodemon.json, 启动服务会自动加载配置文件
{
    "ignore": ["dist"],
    "verbose": true,
    "env": {
        "NODE_ENV": "development"
    }
}
```

`nodemon ./app.js`

`nodemon ./app.js  localhost 3000`

`nodemon --debug ./app.js 3000`

## npm相关

`npm init` #初始化, 创建package.json

`packages.json`

```
{
	"script": {
		"build": "webpack",
		"dev": "webpack-dev-server --inline --hot --quiet"
	},
	dependencies: {
	},
	devDependencies: {
	}
}

那么npm run build就等价于webpack， npm run dev等价于webpack-dev-server --inline

npm install <package> --save-dev 会把包写到devDependencies, 表示测试环境的包

npm install <package> --save 会把包写到dependencies, 表示正式环境的包

线上环境执行npm install --production则只安装dependencies里的包

```

`npm install bower@^1.2.3`  #安装指定版本,`^`表示大于

`npm outdated [-g]` #查看过期的包

`npm uninstall <package> [--save|--save-dev|-g]` #卸载依赖包

`npm config get <key>` 或 `npm get <key>`

`npm config set <key> <value> [-g]` 或 `npm set <ke> <value> [-g]`

`npm config delete <key>`  #删除配置选项

`npm config list` #配置列表

`npm config edit` #编辑配置

`npm search <pkg>`  #搜索包

`npm docs|repo <pkg>`  #打开包的官方文档

`npm explore <pkg> [cmd]` #定位到包目录

`npm rebuilt <pkg>` #重新编译包

`npm link <pkg>`  #链接全局包

`npm ls|ll|la [-g]`  #npm安装的包列表

`npm prune` #在package.json路径下运行, 清除没有列举node_modules的包

`npm root -g` #查看全局安装路径

`npm run [cmd]` #用npm run来跑package.json里的script字段内的命令

`npm shrinkwrap` #指定安装的包版本

`npm update [-g] <pkg>` #升级包

`npm view <pkg> [versions]` #查看包信息

`npm config get userconfig`  #当前配置

`npm config get globalconfig`  #全局配置


`npm update` #升级npm

`npm install -g n` #全局安装n模块

`n stable`  #升级node.js到当前稳定版

`n latest`  #升级nodejs到最新版

`n 7.0.0`    #安装指定版本

`n - 7.0.0` 或 `n rm 7.0.0`  #删除指定版本

`n use 7.0.0 abc.js` #使用指定版本执行脚本


# AMD  Asynchronous Module Definition 异步模块定义

> 实现了AMD规范的JS库有require.js和curl.js

> define(id, deps, factory);


# CMD  Common Module Definition 通用模块定义

> SeaJS实现了CMD规范

> define(function(require, exports, module){});


# babel是下一代javascript语法编译器

`babel demo.js`  #将es6语法转为es5

`babel demo.js --out-file compiled.js` #转换并输出文件

`babel demo.js -o compiled.js`

`babel src --out-dir lib`  #将src目录下全部js转码并输出到lib目录

`babel src -d lib`

`babel src -d lib -s` #生成source map 文件



# node.js模块系统
```
hello.js
//导出的实例化对象, 可直接访问
(module.)exports.world = function() {
	console.log('hello world');
}

module.exports = (input) => {
    return parseInt(input.a, 10) + parseInt(input.b, 10);
}

//main.js
var hello = require('./hello');  //hello是实例化对象
hello.world();



//hello.js  导出的一个特定类型，需要实例化
module.exports = function(name, age) {
	this.name = name;
	this.age = age;
	this.about = function(){
		console.log(this.name + ' is ' + this.age + 'years old');
	}
}
或者
function Hello() {}
module.exports = Hello; //Hello是函数对象


//main.js
var Hello = require('./hello');  //Hello是特定类
var a = new Hello('tony', 26);
a.about();
```
