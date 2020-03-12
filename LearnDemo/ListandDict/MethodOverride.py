"""
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你的父类方法
"""
class Parent:
    def myMethod(self):
        print("调用父类方法")

class Child(Parent):
    def myMethod(self):
        print("调用子类方法")


c = Child()
c.myMethod()

"""
类的私有属性
__private_attrs:两个下划线开头，声明该属性为私有，不能再类的外部被使用或者直接访问。在类内部的房中使用时self.__private_attrs
类的方法
在类的内部，使用def关键字可以为类定义一个一个方法，与一般函数定义不同，类方法必须包含参数self，且为第一个参数
类的私有方法
__private_method:两个下划线开头，声明该方法为私有方法，不能在类的外部调用，在类的内部调用self.__private_methonds
"""

class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print("__secretCount:",self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print("publicCount:",counter.publicCount)
# print("__secretCount :",counter.__secretCount)报错，实例不能访问私有变量

"""
类的专有方法：
__init__:构造函数，在生产对象时调用
__del__：析构函数，释放对象时使用
__repr__：打印，转换
__setitem__：按照索引赋值
__getitem__：按照索引获取值
__len__：获得长度
__cmp__:比较运算
__call__:函数调用
__add__:加运算
__sub__:减运算
__mul__:乘运算
__div__：除运算
__mod__:求余运算
__pow__:乘方
"""


class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self,c):
        self.c = c


