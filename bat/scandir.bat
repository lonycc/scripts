@echo off
set work_path=F:\myjob\java
@echo off
for /R %work_path% %%s in (*) do (
echo %%s
)
pause