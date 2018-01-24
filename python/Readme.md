```python
import urllib.parse
import urllib.request
import http.cookiejar
#自定义opener
def makeMyOpener(head = {
  'Connection': 'Keep-Alive',
  'Accept': 'text/html, application/xhtml+xml, */*',
  'Accept-Language': 'zh_CN,zh;q=0.8',
  'User-Agent': 'Mozilla/5.0 ( compatible; MISE 5.5; Windows NT)' 
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener()
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

values = {'user':'admin','pass':'123456'}
data = urllib.parse.urlencode(values).encode(encoding='UTF8')
user_agent = 'Mozilla/5.0 ( compatible; MISE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent } #发送header信息
req = urllib.request.Request(url,data) #POST构造请求
req.add_header('User-Agent',user_agent)  #单独加入header
req.add_header('Content-Type','plain/text')  #单独加入header
try:
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
except urllib.request.URLError as e:
    print(e.reason)  #打印异常原因
    print(e.code)     #打印异常代码
else:
    response.geturl()  #获取真实url
    response.info()   #返回headers
    response.getcode()  #返回代码
```

# 打开debug
```
httpHandler = urllib.request.HTTPHandler(debuglevel=1)
httpsHandler = urllib.request.HTTPSHandler(debuglevel=1)
opener = urllib.request.build_opener(httpHandler, httpsHandler)
urllib.request.install_opener(opener)
response = urllib.request.urlopen('http://www.baidu.com')
```

# HTTP认证
```
pass_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
url = 'https://www.baidu.com/
pass_mgr.add_password(None,url,'rekfan','xxxx')
handler = urllib.request.HTTPBasicAuthHandler(pass_mgr)
opener = urllib.request.build_opener(handler)
x = opener.open(url)
```

# 检测重定向
```
import urllib.request
class RedirectHandler(urllib.request.HTTPRedirectHandler):

    def http_error_301(self, req, fp, code, msg, headers):
        print("301")
        pass
        
    def http_error_302(self, req, fp, code, msg, headers):
        print("303")
        pass
opener = urllib.request.build_opener(RedirectHandler)

try:
    opener.open('http://rrurl.cn/b1UZuP')
except urllib.request.URLError as e:
    print(e.reason)
```

# cookie处理
```
import urllib.request
import http.cookiejar
cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
response = opener.open('http://www.baidu.com')
for item in cookie:
    print('Name = '+item.name)
    print('Value = '+item.value)
```

# try/except
> 执行try语句, 若发生异常, except根据类型异常捕获; 若异常与任意except不匹配, 则异常会传递给上层try

# try/except/else
执行try语句，若无异常发生，try子句执行完将继续执行else子句；否则except处理异常，else子句被忽略。

# raise 抛出异常

`raise NameError('hi')`

> 在except子句中可以用raise关键字抛出异常

# 用户自定义异常

> 创建一个新的exception类来拥有自己的异常, 异常应该继承自Exception类.

```
class mError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# 基础类
class Error(Exception):
    pass
    
class InputError(Error):
    def __init__(self,expression,message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    def __init__(self,previous,next,message):
        self.previous = previous
        self.next = next
        self.message = message

try:
    raise mError(3)
except mError as e:
    print(e)
```

# 定义清理行为try/finally

> 不论try子句是否发生异常, finally都会执行; try/except/else/finally

# 预定义的清理行为 with子句, 执行完会自动关闭文件

```
with open(r'filename') as filer:
    for line in filer:
        print(line)
```

# subprocess

fork一个子进程并与之通信; subprocess模块中只有一个类: Popen. 可以用来创建子进程, 并与子进程进行交互, 它的构造函数如下： 

`subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)`

