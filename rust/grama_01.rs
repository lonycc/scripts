use ferris_says::say;
use std::io::{stdout, BufWriter};
use std::cell::Cell;
use std::error::Error;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;


static LOREM_IPSUM: &'static str =
"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
";

#[derive(Default)]
struct Point3d {
  x: i32,
  y: i32,
  z: Cell<i32>,
}

#[allow(dead_code)]
enum Message {
    Quit,
    Status(i32),
    ChangeColor(i32, i32, i32),
    Move { x: i32, y: i32 },
    Write(String),
}

#[allow(dead_code)]
enum OptionalInt {
    Value(i32),
    Missing,
}

mod graph {
    #[derive(Default)]
    pub struct Point {
        pub x: i32,
        y: i32,
    }

    pub fn inside_fn() {
        let p = Point {x:1, y:2};
        println!("graph.inside_fn, {}, {}", p.x, p.y);
    }
}

fn main() {
    ferris();
    array_test();
    vec_test();
    string_test();
    struct_test();
    control_flow();
}

fn ferris() {
    let stdout = stdout(); // 标准输出
    let out = b"Hello fellow Rustaceans!";
    let width = 24;

    let mut writer = BufWriter::new(stdout.lock());
    say(out, width, &mut writer).unwrap();
}


fn test_file_reader() {
    // 创建一个文件路径
    let path = Path::new("hello.txt");
    let display = path.display();

    // 打开文件只读模式, 返回一个 `io::Result<File>` 类型
    let mut file = match File::open(&path) {
        // 处理打开文件可能潜在的错误
        Err(why) => panic!("couldn't open {}: {}", display, Error::description(&why)),
        Ok(file) => file,
    };

    // 文件输入数据到字符串，并返回 `io::Result<usize>` 类型
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("couldn't read {}: {}", display, Error::description(&why)),
        Ok(_) => print!("{} contains:\n{}", display, s),
    }
}

fn test_file_writer() {
    let path = Path::new("out/lorem_ipsum.txt");
    let display = path.display();

    // 用只写模式打开一个文件，并返回 `io::Result<File>` 类型
    let mut file = match File::create(&path) {
        Err(why) => panic!("couldn't create {}: {}", display, Error::description(&why)),
        Ok(file) => file,
    };

    // 写入 `LOREM_IPSUM` 字符串到文件中, 并返回 `io::Result<()>` 类型
    match file.write_all(LOREM_IPSUM.as_bytes()) {
        Err(why) => {
            panic!("couldn't write to {}: {}", display, Error::description(&why))
        },
        Ok(_) => println!("successfully wrote to {}", display),
    }
}

fn test_std_io() {
    let mut input = String::new();
    print!("enter a string：");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut input).expect("WTF!");
    println!("You typed: {}", input.trim());
}

fn array_test() {
    println!("now test array");
    let mut array: [i32; 3] = [0; 3];

    array[1] = 1;
    array[2] = 2;

    assert_eq!([1, 2], &array[1..]);

    for x in &array {
        println!("{} ", x);
    }
}

fn vec_test() {
    println!("now test vector");
    //创建空Vec
    //let v: Vec<i32> = Vec::new();
    //使用宏创建空Vec
    //let v: Vec<i32> = vec![];
    //创建包含5个元素的Vec
    //let v = vec![1, 2, 3, 4, 5];
    //创建十个零
    //let v = vec![0; 10];
    //创建可变的Vec，并压入元素3
    //let mut v = vec![1, 2];
    //v.push(3);
    //创建拥有两个元素的Vec，并弹出一个元素
    //let mut v = vec![1, 2];
    //let two = v.pop();
    //创建包含三个元素的可变Vec，并索引一个值和修改一个值
    let mut v = vec![1, 2, 3];
    v[1] = v[1] + v[2];
    for x in v {
        println!("{}", x)
    }
}


