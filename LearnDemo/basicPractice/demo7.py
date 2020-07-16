"""
封装：
   数据角度：将多个变量封装到一个自定义类中
   优势"符合人了的思考方式，可以将数据与对数据的操作封装到一起
   功能角度：对外提供必要的功能，隐藏实现的细节
   ---私有化：将名称命名为以双下划线开头__aa
   __slots__限定一个类创建的实例只能有固定的实例变量，不能添加新的实例变量
   设计角度：
        分而治之：将大的需求分解为多个类，每个类负责一个职责
        变则疏之：遇到变化点单独封装为一个类
        高内聚：一个类有且只有一个发生变化的原因
        低耦合：类与类之间的关系松散

"""
class Student:
    __slots__ = ('name','age')
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_self(self):
        print(self.name,self.age)

s01 = Student('hello',22)
# s01.nmae = 'kitty'
# print(s01.nmae)

class Student01:

    __slots__ = ("__age")
    def __init__(self,age):
        self.age = age

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age = age

s02 = Student01(23)
print(s02.age)


class Person:
    def __init__(self,name,ablitiy,salary):
        self.name = name
        self.ablitiy = ablitiy
        self.salary = salary

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def ablitiy(self):
        return self.__ablitiy
    @ablitiy.setter
    def ablitiy(self,ablitiy):
        self.__ablitiy = ablitiy

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        self.__salary = salary


    def teach(self,other):
         print('%s教%s去%s'%(self.name,other.name,self.ablitiy))

    def work(self):
        print(self.name + '上班挣了'+self.salary)






















