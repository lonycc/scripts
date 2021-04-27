package main

import (
	"fmt"
	"os"
    "os/signal"
    "syscall"
    "time"
)

// 处理退出信号
func SetupCloseHandler() {
	c := make(chan os.Signal, 2)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	go func() {
		<-c
		fmt.Println("\n rain stopped")
		os.Exit(0)
	}()
}

func main() {
	fmt.Println("god: let it rain")  // 神说：要下一场雨才好
	fmt.Println("coder: bit rain")  // 程序员：那就来一场二进制雨

	SetupCloseHandler()

	time.Sleep(2 * time.Second)

	c := make(chan int)

	// 消费
	go func() {
		for {
			fmt.Print(<-c, " ")
		}
	}()

	// 生产
	for {
		select {
		case c <- 0:
		case c <- 1:
		}
	}

}
