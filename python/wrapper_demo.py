# coding=utf-8

# 自动给多个函数加上装饰器

from functools import wraps
import copy
import types

def wrap(func):
    @wraps(func)
    def _call(*args, **kwargs):
        result = func(*args, **kwargs)
        print('wrap you')
        return result
    return _call

def test():
    print('test')

def test2():
    print('test3')

glocal_dict = copy.copy(globals())

func_list = [[k, v] for k, v in glocal_dict.items() if not k.startswith('__')]

for func_name, func in func_list:
    if func_name in ['wraps', 'copy', 'wrap', 'types']:
        continue
    if types.FunctionType == type(func):
        globals()[func_name]= wrap(func)
print('-----------------------------------------------------------------------------\n')        

# 嵌套函数, 内部函数能访问外部函数的变量
def outer():
    x = 7

    def inner():
        print('i am inner func')
        print('i can revoke outer variable x: %d' % x)
    inner()

# 把函数当做对象
print(outer.__class__)
print(outer.__class__.__name__)
print('-----------------------------------------------------------------------------\n')

# 函数作为其他函数的参数
def applyfunc(func, args, repeat=3):
    for i in range(0, repeat):
        func(args)

def test(s):
    print('a test function', s)

applyfunc(test, 'love is important', repeat=3)
print('-----------------------------------------------------------------------------\n')

# Closures 可理解为闭包
def outer2():
    x = 127
    def inner2():
        print(x)
    return inner2

foobar = outer2()
foobar  # <function outer2.<locals>.inner2 at 0x10aefcbf8>
print(foobar.__closure__)  # (<cell at 0x00706230: int object at 0x5C3EC7F0>,)
foobar()  # print 127
print('-----------------------------------------------------------------------------\n')

# Decorators  装饰器 - 以函数作为参数, 并输出一个装饰后的新函数
def outer(somefunc):
    def inner():
        print('have not run ', somefunc.__name__, end='\n')
        result = somefunc()
        print(result + ' finished')
    return inner

def foo6():
    return 'i am foo6'

decorator = outer(foo6)
decorator()
print('-----------------------------------------------------------------------------\n')

# 装饰器2
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'I am a {name}, my attributes: {dict}'.format(name=self.__class__.__name__, dict=self.__dict__)

def add(a, b):
    return Point(a.x + b.x, a.y + b.y)

print('-----------------------------------------------------------------------------\n')

# @log 相当于执行了 log(func)
def log(function):
    def wrapper(*args, **kwargs):
        print('before function [%s()] run.' % function.__name__)
        rst = function(*args, **kwargs)
        print('after function [%s()] run.' % function.__name__)
        return rst
    return wrapper

@log
def func():
    print('func() run.')

func()
print('-----------------------------------------------------------------------------\n')

# decorator本身需要传入参数, 那就需要编写一个返回decorator的decorator
import functools

def log(text=''):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print('before function [%s()] run, text: [%s].' %
                  (function.__name__, text))
            rst = function(*args, **kwargs)
            print('after function [%s()] run, text: [%s].' %
                  (function.__name__, text))
            return rst
        return wrapper
    return decorator

@log('log text')
def func():
    print('func() run.')

func()
print('-----------------------------------------------------------------------------\n')

# 实现支持带/不带参数的装饰器
import functools

def log(argument):
    if not callable(argument):
        def decorator(function):
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                print('before function [%s()] run, text: [%s].' % (
                    function.__name__, text))
                rst = function(*args, **kwargs)
                print('after function [%s()] run, text: [%s].' % (
                    function.__name__, text))
                return rst
            return wrapper
        return decorator

    def wrapper(*args, **kwargs):
        print('before function [%s()] run.' % function.__name__)
        rst = argument(*args, **kwargs)
        print('after function [%s()] run.' % function.__name__)
        return rst
    return wrapper
