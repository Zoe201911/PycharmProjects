"""
封装变量，使用property(读取方法，写入方法），封装变量
公开的实例变量缺少逻辑验证，私有的实例变量与两个公开的方法相结合，又使调用者的操作略显复杂
而属性可以将两个方法的使用方式像操作变量一样方便
1、定义：
@property
def name(self):
    :return self.__name
@name.setter
def name(self,value)
    self.__name = value
2、调用:
 对象.属性名 = 数据
 变量 = 对象。属性名

3、说明
----通常两个公开的属性，包含一个私有变量
----@property负责读取，@属性名.setter负责写入
----只写：属性名= property(None,写入方法名）

"""
class Wife:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    @property #创建property对象只负责读取
    def age(self):
        return self.__age
    @age.setter #只负责拦截写入操作
    def age(self,age):
        if 21<age<=31:
            self.__age = age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self,weight):
        self.__weight = weight


w01 = Wife('Zoe',25,45)
w01.age = 25
print(w01.age)