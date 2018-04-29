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


**使用export和import实现模块化**

// 导出常量
export const sqrt = Math.sqrt;

// 导出函数
export function square(x) {
    return x * x;
}

// 导出函数
export function diag(x, y) {
    return sqrt(square(x) + square(y));
}

export let foo = () => { console.log('haha'); return 'haha'; };

// 一次导出多个
export{ sqrt as sqrt_s , square, diag}

// 导入
import { sqrt_s as sqrt, square, diag } from './lib';
