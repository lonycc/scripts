# 记录go语言学习笔记

> 标准库手册[docs](https://gowalker.org/search?q=gorepos)

## test_01.go

- 程序基本结构和基本数据类型
  - 文件名、关键字、标识符
  - 变量、常量、基本类型、运算符
  - 字符串、strings和strconv包、时间和日期、指针
  
## test_02.go

- 控制结构
  - if-else
  - swtich-case
  - for
  - break 与 continue
  - 标签 与 goto

## test_03.go

- 函数
  - 函数参数、返回值、传递变长参数
  - defer关键字和追踪
  - 内置函数、递归函数
  - 将函数作为参数
  - 闭包、应用闭包(函数作为返回值)、使用闭包调试
  - 计算函数执行时间、内存缓存提升性能

## test_04.go

- 数组和切片
  - 数组和切片的声明/初始化
  - 切片的重组、复制、追加
  - 字符串、数组和切片的应用, 查找排序等

- map
  - map声明、初始化
  - map类型切片、map排序

## test_05.go

- 包
  - 标准包使用
  - 自定义包的导入、godoc、go install、go get、go test等

- 结构 struct 与方法 method
  - 结构体定义、实例
  - 带标签的结构体、匿名字段、内嵌结构体
  - 方法、通过接口实现多态
  - 类型的String()方法、垃圾回收和SetFinalizer

## test_06.go

- 接口和反射
  - 接口定义、接口嵌套接口
  - 类型断言、类型判断type-switch
  - 方法集与接口
  - 空接口、反射包
  - 接口与动态类型
  - 接口与面向对象

## test_07.go

- 读写数据
  - 标准输入/输出/错误
  - 文件读写/缓冲读写
  - json/xml/gob数据格式
  - go密码学
