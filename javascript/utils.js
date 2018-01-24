/*
encodeURI() / decodeURI()
该方法不会对 ASCII 字母和数字进行编码，也不会对这些 ASCII 标点符号进行编码： - _ . ! ~ * ' ( ) 。
该方法的目的是对 URI 进行完整的编码，因此对以下在 URI 中具有特殊含义的 ASCII 标点符号，encodeURI() 函数是不会进行转义的：;/?:@&=+$,#

encodeURIComponent() / decodeURIComponent()
该方法不会对 ASCII 字母和数字进行编码，也不会对这些 ASCII 标点符号进行编码： - _ . ! ~ * ' ( ) 。
其他字符（比如 ：;/?:@&=+$,# 这些用于分隔 URI 组件的标点符号），都是由一个或多个十六进制的转义序列替换的。


escape() / unescape()
该方法不会对 ASCII 字母和数字进行编码，也不会对下面这些 ASCII 标点符号进行编码： * @ - _ + . / 。其他所有的字符都会被转义序列替换。

*/

//封装Base64对象
!function(W){
  W.Base64 = {
     utf8ToBase64:function (str){
       return btoa(unescape(encodeURIComponent(str)));
     },
     base64ToUtf8: function(str){
        return decodeURIComponent(escape(atob(str)));
      }
  }
}(window);
//Base64.utf8ToBase64('中国');
//Base64.base64ToUtf8('3e7dm3');



//模板编译实例
function compile(template){
  var evalExpr = /<%=(.+?)%>/g;
  var expr = /<%([\s\S]+?)%>/g;

  template = template
    .replace(evalExpr, '`); \n  echo( $1 ); \n  echo(`')
    .replace(expr, '`); \n $1 \n  echo(`');

  template = 'echo(`' + template + '`);';

  var script =
  `(function parse(data){
    var output = "";

    function echo(html){
      output += html;
    }

    ${ template }

    return output;
  })`;

  return script;
}

var template = `
<ul>
  <% for(var i=0; i < data.supplies.length; i++) { %>
    <li><%= data.supplies[i] %></li>
  <% } %>
</ul>
`;


var parse = eval(compile(template));
div.innerHTML = parse({ supplies: [ "broom", "mop", "cleaner" ] });


/*
1、字符的Unicode表示法
\u0000~\uFFFF
超出的用双字节
"\uD842\uDFB7"
"\u20BB7"
大括号表示法
"\u{20BB7}" === "\uD842\uDFB7"
'\z' === 'z'
'\172' === 'z'  #8进制表示
'\x7A' === 'z'
'\u007A' === 'z'
'\u{7A}' === 'z'

'\0o17'  8进制表示
'\0b101'  2进制表示
'\0xa'  16进制表示

javascript内部，字符以UTF-16格式存储，每个字符固定为2个字节。对于需要4个字节存储的字符，js认为它们是两个字符。
*/

s.charCodeAt(k); //返回字符串s第k个字符的十进制码点
s.codePointAt(k); //可返回32位UTF-16字符的码点
s.toString(16);  //转16进制

// 字符串遍历接口
var s = '𠮷a';
for (let ch of s) {
  console.log(ch.codePointAt(0).toString(16));
}

// 判断是否双字节字符
function is32Bit(c) {
	return c.codePointAt(0) > 0xFFFF;
}

String.fromCharCode(0x4A5B); //从码点返回对应字符，不能识别32位UTF-16码点
String.fromCodePoint(0x20BB7);
String.fromCodePoint(0x78, 0x1f680, 0x79);

// normailize()，用于将字符的不同表示方法统一
'\u01D1'.normalize() === '\u004F\u030C'.normalize();

s.startsWith('tt'); //字符串s是否以tt开头
s.endsWith('tt');
s.includes('tt');
s.repeat(3);  //字符串s重复3次
'x'.padStart(5, 'ab');  // 'ababx', 头部补全
'x'.padStart(4, 'ab');  // 'abax'
'x'.padEnd(5, 'ab');    // 'xabab'
'x'.padEnd(4, 'ab');    //'xaba'

