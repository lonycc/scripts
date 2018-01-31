package main

fmt.Scan(a ...interface{}) (n int, err error) //扫描来自标准输入的文本, 空格分隔, 换行也算空格
fmt.Scan(&a, &b)
fmt.Scanln(a ...interface{}) (n int, err error)  //扫描来自标准输入的文本, 将空格分隔的值一次存放在后续参数内, 知道遇到换行
fmt.Scanf(format string, a ...interface{}) (n int, err error)  //格式化字符串, 决定如何读取
fmt.Scanf("%3s%d", &a, &b)
fmt.Sscan(str string, a ...interface{}) (n int, err error)  //第一个参数是输入字符串
fmt.Sscanf(str string, format string, a ...interface{}) (n int, err error)  //第一个参数是输入字符串, 第二个参数格式化输入字符串
fmt.Sscanf("10.0 / 10 / go", "%f / %d / %s", &a, &b, &c)
 Fscan(r io.Reader, a ...interface{}) (n int, err error) //从文件句柄中读取文本, 按空格分隔保存到后续参数内
 Fscanln(r io.Reader, a ...interface{}) (n int, err error) //同上, 但会在遇到换行时停止

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
// 如果写入内容很简单, 可直接 fmt.Fprintf(of, "some data\n"), 而无需创建ow; 或者也可of.WriteString("some data\n")
