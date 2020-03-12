"""
类（Class)：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象类是实例
类变量：类变量在整个实例化的对象中的公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用
数据成员：类变量或者实例变量用于处理类以及实例对象的相关数据
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖，也成为方法重写
实例变量：定义在方法中的变量，只作用域当前实例的类
继承：即一个派生类继承基类的字段和方法，继承也允许把一个派生类的对象作为一个基类对象对待。
实例化：创建一个类的实例，类的具体对象
方法：类中定义的函数
对象：通过类定义的数据结构实例，对象包括两个数据成员（类变量和实例变量）和方法
"""
class MyClass:
    i = 123456
    def f(self):#在类的内部，使用def关键可以我类定义一个方法，与一般函数定义不同，类方法必须包含参数self，且为第一个参数
        return 'hello world'

x = MyClass()

print("MyClass 类的属性i为:",x.i)
print("MyClass 类的方法f输出为:",x.f())

class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart

y = Complex(1.0,-4.5)
print(y.i,y.r)

class People:
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说:我 %d 岁" %(self.name,self.age))

class student(People):
    grade = ''
    def __init__(self,n,a,w,g):
        People.__init__(self,n,a,w)
        self.grade = g
    def speak(self):
        print("%s say :I am %d years old ,I am in %d grade "%(self.name,self.age,self.grade))

class Speak:
    topic = ''
    name = ''
    def __init__(self,t,n):
        self.topic = t
        self.name = n
    def speak(self):
        print("my name is %s,I am a speaker, my topic is %s"%(self.name,self.topic))

class sample(Speak,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        Speak.__init__(self,n,t)


test = sample('Tim',25,80,4,'python')
test.speak()

p = People('Zoe',25,45)
p.speak()

s = student('ken',10,60,3)
s.speak()