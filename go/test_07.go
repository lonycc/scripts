package main

fmt.Scan(a ...interface{}) (n int, err error) //扫描来自标准输入的文本, 空格分隔, 换行也算空格
fmt.Scan(&a, &b)
fmt.Scanln(a ...interface{}) (n int, err error)  //扫描来自标准输入的文本, 将空格分隔的值一次存放在后续参数内, 知道遇到换行
fmt.Scanf(format string, a ...interface{}) (n int, err error)  //格式化字符串, 决定如何读取
fmt.Scanf("%3s%d", &a, &b)
fmt.Sscan(str string, a ...interface{}) (n int, err error)  //第一个参数是输入字符串
fmt.Sscanf(str string, format string, a ...interface{}) (n int, err error)  //第一个参数是输入字符串, 第二个参数格式化输入字符串
fmt.Sscanf("10.0 / 10 / go", "%f / %d / %s", &a, &b, &c)
fmt.Fscan(r io.Reader, a ...interface{}) (n int, err error) //从文件句柄中读取文本, 按空格分隔保存到后续参数内
fmt.Fscanln(r io.Reader, a ...interface{}) (n int, err error) //同上, 但会在遇到换行时停止

func Fprintf(w io.Writer, format string, a ...interface{}) (n int, err error) //常用io.Writer有os.Stdout/os.Stderr/os.File

os.Stdin  //标准输入
os.Stderr //标准错误
os.Stdout //标准输出

var inputReader *bufio.Reader = bufio.NewReader(os.Stdin)  //创建一个读取器, 绑定标准输入
input, err = inputReader.ReadString('\n')  //获取标准输入, 遇到\n结束

file, err = os.Open("input.dat") //文件读取
defer file.Close() //延后关闭文件句柄
ir := bufio.NewReader(file) //读取器绑定文件句柄
for {
  line, err = ir.ReadString('\n')
  if err == io.EOF {
    return
  }
}

import "io/ioutil"
buf, err = ioutil.ReadFile("a.txt") //buf的类型为[]byte
string(buf) //将[]byte转为string
err = ioutil.WriteFile("b.txt", buf, 0644) //将buf以0644的权限模式写入b.txt
if err != nil {
  panic(err.Error()
}

// 带缓冲的读取
buf := make([]byte, 1024)
n, err := inputReader.Read(buf)
strArr = append(strArr, "demo") //在字符串数组strArr里追加元素demo

// 文件路径相关
import "path/filepath"
filename := filepath.Base("/usr/local/src/demo.sh")  //获取文件名, 返回demo.sh
filepath.Ext("index.go") //获取后缀名
filepath.IsAbs(path string) (b bool)  //给定路径是否是绝对路径
filepath.Dir("/usr/local/src/demo.sh")  //获取所在目录, 返回/usr/local/src
filepath.Join(elem ...string) string   //获取绝对路径
filepath.Join("/usr/local", "src", "demo.sh")  //返回/usr/local/src/demo.sh
filepath.Match（pattern, name string) (matched book, err error)  //路径是否匹配模式

// 读取压缩文件
import "compress/gzip"
fi, err := os.Open("abc.gz")
fz, err := gzip.NewReader(fi)
if err != nil {
  r := bufio.NewReader(fi)
} else {
  r := bufio.NewReader(fz)
}

// 写文件, os.O_RDONLY 只读; os.O_WRONLY 只写; os_O_CREATE 创建; os.O_TRUNC 截断;
of, err := os.OpenFile("output.dat", os.O_WRONLY|os.O_CREATE, 0666)
defer of.Close()
ow := bufio.NewWriter(of)
ow.WriteString("hello demo")
ow.Flush()
// 如果写入内容很简单, 可直接 fmt.Fprintf(of, "some data\n"), 而无需创建ow; 或者也可of.WriteString("some data\n"); 或者直接输出到标准输出os.Stdout.WriteString("hello")

// 文件复制
io.Copy(dst Writer, src Reader) (written int64, err error)
io.CopyBuffer(dst Writer, src Reader, buf []byte) (written int64, err error)

// 从命令行读取参数
os.Args // 切片变量, 命令行参数保存在这个变量里; os.Args[0]为程序本身名字, os.Args[1:]为用户参数
 
// flag包
var a = flag.Bool("n", false, "print ha")  //输出 -n flag, 是一个*bool类型变量
flag.PrintDefaults()  //打印flag使用帮助
flag.Parse()  //扫描命令行参数列表并设置flag
flag.Arg(i) //第i个参数
flag.NArg()  //参数个数
flag.VistiAll(fn func(*Flag)) //按字典顺序遍历flag
 
// 通过buffer读取并打印
var r *bufio.Reader
buf, err := r.ReadBytes('\n')
fmt.Fprintf(os.Stdout, "%s", buf)
 
// 用切片读写文件
func cat(f *os.File) {
	const NBUF = 512
	var buf [NBUF]byte
	for {
		switch nr, err := f.Read(buf[:]); true {
		case nr < 0:
			fmt.Fprintf(os.Stderr, "cat: error reading: %s\n", err.Error())
			os.Exit(1)
		case nr == 0: // EOF
			return
		case nr > 0:
			if nw, ew := os.Stdout.Write(buf[0:nr]); nw != nr {
				fmt.Fprintf(os.Stderr, "cat: error writing: %s\n", ew.Error())
			}
		}
	}
}
 
// json数据格式
import "encoding/json" 
js, _ := json.Marshal(v interface{}) ([]byte, error)  //序列化
json.MarshalforHtml(v interface{}) ([]byte, error)  //过滤了xss
enc : = json.NewEncoder(w io.Writer) *Encoder  //编码流
err := enc.Encode(v interface{}) error

dec := json.NewDecoder(r io.Reader) *Decoder
err := dec.Decode(v interface{}) error

 json.Unmarshal(data []byte, v interface{}) error //反序列化
var f interface{}
err := json.Unmarshal(js, &f)
 
json.NewDecoder(r io.Reader) *Decoder //解码流
json.NewEncoder(w io.Writer) *Encoder //编码流

// xml数据格式
import "encoding/xml"

// gob传输数据
import "encoding/gob"

// 加密解密相关
import "crypto/sha1" 
hasher := sha1.New()  // 创建一个hash.Hash对象
io.WritString(hasher, "test")
b : = []byte{}
hasher.Sum(b)

hasher.Reset()
n, err := hasher.Write([]byte("what about"))
checksum := hasher.Sum(b)
	
