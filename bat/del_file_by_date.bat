@echo off
set SrcDir=C:\Users\tony\Documents
set DaysAgo=5
forfiles /p "%SrcDir%" /d -%DaysAgo% /c "cmd /c echo removing the file: [@file] last modified time is: [@fdate @ftime] && del /f @path"
exit