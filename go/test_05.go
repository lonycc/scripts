package main

import (
	"container/list"
	"fmt"
  "regexp"
)

// 双向链表
func testList() {
	lst := list.New()
	lst.PushBack(1)
	lst.PushBack(2)
	for e := lst.Front(); e != nil; e = e.Next() {
		fmt.Println(e.Value)
	}
}

// unsafe.Sizeof(1) 平台相关的, 32位系统返回4, 64位返回8

// 正则包
func testReg() {
	searchIn := "John: 2578.34 William: 4567.23 Steve: 5632.18" //要查找的字符串
	pat := "[0-9]+.[0-9]+" //模式
  
  ok, _ := regexp.Match(pat, []byte(searchIn))
  ok, _ := regexp.MatchString(pat, searchIn)
  
  re, _ := regexp.Compile(pat)
  str := re.ReplaceAllString(searchIn, "@@@") //将匹配到的部分都替换
  str2 := re.ReplaceAllStringFunc(searchIn, f) //匹配到的部分用函数f替换
}

// 锁机制, sync包
type Info struct {
  mu sync.Mutex
  name string
}

func Update(info *Info) {
  info.mu.Lock()
  info.name = "tony"
  info.mu.Unlock()
}

// 精密计算, math/big包
im = big.NewInt(math.MaxInt64) //声明整数
io = big.NewInt(1)
ip = big.NewInt(1990)
io.Mul(im, im).add(io, im).Div(io, ip)
rm = big.NewRate(math.MaxInt64, 1990) //声明有理数, 参数1为分子, 参数2为分母

// 自定义包和可见性
import "包的本地路径或URL地址"
import "./demo/myTest"  //从当前目录demo/myTest导入
import "project/demo"  //从$GOPATH/src/project/demo导入
import "github.com/xxx/yyy"  //先从远程下载到本地$GOPATH再导入
