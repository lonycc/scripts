package main

// go没有类和继承的概念, 通过结构来实现面向对象的特性.
// 接口定义了一组方法[方法集], 但是这些方法不包含实现代码, 它们没有被实现[它们是抽象的], 接口里也不能包含变量.
// 按约定, 接口的名字由方法名加[e]r后缀组成; 遇到不适合er后缀的, 用able结尾, 或I开头.

type Namer interface {
    Method1(param_list) return_type
    Method2(param_list) return_type
    // ...
}

// 接口值 var ai Namer, 其内存结构是一个多字, 它的值为nil
// 类型不需要显式声明它实现了某个接口: 接口被隐式地实现. 多个类型可以实现同一个接口.
// 实现某个接口的类型, 除了实现接口方法外, 可以有其他的方法
// 一个类型可以实现多个接口
// 接口类型可以包含一个实例的引用, 该实例的类型实现了此接口, 接口是动态类型
type Shaper interface {
    Area() float32
}
func Circle(s Shaper) string {  // 所有Shaper类型变量都可调用该方法
    return "h"
}
type Square struct {
    side float32
}
type Rectangle struct {
    width, height float32
}
func (r Rectangle) Area() float32 {
    return r.width * r.height
}
func (sq *Square) Area() float32 {
    return sq.side ^ 2   
}
sq := new(Square)
sq.side = 5.0
var sp Shaper
sp = sq  //由于sq是Square的实例, Square实现了接口Shaper的方法, 所以可将sq赋值给Shaper类型的变量sp
sp.Area()

//实现多态
r := Rectangle{5.0, 3.0}
q := &Square(5.9)
shapes := []Shaper{r, q}
for n, _ := range shapes {
    shapes[n].Area()
}

// 接口嵌套接口
type ReadWrite interface {
    Read(b Buffer) bool
    Write(b Buffer) bool
}

type Lock interface {
    Lock()
    Unlock()
}

type File interface {
    ReadWrite
    Lock
    Close()
}

// 类型断言, varI必须是一个接口变量, T是类型
v, ok := varI.(T)
t, ok := sp.(*Square)
sp.(type)  //返回sp变量的类型

// 类型判断 type-switch, 不允许fallthrough
// 测试一个值是否实现了某个接口
// 
// 类型 *T 的可调用方法集包含接受者为 *T 或 T 的所有方法集
// 类型 T 的可调用方法集包含接受者为 T 的所有方法, 不包含接受者为 *T 的方法集

// 空接口, 不包含任何方法, 对实现不做要求
// 空接口常用语构建通用类型 / 包含不同类型的数组, 切片复制等
type Any interface {}
testFunc := func(any interface {}) { }

// 反射是用程序检查其拥有的结构/类型的能力, 可以从接口值反射到对象, 也可从对象反射回接口值
func TypeOf(i interface{}) Type
func ValueOf(i interface{}) Value

var x float64 = 3.4
reflect.TypeOf(x)
v = reflect.ValueOf(x)
v.CanSet()
v.Type()
v.Kind()
v.Float()
v.Interface()
v.Interface().(float64)
w = reflect.ValueOf(&x)
w = w.Elem()
w.SetFloat(3.1415)

v.NumField() // 实例v的字段个数
v.Field(i)  //指定索引的字段值
v.Method(i).Call(nil) //调用指定索引的方法, 传入参数nil

// Prinft和反射
func Printf(format string, args ... interface{}) (n int, err error) //...参数为空接口类型

// 获取v的类型
func typeof(v interface{}) string {
	return reflect.TypeOf(v).String()
}
