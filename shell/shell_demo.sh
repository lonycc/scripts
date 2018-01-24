#!/bin/bash

echo "-------1到10循环--------"
# for((i=1;i<=10;i++))
for i in `seq 10`
do
    echo $(expr $i\*4)
done

echo "-------目录遍历--------"
for i in `ls`
do
	echo $i
done

echo "-------arr[@]--------"
for i in ${arr[@]}
do
	echo $i
done

echo "-------\$*--------"
for i in $*
do
	echo $i
done

echo "---f1 f2 f3---"
for i in a b c
do
	echo $i
done

# shell上, 0表示标准输入, 1表示标准输出, 2表示标准错误输出
# > 默认为标准输出重定向, 与1>相同
# 2>&1 表示把错误输出重定向到标准输出
# &>file 把标准输出和标准错误都重定向到文件file中

# 数组定义
arr=('/home/demo' '/home/demo2' '/home/demo3')

array  
array[0]="a"  
array[1]="b"  
array[2]="c"
echo ${#array[@]}  #数组长度

for var in ${arr[@]};  
do  
  echo $var  
done

# 遍历, 带数组下标  
for i in "${!arr[@]}";   
do   
    printf "%s\t%s\n" "$i" "${arr[$i]}"  
done
  
# 遍历While循环法  
i=0  
while [ $i -lt ${#array[@]} ]  
do  
    echo ${ array[$i] }  
    let i++  
done


# 向函数传递数组参数
fun() {  
    local _arr=(`echo $1 | cut -d " "  --output-delimiter=" " -f 1-`)  
    local _n_arr=${#_arr[@]}  
    for((i=0;i<$_n_arr;i++));  
    do    
       elem=${_arr[$i]}
       echo "$i : $elem"  
    done;   
}  
   
array=(a b c)  
fun "$(echo ${array[@]})" 

# 下载bing封面图
domain='https://cn.bing.com'
pic_url=`curl -s $domain | grep -E "g_img" | awk -F "g_img={url: " '{print $2}' | awk -F '"' '{print $2}'`
echo $domain$pic_url
# wget -P /home/bing $domain$pic_url
curl -O $domain$pic_url

# 通过ftp下载整个目录
wget ftp://IP:PORT/* --ftp-user=xxx --ftp-password=xxx -r

# ftp连接
host=l27.0.0.1
cd /home/demo
ftp -ivn $host <<EOF
user username password
binary
passive
# prompt off
cd $(date +%Y%m%d)
get post.txt
get thread.txt
put xxx.txt
mget *
mput *
bye
EOF

# 通过git更新线上代码1
cd /path/to/project
git remote update -p
git checkout -f origin/master
git submodule update --init


# 通过git更新线上代码2
WEB_PATH='/var/www'
WEB_USER='nginx'
WEB_USERGROUP='nginx'

echo ---Start deployment---
cd $WEB_PATH
echo ---pulling source code---
git reset --hard origin/master
git clean -f
git pull
git checkout master
echo ---change owner---
chown -R $WEB_USER:$WEB_USERGROUP $WEB_PATH

# 递归遍历目录
function read_dir(){
	for file in `ls $1`
	do
		if [ -d $1"/"$file ]
		then
			read_dir $1"/"$file
		else
			if [[ $file =~ ^content_[0-9]{1,20}.htm$ ]] || [[ $file =~ ^[0-9]{1,20}.htm$ ]] || [[ $file =~ ^t[0-9]{8}_[0-9]{1,20}.htm$ ]]
			then
				bool=`grep -l 'aaa' $1"/"$file | xargs grep -c 'bbb'`
				#if grep -qE 'aaa|bbb|ccc' $1"/"$file
				if [[ $bool -ne "" ]] && [[ $bool -ne 0 ]]
				then
					echo $1"/"$file
				fi
			fi
		fi
	done
}
scan_path=$1
save_path=$2
last_string=${scan_path:0-1:1}
pp=/
if [ -d $scan_path ] && [[ $scan_path != "" ]] && [[ $last_string != $pp ]];then	
	echo 'scan the directory:' $1
	#echo $(date +"%Y-%m-%d %H:%M:%S") >> $save_path
	read_dir $1
	#echo $(date +"%Y-%m-%d %H:%M:%S") >> $save_path
	echo 'finished! you can find result from '$save_path
else
	echo 'Usage: scandir.sh scan_path save_path'
fi
echo ---Finished---

# iptables相关
echo '---初始化---'
iptables -F  # 清除预设表filter中的所有规则链的规则 
iptables -X  # 清除预设表filter中使用者自定链中的规则
iptables -Z  # 清除预设表filter中计数器

echo '---set the default rules---'
iptables -P INPUT DROP    #这条要在添加ssh规则之后再执行
iptables -P OUTPUT DROP   #出口包都drop掉
iptables -P FORWARD DROP  #转发数据包都drop掉

# -----------
service iptables save  #写入/etc/sysconfig/iptables
echo "--------------------------"
iptables -L -n  #查看自定链规则

iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT #允许所有已经建立的和相关的连接
iptables -A INPUT -s 192.168.1.5/24 -p icmp -j ACCEPT  #允许ping 如果INPUT DROP
iptables -A OUTPUT -s 192.168.1.5/24 -p icmp -j ACCEPT #允许ping 如果OUTPUT DROP

iptables -A INPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT   #允许本机
iptables -A INPUT -p tcp --dport 20 -j ACCEPT  #允许ftp接收
iptables -A INPUT -p tcp --dport 21 -j ACCEPT  #允许ftp发送
iptables -A INPUT -s 192.168.1.5 -p tcp --dport 22 -j ACCEPT  #允许来自172.23.170.51的ssh连接

iptables -A INPUT -s !192.168.1.5 -p tcp --dport 22 -j ACCEPT  #允许除172.23.170.51之外的所有ssh连接

iptables -A INPUT -p tcp --dport 80 -j ACCEPT    #允许http
iptables -A INPUT -m state --state NEW -p udp --dport 123 -j ACCEPT    #允许ntpd
iptables -A INPUT -p udp --dport 161 -j ACCEPT   #允许cacti
iptables -A INPUT -p tcp --dport 3306 -j ACCEPT  #允许mysql
iptables -A INPUT -p tcp --dport 5666 -j ACCEPT  #允许nagios
iptables -A INPUT -p tcp --dport 8080 -j ACCEPT  #允许tomcat

iptables -D INPUT -p tcp --dport 22 -j ACCEPT #删除一条规则
iptables -A INPUT -m state --state INVALID -j DROP #drop掉非法连接
iptables -A INPUT -i lo -p all -j ACCEPT   #允许loopback 如果是INPUT DROP
iptables -A OUTPUT -o lo -p all -j ACCEPT  #允许loopback 如果是OUTPUT DROP
iptables -A OUTPUT -o eth0 -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT  #允许所有已经建立的连接通过网卡eth0端口22出口包
iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT  #做nat时,forward默认规则是drop,所以必须允许从网卡eth0转发到网卡eth1的所有已经建立的和相关的连接
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT #允许从eth1转发到eth0的连接
iptables -A FORWARD -p TCP ! --syn -m state --state NEW -j DROP #丢弃坏的tcp包

iptables -A FORWARD -f -m limit --limit 100/s --limit-burst 100 -j ACCEPT #处理IP碎片数量,防止攻击,允许每秒100个
iptables -A FORWARD -p icmp -m limit --limit 1/s --limit-burst 10 -j ACCEPT #设置ICMP包过滤,允许每秒1个包,限制触发条件是10个包.
iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT  #当达到100个连接时,触发25个每分钟的连接限制
iptables -t nat -A PREROUTING -p tcp -d 192.168.102.37 --dport 422 -j DNAT --to 192.168.102.37:22  #端口422转发到22,这样通过422端口也可以ssh

iptables -t nat -L #查看本机关于nat的设置
iptables -F -t nat
iptables -X -t nat
iptables -Z -t nat

#防止外网用内网IP欺骗
iptables -t nat -A PREROUTING -i eth0 -s 10.0.0.0/8 -j DROP
iptables -t nat -A PREROUTING -i eth0 -s 172.16.0.0/12 -j DROP
iptables -t nat -A PREROUTING -i eth0 -s 192.168.0.0/16 -j DROP

#禁止与211.101.46.253的所有连接
iptables -t nat -A PREROUTING -d 211.101.46.253 -j DROP

#禁止211.101.46.253的21端口
iptables -t nat -A PREROUTING -p tcp --dport 21 -d 211.101.46.253 -j DROP

#防止同步包洪水
iptables -A FORWARD -p tcp --syn -m limit 1/s -j ACCEPT
#防止各种端口扫描
iptables -A FORWARD -p tcp --tcp-flags SYN,ACK,FIN,RST RST -m limit --limit 1/s -j ACCEPT
#防PING攻击
iptables -A FORWARD -p icmp --icmp-type echo-request -m limit --limit 1/s -j ACCEPT

iptables -L -n --line-numbers  #带标记
iptables -D INPUT number #删除第number条规则
iptables -A INPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT #允许本地回环
iptables -A OUTPUT -j ACCEPT  #允许本机对外访问
iptables -A INPUT -s xx.xx.xx.xx -j DROP #永久屏蔽单个ip
iptables -I INPUT -s 192.0.0.0/8 -j DROP #屏蔽192段ip
