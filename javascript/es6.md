**Symbol**

> `Symbol`, 是ES6引入的一种原始数据类型, 表示唯一的值.

`Symbol`值通过`Symbol()`函数生成, 对象的属性名可以是字符串或`Symbol`类型.

`Symbol`值作为对象属性名, 可避免被覆盖; 并且属性为公开属性.

```
let s1 =  Symbol('foo'); //带参数时为了便于区分
s1.toString();
Boolean(s1); //Symbol值只能转字符串或布尔值, 不能转数值

const obj = { toString() { return 'abc'; } };
let s2 = Symbol(obj);  //参数是对象, 则会调用对象的toString方法将其转为字符串再返回

let s2 = Symbol();
let a = {};
a[s2] = 's2'; 
Object.defineProperty(a, s1, {value: 's1'});

let b = {[s2]: 's2'};

let c = { [s](arg) { .. } }; //[s]为Symbol类型, 其对应的值可为function

Object.getOwnPropertyNames(a); //获取对象的字符串属性名
Object.getOwnPropertySymbols(a);  //获取对象的Symbol属性名
Reflect.ownKeys(a);  //获取对象的所有类型属性名

let s3 = Symbol.for('foo');  //搜索是否已存在以foo为名称的Symbol值, 有则使用, 无则创建;
Symbol.keyFor(s3); //"foo"

// 使用Symbol实现模块的单例
const FOO_KEY = Symbol.for('foo');
function A() = { this.foo = 'hello'; }
if ( ! globla[FOO_KEY] ) { global[FOO_KEY] = new A(); }
module.exports = global[FOO_KEY];

// 内置的Symbol值
foo instanceof Foo  // Foo[Symbol.hasInstance](foo) {}
Symbol.isConcatSpreadable  //对象用于Array.protype.concat()时是否可以展开
Symbol.species  //指向一个构造函数, 创建衍生对象时会使用
static get[Symbol.species]() { return this; }

[Symbol.match](string) {}  //指向一个函数, 当执行str.match(obj)时, 如果该属性存在则调用它, 返回该方法的返回值

Symbol.replace  //当对象被String.prototype.replace方法调用时, 会返回调用Symbol.replace 并返回其返回值;
Symbol.search
Symbol.split

Symbol.iterator //指向对象默认遍历器方法
for(let col of Col) //对象进行for of 循环时, 会调用Symbol.iterator方法

Symbol.toPrimitive //对象被转为原始类型时会调用该属性指向的方法
Symbol.toStringTag //对象执行Object.prototype.toString方法时,若该属性存在, 其返回值会出现在toString方法返回的字符串中, 表示对象的类型

Symbol.unscopables //指向一个对象, 该对象使用了with关键字时, 哪些属性会被with环境排除
```

**Set 和 Map 数据结构**

> Set数据结构, 类似数组, 但其成员的值都是唯一的.

```
const s = new Set(); //or new Set([1, 'a', null, false]);
s.add('a');
s.size;
s.delete('a');
s.has('a');
s.clear();
s.keys(); //由于Set结构没有键名, 同values(), 返回遍历器对象
s.values(); 
s.entries();
s.forEach((k, v) => { console.log(k, v); });

Array.from(s);  //将Set结构转为数组

[...new Set(array)]; //数组去重， 或者 Array.from(new Set(array));

let union = new Set([...a, ...b]); //并集
let intersect = new Set([...a].filter(x=>b.has(x))); //交集
let difference = new Set([...a].filter(x=>!b.has(x))); //差集
```

> WeakSet结构, Set结构的特例, 成员只能是对象; 没有size属性, 无法遍历;

```
const ws = new WeakSet([[1, 2], ['a', 'b']]);
ws.add(value);
ws.delete(value);
ws.has(value);
```

> Map结构, 键名不限于字符串, 提供了"值-值"的对应; 其构造函数接受数组作为参数, 数组成员是一个个表示键值对的数组; 也可以接受Map或Set对象来初始化Map对象; Map的键是跟内存地址绑定的, 只要内存地址不同, 就视为不同键;

