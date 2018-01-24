#!/usr/bin/env python3
# coding=utf-8

from threading import Thread
from multiprocessing import Process
import time
import requests
import queue

SHARE_Q = queue.Queue()
_WORKER_THREAD_NUM = 5

def queue_test():
    fifo = queue.Queue(maxsize=100)
    lifo = queue.LifoQueue(maxsize=100)
    pq = queue.PriorityQueue(maxsize=100)
    fifo.empty()
    fifo.full()
    #fifo.put('what'[, block[, timeout]])
    fifo.put_nowait('fuck')
    #fifo.get([block[, timeout]])
    fifo.get_nowait()
    fifo.task_done() #完成task后, 发送一个信号
    fifo.join() #等待fifo为空

class MyThread(Thread):
    def __init(self, func):
        super(MyThread, self).__init__()
        self.func = func
    def run(self):
        run(self.func)

def do_something(item):
    print(item)

def worker():
    global SHARE_Q
    while True:
        if not SHARE_Q.empty():
            item = SHARE_Q.get()
            do_something(item)
            time.sleep(1)
            SHARE_Q.task_done()

def queue_main():
    global SHARE_Q
    threads = []
    for task in range(100):
        SHARE_Q.put(task)
    for i in range(_WORKER_THREAD_NUM):
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    SHARE_Q.join()


# CPU密集运算
def counter(x, y):
    c = 0
    while c < 50000:
        c += 1
        x += x
        y += y

# IO密集运算
def write():
    f = open('tmp.txt', 'w')
    for x in range(50000):
        f.write('test write %d \n' % x)
    f.close()

def read():
    f = open('tmp.txt', 'r')
    lines = f.readlines()
    f.close()

# 网络请求运算
def http_request():
    try:
        r = requests.get('https://www.baidu.com', headers={'User-Agent': 'Mozilla/5.0'})
        html = r.text
        return  {"context": html}
    except Exception as e:
        return {"error": e}


# 单线程多次
def main(target, args):
    start_time = time.time()
    for tid in range(100):
        t = Thread(target=target, args=args)
        t.start()
        t.join()
    end_time = time.time()
    print("total time of single is: {}".format(end_time - start_time))

# 多线程
def multi_thread_main(target, args):
    thread_all = []
    start_time = time.time()
    for tid in range(100):
        t = Thread(target=target, args=args)
        thread_all.append(t)
        t.start()
    for thread in thread_all:
        thread.join()

    # 另一种写法
    '''
    e = thread_all.__len__()
    while True:
        for th in thread_all:
            if not th.is_alive():
                e -= 1
            if e <= 0:
                break
    '''
    end_time = time.time()
    print("total time of multi thread is: {}".format(end_time -start_time))

# 多进程
def multi_process_main(target, args):
    process_all = []
    start_time = time.time()
    for x in range(100):
        process = Process(target=target, args=args)
        process_all.append(process)
        process.start()
    for process in process_all:
        process.join()
    '''
    e = process_all.__len__()
    while True:
        for th in process_all:
            if not th.is_alive():
                e -= 1
            if e <= 0:
                break
    '''
    end_time = time.time()
    print("total time of multi process is: {}".format(end_time -start_time))

if __name__ == '__main__':
    #main(counter, (1, 1))
    #multi_thread_main(counter, (1, 1))
    #multi_process_main(counter, (1, 1))
    #queue_main()