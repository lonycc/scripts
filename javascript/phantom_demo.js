/**
 * API手册  http://phantomjs.org/api/
 * 淘宝源    http://npm.taobao.org/dist/phantomjs/
 *
 * 属性
 * phantom.args {String[]}; //获取传递给js脚本的参数,建议用systom.args
 * phantom.version {Object}; //获取phantom的版本信息,类似{'major':2,'minor':0,'patch':0};
 * phantom.scriptName {String}; //获取指定脚本名,建议用system.args[0]
 * phantom.libraryPath {String}; //保存injectJs中脚本路径
 * phantom.cookies {Object[]}; //获取或设置cookies,保存在Cookiejar中
 * phantom.cookiesEnabled {Boolean}; //设置是否允许Cookiejar
 * 
 * 方法
 * addCookie(Object) {Boolean}; //添加cookie到Cookiejar,成功返回true,否则false
 * clearCookies() {void}; //删除Cookiejar中所有cookies
 * deleteCookie(cookieName) {Boolean}; //删除指定名字cookie
 * phantom.exit(returnValue) {void}; //退出程序
 * phantom.injectJs(filename) {Boolean}; //从文件中注入外部脚本代码
 */

var page = require('webpage').create(),
    system = require('system'),
    webdomain, address;
phantom.outputEncoding = 'utf-8';

page.settings = {
    "javascriptEnabled": "true",
    "XSSAuditingEnabled": "true",
    "userAgent": "Mozilla/5.0 (Windows NT 6.1)"
};

function sleep(numberMillis) {
    var now = new Date();
    var exitTime = now.getTime() + numberMillis;
    while (true) {
        now = new Date();
        if (now.getTime() > exitTime)
            return;
    }
}

//websites.forEach(function(arg,i){});

if (system.args.length === 1) {
    console.log('Usage: ' + system.args[0] + ' <some website>');
    phantom.exit(1);
}

webdomain = system.args[1];
address = 'http://www.alexa.cn/' + webdomain;
page.open(address, function(status) {
    if (status !== 'success') {
        phantom.exit(1);
    } else {
        var sc = page.evaluate(function(s) {
            var elements = document.querySelectorAll('tr#ALEXA>td>span.c036');
            var worldrank = "0";
            if (elements.length > 0) {
                worldrank = elements[0].textContent;
            }
            return worldrank;
        }, webdomain);
        console.log(sc);
        phantom.exit();
    }
});