```
const map = new Map();
const o = {p: 'content'};
map.set(o, 'oo'); //set支持链式操作, 多次赋值
map.get(o);
map.has(o);
map.delete(o);
map.clear();
map.size;
map.keys();
map.values();
map.entries(); //Map结构默认遍历器接口(Symbol.iterator属性), 就是entries方法;
map.forEach( (v, k, map) => { console.lgo(v, k); } );
map.forEach( (v, k, map) => { this.report(k, v); }, reporter); //forEach方法的第二个参数用于绑定this, 指向的就是reporter;

const s = new Set([['foo', 1], ['bar', 2]]);
const k = new Map(s);
const m = new Map([['name','tony'],['age', 25]]);
const n = new Map(m);

NaN === NaN;  //false, 尽管如此, Map结构将其视为同一个键;
typeof NaN; //number

[...map.keys()];  //keys转数组
[...map.values()];  //values转数组
[...map.entries()]; //键值对数组;
```

> WeakMap结构, 只接受对象作为键名, 弱引用; 一般用于网页DOM; 弱引用, 也就是外部消除了键名, 则WeakMap结构中的键名也被消除了;


**Proxy**

> 对对象的访问经过Proxy过滤和改写;

```
var proxy = new Proxy(target, handler); //handler也是一个对象
var obj = {proxy: new Proxy(target, handler)};


Proxy支持的拦截操作:
get(target, propKey, receiver);  //拦截对象属性的读取
set(target, propKey, value, receiver);  //拦截对象属性的设置
has(target, propKey); //拦截propKey in proxy的操作, 返回布尔值
deleteProperty(target, propKey); //拦截delete proxy[propKey]的操作, 返回布尔值
ownKeys(target); //拦截各种遍历属性名的方法操作; 返回数组
getOwnPropertyDescriptor(target, propKey);
defineProperty(target, propKey, propDesc);
preventExtensions(target);
getPrototypeOf(target);
isExtensible(target);
setPrototypeOf(target, proto);
apply(target, object, args);
construct(target, args);

let {proxy, revoke} = Proxy.revocable(target, handler);
proxy.foo = 123;
revoke();
proxy.foo; //报错, Revoked
```

```
const a1 = [undefined, false, null];
const a2 = [, , ,]; //对于a2, 虽然有长度, 但其属性都是未定义的, 所以in/hasOwnProperty/Object.keys操作都娶不到属性名;
```

**Reflect**

> 将Object对象的一些内部方法, 放到Reflect对象上, 例如defineProperty方法; 让Object操作变成函数行为, 例如name in obj 和 delete obj[name] 转为 Reflect.has(obj, name) 和 Reflect.deleteProperty(obj, name);

> Refelct对象的方法和Proxy对象的方法一一对应; 

```
var loggedObj = new Proxy(obj, {
  get(target, name) {
    console.log('get', target, name);
    return Reflect.get(target, name);
  },
  deleteProperty(target, name) {
    console.log('delete' + name);
    return Reflect.deleteProperty(target, name);
  },
  has(target, name) {
    console.log('has' + name);
    return Reflect.has(target, name);
  }
});

// 老写法
Function.prototype.apply.call(Math.floor, undefined, [1.75]);
// 新写法
Reflect.apply(Math.floor, undefined, [1.75]);

// Reflect对象的13个静态方法
Reflect.apply(target, thisArg, args)
Reflect.construct(target, args)
Reflect.get(target, name, receiver)
Reflect.set(target, name, value, receiver)
Reflect.defineProperty(target, name, desc)
Reflect.deleteProperty(target, name)
Reflect.has(target, name)
Reflect.ownKeys(target)
Reflect.isExtensible(target)
Reflect.preventExtensions(target)
Reflect.getOwnPropertyDescriptor(target, name)
Reflect.getPrototypeOf(target)
Reflect.setPrototypeOf(target, prototype)

// Proxy实现观察者模式: 函数自动观察数据对象, 一旦对象变化, 函数自动执行;
const queuedObservers = new Set();

const observe = fn => queuedObservers.add(fn);
const observable = obj => new Proxy(obj, {set});

function set(target, key, value, receiver) {
  const result = Reflect.set(target, key, value, receiver);
  queuedObservers.forEach(observer => observer());
  return result;
}
```

**Iterator**

> 四种数据集合, Array / Object / Map / Set; 遍历器是一种接口, 为不同数据集合提供统一访问机制; 任何数据结构只要部署Iterator接口, 就可完成遍历操作; `for...of`循环, 会自动寻找Iterator接口; Object原生不具备Iterator接口, 可定义`Symbol.iterator`属性, 作为默认Iterator.

