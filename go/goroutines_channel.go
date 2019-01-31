// 协程和通道, go利用goroutines处理并发, 利用channels同步goroutines.

import "fmt"

// 只读channel声明
var 变量名 <-chan 类型

// 只写channel声明
var 变量名 chan<- 类型

// 函数接收一个只写通道作为参数
func readFromChannel(input <-chan string) {}
// 函数返回通道
func getChannel() chan bool {
	return make(chan bool)
}

func testChann() {
	/* channel, 用于多个 goroutine 通讯
	   a. 类似unix中管道（pipe）
	   b. 先进先出, 类似队列
	   c. 线程安全，多个goroutine同时访问，不需要加锁
	   d. channel是有类型的，一个整数的channel只能存放整数
	*/
	c1 := make(chan int)    // 无缓冲, 同步
	c2 := make(chan int, 1) // 有缓冲, 非同步
	go func() { c1 <- 1 }()  // 流向通道, 写入
	a := <-c1               // 流出通道, 读取
	fmt.Printf("len(c1)=%d, cap(c1)=%d\n", len(c1), cap(c1))
	
	defer close(c1)  // 关闭通道
	if b, ok := <-c1; ok {
		// 判断c1是否关闭
	}
		
	c2 <- 2
	fmt.Println(<-c2)
	
	c := make(chan int, 3)
	var send_c chan<- int = c //只写
	var recv_c <-chan int = c //只读
	
	r := make(<-chan string)   // 只读通道
	w := make(chan<- []os.FileInfo)  //只写通道
	c3 = make(chan<- chan bool)   //只写通道, 其值类型是另一个通道
	
	send_c <- 1
	if val, ok := <-recv_c; ok {
		fmt.Println(val)
	}
}


// 在main函数里执行耗时任务, 可以加上go关键字, 就将以goroutines方式执行 
go longTimetask()
time.Sleep(2 * 1e9) //主进程中必须sleep足够的时间以等待goroutines任务执行完成

// 指定使用核心数量, 一个经验法则: GOMAXPROCS = 核心数 - 1
runtime.GOMAXPROCS(2)

// 声明channel, 未初始化的channel值为nil
var aa chan int
aa = make(chan int)
// or
aa := make(chan int)

// 流向通道
ch <- int1
// 从通道流出
int2 = <- ch
// 单独调用获取通道的值
fmt.Println(<-ch) 

// 通道阻塞, 只有生产者而无消费者时
c := make(chan int)
go func() {
	time.Sleep(1e9)
	x := <-c
	fmt.Println("received", x)
}()
fmt.Println("sending", 10)
c <- 10
fmt.Println("sent", 10)

// 带缓冲的通道
ch1 := make(chan string, buffer_size)

// 在缓冲满载（缓冲被全部使用）之前，给一个带缓冲的通道发送数据是不会阻塞的，而从通道读取数据也不会阻塞，直到缓冲空了。
// 如果容量是0或者未设置，通信仅在收发双方准备好的情况下才可以成功。

// 使用通道让main程序等待协程完成, 即信号量模式
c := make(chan int)
go func(c chan int) { c <- 10 }()
doSth()
rs := <- c //等待协程完成
<-c //不返回

// 并行for循环
for i, j := range data {
	go func(i, j int){ doSth(i, j) }(i, j) //立即执行匿名函数
}

// 通道工厂模式, 不将通道作为参数传递给协程, 而用函数来生成一个通道并返回(工厂角色)
stream := pump() //生成一个通道, 函数内有个匿名函数被协程调用
go suck(stream)

// 生产者消费者模式
for {
	Consume(Produce())
}

func (in <-chan int, out chan<- string) {
	for inValue := in {
		result := inValue
		out <- result
	}
}()

// 关闭通道, 仅当发送和接收通道不同步时要手工执行
close(ch)

// select 切换通道, case条件生效仅当通道可操作
for {
	select {
	case c := <- ch1:
		//...
	case c := <- ch2:
		//...
	default:
		//...
	}
}

tick := time.Tick(1e9)   //定时通道
boom := time.After(5e9)  //停止通道
for {
	select {
	case <-tick:
		fmt.Println("tick")
	case <-boom:
		fmt.Println("boom")
		return
	default:
		time.Sleep(1e9)
	}
}

// 协程和恢复recover, defer修饰的函数中, 用了recover来避免panic
// 使用通道处理异步任务, 而非互斥锁

// 惰性生成器
// 实现futures模式, 需要计算得到的变量用协程计算, 以实现并行
