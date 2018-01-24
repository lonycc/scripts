#!/bin/bash

# 密码最长天数180天
sed -i 's/PASS_MAX_DAYS.*/PASS_MAX_DAYS\   180/g' /etc/login.defs

# 密码最短天数1天
sed -i 's/PASS_MIN_DAYS.*/PASS_MIN_DAYS\   1/g' /etc/login.defs

# 密码最小长度8位
sed -i 's/PASS_MIN_LEN.*/PASS_MIN_LEN\   8/g' /etc/login.defs

# 密码提醒周期
sed -i 's/PASS_WARN_AGE.*/PASS_WARN_AGE\   30/g' /etc/login.defs

# 未活动状态下登录失效时间60s
sed -i '$a LOGIN_RETRIES\  5\nLOGIN_TIMEOUT\ 60' /etc/login.defs

# ssh会话过期时间
sed -i '$a TIMEOUT=600' /etc/profile

# 密码安全
sed -i 's/password\    requisite\     pam_cracklib.so .*/password\    requisite\     pam_cracklib.so \ try_first_pass\ retry=3\ minlen=10\ lcredit=-1\ ucredit=-1\ dcredit=-1\ ocredit=-1\ difok=6/g' /etc/pam.d/system-auth

# bash漏洞检测
if [ `env t='() { :;}; echo 123.' bash -c "true"` =  "123."]
then
    yum clean all
    yum -y update bash
fi