```
let arr = ['a', 1, false, null];
let iter = arr[Symbol.iterator]();
iter.next();

// array-like 对象 使用数组的遍历接口
NodeList.prototype[Symbol.iterator] = [][Symbol.iterator];
let iter = [...document.querySelectorAll('div')][Symbol.iterator]();
iter.next();

for (let item of iterable) {}


// 调用Iterator接口场合
1. 解构赋值
let set = new Set().add('a').add('b').add('c');
let [x, y] = set;  // x = 'a'; y = 'b';
let [first, ...rest] = set; // first = 'a'; rest = ['b', 'c'];

2. 扩展运算符
var str = 'hello';
[...str]; // ['h','e','l','l','o'];
let arr = ['b', 'c'];
['a', ...arr, 'd']; // ['a', 'b', 'c', 'd'];
let arr2 = [...iterable]; // 可将任何部署了Iterator接口的数据结构转数组;

3. yield* 后面跟一个可遍历结构, 会调用该结构的遍历器接口;
let generator = function* () { yield 1; yield* [2,3,4]; yield 5; }

// 字符串的Iterator接口
typeof 'ha'[Symbol.iterator];  // 'function'
var iter = 'ha'[Symbol.iterator]();
iter.next();

var str = new String('hi');
[...str]; // ['h', 'i'];
str[Symbol.iterator] = function() {};  // 覆盖原生Symbol.iterator方法

// 给对象部署Symbol.iterator方法, 也就是生成函数
let obj = {
  * [Symbol.iterator]() {
    yield 'hello';
    yield 'world';
  }
};
[...obj];

// 遍历器对象的 return(), throw(); return()必须返回一个对象; 
// for of 可以中途break/continue/return, forEach不行;
```

**Generator函数**

> 执行Generator函数会返回一个Iterator对象; 与普通函数不同的是, `function*`作声明, 函数体内部用`yield`表达式; 调用时对Iterator对象做next()操作;

> yield表达式, 惰性求值; 只能放在Generator函数里; yield表达式如果用在另一表达式中, 必须放在括号里; `console.log('hello' + (yield 123));`

```
function* fibonacci() {
  let [prev, curr] = [0, 1];
  for (;;) {
    [prev, curr] = [curr, prev + curr];
    yield curr;
  }
}

// 对象的Symbol.iterator方法, 等于该对象的遍历器生成函数;
// yield表达式总是返回undefined, next方法可以带一个参数, 作为上一个yield表达式的返回值; 只有从第二次next开始后带上参数才有效, 第一次next用于启动遍历器对象, 不用带参数;

// 使用for...of可以遍历生成器函数生成的Iterator对象, 但不会包含返回对象;

对象要实现遍历器接口, 可以增加属性Symbol.iterator, 其值为生成器函数;
function* objectEntries() {
  let propKeys = Object.keys(this);

  for (let propKey of propKeys) {
    yield [propKey, this[propKey]];
  }
}
let jane = { first: 'Jane', last: 'Doe' };
jane[Symbol.iterator] = objectEntries;

function* numbers () {
  yield 1;
  yield 2;
  return 3;
  yield 4;
}
[...numbers()]; //扩展运算符可使用Iterator对象
Array.from(numbers()); 
let [x, y] = numbers();
for (let n of numbers()) {}

// Generator.prototype.throw(), generator函数返回的遍历器对象, 都有一个throw方法, 可以在函数外抛出异常, 然后在函数内捕获;

var g = function* () { 
	try {
		yield;
	} catch (e) {
		console.log(e);
	}
};
var i = g();
i.next();
i.throw(new Error('wrong')); //该异常由遍历器对象的throw方法抛出, 会被函数体内异常捕获;

// Generator.prototype.return(), 可以返回给定的值, 请结束遍历;
g.return('foo');  //返回foo, 之后执行g.next()永远都是undefined;

// yield* 表达式, 当在一个generator里执行另一个generator时, 需要用yield*才能生效;


// Generator函数的this
function* gen() {
	this.a = 1;
	yield this.b = 2;
	yield this.c = 3;
}
function F() {
	return gen.call(gen.prototype);
}
var f = new F();
f.next();
f.a;

// Generator与状态机
var clock = function* () {
  while (true) {
    console.log('Tick!');
    yield;
    console.log('Tock!');
    yield;
  }
};

// Generator与上下文
全局上下文, 执行函数时切换到函数运行上下文, 由此形成一个上下文环境的栈(context stack).
Generator函数的上下文环境, 一旦遇到yield命令, 就暂时退出栈, 上下文冻结, 等执行next命令时则上下文环境重新加入调用栈, 恢复上下文;

function* gen() {
  yield 1;
  return 2;
}

let g = gen();

console.log(
  g.next().value,
  g.next().value,
);


// Generator应用
1. 部署Iterator接口
function* iterEntries(obj) {
  let keys = Object.keys(obj);
  for (let i=0; i < keys.length; i++) {
    let key = keys[i];
    yield [key, obj[key]];
  }
}

let myObj = { foo: 3, bar: 7 };

for (let [key, value] of iterEntries(myObj)) {
  console.log(key, value);
}
```

