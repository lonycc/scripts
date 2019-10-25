# coding:utf-8

# 进程池中进程间通信使用multiprocessing.Manager().Queue()

import multiprocessing
import os
import time

def f1(name):
    print(name)

def f2(x):
    return x**2

def test_1():
    p = multiprocessing.Process(target=f1, args=('tony',))
    p.start()
    p.join()
    
    with multiprocessing.Pool(5) as p1:
        print(p1.map(f2, [1, 2, 3, 4]))
    
    p2 = multiprocessing.Pool(5)
    p2.map(f2, [1, 3, 5])
    # p2.apply_async(f2, (10,)) # 异步调用
    p2.close()  # 关闭pool, 不再接受新任务
    p2.join()  # 主进程阻塞, 等待子进程执行完成
    # p2.terminate()  # 立即终止

def write(q):
    print("write启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in "python":
        q.put(i)

def read(q):
    print("read启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("read从Queue获取到消息：%s" % q.get(True))

if __name__ == '__main__':
    print("(%s) start" % os.getpid())
    q = multiprocessing.Manager().Queue()
    po = multiprocessing.Pool()
    po.apply_async(write, args=(q,))

    time.sleep(2)   
    
    po.apply_async(read, args=(q,))
    po.close()
    po.join()
    
    print("(%s) end" % os.getpid())  
