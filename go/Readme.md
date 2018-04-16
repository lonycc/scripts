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

**golang 交叉编译**

`CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build hello.go`

`CGO_ENABLED=1 GOOS=linux GOARCH=386 go build hello.go`

`GOOS=linux GOARCH=arm go build hello.go`

`GOOS=windows GOARCH=amd64 go build hello.go`

`GOOS=windows GOARCH=386 go build hello.go`

`GOOS=darwin GOARCH=amd64 go build hello.go`

`GOOS=darwin GOARCH=386 go build hello.go`

> 其中CGO_ENABLED配置表示是否用C语言版本的GO编译器执行编译; GOOS表示目标系统, GOARCH表示目标架构;

**makefile**

```
GOCMD=go
GOBUILD=$(GOCMD) build
GOCLEAN=$(GOCMD) clean
GOTEST=$(GOCMD) test
GOGET=$(GOCMD) get
BINARY_NAME=mybinary
BINARY_UNIX=$(BINARY_NAME)_unix

all: test build
build:
        $(GOBUILD) -o $(BINARY_NAME) -v
test:
        $(GOTEST) -v ./...
clean:
        $(GOCLEAN)
        rm -f $(BINARY_NAME)
        rm -f $(BINARY_UNIX)
run:
        $(GOBUILD) -o $(BINARY_NAME) -v ./...
        ./$(BINARY_NAME)
deps:
        $(GOGET) github.com/markbates/goth
        $(GOGET) github.com/markbates/pop


# 交叉编译
build-linux:
        CGO_ENABLED=0 GOOS=linux GOARCH=amd64 $(GOBUILD) -o $(BINARY_UNIX) -v
docker-build:
        docker run --rm -it -v "$(GOPATH)":/go -w /go/src/bitbucket.org/rsohlich/makepost golang:latest go build -o "$(BINARY_UNIX)" -v
```

**glide工具**

glide init #初始化

glide install #安装依赖

glide up #升级依赖

glide get github.com/xxx/yyy  #获取依赖

glide mirror set golang.org/x/crypto github.com/golang/crypto #设置镜像

glide mirror set golang.org/x/sys github.com/golang/sys

glide mirror remove golang.org/x/crypto  #移除镜像

GLIDE_HOME 默认 $HOME/.glide

glide --home [path]  #设置glide_home

cat $HOME/.glide/mirrors.yaml

```
repos:
- original: https://golang.org/x/crypto
  repo: https://github.com/golang/crypto
- original: https://golang.org/x/crypto/acme/autocert
  repo: https://github.com/golang/crypto
  base: golang.org/x/crypto
- original: https://golang.org/x/sys/unix
  repo: https://github.com/golang/sys
  base: golang.org/x/sys
- original: https://golang.org/x/net
  repo: https://github.com/golang/net
- original: https://golang.org/x/oauth2
  repo: https://github.com/golang/oauth2
- original: https://golang.org/x/sync
  repo: https://github.com/golang/sync
- original: https://golang.org/x/tools
  repo: https://github.com/golang/tools
- original: https://golang.org/x/time
  repo: https://github.com/golang/time
- original: https://google.golang.org/grpc
  repo: https://github.com/grpc/grpc-go
- original: https://google.golang.org/cloud
  repo: https://github.com/GoogleCloudPlatform/gcloud-golang
```


**上下文模块context**

```
type Context interface {
    // context被取消或超时时返回一个关闭的channel
    Done() <-chan struct{}
    // context取消的原因
    Err() error
    // context将被取消的时间
    Deadline() (deadline time.Time, ok bool)
    // context相关数据或nil
    Value(key interface{}) interface{}
}

// Backgroud()是所有context的root, 不能被cancel
func Background() Context

// 返回一个继承的context, 这个context在父context的Done被关闭时(或者在自己被cancel时)关闭自己的Done通道; 同时还返回一个取消函数cancel, 用于取消当前context
func Withcancel(parent Context) (ctx context, cancel CancelFunc)

// 
func withTimeout(parent Context, timeout time.Duration) (Context, CancelFunc) {
    return WithDeadline(parent, time.Now().Add(timeout))
}
```

**golang/flag包**

```
cmd -flag  //只支持bool类型
cmd -flag=x
cmd -flag x  //只支持非bool类型
```
以上语法对一个`-`或两个`-`效果一致; 对于int flag, 合法的值可以为1234, 0664, 0x1234或负数; 对于bool flag, 合法的值可以为1, 0, t, f, true, false, TRUE, FALSE, True, False等;

```
// 第一个参数为flag名称, 第二个为flag默认值, 第三个为说明
// flag.String(), flag.Bool(), flag.Int(), 返回的是变量引用
var f = flag.Int("flagname", 1234, "help message")

// 通过flag.XxxVar()将flag绑定到一个变量
var flagvar int
flag.IntVar(&flagvar, "flagname", 1234, "help message")

// 通过flag.Var()绑定自定义类型, 自定义类型需实现Value接口
flag.Var(&flagVar, "name", "help message")

// 解析命令行参数到定义的flag
flag.Parse()
args := flag.Args()
```


**docker容器化部署golang项目**
```
# 拉取centos基础镜像
docker pull centos:7.4.1708
# 创建并进入容器
docker run -p 8888:80 --name godocker -e ENV="dev" -it [image_id or image_name] /bin/bash
# 退出容器
exit

# 项目构建, 会在项目目录下生成一个与项目目录名同名的二进制文件
cd /path/to/project_name
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o project_name -v
# 将二进制文件拷贝到容器指定目录
docker cp /path/to/project_name/project_name godocker:/var/www/

# 将容器转为镜像
docker commit -m "提交信息" -a "附加信息" [container_id or container_name] tony/centos-go:1.0.0
# 镜像打包
docker save -o /path/to/centos-go-1.0.0.tar [container_id or container_name]
# 删除镜像
docker rmi [container_id or container_name]
# 恢复镜像
docker load < /path/to/centos-go-1.0.0.tar
# 启动上一步恢复的镜像
docker run -it [image_id or image_name] /bin/bash
```
