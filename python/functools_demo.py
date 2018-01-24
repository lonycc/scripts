# coding=utf-8
# functools模块小结

import functools

# functools.partial
'''
通过包装手法, 允许“重新定义”函数签名
用一些默认参数包装一个可调用对象, 返回结果是可调用对象, 并且可以像原始对象一样对待
冻结部分函数位置函数或关键字参数, 简化函数, 更少更灵活的函数参数调用

应用场景: 当一个函数有某些参数是已知的, 可以通过functools.partial包装, 以便用更少的参数去调用
'''

def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords) #合并，调用原始函数，此时用了partial的参数
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc

demo_1 = functools.partial(demo, coding='utf-8')

# 当调用 demo_1(args, *kargs) 相当于 demo(args, *kargs, coding=utf-8)

def add(a, b):
    return a + b

add(4, 2)

plus3 = functools.partial(add, 3)
plus5 = functools.partial(add, 5)

# plus3(4) 相当于 add(4, 3)
# plus5(4) 相当于 add(4, 5)
print('--------------------------------------------------------------------------------------------------\n')


# functools.update_wrapper
'''
默认partial对象没有__name__和__doc__, 这种情况下，对于装饰器函数非常难以debug.使用update_wrapper(),从原始对象拷贝或加入现有partial对象
它可以把被封装函数的__name__、module、__doc__和 __dict__都复制到封装函数去(模块级别常量WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES)
这个函数主要用在装饰器函数中，装饰器返回函数反射得到的是包装函数的函数定义而不是原始函数定义
'''

def wrap(func):
    def call_it(*args, **kwargs):
        '''wrap func: call_it'''
        print('before call')
        return func(*args, **kwargs)
    return call_it

@wrap
def hello():
    '''say hello'''
    print('hello world')

def wrap2(func):
    def call_it(*args, **kwargs):
        '''wrap func: call_it2'''
        print('before call')
        return func(*args, **kwargs)
    return functools.update_wrapper(call_it, func)

@wrap2
def hello2():
    '''test hello'''
    print('hello world2')

hello()
hello.__name__
hello.__doc__
hello2()
hello2.__name__
hello2.__doc__
print('--------------------------------------------------------------------------------------------------\n')


# functools.wraps
'''
调用函数装饰器partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)的简写
'''
def wrap3(func):
    @functools.wraps(func)
    def call_it(*args, **kwargs):
        '''wrap func: call_it2'''
        print('before call')
        return func(*args, **kwargs)
    return call_it

@wrap3
def hello3():
    '''test hello 3'''
    print('hello world3')

hello3()
print('--------------------------------------------------------------------------------------------------\n')


# functools.reduce
'''
functools.reduce(function, iterable[, initializer])
对iterable中的item顺序迭代调用function, 如果有initializer, 可作为初始值.
等同于内置函数reduce(), 用这个的原因是代码更兼容PY3
'''

functools.reduce(add, range(1, 11)) #从加1到加10
functools.reduce(add, range(1, 11), 20) #初始值为20, 再执行加1到加10
print('--------------------------------------------------------------------------------------------------\n')


# functools.cmp_to_key
'''
functools.cmp_to_key(func)
将比较函数转换成key函数，用在接受key函数的方法中(sorted([5,1,3,2]), min(a, b [...]), max(a, b), heapq.nlargest(), heapq.nsmallest(), itertools.groupby())
key函数, 接收一个参数, 返回一个表明该参数在期望序列中的位置

'''

sorted(['andy', 'tony', 'linda'], key=functools.cmp_to_key(locale.strcoll))
print('--------------------------------------------------------------------------------------------------\n')


# functools.total_ordering
'''
针对某个类如果定义了__lt__、__le__、__gt__、__ge__这些方法中的至少一个，使用该装饰器，则会自动的把其他几个比较函数也实现在该类中
'''

@functools.total_ordering
class Student:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))

    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
print(dir(Student))
