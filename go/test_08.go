package main

// go中错误处理defer-panic-and-recover
// 产生错误的函数返回两个变量, 一个值和一个错误码; 如果后者是nil就成功
// 调用函数时必须检查返回值

type error interface {
  Error() string
}

var errNotFound error = errors.New("Not found error") //声明一个错误变量
var err error = fmt.Errorf("math: square root of negative number %g", -5);

panic("error, quit")  //抛出一个runtime.Error接口类型的错误, 退出程序

// recover只能在defer修饰的函数中使用, 用于取得panic调用中传递过来的错误值
func badCall() { panic("bad end") }

func test() {
	defer func() {
		if e := recover(); e != nil {
			fmt.Printf("Panicing %s\r\n", e)
		}
	}()
	badCall() //执行了Panicing bad end就退出
	fmt.Printf("After bad call\r\n") //这里不会执行
}
