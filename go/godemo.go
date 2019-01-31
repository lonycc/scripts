package main

import (
	"fmt"
	"github.com/PuerkitoBio/goquery"
	"log"
	"os"
	"runtime"
	"strconv"
	"strings"
	"math"
	"unicode"
	"unicode/utf8"
	"time"
	"net/url"
)

/* go命令行
 * go get github.com/<user>/<package> 相当于git clone之后再go install
 * go build [source.go]  测试编译, 生成可执行文件
 * go install            编译源代码以后安装到指定目录
 * go clean              清除编译生成的文件
 * go run [source.go]    编译并运行
 * go fmt [source.go]    格式化代码
 * go doc [source.go]    生成文档
 */

const MAX int = 3
var Pi float64
const beef, two, c = "eat", 2, "veg"
const (
	Monday, Tuesday, Wednesday = 1, 2, 3
	Thursday, Friday, Saturday = 4, 5, 6
)
// iota从0开始, 每遇到一次const重新置0
const (
	d = iota  // 0
	e  // 1
	f  // 2
)

type TZ int  // 类型别名
var ch byte = 65  // byte类型是uint8的别名
var ch_1 byte = '\x41'
var ch_2 byte = 'A'
var ch_3 int = '\u0041'
var ch_4 int = '\U00101234'

type HotsContent struct {
	num     int
	content string
	comment string
	url     string
}

// init函数在每个包完成初始化后自动执行, 比main优先级高
func init() {
	Pi = 4 * math.Atan(1)
}

// 测试url包, 获取绝对地址
func test_url() {
	uri := "12#aa-comment"
	line := "http://jandan.net/demo"
	base, _ := url.Parse(line)
	u, _ := url.Parse(uri)
	v := line.ResolveReference(uri)
	fmt.Println(base)
	fmt.Println(v)
}

func crawl(url string, page int) {
	fmt.Printf("开始爬取糗事百科热点笑话第%d页: %s\n", page, url)
	js, err := goquery.NewDocument(url)
	if err != nil {
		log.Fatal(err)
	}
	js.Find("#content-left .article").Each(func(i int, contentSelection *goquery.Selection) {
		//先判断是否有图片
		img, _ := contentSelection.Find(".thumb a").Attr("href")
		if len(img) == 0 {
			hotsArt := HotsContent{}
			content := contentSelection.Find(".content span").Text()
			url, _ := contentSelection.Find(".contentHerf").Attr("href")
			comment_name := contentSelection.Find(".cmtMain .cmt-name").Text()
			comment_cont := contentSelection.Find(".cmtMain .main-text").Text()
			hotsArt.num = i + 1
			hotsArt.url = "https://www.qiushibaike.com" + url
			hotsArt.content = strings.Replace(content, "\n", "", -1)
			hotsArt.comment = strings.Replace(comment_name+comment_cont, "\n", "", -1)
			fmt.Println("第", hotsArt.num, "个笑话:")
			fmt.Println("\t", hotsArt.content)
			fmt.Println("\t 最热评论:" + hotsArt.comment)
			fmt.Println("\t 地址", hotsArt.url)
			fmt.Println("======================================================")
		}
	})
	next := js.Find("a .next").Text()
	if next != "" {
		url = strings.Replace(url, strconv.Itoa(page), strconv.Itoa(page+1), -1)
		crawl(url, page+1)
	}
}

func swap(x *int, y *int) {
	var temp int
	temp = *x /* 保存 x 地址的值 */
	*x = *y   /* 将 y 赋值给 x */
	*y = temp /* 将 temp 赋值给 y */
}

func testStrings() {
	fmt.Println("test Contains es:  ", strings.Contains("test", "es"))
	fmt.Println("test Count t:     ", strings.Count("test", "t"))
	fmt.Println("test HasPrefix te: ", strings.HasPrefix("test", "te"))
	fmt.Println("test HasSuffix st: ", strings.HasSuffix("test", "st"))
	fmt.Println("test Index e:     ", strings.Index("test", "e"))
	fmt.Println("solomo last index o: ", strings.LastIndex("solomo", "o"))
	var r rune = 10  #rune是int32的别名
	fmt.Println("cn 中国", strings.IndexRune("cn 中国", r))
	fmt.Println("Join:      ", strings.Join([]string{"a", "b"}, "-"))
	fmt.Println("a Repeat 5:    ", strings.Repeat("a", 5))
	fmt.Println("foo Replace all o to 0:   ", strings.Replace("foo", "o", "0", -1))
	fmt.Println("foo Replace first o to 0:   ", strings.Replace("foo", "o", "0", 1))
	fmt.Println("a-b-c-d-e Split by -:     ", strings.Split("a-b-c-d-e", "-"))
	fmt.Println("TEST ToLower:   ", strings.ToLower("TEST"))
	fmt.Println("test ToUpper:   ", strings.ToUpper("test"))
	fmt.Println()
	fmt.Println("Len: ", len("hello"))
	fmt.Println("Char:", "hello"[1])
	// strings.TrimSpace(s)  去空白字符
	// strings.Trim(s, "\n")  去掉换行
	// strings.TrimLeft(s, "\n")
	// strings.TrimRight(s, "\n")
	// strings.Fields(s)  用空白符作为分隔符切割字符串, 返回slice
	// strings.Split(s, "@")
	// strings.Join(s1 [] string, sep string) string
	y, err := strconv.Atoi("fuck")  //string转int
	if err != nil {
		fmt.Println("y is ", y)
	}
	// strconv.Itoa(i int) string 返回数字i锁表示的字符串类型的十进制数
	// strconv.FormatFloat(f float64, fmt byte, prec int, bitSize int) string
}

