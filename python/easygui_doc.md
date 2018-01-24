## 1.安装 easygui
`pip install easygui`

## 2.easygui 的功能演示
`import easygui`

`easygui.egdemo()`

## 3.使用 easygui

`import easygui as eg`

`from easygui import *`

**msgbox 弹出信息框**

```
@msgbox(msg='(Your message goes here)', title='', ok_button='OK', image=None, root=None)

msg:显示文本内容,
title:提示框标题, 
ok_button:消息提示框按钮上的文字, 
image:显示图片(仅仅显示 gif 图片),
root:顶层 Tk 控件.
@ return :OK 按钮的文本内容
```

**ccbox**

`ccbox(msg='Shall I continue?', title=' ', choices=('C[o]ntinue', 'C[a]ncel'), image=None,
default_choice='Continue', cancel_choice='Cancel')`

@ return: True if 'Continue' or dialog is cancelled, False if 'Cancel'

```
例子:
if ccbox():
    pass  # user chose to continue,选择了 shall I continue
else:
    return # user chose to cancel  #选择了 cancel
```

**choicebox 选择框**

`choicebox(msg='Pick something.', title=' ', choices=())` #choices 是一个选择元组或列表

@ return: List containing choice selected or None if cancelled

`choices = ['愿意', '不愿意', '有钱的时候愿意']`

`reply = choicebox('你愿意吗？', choices = choices)`

**ynbox -- yes or no 对话框**

`ynbox(msg='Shall I continue?', title=' ', choices=('[<F1>]Yes', '[<F2>]No'), image=None,
default_choice='[<F1>]Yes', cancel_choice='[<F2>]No')`

@ return: True if 'Yes' or dialog is cancelled, False if 'No'

**buttonbox 按钮选择框**

`buttonbox(msg='', title=' ', choices=('Button[1]', 'Button[2]', 'Button[3]'), image=None,
root=None, default_choice=None, cancel_choice=None)`

@ return: the text of the button that the user selected

**indexbox** 

`indexbox(msg='Shall  I  continue?',  title='  ',  choices=('Yes',  'No'),  image=None,
default_choice='Yes', cancel_choice='No')`

@ return: the index of the choice selected, starting from 0

**boolbox**

`boolbox(msg='Shall I continue?', title=' ', choices=('[Y]es', '[N]o'), image=None,
default_choice='Yes', cancel_choice='No')`

@ return: True if first button pressed or dialog is cancelled, False if second button is pressed

**multchoicebox 多选框**

`multchoicebox(msg='Pick as many items as you like.', title=' ', choices=(), **kwargs)`

@ return: List containing choice selected or None if cancelled #返回多个选择.

**enterbox 让用户输入选择**

```
enterbox(msg='Enter something.', title=' ', default='', strip=True, image=None, root=None)

msg:提示信息
title:标题
default:默认显示文本
strip:如果为 true, 将把文本框里面的空白剔除,然后返回. 
image:显示图片
root:顶层窗口

@ return: the text that the user entered, or None if he cancels the operation.
```

**integerbox 整数输入框**

`integerbox(msg='', title=' ', default='', lowerbound=0, upperbound=99, image=None,
root=None)`

注:用户只能输入 0-99 范围内的整数,否则要求重新输入.

**mulenterbox -- 多项输入框**

`multenterbox(msg='Fill in values for the fields.', title=' ', fields=(), values=())`

fields,文本框前面的提示信息.需要六个字符串. 

value 对应六个文本框的默认值

@ return: String

**passwordbox 让用户输入密码**

`passwordbox(msg='Enter your password.', title=' ', default='', image=None, root=None)`

@ return: the text that the user entered, or None if he cancels the operation.


**multpasswordbox 多项密码框**

`multpasswordbox(msg='Fill in values for the fields.', title=' ', fields=(), values=())`

fields:文本框一和文本框二前面的提示字符串. 

values:文本框默认值

最后一个文本框以密码形式加密显示输入.

**textbox 显示文本**

`textbox(msg='', title=' ', text='', codebox=0)`

msg:提示信息 title:标题 text:显示文本 codebox:字体

**codebox 代码框**

`codebox(msg='', title='', text='') <=> textbox(codebox = 1)`

**diropenbox 目录文件框**

`diropenbox(msg=None, title=None, default=None)`

msg:提示信息

title:标题内容

default:默认打开目录

@ return: Normalized path selected by user

**fileopenbox 文件打开框**

`fileopenbox(msg=None, title=None, default='*', filetypes=None, multiple=False)`

default:默认匹配所有目录的所有文件.例如`r'f:\*.py'` .

filetypes: `['*.txt', '*.py']`或可以是字符串列表,列表的最后一项字符串是文件类型的描述.例如:`filetypes = [*.css,['*.htm','*.html','HTML files']]`

@ return: the name of a file, or None if user chose to cancel

**记住用户配置 EgStore 类**

**exceptionbox 捕获异常**
`exceptionbox(msg=None, title=None)`

```
try:
    ...
except:
    exceptionbox()
```