// 模板字符串
// 用``括字符串
// 若要嵌入变量，则需要将变量名写入${}中
// 标签模板
alert`123`;  //模板字符串紧跟在函数名后

{
	let a = 10; //该代码块内有效
	var b = 1;
	let a;  // 在代码块内let会绑定变量
}
var a = [];
for (let i = 0; i < 10; i++) {
	a[i] = function () {
		console.log(i);
	};
}
a[6](); // 6

function bar(x = y, y = 2) {
  return [x, y];
}
bar(); // 报错

function bar(x = 2, y = x) {
  return [x, y];
}
bar(); // [2, 2]

//let不允许在相同作用域重复声明一个变量
//块级作用域 {let a = 10;}

const PI = 3.1415; //const声明一个只读变量
const demo = {};
demo.a = 'fuck';
demo.b = 12;

//变量的解构赋值
let [u,t,f] = [1,2,3];
let [head,...tail]=[1,3,5,7];
var [foo=true] = [];


// 箭头函数, 都是匿名的; 拥有词法作用域的this
() => 3.14;
(x) => x * x;
(x, y) => x * y;
x => ({foo: bar});
(x, y, ...rest) => { statements };
var fn = (x, y) => {
	if(x>0) {
		return x * y;
	} else {
		return -x * y;
	}
};
// 用call()或apply()调用箭头函数时, 无法对this进行绑定, 即传入的第一个参数被忽略.


/*
 * call和apply是为了动态改变this而出现的
 * 当一个object A 没有某个方法 m，但是object B有，可以借助call或apply用其它对象的方法来操作
 * objB.m.call(objA, arg1[,...]); 或者 objB.m.apply(objA, arguments);
 *
 * 用法举例
 * var domNodes = Array.prototype.slice.call(document.getElementsByTagName('*'));
 *
 * bind()会绑将第一个参数作为this, 返回的是函数, 不会立即执行.
 */

function bindThis(f, oTarget) {
    if (f.bind) {
        return f.bind(oTarget);
    } else {
        return function() {
            return f.apply(oTarget, arguments);
        };
    }
}

function bindThis(f, oTarget) {
    var result = function(x, y) {
        return f.call(oTarget, x, y);
    };
    return result;
}

// 查找两个节点最近的父节点
function commonParentNode(oNode1, oNode2) {
    for (;oNode1;oNode1=oNode1.parentNode) {
        if (oNode1.contains(oNode2)) {
            return oNode1;
        }
    }
}

// 数组去重
Array.prototype.uniq = function () {
	var a = new Set();
	this.forEach((arr,i)=>{
		a.add(arr);
	});
	return Array.from(a);
};