**event loop**

> javascript的执行是单线程的, 单线程意味着所有任务都需要排队, 前一个任务结束, 才执行下一个任务; 异步任务, 不进入主线程, 而进入任务队列, 只有任务队列通知主线程, 异步任务才进入主线程执行;

> node.js中的事件循环, V8引擎解析JavaScript脚本, 解析后的代码调用Node Api; libuv库负责Node Api的执行, 它将不同任务分配给不同线程, 形成一个event loop, 以异步的方式将任务的执行结果返回给V8引擎; V8引擎再将结果返回给用户.

```
// node.js 与任务队列有关的方法: setTimeout, setInterval, process.nextTick, setImmediate;
// process.nextTick方法可以在当前执行栈的尾部, 也就是下一次EventLoop之前触发回调, 它指定的任务总是发生在所有异步任务之前;
process.nextTick( () => {
	console.log('method in process.nextTick');
	process.nextTick( () => { console.log('method in method'); } );
});

// setImmediate方法在当前任务队列尾部添加事件, 总是在下一次EventLoop时执行;
setImmediate( () => console.log('method in setImmediate'); );
```

**Generator函数的异步方法**

> ES6之前, 异步编程的实现方法有callback, callback层层嵌套, 形成callback hell; Promise只是新的写法, 将callback嵌套改成了链式调用.


Thunk函数, 编译器的"传名调用", 往往是将参数放到一个临时函数中, 再将这个临时函数传入函数体. 这个临时函数即为Thunk函数.

```
const Thunk = function(fn) {
  return function (...args) {
    return function (callback) {
      return fn.call(this, ...args, callback);
    }
  };
};

var readFileThunk = Thunk(fs.readFile);
readFileThunk(fileA)(callback);

// 生产环境用Thunkify模块实现转换
const thunkify = require('thunkify');
const fs = require('fs');
var read = thunkify(fs.readFile);
read(filename)(callback);

// Thunk函数结合Generator函数实现自动流程管理
function run(fn) {
  var gen = fn();

  function next(err, data) {
    var result = gen.next(data);
    if (result.done) return;
    result.value(next);
  }

  next();
}

function* g() {}

run(g);

// co模块
const co = require('co');
co(gen).then();  //co模块可用于执行generator函数, 返回promise对象;
```

**Promise 对象**

> Promise 对象里面保存着异步任务, 有三种状态: pending(进行中)、resolved(完成)、rejected(失败), 状态可从pending转为resolved和rejected, 一旦状态改变, 就不会再变, 这时称为resolved.


resolve和reject两个参数都是函数, 由JavaScript引擎提供;

resolve函数的作用, 将Promise对象的状态从pending转为resolved, 在异步操作成功时调用, 并将结果作为参数传递出去; reject函数将Promise对象的状态从pending转为rejected, 在异步操作失败时调用, 并将错误作为参数传递出去;

Promise实例一旦新建立即执行; 一般而言, Promise对象中调用了resolve或reject以后, Promise的使命就完成了, 后继任务应该放在then方法里.

```
const promise = new Promise( (resolve, reject) => { return resolve(xx); } );
promise.then( value => {}, error => {} );
```