func testDateTime() {
	t := time.Now()
	t.Day()
	t.Month()
	t.Year()
	week = 60 * 60 * 24 * 7 * 1e9  //纳秒
	t.Add(week)
	t.Format("2006-01-02 15:04:00")
	// time.Sleep(Duration d)
	// time.After
	// time.Ticker
}

/* int转uint8 */
func Uint8FromInt(n int) (uint8, error) {
	if 0 <=n && n <= math.MaxUint8 {
		return uint8(n), nil
	}
	return 0, fmt.Errorf("%d is out of the uint8 range", n)
}

/* float64转int */
func IntFromFloat64(x float64) int {
	if math.MinInt32 <= x && x <= math.MaxInt32 {
		whole, fraction := math.Modf(x)
		if fraction >= 0.5 {
			whole++
		}
		return int(whole)
	}
	panic(fmt.Sprintf("%g is out of the int32 range", x))
}

func main() {
	var a int = 3
	b := 10  // 这种声明方式只能在函数体内
	var ptr *int
	var pptr **int
	var ppptr ***int

	ptr = &a
	pptr = &ptr
	ppptr = &pptr

	fmt.Println("变量 a 的内存地址是：%p", &a)
	fmt.Printf("指针变量 *ptr = %d\n", *ptr)
	fmt.Printf("指向指针的指针变量 **pptr = %d\n", **pptr)
	fmt.Printf("***ppptr = %d\n", ***ppptr)

	if ptr == nil {
		fmt.Println("ptr 是空指针")
	}

	fmt.Printf("交换前 a 的值 : %d\n", a)
	fmt.Printf("交换前 b 的值 : %d\n", b)
	swap(&a, &b)
	fmt.Printf("交换后 a 的值 : %d\n", a)
	fmt.Printf("交换后 b 的值 : %d\n", b)


	var goarch string = runtime.GOARCH
	var goos string = runtime.GOOS
	var compiler string = runtime.Compiler
	path := os.Getenv("PATH")

	var env = fmt.Sprintf("the arch is %s, the os is %s, the compiler is %s, the path env is %s", goarch, goos, compiler, path)
	fmt.Println(env)

	fmt.Println(math.MaxUint8)
	fmt.Println(math.MaxInt64)

	var inta int = 6;
	var int64a int = 6;

	fmt.Println("int == int64 %t", inta == int64a)  // true, int与系统架构有关, int64则固定长度

	var c1 complex64 = 5 + 10i
	fmt.Printf("c1 is: %v \n", c1)  // %v表示已变量结构输出
	var c2 = complex(5, 10)
	fmt.Printf("c2 is: %v, the real part is %f, the imag part is %f \n", c2, real(c2), imag(c2))

	unicode.IsLetter(ch_1)
	unicode.IsDigit(ch_2)
	unicode.IsSpace(ch_3)
	len(goarch)  //字节个数
	utf8.RuneCountInString(goarch) //字符个数

	//slice := make([]string, 3)  /*声明切片, 初始长度为3*/
	//crawl("https://www.qiushibaike.com/hot/page/1/", 1)
}

/**
 * 变量/常量/函数如果以大写字母开头, 则可以被外部包导入
 *
 * 值类型和引用类型
 *
 * int float bool string 数组 结构 都是值类型, 使用这些类型的变量直接指向存在内存中的值
 * 值类型的变量的值存储在栈中, 用&取其内存地址
 *
 * 引用类型的变量存储的是该变量的值所在的内存地址, 或内存地址中第一个字节位置, 这个内存地址就是指针
 * 指针 slices maps channel 都是引用类型, 引用类型的变量存储在堆中
 *
 * 交换两个变量的值 a, b = b, a
 * _用于抛弃值 _, b = 5, 7
 */