fn string_test() {
    println!("now test string");
    let a = "aa";
    // &str类型就是[u8]切片, 即&[u8], 固定长度
    let b: &'static str = "aa";
    assert_eq!(a, b);

    // String 是一个带有的 vec:Vec<u8> 成员的结构体
    // 创建一个空的字符串
    // let mut s = String::new();
    // 从 `&str` 类型转化成 `String` 类型
    let mut s = String::from("r");
    // 压入字符和压入字符串切片
    s.push('u');
    s.push_str("st");
    println!("{}", s);
    // 弹出字符, FILO(类似队列)
    assert_eq!(s.pop(), Some('t'));
    //assert_eq!(s.pop(), None);
}

fn struct_test() {
    println!("now test struct");
    let point3d = Point3d { x: 0, y: 1, z: Cell::new(6) };
    point3d.z.set(2);
    println!("point3d.x={:?}, point3d.y={:?}, point3d.z={:?}", point3d.x, point3d.y, point3d.z);

    let origin = Point3d::default();
    let point = Point3d { y: 1, ..origin };
    let Point3d { x: x0, y: y0, .. } = point;
    println!("x0={:?}, y0={:?}", x0, y0);

    // 元组结构体
    //struct Color(u8, u8, u8);
    //let android_green = Color(0xa4, 0xc6, 0x39);
    //let Color(red, green, blue) = android_green;

    // 只有一个field的元组结构体为newtype
    //struct Digit(i32);
    //let v = vec![0, 1, 2];
    //let d: Vec<Digit> = v.into_iter().map(Digit).collect();

    // 没有field的结构体, unit-like struct
    //struct EmptyStruct;
    //let empty = EmptyStruct;

    // 模块引用
    let p = graph::Point::default();
    println!("p = graph::Point::default(), p.x={:?}", p.x);
    graph::inside_fn();

    // 枚举类型, 如果模块里pub修饰, 则枚举结构里的数据类型都是公共的
    //let m: Message = Message::Move { x: 3, y: 4 };

}

#[allow(dead_code)]
fn control_flow() {
    println!("now test control_flow");
    // 声明语句
    let x = 5;
    // 表达式语句, 如果有;,比如{10; }, 则表达式变成语句, 值丢弃, 返回unit()
    let y = if x == 5 { 10 } else { 15 };
    println!("x={:?}, y={:?}", x, y);

    for i in 0..3 {  // 0到2, for j in [0, 1, 2].iter()
        println!("{}", i);
    }

    // 死循环, 可以加label, break/continue停止和跳过循环;
    'outer: loop {
       println!("Entered the outer loop");

       'inner: loop {
           println!("Entered the inner loop");
           break 'outer;
       }

       //println!("This point will never be reached");
    }

    println!("Exited the outer loop");

    // match表达式, 类似switch/case,
    let day = 3;

    match day {
      0 | 6 => println!("weekend"),
      e @ 1 ... 5 => println!("the {} weekday", e),
      _ => println!("invalid day"),
    }

    match x {
        ref r => println!("got a reference to {}", r),
    }

    let mut m = 5;
    match m {
        ref mut m => println!("got a mutable reference to {}", m)
    }

    let pair = (1, -2);
    match pair {  // 解构元组
        (0, y) => println!("x is `0` and `y` is `{:?}`", y),
        (x, 0) => println!("`x` is `{:?}` and y is `0`", x),
        _ => println!("It doesn't matter what pair(x, y) are"),
    }

    // 解构结构体
    /*
    let origin = Point{x: 1, y: 2};
    match origin {
        Point { x, .. } => println!("x is {}", x),
    }
    */

    let op = OptionalInt::Value(5);

    match op {
        // 这里是 match 的 if guard 表达式
        OptionalInt::Value(i) if i > 5 => println!("Got an int bigger than five!"),
        OptionalInt::Value(..) => println!("Got an int!"),
        OptionalInt::Missing => println!("No such luck."),
    }


    let mut optional = Some(0);
    //if let Some(i) = Some(7)
    //while let Some(i) = optional
    while let Some(i) = optional {
        if i > 9 {
            println!("Greater than 9, quit!");
            optional = None;
        } else {
            println!("`i` is `{:?}`. Try again.", i);
            optional = Some(i + 1);
        }
    }

}
