package main

import (
	"fmt"
)

func main() {
	fmt.Println("return:", a()) // 依次输出defer1: 1 defer2: 2 return: 0
	fmt.Println("return:", b()) // 依次输出defer1: 1 defer2: 2 return: 2
  fmt.Println("c return:", *(c())) // 依次输出defer1: 1 defer2: 2 return 2
  /*
  多个defer语句, 先声明的后执行; return最先执行, 负责把结果写入返回值; 接着defer执行, 最后函数带着当前返回值退出;
  */
}

// 无名返回值, 返回值是最先被赋值的, defer语句并没有修改返回值
func a() int {
	var i int
	defer func() {
		i++
		fmt.Println("defer2:", i) // 打印结果为 defer: 2
	}()
  
	defer func() {
		i++
		fmt.Println("defer1:", i) // 打印结果为 defer: 1
	}()
  
	return i
}

// 有名返回值, 返回值会被defer语句修改;
func b() (i int) {
	defer func() {
		i++
		fmt.Println("defer2:", i) // 打印结果为 defer: 2
	}()
  
	defer func() {
		i++
		fmt.Println("defer1:", i) // 打印结果为 defer: 1
	}()
  
	return i // 或者直接 return 效果相同
}

func c() *int {
	var i int
	defer func() {
		i++
		fmt.Println("defer2:", i) // 打印结果为 c defer: 2
	}()
	defer func() {
		i++
		fmt.Println("defer1:", i) // 打印结果为 c defer: 1
	}()
	return &i
}
