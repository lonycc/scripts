# 一些javascript的东西

- 事件冒泡: 当一个元素上的事件被触发的时候，比如说鼠标点击了一个按钮，同样的事件将会在那个元素的所有祖先元素中被触发。这 一过程被称为事件冒泡；这个事件从原始元素开始一直冒泡到DOM树的最上层。

- 目标元素: 任何一个事件的目标元素都是最开始的那个元素，在我们的这个例子中也就是按钮，并且它在我们的元素对象中以属性的形 式出现。使用事件代理的话我们可以把事件处理器添加到一个元素上，等待一个事件从它的子级元素里冒泡上来，并且可以很方便地得知这个事件是从哪个元素开始 的。
捕获是从上级元素到下级元素，冒泡是从下级元素到上级元素.

`obj.attachEvent("onclick", fn);`  //给对象附加事件处理函数 

`obj.detachEvent("onclick", fn);`  //将事件处理函数分离出对象

// mouseenter、mouseleave IE专有事件,不冒泡事件 

//mouseover、mouseout 冒泡事件

```javascript
//事件冒泡举例
function getEventTarget(e){  //返回目标元素
  e = e || window.event;
  return e.target || e.srcElement;
}
function editCell(e){
  var target = getEventTarget(e);
  if(target.tagName.toLowerCase() === 'td'){
        //DO Something
  }
}

//消除事件冒泡
var e = (evt)?evt:window.event;
if(window.event){
   e.cancelBubble = true;
}else{
   e.stopPropagation;
}
```


> `break`语句用于跳出循环, `continue`用于跳过循环中的一个迭代

```
label: 
   statement;
break labelname; 
continue labelname;
```

> javascript错误 Throw/Try/Catch

`try {}catch(err){}  throw exception;`

## javascript对象

```
//创建对象
obj = new Object();
obj.a = "";
obj.b = "";
obj = {a:"",b:""}; //直接创建对象，并给属性赋值


//使用对象构造器
function obj(a,b){
    this.a=a;
    this.b=b;
    this.c=c;
    function c(x){
        this.a=x;
    }
}

function name(obj){alert(obj);}
name("wang");  //自调用
var test = new name("zhang"); //实例化一个对象
test();
console.log(typeof name);  //function
console.log(typeof test);  //object

function name(){
   alert(JSON.stringify(name.prototype))//{},是个空对象
}
name(); //{}
var test = new name();  //{}
alert(JSON.stringify(test.prototype))//undefined,不存在这个对象, 直接声明的函数有prototype属性,而new构造出来的对象没有


//创建对象实例
var mySon = new person("xu","lim",8);
javascript类

ES5基于prototype，而非类。 
prototype属性用于向对象添加属性和方法。

object.prototype.name = value;  //添加name属性
object.prototype.func();  //添加func()方法
var person = {fname:"bill",lname:"gates",age:56};
for(x in person){}
```

## javascript数字

> 只有一种数字类型, 可以加或不加小数点来书写. 所有javascript数字均为64位精度, 整数最多为15位, 小数最大位数为17位.

## JavaScript RegExp对象

> 用于规定在文本中检索的内容

```
//定义RegExp对象 
var patt1=new RegExp("e"); 

//对象方法 
test() 检索字符串中的指定值，返回值为true或false 
exec() 检索字符串中的指定值，返回被找到的值。若无匹配返回null 
compile()用于改变regexp，或者改变检索模式，或者增添第二个参数。

//创建regexp对象的语法 
var reg = /pattern/attributes 
var reg = new RegExp(pattern,attributes) 

//修饰符 
i大小写不敏感 
g 执行全局匹配 
m执行多行匹配

//pattern 
[]用于查找某个范围内的字符

元字符是拥有特殊含义的字符，如 
\w 查找单词字符 
\d查找数字 
\s 查找空白字符

//RegExp对象属性 
global 
ignoreCase 
lastIndex 
multiline

//支持正则表达式的String对象方法 

search(regexp);  //检索字符串中指定的子字符串, 返回值为第一个匹配的子串起始位置, 忽略标志g

match(searchvalue);  //检索字符串中指定的值, 返回该值

match(regexp);

replace(regexp/substr,replacement);  //字符串替换

split(separator,howmany);  //把一个字符串分割成字符串数组

call([thisObj][,arg1[,arg2[, [,.argN]]]);  //调用一个对象的一个方法, 以另一个对象替换当前对象 

apply([thiObj][,arg1,arg2,...]);
```

