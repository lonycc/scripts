package main

import (
	"fmt"
)

func main() {

	// if分支中可以初始化变量
	if a := 3; condition1 {
		//
	} else if condition2 {
		//
	} else {
		//
	}
	// case a: fallthrough 执行完该分支会继续执行下面的分支
	// case b: 空分支
	switch v {
	case val1:
		//
	case val2, val3:
		//
	default:
		//
	}

	switch {
	case i < 0:
		f1()
	case i == 0:
		f2()
	case i > 0:
		f3()
	}
	// for 初始化语句; 条件语句; 修饰语句 {} 其中初始化语句/修饰语句可以省略
  for i, j := 10, 20; i < 10; i++ {
  
  }
  // for语句块, 无限循环, 在语句块里控制退出
  for {
    i:=1
    i++
    if i > 10 {
      return    // 直接返回, 退出函数
      // break  退出该次循环体
    }
  }
  
  for i < 10 {
  }
  // for-range
  for pos, char := range str {
  }
  
  // label可配合for/switch/select结构
  goto LABEL  //保证label在goto之后
  continue LABEL //跳过下面的语句回到LABEL标签处
  break LABEL  //直接退出循环

}
