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

**bufio包的使用**

```
func testBufio() {
	counts := make(map[string]int)
	input := bufio.NewScanner(os.Stdin)
	for input.Scan() {
		counts[input.Text()]++
	}
	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d\t%s\n", n, line)
		}
	}
	fmt.Println(counts)
}
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

**云原生与微服务**

```
go-micro rpc框架, 抽象出了分布式系统的细节
service discovery(服务发现)  负责微服务的自动注册和名字解析
load balancing(负载均衡)  基于服务发现,智能的客户端负载均衡
synchronous comms(同步通信) 对基于rpc通信的双向流的支持
asynchronous comms(异步通信) 事件驱动架构的发布订阅接口
message encoding(消息编码)  基于内容类型如protobuf和json的动态编码
service interface(服务接口) 所有特性都封装在简单的高级接口

go-micro 模块分解
transport  服务间的同步请求/响应
broker  异步通信的消息代理
codec 请求响应编码, json/protobuf/bson/msgpack等, 支持rpc格式json-rpc/proto-rpc
registry  服务发现
selector 负载均衡
client  发送请求, rpc客户端
server  处理请求, rpc服务端

micro 云原生应用开发工具集
api gateway 轻量级网关/代理, 用于将http请求转为rpc请求
cli  命令行接口
sidecar  非go-micro应用的http代理
web ui/proxy 可视化查看服务


IaaS: 基础设置服务, 提供基础资源如服务器/存储/网络; 商业方案有AWS / Digital Ocean / vSphere, 开源的有OpenStack;
PaaS: 平台服务, 提供应用开发/运行环境; 商业方案有GAE / OpenShift / Heroku; 开源的有Deis / OpenShift;
SaaS: 软件服务, 提供直面用户的互联网服务; 比如Dropbox / Google Apps / Facebook / Twitter / Instagram;

服务网格 Service Mesh, 在Kubernetes上践行微服务架构进行服务治理所必须的组件;
无服务器架构 Serverless, 以Faas为代表;

虚拟化是通过软件手段对计算机硬件资源镜像整合管理和再分配的一种技术。最常用的就是基于虚拟机（Hypervisor-based）的虚拟化，它通过一个软件层的封装，提供和物理硬件相同的输入输出表现，实现了操作系统和计算机硬件的解耦，将OS和计算机间从1对1变成了多对多（实际上是1对多）的关系。该软件层称为虚拟机管理器（VMM/Hypervisor），它可以直接运行在裸机上（Xen、VMware EXSi），也可以运行在操作系统上（KVM、VMware workstation）。
基于虚拟机的虚拟化方案存在一个缺陷，在虚拟机上运行了一个完整的OS（GuestOS），在其下执行的还有虚拟化层和宿主机OS，比直接在物理机上运行相当的服务性能差。而且有GuestOS的存在，虚拟机镜像大至几G到几十G，占用存储空间，便携性差，迁移时通信代价大，不便于集群管理。想要增加硬件资源，需要启动新的虚拟机，要等待GuestOS启动，耗时几分钟。
Docker容器技术，基于Linux内核的两个机制：Cgroups(实现资源按需分配)和Namespace(实现任务隔离)。多个容器共用一个OS内核，容器内只包含应用和runtime，因此容器大小通常只有几十到几百M，轻量便携，启动速度快，更高密度的存储和使用，更方便集群管理。
```
