## 记录学习rust笔记

**cargo用法**

`cargo new proj_name`  # 创建一个项目

`cd proj_name`

`cargo run`  # 运行项目

在Cargo.toml里新增依赖

`cargo build`  # 构建

`cargo test`  # 测试

`cargo doc`  # 构建文档

`cargo publish` # 发布库


**变量绑定与原生类型**

```
// let表达式是一种模式匹配
let a = "rust";  // 不可变, 类型推导
let b: i32 = 2;  // 不可变, 显式类型
let mut c: i32 = 5;  // 可变, 显式类型
c = 2;    // 改变绑定
assert_eq!(b, c);  // 断言b和c是否相同, 必须类型和值一致
let d = 2.0f32;  // 不可变, 显式类型
let mut e = "haha"  // 可变, 类型推导
let f = 5;  // 不可变, 类型推导, i32
let c = f;  // 重新绑定为不可变

let (g, mut h): (bool, bool) = (false, true);
println!("g={:?}, h={:?}", g, h);


布尔类型：有两个值true和false。
字符类型：表示单个Unicode字符，存储为4个字节。
数值类型：分为有符号整数 (i8, i16, i32, i64, isize)、 无符号整数 (u8, u16, u32, u64, usize) 以及浮点数 (f32, f64)。
字符串类型：最底层的是不定长类型str，更常用的是字符串切片&str和堆分配字符串String， 其中字符串切片是静态分配的，有固定的大小，并且不可变，而堆分配字符串是可变的。
数组：具有固定大小，并且元素都是同种类型，可表示为[T; N]。
切片：引用一个数组的部分数据并且不需要拷贝，可表示为&[T]。
元组：具有固定大小的有序列表，每个元素都有自己的类型，通过解构或者索引来获得每个元素的值。
指针：最底层的是裸指针*const T和*mut T，但解引用它们是不安全的，必须放到unsafe块里。
函数：具有函数类型的变量实质上是一个函数指针。
元类型：即()，其唯一的值也是()

// boolean type
let t = true;
let f: bool = false;

// char type
let c = 'c';  // 单字节字符b'c', 单字符字符串b"rust", r#"..."#可以保留原始字符串不转义

// numeric types
let x = 42;
let y: u32 = 123_456;  //123456, 用_增加可读性
let z: f64 = 1.23e+2;
let zero = z.abs_sub(123.4);
let bin = 0b1111_0000;
let oct = 0o7320_1546;
let hex = 0xf23a_b049;

// string types
let str = "Hello, world!";
let mut string = str.to_string();  // 用&符号将String类型转&str类型更廉价, to_string()涉及到内存分配

// arrays and slices
// 不多于32个元素的数组和不多于12个元素的元组在值传递时是自动复制的
let a = [0, 1, 2, 3, 4]; // 数组长度不可变, 动态的数组称为Vec (vector)，可以使用宏vec!创建
let middle = &a[1..4];
let mut ten_zeros: [i64; 10] = [0; 10];

// tuples, 可以使用==和!=运算符来判断是否相同
let tuple: (i32, &str) = (50, "hello");
let (fifty, _) = tuple;
let hello = tuple.1;

// raw pointers
let x = 5;
let raw = &x as *const i32;
let points_at = unsafe { *raw };

// functions
fn foo(x: i32) -> i32 { x }
let bar: fn(i32) -> i32 = foo;

// Rust不提供原生类型之间的隐式转换，只能使用as关键字显式转换
// 可以使用type关键字定义某个类型的别名，并且应该采用驼峰命名法
let decimal = 65.4321_f32;
let integer = decimal as u8;
let character = integer as char;

type NanoSecond = u64;
type Point = (u8, u8);
 ```
 
