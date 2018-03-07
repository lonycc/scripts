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
