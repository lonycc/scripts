# 记录go语言学习笔记

> 标准库手册[docs](https://gowalker.org/search?q=gorepos)

[xorm](http://xorm.io/docs)

[gorm](http://gorm.io/docs/index.html)


**golang 交叉编译**

`CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build hello.go`

`CGO_ENABLED=1 GOOS=linux GOARCH=386 go build hello.go`

`GOOS=linux GOARCH=arm go build hello.go`

`GOOS=windows GOARCH=amd64 go build hello.go`

`GOOS=windows GOARCH=386 go build hello.go`

`GOOS=darwin GOARCH=amd64 go build hello.go`

`GOOS=darwin GOARCH=386 go build hello.go`

> 其中CGO_ENABLED配置表示是否用C语言版本的GO编译器执行编译; GOOS表示目标系统, GOARCH表示目标架构;

**GOGC 环境变量**

`GOGC = 新分配对象 / 上次 GC 后剩余对象`

> 默认100(%), 表示新分配对象数量等于上次GC后剩余对象数量时, 进行GC;

> 启动一个GO程序时, 设置`GODEBUG=gctrace=1`打印GC日志;

**import "runtime/debug"**

> `func FreeOSMemory()` 释放系统内存

> `func SetGCPercent(percent int) int` 设置GC触发比例值, 返回之前的值;

> `func SetMaxStack(bytes int) int` 设置单个goroutine堆栈能使用的最大内存数值, 返回之前的值, 初始为1GB/64bit系统, 250MB/32bit系统;

> `func SetMaxThreads(threads int) int` 设置go程序最大能跑的系统线程数, 返回之前的值, 初始为10000线程;


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
args := flag.Args()  // flag绑定之外的参数, 比如  go run t.go -a xx -b yy aa bb,  args是一个数组,只能获取到[aa bb]
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


**go引用**
```
import math/rand   //实际引用从rand开始
import fmt
import "github.com/xx/yy"    //从网络库引入
import _ "github.com/aa/bb"  //别名, "_"表示忽略掉,
import "./aaa"    // 同级目录aaa.go, 实际引入aaa.Method()
```

**go structTag**

```
type User struct {
    UserId   int    `json:"user_id" bson:"user_id"`
    UserName string `json:"user_name" bson:"user_name"`
}

u := &User{UserId: 1, UserName: "tony"}
j, _ := json.Marshal(u)
fmt.Println(string(j))   // {"user_id": 1, "user_name": "tony"}

t := reflect.TypeOf(u)
field := t.Elem().Field(0)
fmt.Println(field.Tag.Get("json"))  // user_id
```

