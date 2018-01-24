@echo off 
echo ================================================
echo 参考资料：http://www.cnblogs.com/luluping/archive/2010/03/16/1687103.html
echo  Windows环境下Oracle数据库的自动备份脚本
echo  1. 使用当前日期命名备份文件。
echo  2. 自动删除7天前的备份。
echo ================================================
::以“YYYYMMDD”格式取出当前时间。
set backupdate=%date:~0,4%%date:~5,2%%date:~8,2%
set backuptime=%time:~0,2%%time:~3,2%%time:~6,2%
::设置用户名、密码和要备份的数据库。
set username=username
set password=password
set sid=dbtest
set connect=%username%/%password%@%sid%
::创建备份目录
if not exist "d:\backup\data" 		mkdir d:\backup\data
if not exist "d:\backup\log" 		mkdir d:\backup\log
set datadir=d:\backup\data
set logdir=d:\backup\log
::执行全表备份
exp %connect% file=%datadir%\data_%backupdate%.dmp log=%logdir%\log_%backupdate%_%backuptime%.log full=y
::增量备份,备份上一次备份后改变的数据
::exp %connect% inctype=incremental file=%datadir%\data_%backupdate%_%backuptime%.dmp
::删除7天前的备份
forfiles /p "%datadir%" /s /m *.* /d -7 /c "cmd /c del @path"
forfiles /p "%logdir%" /s /m *.* /d -7 /c "cmd /c del @path"
::压缩备份文件
"C:\Program Files\WinRAR\WinRAR.exe" a -k -s -m5 %datadir%\data_%backupdate%.zip %datadir%\data_%backupdate%.dmp
::删除原始备份文件
del %datadir%\data_%backupdate%.dmp
exit