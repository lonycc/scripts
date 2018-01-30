package main

// go没有类和继承的概念, 通过结构来实现面向对象的特性.
// 接口定义了一组方法[方法集], 但是这些方法不包含实现代码, 它们没有被实现[它们是抽象的], 接口里也不能包含变量.

type Namer interface {
    Method1(param_list) return_type
    Method2(param_list) return_type
    // ...
}
