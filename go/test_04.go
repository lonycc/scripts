package main

// 数组声明, 数组也是值类型
var identifier [len] type

// 声明数组的两种方式, 区别在于aa的类型是[3]int, bb的类型是*[3]int
var aa [5]int
var bb = new([3]int)

// 多维数组
var cc = [3][4]int

// 将数组传递给函数, 为避免消耗过多内存, 可以传递数组的指针或使用数组的切片

// 切片是对数组一个连续片段的引用, 提供了一个相关数组的动态窗口, 因此切片可看作长度可变的数组.切片的容量
var identifier []type
var s1 []int = aa[1:3] //长度为len(s)=3-1=2, 容量cap(s1) = len(s)+数组aa除切片之外的长度=2+3=5
var s2 []int = [3]int{1,2,3}[:]
var s1 = s1[1:] //切片可后移, 不可前移

// 将切片传递给函数, 而非数组

// 用make()创建一个切片
var dd = make([]int, 10)
var ee = make([]int, 5, 10) //长度为5, 容量为10
var ff = new([5]int{1,3,5,7,9})[:2]

// new()和make()的区别
// new(T)返回一个指向类型为T, 值为0的地址的指针, 适用于数组和结构体; make(T)返回一个类型为T的初始值, 适用于切片/map/channel;
// 多维切片, 内层切片必须单独分配

// bytes包, 专门用于处理[]byte类型的切片
var buffer bytes.Buffer
var r *butes.Buffer = new(bytes.Buffer)
func newBuffer(buf []byte) *Buffer

// for-range结构
for k,v := range array1
for k,v := range slice1
for _,v = range array1
for k = range slice1

// 切片重组
s1 = s1[0, len(s1)+1]

func main() {
  a := [...]string{"a", "b", "c", "d"} //数组
  b := []string{"a", "b", "c", "d"}  //切片
  m := make([]string, 10)
  c := [5]string{3: "Chris", 4: "Ron"} //数组, 只有索引3和4别赋值, 其他元素被设置为空
  
  n := copy(m, b) //将切片b复制到切片m, 返回b的长度n
  n2 := append(b, 'e', 'f', 'g')
}
