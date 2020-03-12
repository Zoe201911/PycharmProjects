"""
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你的父类的方法
类的方法使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self，且为第一个参数
"""
class Parent:
    def myMethod(self):
        print("调用父类方法")

class Child(Parent):
    def myMethod(self):
        print("调用子类方法")

c = Child()
c.myMethod()

#类的私有属性：__private_attrs：两个下划线开头，声明该属性为私有，不能再类的外部使用或者直接访问，在类的内部的方法中使用self.__private_attrs
#类的私有方法__private_method两个下划线开头，声明该方法为私有方法，不能再类的外部调用，在类的内部调用self.__private_methods
class JustCounter:
    __secretCount = 0
    publicCount = 0
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print("__secretCount is :",self.__secretCount)

counter = JustCounter()
counter.count()
print("publicCount is :",counter.publicCount)
# print(counter.__secretCount)

"""
__init__:构造函数，在生产对象时调用
__del__：析构函数，释放对象时使用
__repr__：打印，转换
__setitem__：按照索引赋值
__get
"""
