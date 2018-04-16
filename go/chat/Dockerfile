# 基础镜像
FROM golang:1.9

# 维护者
MAINTAINER tony "tony@163.com"

# 环境变量
ENV XXX yyy

#
RUN mkdir -p $GOPATH/src/chat

# 镜像内的工作目录
WORKDIR $GOPATH/src/chat

# 将宿主机上的文件拷贝到镜像中
COPY . $GOPATH/src/chat
# COPY命令复制压缩包不会解压, ADD会解压
# COPY aaa.tar $GOPATH/src/aaa.tar

# 暴露端口
EXPOSE 8080

# 挂载目录
VOLUME [$GOPATH/src]

# 程序入口
ENTRYPOINT ["./chat"]

# 执行命令
# CMD [/run.sh]
