#!/usr/bin/python
#coding=utf-8

########################
# 类可以访问静态方法, 类方法, 成员变量; 不能访问成员方法, 属性;
# 类的实例可以访问静态方法, 类方法, 公开属性, 成员方法, 成员变量, 不能访问私有属性;
# 静态方法和类方法可以被继承
##########################


class myclass(object):
	x = '公开成员变量'
	def __init__(self, xxx, yyy):
		self.x = 'instance' # 公开属性
		self._x = xxx   # 公开属性
		self.__yyy = yyy # 私有属性

	@staticmethod
	def static_method():
		print('静态方法被调用')

	@classmethod
	def class_method(cls):
		print('类方法被调用:' + cls.x)
		cls().inst()  # 调用成员方法

	def inst(self):
		print(self.x)
		
	@property
	def x(self):
		return self._x
	
	@x.setter
	def x(self, value):
		self._x = value
	
	@x.deleter
	def x(self):
		del self._x

	def get_xxx(self):
	    return self.xxx
	def set_xxx(self):
	    self.xxx = xxx

# 继承myclass
class sub1(myclass):
	x = 'sub1'       # 公开成员变量，覆盖父类
	__name = 'tony'	 # 私有成员变量

	@staticmethod
	def static_method():
		print('覆盖父类，子类静态方法被调用')

	@classmethod
	def class_method(cls):
		print('覆盖父类，子类类方法被调用:' + cls.x)

	def __test(self):
		print('私有成员方法被调用')

	def __call(self):
		self.__test() # 类内调用私有成员方法


print('类访问类方法：类名.类方法名')
myclass.class_method()

print('类访问静态方法：类名.静态方法名')
myclass.static_method()   #非实例化调用
myclass().static_method()  #实例化调用

print('类访问公开成员变量: 类名.公开成员变量名')
print(myclass.x)

print('类访问私有成员变量 类名._类名__私有成员变量名')
print(sub1._sub1__name)

dd = sub1('fuckoff', 'suck')
print('类的实例访问私有成员 实例名._类名__私有成员变量名')
print(dd._sub1__name)

print('类的实例访问公开属性 实例名.公开属性名')
print(dd.xxx)

print('类的实例访问公开成员方法 实例名.公开成员方法名')
dd.inst()

print('类的实例访问私有成员方法 实例名._类名__私有成员方法名')
dd._sub1__call()

print('-------------------------------------------------------------------\n')

myclass.fuck = 'what' # 动态绑定一个成员变量

def demo(self):
    print('这是动态绑定的成员方法')

myclass.demo = demo # 动态绑定一个成员方法


# 类与继承
class A:
	def __init__(self):
		self.kk = '初始化数据'
	def test(self):
		print(self.kk)

class B(A):
	def test(self):
		print('B')

class C(A):
	def test(self):
		print('C')

# D(B, C)多继承, 若B和C中均有某方法, D中没有某方法, 则实例调用时先调用B的方法; 若class D(C, B):则改变了继承顺序
class D(B, C):
	def test(self):
		print('D')

print('判断A是否B的子类 issubclass(A, B)')
print(issubclass(A, B))  #A是否B的子类

B.__bases__  # B的基类
b = B()
isinstance(b, B)  # b是否B的实例
type(b)  #b的类型
dir(B)  #类B的全部属性

d = D()
print('d中是否有test方法 hasattr(实例名, 属性或方法名)')
print(hasattr(d, 'test'))

print('d的test方法是否可调用 hasattr(d.test,\'__call__\')')
if hasattr(d.test,'__call__'):
    print(getattr(d, '__call__'))

print('-------------------------------------------------------------------\n')

# 将类实例化时,会创建一个空的类实例,__init__()用于类实例的初始化,当调用了类的实例化方法后,__init__()方法会立刻被这个类的实例调用
class E:
	count = 0
	def __init__(self):
		self.fuck = 'what the fuck' #添加实例属性fuck
		E.count += 1
	def again(self,name):
		self.name = name #添加实例属性name

e = E()
print('可以直接访问实例属性fuck')
print('e.fuck: ' + e.fuck)
print('初始化实例属性name e.again(\'tony\')')
e.again('tony')
print('e.name: ' + e.name)
print('添加e的实例属性age e.age=25')
e.age = 25
print('e.age: ' + str(e.age))

e1 = E()
e2 = E()
e3 = E()
E.count  #输出4,因为__init__()被调用了4次
E.count = 2    #更改E的类属性count为2
e1.count,e2.count,e3.count,E.count  #2,2,2,2 E的全部实例的count同样被改变

e1.count = 100  #通过E的一个实例e1更改count,这时count成为e1的实例属性了
e1.count,e2.count,e2.count,E.count #100,2,2,2  只有e1的count发生改变

E.count = 8
e1.count,e2.count,e2.count,E.count #100,8,8,8  e1的count仍为100

print('-------------------------------------------------------------------\n')


print('-----__slots__限定添加属性，不能限定通过添加方法来添加属性-----------')
class F(object):
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'F object (name: %s)' % self.name

    __repr__ = __str__

    # @property把方法变成属性来调用
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, int):
            raise ValueError('birth must be an integer')
        if value > 2017 or value < 0:
            raise ValueError('birth must between 0 and 2017')
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

def set_city(self, city):
    self.city = city

F.set_city = types.MethodType(set_city, F)


# [深刻理解Python中的元类](http://blog.jobbole.com/21351/)

# @property
# 把一个getter方法变成属性，只需加上@property，此时@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值。

print('-------------------------------------------------------------------\n')

# %r 即 repr()
# %s 即 str()
class H(object):
    def __str__(self):
        return "a __str__"
    def __repr__(self):
        return "a __repr__"

dr = H()
print(dr)  #执行了__str__方法
dr         #执行了__repr__方法
"%s" % dr  #'a __str__'
"%r" % dr  #'a __repr__'

print('-------------------------------------------------------------------\n')
