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
var s1 []int = aa[1:3] //长度为len(s)=3-1=2, 容量cap(s1) = len(s)+数组aa除切片之外的长度=2+(5-3)=4
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


var (
	arr          = [...]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} // array
	slice0 []int = arr[3:7]
	slice1 []int = arr[:5]
	slice2 []int = arr[5:]
	slice3 []int = arr[:]
	slice4       = arr[:len(arr)-1]
	slice5       = make([]int, 10)
	slice6       = make([]int, 10, 10)
	arr2         = [][]int{
		[]int{1, 2, 3},
		[]int{12, 13},
		[]int{5, 6, 7, 8},
	}
)

func testSlice() {
	fmt.Println("----------------------------------")
	a := []int{1, 2, 3} // slice
	a[1] = 10
	fmt.Printf("a is %v\n", a)

	p := &a[2]
	*p += 100
	fmt.Printf("after p := &a[2]; *p += 100; a is %v\n", a)

	// make 用于创建内置引用类型map/slice/channel, new 用于创建值类型和用户自定义类型
	b := make([]int, 3) // make分配内存并初始化成员结构, 返回对象
	b[1] = 10
	fmt.Printf("make([]int, 3) is %v\n", b)

	c := new([]int) // new计算类型大小, 分配零值内存, 返回指针
	fmt.Printf("new([]int) is %v\n", c)

	d := [5]struct {
		x int
	}{}
	fmt.Printf("stuct array/slice %v\n", d)
	s := d[:]
	d[1].x = 10
	s[2].x = 100
	fmt.Printf("modified stuct array/slice is %v\n", d)
	fmt.Printf("&d=%p, &d[0]=%p, so &d == &d[0]\n", &d, &d[0])

	fmt.Printf("arr is %v, cap(arr)=%d\n", arr, cap(arr))
	fmt.Printf("slice0 := arr[3:7] is %v\n", slice0)
	fmt.Printf("slice1 := arr[:5] is %v\n", slice1)
	fmt.Printf("slice2 := arr[5:] is %v, cap(slice2)=%d\n", slice2, cap(slice2))
	fmt.Printf("slice3 := arr[:] is  %v\n", slice3)
	fmt.Printf("slice4 := arr[:len(arr)-1] is %v\n", slice4)
	fmt.Printf("slice5 := make([]int 10) is %v\n", slice5)
	fmt.Printf("slice6 := make([]int, 10, 10) is %v\n", slice6)
	s1 := []int{0, 1, 2, 3, 8: 15} // 通过初始化表达式构造, s1[8] = 15, s1[4/5/6/7] = 0
	d1 := s1[:2:3]   // d1是切片, 值为[0, 1], cap(s)=3
	d1.append(d1, 100, 200) //对d1扩容, 超出了cap(s), 切片扩容的规律通常是以2倍递增
	fmt.Printf("s1 is %v, len(s1)=%d, cap(s1)=%d\n", s1, len(s1), cap(s1))
	fmt.Printf("2-d slice arr2 is %v\n", arr2)
}


func main() {
  a := [...]string{"a", "b", "c", "d"} //数组
  b := []string{"a", "b", "c", "d"}  //切片
  m := make([]string, 10)
  c := [5]string{3: "Chris", 4: "Ron"} //数组, 只有索引3和4别赋值, 其他元素被设置为空
  
  n := copy(m, b) //将切片b复制到切片m, 返回b的长度n
  n2 := append(b, 'e', 'f', 'g') //切片b扩充e/f/g
  
  //字符串本质是一个字节数组, 字符串的内存结构: 一个指向实际数据的指针和记录字符串长度的整数, 占用两个字节
  bt := []byte("what")  // 中文字符需要用[]rune(str)
  // 应及时将所需数据 copy 到较小的 slice，以便释放超大号底层数组内存。的长度的部分会丢掉
  // 将"abc"复制到切片bt, bt的值变成[]byte("abct"), 超过bt原来
  copy(bt, "abc") 
  
  s := make([]byte, 3)
  bt = append(bt, s...)  // 切片bt后添加切片s
	
  // 切片resize
  c := bt[1:2]  // ["b"]
  d := c[0:3] // ["b", "c", "d"]
	
  // string底层就是byte数组, 故字符串可进行切片操作
  str := "hello world"
  s2: = str[0:5]
  
  // 字符串不可变, 需要转为数组后再改变指定索引的值
  
  // 排序和搜索
  sort.Ints(a)
  sort.Float64s(a []float64)
  sort.Strings(a []string)
  sort.IntAreSorted(a []int) bool
  sort.SearchFloat64s(a []float64, x float64) int
  sort.SearchStrings(a []string, x string) int
}

func testMap() {
  var mapLit map[string]int  //声明一个map
  mapLit = map[string]int{"one": 1, "two": 2} //赋值
  
  map2 := make(map[string]float32 [, cap])  //通过make()创建map, 容量参数可选
  
  mf := map[int]func() int { }  //map的值类型可以是函数
  
  map3 := make(map[int][]int) //值类型是切片
  map4 := make(map[int]*[]int) //值类型是切片的引用
  
  _, ok = map2[key] //如果存在key, 则ok为true
  delete(map2, key) //删除key
  
  // map是无序的, 若需要一个排序的列表, 使用结构体切片
  for key, value := range map1 {
  }
  
  type name struct {
    key string
    value string
  }
  
  // map类型切片, 通过索引使用切片的map元素
  items := make([]map[int]int, 5)
  for i:= range items {
    items[i] = make(map[int]int, 1)
    items[i][1] = 2
  }
}
