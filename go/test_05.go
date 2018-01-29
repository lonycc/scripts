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


// 结构体, 可看做类的简化形式
type identifier struct {
  field1 type1
  field2 type2
  field3 map[type]*field3
  //...
}
var t *T = new(T) //struct as a pointer
t.field1 = xx
(*t).field2 = yy

var t T  // struct as a value type
t.field1 = 5

t := &T{10, "Chris"} //struct-iteral

// 二叉树结构
type Btree struct {
  pri *Node
  data float64
  su *Node
}


type File struct {
  fd      int     // 文件描述符
  name    string  // 文件名
}

//工厂方法以new/New开头
func NewFile(fd int, name string) *File {
  if fd < 0 {
    return nil
  }
  return &File{fd, name}
}

f := NewFile(10, "./test.txt")  //实例化

//对于结构体 type A struct { a, b int} 可以使用y := new(A) 不能使用 y := make(A)
//对于结构体 type B map[string]string 可以使用y := make(B) 不能使用 y := new(B)

// 带标签的结构体
type TagType struct { // tags
  field1 bool   "An important answer"
  field2 string "The name of the thing"
  field3 int    "How much there are"
}

func refTag(tt TagType, ix int) {
  ttType := reflect.TypeOf(tt)
  ixField := ttType.Field(ix)
  fmt.Printf("%v\n", ixField.Tag)
}

// 匿名字段
type innerS struct {
  in1 int
  in2 int
}

type outerS struct {
  b int
  c float32
  int  //匿名字段
  innerS  //匿名字段
}

// 定义方法
func (recv receiver_type) methodName(parameter_list) (return_value_list) { ... }

// 方法和函数的区别: 函数将变量作为参数, function(recv); 方法在变量上被调用, recv.method()
