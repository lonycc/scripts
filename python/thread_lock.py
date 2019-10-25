# coding:utf-8

import sys
import threading

'''
CPython解释器的内存管理是线程不安全的, 故而引入了GIL, 也就是防止多线程并发执行机器码的Mutex(互斥锁);
线程锁, threading.Lock(), 获得线程锁的线程未释放, 则其他线程都得等;
'''

lock = threading.Lock()   # 全局锁
pages = ['abc', 'def', 'haha']   # 全局待处理列表
paged = []  # 全局已处理列表

class MyThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self._running = True

	def terminate(self):
		self._running = False

	def extract(self, page):
		print(page)

	def run(self):
		try:
			while len(pages) > 0 and self._running:
				lock.acquire()  # 获取锁
				page = pages[0]
				pages.remove(page)
				lock.release()  # 释放锁
				self.extract(page)  # 耗时IO操作要在释放锁后执行
				lock.acquire()   # 获取锁
				paged.append(page)
				lock.release()   # 释放锁
		except Exception as e:
			print('failed', str(e))


list_thread = []
try:
	for i in range(4):
	    list_thread.append(MyThread())
	for th in list_thread:
	    th.start()
	    th.join()
except:
    for th in list_thread:
        th.terminate()
    print('error!', sys.exc_info()[0])
finally:
    print('finished')