```
args 可以是字符串或者list、元组，用于指定进程的可执行文件及其参数。
bufsize 0表示不缓冲,1表示缓冲,其他整数表示近似的缓冲区字节数。
stdin,stdout,stderr 分别表示子进程的标准输入、输出和错误句柄。它们可以是PIPE, 文件描述符或文件对象，也可以设置为None，表示从父进程继承。
shell 如果为True, 子进程将通过shell执行。
env 字典类型, 用于指定进程的环境变量。如果设为None，则从父进程继承。
subprocesss.PIPE 
在创建Popen对象时，可用于初始化stdin，stdout，stderr等参数，表示与子进程通信的标准流。 
subprocess.STDOUT 
创建Popen对象时，用于初始化stderr参数，表示将错误通过标准输出流输出。

Popen.poll() 
用于检查子进程是否已经结束。设置并返回returncode属性。 
Popen.wait() 
等待子进程结束，设置并返回returncode属性。 
Popen.communicate(input=None) 
与子进程进行交互。向stdin发送数据(创建Popen时stdin=subprocess.PIPE),从stdout和stderr中读取数据，可选参数input指定发送到子进程的参数。communicate()返回一个元组: (stdoutdata,stderrdata)。 
Popen.send_signal(signal) 
向子进程发送信号。 
Popen.terminate() 
停止子进程 
Popen.kill() 
杀死子进程 
Popen.pid 获取子进程的id 
Popen.returncode 获取进程返回值，若进程还没结束，返回None

# 死锁

如果使用了PIPE，而又不去处理管道输出，那么一旦子进程输出数据过多，死锁就会发生。 
使用p.stdout.readlines()或p.communicate()去清理输出。

subprocess.call(*pepenargs, **kwargs) 执行子进程，并等待命令结束，返回子进程返回值。参数同Popen。 
subprocess.check_call(*pepenargs, **kwargs) 执行上面的call命令，并检查返回值。如果子进程返回非0，则抛出CalledProcessError异常。

subprocess.Popen(["gedit","abc.txt"])  #用gedit打开abc.txt
subprocess.Popen("gedit abc.txt")      #用gedit打开abc.txt，windows下可行
subprocess.Popen("gedit abc.txt",shell=True) #linux下可行
subprocess.Popen(["/bin/sh","-c","gedit abc.txt"]) #linux下可行

# subprocess.call*

# call()执行程序,并等待完成

def call(*popenargs, **kwargs):
    return Popen(*popenargs, **kwargs).wait()

# check_all()调用前面的call,如果返回值非零,则抛出异常
def check_call(*popenargs, **kwargs):
    retcode = call(*popenargs, **kwargs)
    if retcode:
        cmd = kwargs.get("args")
        raise CalledProcessError(retcode, cmd)
    return 0

# check_output()执行程序,并返回标准输出
def check_output(*popenargs, **kwargs):
    process = Popen(*popenargs, stdout=PIPE, **kwargs):
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        raise CalledProcessError(retcode, cmd, output=output)
    return output

p = subprocess.Popen('python test.py', shell=True, stdout=subprocess.PIPE)
c = p.stdout.readline()  #或者可以for line in p.stdout: yield line
while c:   #或者也可以判断 while p.poll() == None:
    print(c)
    c = p.stdout.readline()
p.wait()
```

# python2.x 到python3.x内置模块的变动

| python2 | python3 |
|:--|:--|
| cookielib |	http.cookiejar |
| urllib2 |	urllib.request |
| StringIO | io.StringIO |
| httplib | http.client |
| Cookie | http.cookies |
| BaseHTTPServer | http.server | 
| SimpleHTTPServer | http.server |
| CGIHttpServer | http.server |
| urlparse | urllib.parse |

# python signal

为异步事件设置操作句柄; signal.signal() 允许定义一个句柄来执行接收到的信号，操作系统规定了进程收到信号以后的默认行为，但我们可以通过绑定信号处理函数来修改进程收到信号后的行为；有两个信号不可更改，SIGTOP和SIGKILL

`signal.SIG_DFL` #执行默认函数 

`signal.SIG_IGN` #忽略信号 

`SIG*` #所有信号 

`signal.CTRL_C_EVENT`  #对应于Ctrl + C 键盘事件,该信号只能被os.kill()调用 

`signal.CTRL_BREAK_EVENT`  #对应于Ctrl + Break 键盘事件，也只能被os.kill()调用 

`signal.NSIG` #比最大信号量大一 

`signal.ITIMER_REAL`
