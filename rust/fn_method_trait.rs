use std::fmt::Debug;

// Rust通过impl关键字在struct、enum或者trait对象上实现方法调用语法
// 关联函数的第一个参数通常为self, 有3种变体
// self，允许实现者移动和修改对象，对应的闭包特性为FnOnce
// &self，既不允许实现者移动对象也不允许修改，对应的闭包特性为Fn
// &mut self，允许实现者修改对象但不允许移动，对应的闭包特性为FnMut
// 不含self参数的关联函数称为静态方法(static method)
struct Circle {
    x: f64,
    y: f64,
    radius: f64,
}

impl Circle {  // impl HasArea for Circle
    fn new(x: f64, y: f64, radius: f64) -> Circle {
        Circle {
            x: x,
            y: y,
            radius: radius,
        }
    }

    fn area(&self) -> f64 {
        std::f64::consts::PI * (self.radius * self.radius)
    }

    #[allow(dead_code)]
    fn position(&self) {
        println!("position of circle is ({}, {})", self.x, self.y)
    }
}

fn main() {
    add_one(3);
    //let x: i32 = diverges();
    //let _y: String = diverges();
    // 闭包创建匿名函数
    let num = 5;
    let plus_num = |x: i32| x + num;
    plus_num(3);

    let mut n = 1;
    {
        // move实现了Copy特性, 获得n所有权
        let mut add_num = move |x: i32| n += x;
        add_num(3);
    }
    assert_eq!(1, n);

    // 方法测试
    method_test();

    let transform: fn(i32) -> i32 = add_one;
    let f0 = add_one(2i32) * 2;
    let f1 = apply(add_one, 2);
    let f2 = apply(transform, 2);
    println!("f0={}, f1={}, f2={}", f0, f1, f2);

    let closure = |x: i32| x + 1;
    let c0 = closure(2i32) * 2;
    let c1 = apply(closure, 2);
    let c2 = apply(|x| x + 1, 2);
    println!("c0={}, c1={}, c2={}", c0, c1, c2);

    let box_fn = factory(1i32);
    let b0 = box_fn(2i32) * 2;
    let b1 = (*box_fn)(2i32) * 2;
    let b2 = (&box_fn)(2i32) * 2;
    println!("b0={}, b1={}, b2={}", b0, b1, b2);

    let add_num = &(*box_fn);
    let translate: &Fn(i32) -> i32 = add_num;
    let z0 = add_num(2i32) * 2;
    let z1 = apply(add_num, 2);
    let z2 = apply(translate, 2);
    println!("z0={}, z1={}, z2={}", z0, z1, z2);
}

fn add_one(x: i32) -> i32 {
    x + 1
}

// 发散函数, 返回类型!, 支持任何类型
#[allow(dead_code)]
fn diverges() -> ! {
    panic!("This function never returns!");
}

// 高阶函数, 闭包作为参数
fn apply<F>(f: F, y: i32) -> i32
    where F: Fn(i32) -> i32
{
    f(y) * y
}

fn factory(x: i32) -> Box<Fn(i32) -> i32> {
    Box::new(move |y| x + y)
}


fn method_test() {
    let c = Circle { x: 0.0, y: 0.0, radius: 2.0 };
    println!("c.area() = {}", c.area());

    println!("Circle::new(0.0, 0.0, 2.0).area() = {}", Circle::new(0.0, 0.0, 2.0).area());
}


// 为了描述类型可以实现的抽象接口, rust引入trait(特性)定义函数签名
trait HasArea {
    fn area(&self) -> f64;
}

#[allow(dead_code)]
fn print_area<T: HasArea>(shape: T) {
    println!("This shape has an area of {}", shape.area());
}

#[allow(dead_code)]
fn foo<T: Clone, K: Clone + Debug>(x: T, y: K) {
    x.clone();
    y.clone();
    println!("{:?}", y);
}

#[allow(dead_code)]
fn bar<T, K>(x: T, y: K)
    where T: Clone,
          K: Clone + Debug
{
    x.clone();
    y.clone();
    println!("{:?}", y);
}

trait Foo {
    fn foo(&self);

    // default method
    fn bar(&self) { println!("We called bar."); }
}

// inheritance
trait FooBar : Foo {
    fn foobar(&self);
}

struct Baz;

impl Foo for Baz {
    fn foo(&self) { println!("foo"); }
}

impl FooBar for Baz {
    fn foobar(&self) { println!("foobar"); }
}

// 多个trait有同名方法, 使用通用函数调用语法
// Trait::method(args);
// <Type as Trait>::method(args);

/*
关于实现特性的几条限制：
1. 如果一个特性不在当前作用域内，它就不能被实现。
2. 不管是特性还是impl，都只能在当前的包装箱内起作用。
3. 带有特性约束的泛型函数使用单态化实现 (monomorphization)， 所以它是静态派分的 (statically dispatched)。

下面列举几个非常有用的标准库特性：
1. Drop提供了当一个值退出作用域后执行代码的功能，它只有一个drop(&mut self)方法。
2. Borrow用于创建一个数据结构时把拥有和借用的值看作等同。
3. AsRef用于在泛型中把一个值转换为引用。
4. Deref<Target=T>用于把&U类型的值自动转换为&T类型。
5. Iterator用于在集合 (collection) 和惰性值生成器 (lazy value generator) 上实现迭代器。
6. Sized用于标记运行时长度固定的类型，而不定长的切片和特性必须放在指针后面使其运行时长度已知， 比如&[T]和Box<Trait>。
*/
