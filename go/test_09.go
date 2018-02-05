// 协程和通道, go利用goroutines处理并发, 利用channels同步goroutines.

// 在main函数里执行耗时任务, 可以加上go关键字, 就将以协程方式执行 
go longTimetask()
time.Sleep(2 * 1e9)