`Promise.prototype.then()`, `then`方法的第一个参数是`resolved`状态的callback, 第二个参数是`rejected`状态的callback; 如果then方法返回了一个新的Promise实例, 则可以链式调用then方法;

`Promise.prototype.catch()`, `catch`方法是`.then(null, rejection)`的别名, 用于指定错误时的callback; catch方法具有冒泡性质, promise对象的错误具有冒泡性质, 会一直向后传递, 直到被捕获; 建议用catch方法代替then方法的第二个参数(reject回调); catch方法返回的是一个新的Promise对象, 所以还可以继续链式调用then方法;

Promise对象抛出的错误如果没有处理, 不会影响到Promise外部代码的运行; Node提供了`unhandleRejection`事件, 专门监听未捕获的reject错误; `process.on('unhandleRejection', (err, p) => { throw err; });`

`Promise.prototype.finally()`, `finally`方法表示最后一定会执行的操作, 与状态无关;

`Promise.all()`, 用于将多个Promise实例包装成一个新的Promise实例; `const p = Promise.all([p1, p2, p3]);`, 当p1/p2/p3均转为resolved状态, p的状态才会转为resolved; p1/p2/p3中只要有rejected, 则第一个被reject的实例的返回值会传给p的callback; 如果p1/p2/p3有自己的catch方法, 则p的catch方法不会捕获, 否则会被p的catch方法捕获; 

`Promise.race()`, 同样将多个Promise实例包装成一个新的Promise实例; `const p = Promise.race([p1, p2, p3]);`, p1/p2/p3任意一个率先改变状态, p的状态随着改变;

`Promise.resolve()`, 将现有对象转为Promise对象; 如果参数是一个Promise实例, 则resolve方法不会改变该实例; 如果参数是具有then方法的对象, resolve方法会将这个对象转为Promise对象, 然后执行该对象的then方法; 如果参数为不具有then方法的对象或不是对象, 则resolve方法返回一个新的Promise对象, 状态为resolved; 如果不带参数, 则直接返回一个resolved状态的Promise对象; Promise.resolve()在本轮event loop结束时执行, setTimeout()在下一轮执行;

`Promise.reject()`, 返回一个新的Promise实例, 状态为rejected;

Promise对象的应用: 图片加载

```
const preloadImage = function (path) {
  return new Promise(function (resolve, reject) {
    const image = new Image();
    image.onload  = resolve;
    image.onerror = reject;
    image.src = path;
  });
};
```

`Promise.try()`, 同步函数同步执行, 异步函数异步执行; 尚处于提案状态;

```
(
	() => new Promise(
		resolve => resolve(f())
	)
)();
```

**ArrayBuffer**

`ArrayBuffer`对象, 代表内存中的二进制数据, 可以通过视图进行操作;

`TypedArray`视图, 包含9种类型的视图, 

`DataView`视图, 自定义复合格式的视图, 支持除`Uint8C`以外的另8种;

```
const buf = new ArrayBuffer(32);  //初始化32字节的连续内存区域, 每个字节默认值0
const dataView = new DataView(buf);  //指定视图
dataView.getUint8(0);  //以无符号8位整数格式, 读取索引0位置的一个字节, 结果为0

const x1 = new Int32Array(buf); //TypedArray视图是一组构造函数
x1[0] = 1;
const x2 = new Uint8Array(buf, 0, 3); //第二个参数为字节偏移, 第三个为长度
x2[0] = 2; //由于操作的是同一段内存, x2修改内存导致x1也被修改
x1[0];  // 2

const typedArray = new Uint8Array([0,1,2]); //也可接受普通数组作为参数
typedArray.length;  // 3
typedArray[0] = 5;
typedArray;  // [5,1,2]
// 可转为普通数组
const na = [...typedArray];
const na_2 = Array.from(typedArray);
const na_3 = Array.prototype.slice.call(typeArray);

// 视图不通过ArrayBuffer对象, 直接分配内存
const f64a = new Float64Array(8); //64字节
f64a[0] = 10;
f64a[1] = 20;
f64a[2] = 30;

const ta = new Int8Array(new Uint8Array(4)); //接受另一个TypedArray实例作为参数, 开辟了新的内存; 若想基于同一段内存, 则用TypedArray实例的buffer属性作为参数;
```