## js正则表达式
```
1、js正则对象的创建

var reg = new RegExp(‘/cat/’);
var reg = /cat/gi;   //Perl风格
2、常用的js正则方法

1)test检查指定的字符串是否存在;

var data = '123';
var reCat = /123/gi;
alert(reCat.test(data));  //true

2)exec返回查询值
var data = '123123,213,123323,3232,Cat,cat,c,';
var reCat = /cat/i;
alert(reCat.exec(data));  //Cat

3)match得到查询数组
var data = '123123,213,12312,321,3,Cat,cat,c,';
var reCat = /cat/gi;
var arrMatches = data.match(reCat);
for(var i=0;i<arrMatches.length;i++){
    alert(arrMatches[i]);  //Cat cat
}

4)search返回搜索位置,类似于indexof
var data = '123123,213,12312,312,3,Cat,cat,c,';
var reCat = /cat/gi;
alert(data.search(reCat));  //23

5)replace替换字符,利用正则替换
var data = ‘123123,213,12312,312,3,Cat,cat,c,’;
var reCat = /cat/gi;
alert(data.replace(reCat,’libinqq’)); //将Cat cat替换为libinqq

6)split使用正则分割数组
var data = '123123,213,12312,312,3,Cat,cat,c,';
var reCat = /\,/;
var arrdata = data.split(reCat);
for(var i=0;i<arrdata.length;i++){
    alert(arrdata[i]);
}
3、简单类/负向类/范围类/组合类 
[xxx]匹配[]内任意字符 
[^xxx] 匹配除[]外的任意字符 
[a-q1-9\n] 匹配a-q之间的任意字符,1-9之间的任意数字
```

# Dom Event

> Event对象代表事务的状态

## 标准event属性
```
bubbles 返回布尔值,指示事件是否为气泡事件类型 
canclelabel返回布尔值,指示事件是否可用有可取消的默认动作 
currentTarget 返回事件监听器触发该事件的元素 
eventPhase 返回事件传播的当前阶段 
target 返回触发此事件的元素 
timeStamp 返回时间生成的日期和时间 
type 返回当前Event对象表示的时间的名称
```

## 标准event方法
```
initEvent() 初始化新创建的Event对象的属性 
preventDefault() 通知浏览器不要执行与实践关键的默认动作 
stopPropagation() 不再派发事件 
Event.observe(window,event,function) 监控事件
```

## 获取触发函数的事件源

```
$(selector).click(function fun_name(e){
    console.debug(this,e);
});
```

```javascript
裸域：不带www的域名。 
cookie属性：domain和path 
cookie.domain = ‘opoo.org’ 该cookie只能发给域opoo.org, 不能发到子域www.opoo.org, static.opoo.org等 
cookie.domain = ‘.opoo.org’该cookie可以发给域opoo.org及其下所有子域，包括www.opoo.org, static.opoo.org等 
cookie.domain = ‘www.opoo.org’该cookie只能发给域www.opoo.org不能发给域opoo.org及static.opoo.org等

/*
**自定义cookie操作实现
**获取cookie  var ck = cookie.getCookie('acfun');
**设置cookie  cookie.setCookie(name,value,expires,path,domain,secure);
**删除cookie  cookie.deleteCookie(name,path,domain);
*/
var cookie = (function(){
    var co={};
    co.getCookie = function (name) {
        var start = document.cookie.indexOf(name + "=");
        var len = start + name.length + 1;
        if ((!start) && (name != document.cookie.substring(0, name.length))) {
             return null;
        }
        if (start == -1) return null;
        var end = document.cookie.indexOf(';', len);
        if (end == -1) end = document.cookie.length;
        return unescape(document.cookie.substring(len, end));
    };
    co.setCookie = function (name, value, expires, path, domain, secure) {
        var today = new Date();
        today.setTime(today.getTime());
        if (expires) {
           expires = expires * 1000 * 60 * 60 * 24;
        }
        var expires_date = new Date(today.getTime() + (expires));
        document.cookie = name + '=' + escape(value) + ((expires) ? ';expires=' + expires_date.toGMTString() : '') +((path) ? ';path=' + path : '') +((domain) ? ';domain=' + domain : '') +((secure) ? ';secure' : '');
    };
    co.deleteCookie = function(name, path, domain) {
        if (co.getCookie(name)) document.cookie = name + '=' +((path) ? ';path=' + path : '') +((domain) ? ';domain=' + domain : '') +  ';expires=Thu, 01-Jan-1970 00:00:01 GMT';
    };
    return co;
})();
```

`document.body.contentEditable='true';`

