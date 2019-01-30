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

// 自定义包中的错误处理和panicking
// 1. 在包内部, 总是应该从panic中recover, 不允许显示的超出包范围的panic.
// 2. 向包的调用者返回错误值, 而非panic

// 一种闭包处理错误的模式, 所有函数都是同一种签名时
fType1 = func f(a type1, b type2)

func check(err error) { if err != nil { panic(err) } }

func errorHandler(fn fType1) fType1 {
	return func(a type1, b type2) {
		defer func() {
			if err, ok := recover().(error); ok {
				log.Printf(“run time panic: %v”, err)
			}
		}()
		fn(a, b)
	}
}

// 启动外部命令和程序
env := os.Environ()
procAttr = &os.ProcAttr{
	Env:env,
	Files: []*os.Files{
		os.Stdin,
		os.Stdout,
		os.Stderr,
	},
}
pid, err := os.StartProcess("/bin/ls", []string{"ls", "-al"}, procAttr)

cmd := exec.Command("ls", "-al")
err = cmd.Run()

// go中的单元测试和基准测试
// 单元测试执行 go test fmt_test.go --chatty
// 基准测试执行 go test -test.bench=.*
import testing

func TestFuncName(t *testing.T)
func BenchmarkReverse(b *testing.B)

// 性能调试