`ArrayBuffer.prototype.byteLength`, ArrayBuffer实例的byteLength属性, 返回所分配内存区域的字节长度; 如果分配内存区域过大, 可能失败, 所以要检查 `buf.byteLength === n`;

`ArrayBuffer.prototype.slice()`, 允许将内存区域的一部分, 拷贝生成一个新的ArrayBuffer对象; `const newBuffer = buf.slice(0, 3);`

`ArrayBuffer.isView()`, 该方法接受ArrayBuffer实例或视图实例作为参数, 返回一个布尔值, 表示是否为ArrayBuffer的视图实例;

字节序, 指的是数值在内存中的表示方式; 一般x86设备采用小端(little endian)字节序, 也就是低地址存放最低有效字节;

8位整数 2 1 3 7 => 00000010 00000001 00000011 00000111

16位整数 00000001 00000010 00000111 00000011 => 0x1273 => 1^256+2=258 7*256+3=1795



```
const BIG_ENDIAN = Symbol('BIG_ENDIAN');
const LITTLE_ENDIAN = Symbol('LITTLE_ENDIAN');

function getPlatformEndianness() {
  let arr32 = Uint32Array.of(0x12345678);
  let arr8 = new Uint8Array(arr32.buffer);
  switch ((arr8[0]*0x1000000) + (arr8[1]*0x10000) + (arr8[2]*0x100) + (arr8[3])) {
    case 0x12345678:
      return BIG_ENDIAN;
    case 0x78563412:
      return LITTLE_ENDIAN;
    default:
      throw new Error('Unknown endianness');
  }
}
```
每种TypedArray的构造函数, 都有个`BYTES_PER_ELEMENT`属性, 表示该种数据类型占据的字节数. 这个属性也可以TypedArray实例上获取`Uint8Array.prototype.BYTES_PER_ELEMENT`或`uint8Array.BYTES_PER_ELEMENT`.

ArrayBuffer与字符串的互相转换, 前提是字符串的编码方式确定.

```
// ArrayBuffer 转为字符串，参数为 ArrayBuffer 对象
function ab2str(buf) {
  // 注意，如果是大型二进制数组，为了避免溢出，
  // 必须一个一个字符地转
  if (buf && buf.byteLength < 1024) {
    return String.fromCharCode.apply(null, new Uint16Array(buf));
  }

  const bufView = new Uint16Array(buf);
  const len =  bufView.length;
  const bstr = new Array(len);
  for (let i = 0; i < len; i++) {
    bstr[i] = String.fromCharCode.call(null, bufView[i]);
  }
  return bstr.join('');
}

// 字符串转为 ArrayBuffer 对象，参数为字符串
function str2ab(str) {
  const buf = new ArrayBuffer(str.length * 2); // 每个字符占用2个字节
  const bufView = new Uint16Array(buf);
  for (let i = 0, strLen = str.length; i < strLen; i++) {
    bufView[i] = str.charCodeAt(i);
  }
  return buf;
}
```

溢出, 视图类型放入的数值超过其位数; 正向溢出(overflow): 当输入值大于当前数据类型的最大值, 结果等于当前数据类型的最小值加上余值, 再减1;
负向溢出(underflow): 当输入值小于当前数据类型的最小值, 结果等于当前数据类型的最大值减去余值, 再加1; `Uint8ClampedArray`视图的溢出规则, 凡是正向溢出, 结果等于255; 负向溢出, 结果等于0;

```
const uint8 = new Uint8Array(1);
uint8[0] = 256; // 1 0000 0000
uint8[0];  // 保留后8位, 即 0000 0000
uint8[0] = -1; // -1对应正值1, 取否1111 1110, 再加1, 得到255
uint8[0]; // 255
```

`TypedArray.prototype.buffer`, 返回内存中对应的ArrayBuffer对象, 只读;

`TypedArray.prototype.byteLength`, 返回TypedArray数组字节长度;

`TypedArray.prototype.byteOffset`, 返回TypedArray数组从底层ArrayBuffer对象的偏移量;

`TypedArray.prototype.length`, 返回TypedArray数组成员数;

`TypedArray.prototype.set(typedArray [, offset])`, 复制数组内容;

`TypedArray.prototype.subarray(start [, end])`, 截取一部分;

`TypedArray.prototype.slice(position)`, 类似subarray, 表示截取从指定位置到结束;

