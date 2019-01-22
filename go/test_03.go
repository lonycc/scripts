package main

import (
	"fmt"
)

//函数参数、返回值以及它们的类型被统称为函数签名

func main() {
	f1(a, b, c int)
	f2(a, b int) (int, int, int)
	f1(f2(a, b))  //函数返回值作为参数

	// go不支持函数重载, 不支持泛型

	type binOp func(int, int) int  //函数类型
  
  	arr := []int{7,9,3,5,1}
	x = min(arr...)  // func min(a ...int) int {}
  
}

//函数形参一般都有名字, 但也可以定义无名字的形参, 没有形参的函数称为niladic函数, 如main.main()
func f(int, int, float64) {
  return
}

// go默认按值传递参数, 也就是传递参数的副本. 使用变量可能会本副本进行修改, 但不影响原变量, 如f(arg).
// 引用传递, f(&arg). 传递给函数的是一个指针, 会修改原变量的值. 引用传递消耗的内存比按值传递少

// 命名返回值
func f2(i int) (x int, y int) {
  x = 2 * i
  y = 3 * i
  return
}

// 非命名返回值, 不推荐
func f3(i int) (int, int) {
  return 2 * i, 3 * i
}

// 如果使用引用传递, 函数可修改外部变量, 可以不用return
func f4(a, b int, reply *int) {
  *reply = a * b
}

//...type形式的参数, 可以传递变长参数, 下例arg是类似slice的参数
func f5(a, b, arg ...int) {
  
}

// 传递struct参数
F1(a, b, Options {par1:val1, par2:val2})

// defer 推迟执行, 一般用于函数执行完后的收尾工作
// 多个defer行为被注册时, 会逆序执行
// defer代码追踪, 在进入和离开某个函数时打印信息
defer file.Close()
mu.Lock()
defer mu.Unlock()

// 递归函数之间可以互相调用

// 将函数作为参数
func f5() {
	asciiOnly := func(c rune) rune {
		if c > 127 {
			return ' '
		}
		return c
	}
	fmt.Println(strings.Map(asciiOnly, "Jérôme Österreich"))
}

// 匿名函数, 也称为闭包, 常配合defer关键字, 用于改变函数的命名返回值
fplus := func(x, y int) int { return x + y }
fplus(2, 4)
func(x, y int) int { return x + y } (2, 4)  //直接调用

// 将函数作为返回值, 调用方式 f := Adder(1); f(3);
func Adder(a int) func(b int) int {
	return func(b int) int {
		return a + b
	}
}

// 闭包的另一种写法, 变量在函数体内声明, 调用方式 f = Adder(); f(1); f(20); f(200); 分别返回1/21/221
// 闭包函数保存并积累其中的变量的值, 不管外部函数退出与否, 它都能够继续操作外部函数中的局部变量. 在这里外部函数值的是f
func Adder() func(int) int {
	var x int
	return func(delta int) int {
		x += delta
		return x
	}
}

// 使用闭包调试
where := func() {
	_, file, line, _ := runtime.Caller(1)
	log.Printf("%s:%d", file, line)
}
where()
// some code
where()
// some more code
where()

// 计算执行时间
start := time.Now()
// some code
end := time.Now()
delta := end.Sub(start)

// 通过内存缓存提升性能, 避免重复计算, 将重复利用的计算结果存入数组, 比如计算斐波那契数列
var fibs [41] uint64

// defer语句的用法
func a() {
	db := sql.connect()
	defer db.close()  //在函数返回前执行关闭连接操作
}

// 在外围函数返回时遵循"先进后出"顺序, 类似于stack, 本例输出3210
func b() {
	for i := 0; i < 4; i++ {
		defer fmt.Print(i)
	}
}

// defer函数会读取并赋值外围函数的命名返回值, 本例会返回3
func c() {
	defer func() { i++ }()
	return 2
}

// panic用法
