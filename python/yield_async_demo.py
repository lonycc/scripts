#coding=utf-8

# 同步I/O操作：导致请求进程阻塞，直到I/O操作完成；
# 异步I/O操作：不导致请求进程阻塞。
# 阻塞，非阻塞：进程/线程要访问的数据是否就绪，进程/线程是否需要等待；
# 同步，异步：访问数据的方式，同步需要主动读写数据，在读写数据的过程中还是会阻塞；异步只需要I/O操作完成的通知，并不主动读写数据，由操作系统内核完成数据的读写。

import asyncio
import socket

loop = asyncio.get_event_loop()
CHUNK_SIZE = 1024

async def connect(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    print("%s:%d" % (host, port))
    try:
        #await loop.sock_connect(sock, (host, port))
        await asyncio.wait_for(loop.sock_connect(sock, (host, port)), timeout=3)
    except (socket.timeout, ConnectionRefusedError):
        pass
    else:
        await loop.sock_sendall(sock, "test\r\n".encode("utf-8"))
        response = b""
        try:
            chunk = await loop.sock_recv(sock, CHUNK_SIZE)
        except (socket.timeout, ConnectionResetError):
            pass
        else:
            while chunk:
                print(chunk)
                response += chunk
                chunk = await loop.sock_recv(sock, CHUNK_SIZE)
    finally:
        sock.close()

def main():
    host_name_list = ["www.163.com", "www.zhihu.com"]
    host_list = [socket.gethostbyname(name) for name in host_name_list]
    port_list = [23, 45, 123, 22, 55, 666, 77, 88, 99, 1010,1 ,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    tasks = asyncio.gather(*[connect(host, port) for host in host_list for port in port_list])
    loop.run_until_complete(tasks)
    loop.close()


if __name__ == "__main__":
    main()

################################################################################
#生成器函数generator
#c是一个生成器, 生成器就是一种迭代器, 可用for迭代, 也可next(c)迭代
from random import randint, uniform

def mygen(alist):
    while len(alist) > 0:
        c = randint(0, len(alist)-1)
        yield alist.pop(c)
a = ["aa","bb","cc"]
c = mygen(a)

################################################################################
# receive = yield value
# 做了三件事 1、向函数外抛出(返回)value, 2、暂停(pause),等待next()或send()恢复; 3、赋值receive, 接收send()发送的值
################################################################################
def gen():
    value = 0
    while True:
        receive = yield value
        if receive == 'e':
            break
        value = 'got: %s' % receive

g = gen()
# next(g) 也可以启动生成器函数
print(g.send(None))    #1. 启动生成器函数, 执行到第一个yield语句结束的位置, 也就是receive = yield value, 返回value并暂停
print(g.send('hello')) #2. 传入'hello', 从上次暂停的位置继续, 赋值receive, 计算value, 回到while头部, yield语句返回value值并暂停, 等待send()激活
print(g.send(123456))  #3. 重复2
print(g.send('e'))     #4. receive接收到send()发送的'e', break退出循环

################################################################################
# yield 直接返回可迭代对象
# yield from 会解析可迭代对象, 将其中每一个item返回
# yield from iterable <=> for item in iterable: yield item
################################################################################
def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

def f_wrapper(fun_iterable):
    print('start')
    for item  in fun_iterable:
        yield item
    print('end')

wrap = f_wrapper(fab(5))
for i in wrap:
    print(i, end=' ')

def f_wrapper2(fun_iterable):
    print('start')
    yield from fun_iterable  #注意此处必须是一个可生成对象
    print('end')

wrap = f_wrapper2(fab(5))
for i in wrap:
    print(i, end=' ')

################################################################################
# asyncio.corouting 和 yield from
# python3.4中用@asyncio.coroutine装饰器和yield from实现异步io
# python3.5用async/await实现协程
# asyncio是一个基于事件循环的实现异步I/O的模块.
# 通过yield from, 我们可以将协程asyncio.sleep的控制权交给事件循环, 然后挂起当前协程;
# 之后, 由事件循环决定何时唤醒asyncio.sleep, 接着向后执行代码.
################################################################################
import asyncio

@asyncio.coroutine
def smart_fib(n):
    index, a, b = 0, 0, 1
    while index < n:
        sleep_secs = uniform(0, 0.2)
        yield from asyncio.sleep(sleep_secs) #通常yield from后都是耗时操作
        print('smart one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1

@asyncio.coroutine
def stupid_fib(n):
    index, a, b = 0, 0, 1
    while index < n:
        sleep_secs = uniform(0, 0.4)
        yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
        print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        smart_fib(10),
        stupid_fib(10),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished.')
    loop.close()

################################################################################
# async/await
# 方法声明前加async关键字, 将变成协程
################################################################################

async def mygen2(alist):
    while (len(alist)) > 0:
        c = randint(0, len(alist)-1)
        print(alist.pop(c))
        await asyncio.sleep(1)

a = ['aa', 'bb', 'cc']
c = mygen2(a)  # c是一个协程对象