`TypedArray.of()`, 静态方法, 将参数转为一个TypedArray实例, `Float32Array.of(0.15, -8, 3.5)`, `Int8Array.of(127, 126, 125).map(x => 2 * x)`;

`TypedArray.from()`, 静态方法, 接收一个iterable结构参数, 返回TypedArray实例;`Uint16Array.from([10, 23, 56])`, 

`Uint16Array.from(Uint8Array.of(0, 1, 2))`, `Int16Array.from(Int8Array.of(127, 126, 125), x => 2 * x)`;

复合视图, 由于视图的构造函数可以指定起始位置和长度, 所以在同一段内存中, 可以依次存放不同类型的数据, 形成复合视图;

```
const buffer = new ArrayBuffer(24);

const idView = new Uint32Array(buffer, 0, 1); // 0~3字节
const usernameView = new Uint8Array(buffer, 4, 16); // 4~19字节
const amountDueView = new Float32Array(buffer, 20, 1); // 20~23字节
```

DataView视图, 操作不同类型数据, `DataView(ArrayBuffer buffer [, start [, length]])`;

`DataView.prototype.buffer`

`DataView.prototype.byteLength`

`DataView.prototype.byteOffset`

`DataView.prototype.getIn8(index)`, 读取指定位置的8位整数

`DataView.prototype.getUint16(index [, bool=false])`, 默认使用大端字节序

`DataView.prototype.setInt32(index, data [, bool=false])`, 在index位置, 写入data, 默认大端字节序

二进制数组的应用, 在xhr2中, 指定responseType为arraybuffer; Canvas二进制像素数据; WebSocket发送接收二进制数据; Fetch API取回的数据; File API; SharedArrayBuffer,

**ES6编程风格**

块级作用域, 用let取代var; 全局环境, 使用const, 而非let;

静态字符串一律使用单引号或反引号, 动态字符串使用反引号;

使用数组成员对变量赋值时优先使用解构赋值 `const [a, b] = [1, 2]`; 函数的参数是对象的成员优先使用解构赋值 `function dn({f1, f2}){}`; 如果函数返回多个值, 优先使用对象的解构赋值, 而非数组;

定义单行的对象, 最后一个成员不以逗号结尾 `const a = {k1:v1, k2:v2}`; 定义多行对象, 最后一个成员以逗号结尾;

对象尽量静态化, 一旦定义就不得随意添加属性; 添加属性使用`Object.assign`方法; 

使用扩展运算符`...`拷贝数组; 使用`Array.from()`将array-link对象转为数组;

立即执行函数写成箭头函数形式, `( () => { console.log('ha'); } )()`; 需要用到函数表达式的场合, 用箭头函数, `[1, 2, 3].map(x => x * x)`; 箭头函数取代`Function.prototype.bind`, `const boundMethod = (...params) => method.apply(this, params)`; 布尔值不直接作为参数, `{option = false} = {}`; 

使用Class写法, 取代prototype操作, `class Q {}`; 使用extends实现继承, `class P extends Q {}`;

使用import取代require, 使用export取代module.exports; 如果模块只有一个输出, 使用export default; 如果模块默认输出一个函数, 函数名首字母应小写, 如果模块默认输出一个对象, 对象首字母应大写;


**使用export和import实现模块化**

在ES6之前, 社区制定了模块加载方案, 有CommonJS和AMD两种, 前者用于服务器, 后者用于浏览器; import是静态执行的, 不能使用表达式或变量; import语句是Singleton模式的;

```
// 导出常量
export const sqrt = Math.sqrt;

// 导出函数
export function square(x) {
    return x * x;
}

// 导出函数
export function diag(x, y) { return sqrt(square(x) + square(y)); }

export let foo = () => { console.log('haha'); return 'haha'; };

// 一次导出多个, 用as重命名
export { sqrt as sqrt_s , square, diag};

// 导入多个, 用as重命名
import { sqrt_s as sqrt, square, diag } from './lib';

// 整体加载模块
import * as circle from './circle';

// 如果模块使用了export default, 那么在import的时候, 可以任意命名;

// 加载默认方法和其他接口
import _, { aa, aa as bb } from './moduleA';

// 模块的继承
export * from 'moduleA'; 
export default xx;
```

