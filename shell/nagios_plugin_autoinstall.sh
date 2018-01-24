#!/bin/bash

echo ---1. add user and user group---
useradd -m -s /bin/bash nagios
groupadd nagcmd
usermod -G nagcmd nagios

echo ---2. check openssl-devel or install---
isinstall=`rpm -qa | grep openssl-devel`
if [ $isinstall -eq "" ];then
	yum -y install openssl-devel
else
	echo ---openssl-devel installed---
fi

echo ---3. tar plugin package---
cd /usr/local/src
tar zxf nagios-plugins-2.2.1.tar.gz
tar zxf nrpe-2.15.tar.gz
rm -f nagios-plugins-2.2.1.tar.gz
rm -f nrpe-2.15.tar.gz

echo ---4. configure and install nagios-plugins---
cd nagios-plugins-2.2.1
./configure --prefix=/usr/local/nagios --with-nagios-user=nagios --with-nagios-group=nagcmd --enable-redhat-pthread-workaround
make && make install

echo ---5. configure and install nrpe---
cd /usr/local/src/nrpe-2.15
./configure --prefix=/usr/local/nagios --enable-command-args
make all
make install
make install-plugin
make install-daemon
make install-daemon-config

echo ---6. edit nrpe.cfg---
sed -i 's/allowed_hosts=127.0.0.1/allowed_hosts=192.168.1.10/g' /usr/local/nagios/etc/nrpe.cfg

echo ---7. add nrpe service---
echo "/usr/local/nagios/bin/nrpe -c /usr/local/nagios/etc/nrpe.cfg -d" > /etc/init.d/nrpe
chmod a+x /etc/init.d/nrpe
/etc/init.d/nrpe
ln -s /etc/init.d/nrpe /etc/rc3.d/S99nrpe

echo ---finished---
