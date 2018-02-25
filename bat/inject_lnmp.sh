#!/bin/bash

# 端口指纹识别
nmap -sV -p 62231 2018.mhz.pw

# rsync查看目录, 下载
rsync rsync://2018.mhz.pw:62231
rsync rsync://2018.mhz.pw:62231/www
rsync -a rsync://2018.mhz.pw:62231/www/pwnhub_6670.git ./

# git裸仓库
# 使用git init --bare创建的仓库
# 使用git init创建的仓库

# 当你已经获取到了一份git裸仓库, 只需在git裸仓库外执行git clone xxx.git即可将裸仓库拉取到本地

git clone pwnhub_6670.git

