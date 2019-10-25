# coding:utf-8

import multiprocessing

def f1(name):
    print(name)

def f2(x):
    return x**2

def test_multi_process():
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