var theme_list = document.evaluate('//div[@class="box"]/div[contains(@class, "item")]', document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
theme_list.snapshotLength;
allpres.snapshotItem(index);


[].forEach.call(array_like_obj, function(item){
    console.log(item);
});

var domNodes = Array.prototype.slice.call(document.getElementsByTagName('*'));  // 浅拷贝, 类数组对象domNodes将获得数组的所有属性和方法


// data:text/html,<body contenteditable> 浏览器编辑器
// 物理像素 :  硬件可达到的最大像素。
// 设备独立像素 device independent pixels : 与屏幕密度有关。
// window.devicePixelRatio = 物理像素/设备独立像素   对于一般设备, 为1; 对于视网膜显示屏, 为2。
// <table><td>属性colspan和rowspan可把多行或多列合并

var o = {flag:true};
var test = o.flag || false; //等效于var test = !!o.flag;
user.replace(/(^\s*)|(\s*$)/g,"");  //替换掉空格和换行

// 防止网站被恶意反向代理
if(document.domain != 'yourdomain.com' && document.domain != 'www.yourdomain.com'){window.location.href = 'http://www.yourdomain.com/';}

//防止被frame嵌套
if(top.location != self.location) top.location = self.location;


// 数组扩展方法
Array.prototype.indexOf = function(val) {
	for (var i = 0; i < this.length; i++) {
		if (this[i] == val) return i;
	}
	return -1;
};

Array.prototype.remove = function(val) {
	var index = this.indexOf(val);
	if (index > -1) {
		this.splice(index, 1);
	}
};

var emp = ['abs','dsf','sdf','fd']
emp.remove('sdf');

// array-like对象,拥有push/slice等方法,拥有length属性
var foo = {0:'hello', 1:'world', length:2, slice:Array.prototype.slice};
console.log(Array.prototype.slice.call(foo,0));  //若foo无slice方法
console.log(foo.slice()) //若foo有slice方法
Array.prototype.slice.call(arguments); //常用arguments对象document.links/document.forms

// 指定日期的加减法
var f = function (date, diff) {
   var day;
   if (typeof date == 'string') {
       // yyyy-mm-dd 不是合法的格式
       date = date.replace(/-/g, '/');
       date = new Date(date);
       day = date.getDate();
       diff = ~~diff || 0;
       date.setMonth(date.getMonth() + diff); // 天数超出目标月的最大天数时，会顺延到下个月
    }

    // 然后设置下个月的第零天，重置到目标月的最后一天
    if (date.getDate() != day) {
       date.setDate(0);
       return date;
       f('2014/11/30', 3); //获取三个月之后日期
    }
}

// 最小化窗口提示
window.onbeforeunload = onbeforeunload_handler;
window.onunload = onunload_handler;
function onbeforeunload_handler() {
    var warning = "确认退出?";
    return warning;
}

function onunload_handler() {
    var warning = "呵呵";
    alert(warning);
}

$(window).resize(function(){
	var w = $(this).width();
	var h = $(this).height();
	console.log(w+'X'+h);
});

$(window).blur(function(){
	alert('guck');
});

/** window.screenTop:   窗口相对于屏幕的Y坐标
 *  window.screenLeft:  窗口相对于屏幕的X坐标
 *  window.outerWidth:  窗口的外部宽度
 *  window.outerHeight: 窗口的外部高度
 */
function isMinStatus() {
	var isMin = false;
	if (window.outerWidth != undefined) {
		isMin = window.outerWidth <= 160 && window.outerHeight <= 27;
	} else {
		isMin = window.screenTop < -30000 && window.screenLeft < -30000;
	}
	return isMin;
}

//function定义的对象有一个prototype属性，prototype属性又指向了一个prototype对象，注意prototype属性与prototype对象是两个不同的东西，要注意区别。在prototype对象中又有一个constructor属性，这个constructor属性同样指向一个constructor对象，而这个constructor对象恰恰就是这个function函数本身。 用伪代码表示如下：

var function{
	prototype:prototype{
		constructor:constructor == function
	}
}

function uw3c(){}
uw3c.prototype.name = "ha";
var test = new uw3c();
console.log(test.name);
//uw3c中prototype属性中的name对象, 在uw3c被new构造函数之后, 被继承到了对象test的属性中.

String.prototype.trim = function(){
	return this.replace(/(^\s*)|(\s*$)/g, "");
}
var s = " fsb ";
s = s.trim();
// 或
String.prototype.trim.call(s);

// call和apply
function cat(){}
cat.prototype = {
	food: 'fish',
	say: function(){alert("I love "+this.food);}
}
var blackCat = new cat;
blackCat.say();
whiteDog = {food: 'bone'};
blackCat.say.call(whiteDog); //动态改变this而出现, 当一个object没有某个方法, 可通过call或apply用其他对象的方法来操作

function changeStyle(attr, value){
	this.style[attr] = value;
}
var box = document.getElementById('box');
window.changeStyle.call(box, "height", "200px");
// 或者
window.changeStyle.apply(box, ['height','200px']);


// 函数调用三种方法
obj.myFunc();
myFunc.call(obj,arg);
myFunc.apply(obj,[arg1,arg2,...]);


/*
 * 获取绝对路径
 */
function getAbsUrl(url) {
    var a=document.createElement('a');
    a.href = url;
    return /^http/i.test(a.href)?a.href:a.getAttribute('href', 4);
}

// arguments必须在函数体内, 是一个类数组对象
arguments.length;  //函数传递的形参个数
arguments[i];      //第i+1个参数
arguments.callee;  //引用当前正在执行的函数
var result = function(x){
    if(x<=1) return 1;
    return x*arguments.callee(x-1);
};   //这能实现递归函数


//utf-16 转 utf-8 编码
function utf16to8(str){
    var out, i, len, c;
    out = "";
    len = str.length;
    for(i=0;i<len;i++){
      c = str.charCodeAt(i);
      if((c>=0x0001)&&(c<=0x007F)){
         out += str.charAt(i);
      }else if(c>0x07FF){
         out += String.fromCharCode(0xE0 | ((c >> 12) & 0x0F));
         out += String.fromCharCode(0x80 | ((c >>  6) & 0x3F));
         out += String.fromCharCode(0x80 | ((c >>  0) & 0x3F));
      }else{
         out += String.fromCharCode(0xC0 | ((c >>  6) & 0x1F));
         out += String.fromCharCode(0x80 | ((c >>  0) & 0x3F));
      }
    }
    return out;
}


//js中定义自己的命名空间
if(typeof com == "undefined"){
  var com = {};
}
//或者
var com;
if(!com) com = {};  //第一级域名
com.ModuleClass = {} //第二级域名
com.ModuleClass.aa="aa";  //定义一个变量
com.ModuleClass.func = function(){} //定义一个方法

//注册多级命名空间
var Namespace = new Object();
Namespace.register = function(path){
     var arr = path.split(".");
     var ns = "";
     for(var i=0;i<arr.length;i++){
        if(i>0){
            ns += ".";
        }
        ns += arr[i];
        eval("if(typeof(" + ns + ") == 'undefined') " + ns + " = new Object();");
    }
}

//注册命名空间 com.boohee.ui
Namespace.register(com.boohee.ui);
//使用命名空间
com.boohee.ui.TreeGrid = function(){
  this.sayHello = function(name){
     alert("Hello " + name);
  }
}
var t = new com.boohee.ui.TreeGrid();
t.sayHello("uid");


//二分法求平方根: eps为精度，如0.001
function sqrt(n0, eps0) {
    var n = parseFloat(n0);
    var eps = parseFloat(eps0);
    if(isNaN(n) || isNaN(eps0))
        return -1; //-1作为返回值表示参数有误
    var low = 0;
    var up = n;
    var lastMid;
    var mid = (low+up)/2;
    do {
        if(mid*mid > n) {    // 平方根左趋
           up = mid;
        } else {            // 平方根右趋
           low = mid;
        }
        lastMid = mid;
        mid = (low+up)/2;
    } while(Math.abs(mid-lastMid) > eps);
    return mid;
}
console.log(sqrt(3, 0.001));

//牛顿迭代法 Xi+1 = (Xi + n/Xi) / 2
function sqrt(x,esp){
    if(x == 0)
        return 0; //-1作为返回值表示参数有误
    var pre;
    var cur = 1;
    do{
        pre = cur;
        cur = x/(2*pre) + pre/2.0;
    }while(Math.abs(cur-pre)>esp);
    return cur;
}
console.log(sqrt(3, 0.001));


//Js获取uri参数方法：
function getUrlParam(name){
  var reg = new RegExp("[?&]" + name + "=([^?&]*)[&]?", "i");
  var match = location.search.match(reg); //location.search获取url参数部分
  return match == null ? "" : match[1];
}   //这种方法对于多次获取同一个参数效率低下

var getUrlParam = function() { //闭包和正则
    var args = null;
    return function(name) {
        if (args === null) {
            if (location.search == "") return "";
            var queryArray = location.search.substring(1).split("&");
            var i;
            args = {};
            for (i = 0; i < queryArray.length; i++) {
                var match = queryArray[i].match(/([^=]+)=([^=]+)/);
                if (match !== null) {
                    args[match[1]] = match[2];
                }
            }
        }
        return args[name] == undefined ? "" : args[name];
    };
}();
//这个方法利用了js的函数闭包，将url参数都保存在一个匿名函数里面