```
function parseURL(url) {   //url解析
    var a =  document.createElement('a');
    a.href = url;
    return {
        source: url,
        protocol: a.protocol.replace(':',''),
        host: a.hostname,
        port: a.port,
        query: a.search,
        params: (function(){
            var ret = {},
                seg = a.search.replace(/^\?/,'').split('&'),
                len = seg.length, i = 0, s;
                for (;i<len;i++) {
                  if (!seg[i]) { continue; }
                  s = seg[i].split('=');
                  ret[s[0]] = s[1];
                }
            return ret;
        })(),
        file: (a.pathname.match(/\/([^\/?#]+)$/i) || [,''])[1],
        hash: a.hash.replace('#',''),
        path: a.pathname.replace(/^([^\/])/,'/$1'),
        relative: (a.href.match(/tps?:\/\/[^\/]+(.+)/) || [,''])[1],
        segments: a.pathname.replace(/^\//,'').split('/')
    };
}
```

 
 

**javascript 中的函数/this/原型** 

`function fun_name(var){}`

`var f=fun_name; f(var1);`   //可将函数直接传递给变量，这个变量表示指向”对象”的指针。 

`var f = function(var){} f(var1);`  //直接将函数赋值给变量 

`var f = new Function("mess","alert(mess);"); f("hello");`  //函数即对象

> this可以看作调用函数的实际作用域上下文 

`function test(){ this.property = 'hello'; } test(); alert(window.property);`

`var obj = {}; test.call(obj);//test对象应用到obj实例上 alert(obj.property);`  //this指向obj实例 

`var obj2 = {}; obj2.test2 = test; obj2.test2(); alert(obj2.property);`

**原型**

```
function Person(){
   this.name = 'haha';
   this.Say = function(){
        alert(this.name);
    };
}
var p1 = new Person();
var p2 = new Person();
alert(p1.Say == p2.Say);  //false,可见Person每个实例中Say方法都是独立的


稍作修改
function Person(){
   this.name = 'haha';
   this.Say = say;
}
function say(){
   alert(this.name);
}

这时候Person每个实例的say方法都是相同的,但这样有违面向对象思想。

原型，可看成类型的共享区，原型本身是一个对象，而对象中的属性对于类型是共享的。JS中每个类型通过prototype属性来表示原型，通过这个属性可指定共享方法：

function Person(){}
Person.prototype.name = 'haha';
Person.prototype.Say = function(){
     alert(this.name);
};
var p1 = new Person();
var p2 = new Person();
alert(p1.Say == p2.Say);  //true
//类型属性查找顺序：先在类型的实例上查找，再继续在类型原型上查到，查到就返回。
```

`'<pre style="white-space:pre-wrap;white-space:-moz-pre-wrap;white-space:-pre-wrap;white-space:-o-pre-wrap;word-wrap:break-word;">'+content.innerHTML + '</pre>'` #文本预定义格式

# chrome extensions

## 1、chrome扩展文件
`.crx`文件，其实是一个压缩文件，可以用压缩软件打开。而打开以后，文件目录类似web应用。

## 2、Browser Actions 
也就是扩展安装后，在工具栏的显示图标。在manifest.json文件中，将扩展图标等参数注册到Browser Actions。

## 3、Page Actions
有些chrome扩展，图标显示在地址栏内部右边，比如添加书签的扩展。与Browser Actions的区别在于, 前者并非随时都显示的，必须在特定页面中这个功能才能使用。

## 4、popup弹出窗口
popup属于Browser Actions，当点击图标时出现这个窗口，可以在里面放置任何html元素，它的宽度是自适应的。并且这个弹出窗口不会被chrome拦截。

## 5、Background Pages后台页面
这个页面不会显示，它是扩展程序的后台服务，它会一直保持运行。比如一些需要数据保存程序中，如果当前用户关闭popup，就需要Background Pages来进行相应的操作。

## 6、本地存储localStorage
`window.localStorage`，以`key/value`方式进行存储，并且`value`只能是字符串形式。如果需要使用其他数据类型，需要进行相应的转换。设置和获取`localStorage`的方法是使用`localStorage.key`，或`localStorage[key]`的形式。

```
localStorage.var1 = 'name';
localStorage['var2'] = 'fuckoff';
alert(localStorage.var1);
alert(localStorage['var2']);
localStorage.var1 = null;  //清空
localStorage.setItem('age','25');
var age = localStorage.getItem('age');
localStorage.removeItem('age');
localStorage.clear();  //清空所有
```
