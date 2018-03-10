// 协程和通道, go利用goroutines处理并发, 利用channels同步goroutines.

// 在main函数里执行耗时任务, 可以加上go关键字, 就将以协程方式执行 
go longTimetask()
time.Sleep(2 * 1e9) //主进程中必须sleep足够的时间以等待协程任务执行完成

// 指定使用核心数量, 一个经验法则: GOMAXPROCS = 核心数 - 1
runtime.GOMAXPROCS(2)

// 声明channel, 未初始化的channel值为nil
var aa chan int
aa = make(chan int)
// or
aa := make(chan int)

// 流向通道(发送)
ch <- int1
// 从通道流出(接收)
int2 = <- ch
// 单独调用获取通道的值
fmt.Println(<-ch) 

// 通道阻塞, 只有生产者而无消费者时
c := make(chan int)
go func() {
	time.Sleep(1 * 1e9)
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
go func(c chan int) { c <- 10 }
doSth()
rs := <- c //等待协程完成
<- c //不返回

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

// 通道的方向
var send_only chan<- int
var recv_only <-chan int

func (in <-chan int, out chan<- string) {
	for inValue := in {
		result := inValue
		out <- result
	}
}

// 关闭通道, 仅当发送和接收通道不同步时要手工执行
close(ch)

// select 切换线程
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

// time.Tick(1e9)   //定时通道
// time.After(5e9)  //停止通道
// 协程和恢复recover, defer修饰的函数中, 用了recover来避免panic
// 使用通道处理异步任务, 而非互斥锁

// 惰性生成器
// 实现futures模式, 需要计算得到的变量用协程计算, 以实现并行
