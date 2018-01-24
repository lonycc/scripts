# 常用的一些shell脚本

```
#!/bin/bash  #使用的解释器

# if条件判断
if ...;then
  ...
elif ...;then
  ...
else
  ...
fi

# for循环
for var in val;
do
  ...
done

# while循环
while ...;
do
  ...
done

# case语句
case "$variable" in
abc) 
    echo "\$variable=abc";;
xyz)
    echo "\$variable=xyz";;
esac
```

`echo $(date +%Y-%m-%d)`  #输出日期格式 YYYY-MM-DD

`#` 一般用于注释

`#!` 特殊注释

`echo ${PATH#*:}` #参数替换

`echo $((2#101111))` #数制转换

`;`  分隔同一行多条命令

`.`  当前目录

`..` 上级目录

`cp /home/package/* .`  #复制到当前目录

文件名前带`.`则隐藏文件

`.`匹配任何单个字符

部分引用`"`  转义"String"中大部分特殊字符

全引用`'`    转义'String'中全部特殊字符

逗号操作符`,`  链接一系列算术操作

转义符`\` 一般用于转义`"`和`'`

命令替换符号````

空命令`:`  等价于"NOP"，在while后，做死循环；在then后，占位引出分支

`: ${username=`whoami`}`  #在一个二元命令中提供一个占位符

`: > filename`  #清空文件

通配符`*`匹配任意个数的字符, 乘法运算

`let "z=3**5"`

`echo $z`

三元操作符  `t=a<b?b:a`

测试变量是否被设置 `${para?err_msg} ${para:?err_msg}`

在正则中, `?`匹配单个字符

变量替换`$`

`var = "haha"`

`echo $var`

在正则中 `$` 表示行结束符

`${}`  参数替换

`$*`, `$@` 位置参数

`$?` 退出状态码变量，0表示执行成功，非0则失败

`$$` 所在脚本的进程ID

`echo $()`  #输出一个换行

`\cp filename /path/`  #覆盖拷贝

`echo -e '\n'`  #-e表示允许后面出现转义

`> /dev/null 2>&1`  #把标准出错重定向到标准输出, 在后台运行