传统HTML页面, 浏览器通过`<script>`标签加载脚本, 默认是同步加载, 如果需要异步加载, 需要设置`<script src="" defer></script>`或`<script src="" async></script>`, defer是渲染完再执行, async是下载完即执行;

加载ES6模块, `<script type="module" src="">`, 模块顶层this关键字返回`undefined`, 而非指向`window`;

CommonJS模块输出值拷贝, ES6模块输出值引用; CommonJS模块运行时加载, ES6模块编译时输出接口;


**async await**

> `async`函数就是将`generator`函数的`*`去掉, 在`function`前加`async`, 将`yield`替换成`await`;

`async`函数对`generator`函数的改进, `generator`函数的执行必须靠执行器, 而`async`函数自带执行器; `async`函数返回值是`Promise`对象, 而`generator`返回的是`Iterator`对象; `await`后可以是`Promise`对象或原始类型的值, `co`模块规定`yield`命令后只能是`Thunk`函数或`Promise`对象; 

```
// 函数声明
async function foo() {}

// 函数表达式
const foo = async function () {};
const foo = async () => {};

// 对象的方法
let obj = { async foo() {} };
obj.foo().then(//...);
```

async函数返回一个Promise对象, 其内部return语句返回的值, 会被then方法回调函数接收到. async函数内部抛出错误, 会导致返回的Promise对象状态转为reject, 抛出的错误对象会被catch方法回调函数接收到.

```
async function f() {
  throw new Error('出错了');
}

f()
.then(v => console.log(v))
.catch(e => console.log(e));
```

一般在await命令后面是一个Promise对象, 如果不是, 会被转成一个立即resolve的Promise对象; 一个await语句后的Promise转为reject, 那么整个async函数都会中断执行, 可以将await放入`try...catch`结构或者`await Promise.reject('').catch();`

```
async function dbFunc(db) {
	let docs = [{}, {}, {}];
	let promises = docs.map((doc) => db.post(doc));
	return await Promise.all(promises);
}

async function logInOrder(urls) {
  // 并发读取远程URL
  const textPromises = urls.map(async url => {
    const response = await fetch(url);
    return response.text();
  });

  // 按次序输出
  for (const textPromise of textPromises) {
    console.log(await textPromise);
  }
}
```

**Class基本语法**

类方法内部如何有`this`, 它默认指向类的实例. 

```
let methodName = 'getArea';
class Point {
  	constructor(x, y) {
  		console.log(new.target === Point);
   		this.x = x;
    	this.y = y;
  	}
  	
	get prop() { return 'getter'; }
	
	set prop(value) { console.log('setter: ' + value); }
	
	* [Symbol.iterator]() {} // generator方法

	static methodA() {}  // 静态方法, 直接通过类调用, 不能被实例继承
	
  	toString() {
    	return '(' + this.x + ', ' + this.y + ')';
  	}
  
  	// 类的属性名可以是表达式
  	[methodName]() {
  	}
}

let p = new Point(5, 6);  // true, 表示构造函数是new命令调用的
p.prop = 123;  // setter, 定义静态属性
p.prop;  // getter, 获得静态属性
typeof Point;  // function
Point === Point.prototype.constructor; // true
p.constructor === Point.prototype.constructor;  // true
Point.name; // name属性返回class关键字后面的类名

// 静态属性, class本身属性, 即Class.propName, 而非定义在实例对象this上的属性

p

// 在类的实例上调用方法, 其实就是调用原型上的方法; 

// 向类添加方法
Object.assign(Point.prototype, {
	toValue(){},
	toA(){}
});

Object.keys(Point.prototype); // [], 类内部定义的方法不可枚举
p.__proto__.hasOwnProperty('toString'); // true

// class表达式, 如果类内部未用到类名, 则Me可以省略; 如果需要立即执行, 同函数一样
const myClass = class Me {};
```

**Class 的继承**

> 通过`extends`关键字实现继承; 子类内部通过`super`关键字调用父类方法和属性; 子类必须在构造函数中调用`super()`方法才能使用`this`关键字;

`Object.getPrototypeOf(childClass)`, 用于从子类上获取父类

```
class A {} 
class B extends A {}

B.__proto__ === A; // true
B.prototype.__proto__ === A.prototype;  // true
```

Mixin模式, 多个对象合成一个新对象, 新对象具有各个组成成员的接口.
