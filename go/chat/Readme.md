# golang项目打包成镜像部署

**构建镜像**

`cd /path/to/chat`

`docker build -t tony/go-chat:1.0 .`

**查看镜像**

`docker images`

**启动容器**

`docker run --name chat -p 8080:8080 -d tony/go-chat:1.0`
