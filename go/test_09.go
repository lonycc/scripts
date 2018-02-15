// 协程和通道, go利用goroutines处理并发, 利用channels同步goroutines.

// 在main函数里执行耗时任务, 可以加上go关键字, 就将以协程方式执行 
go longTimetask()
time.Sleep(2 * 1e9)

// 指定使用核心数量, 一个经验法则: GOMAXPROCS = 核心数 - 1
runtime.GOMAXPROCS(2)

// 声明channel, 未初始化的channel值未nil
var aa chan int
aa = make(chan int)
// or
aa := make(chan int)

//流向通道(发送)
ch <- int1
//从通道流出(接收)
int2 = <- ch
//单独调用获取通道的值
<- ch 
