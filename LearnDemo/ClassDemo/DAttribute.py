from types import MethodType

class Cat:
    def __init__(self,name):
        self.name = name
def walk_func(self):
        print('%s 慢慢地走过'%self.name)

d1 = Cat('Carfield')
d2 = Cat('Kitty')

Cat.walk = walk_func
d1.walk()
d2.walk()

class Dog:
    __slots__ = ('walk','age','name')
    def __init__(self,name):
        self.name = name

d = Dog('Snoopy')
d.walk = MethodType(lambda self:print('%s正在慢慢地走'%self.name),d)

d.age = 5
d.walk()
# d.foo = 30报错
Dog.bar = lambda self:print('abc')
d.bar()

"""
__shots__属性指定的限制只对当前类起作用，如果要限制子类的实例动态添加属性和方法，则需要在子类中也定义__shots__属性，这样
子类的实例允许动态添加属性和方法就是子类的__shots__元组加上父类的__shots__元组
"""
class GunDog(Dog):
    def __init__(self,name):
        super().__init__(name)
    pass

gd = GunDog('Puppy')
gd.speed = 99
print(gd.speed)

def sum(arg1,arg2):
    total = arg1 + arg2
    return total
print(sum(10,20))

sum = lambda x,y:x+y

print(sum(10,20))
"""
参数一：创建的类名
参数二：该类继承的父类集合，由于Python支持多继承，因此此处使用元组指定它的多个父类，即使只有一个父类，也需要使用元组的语法（必须要多一个逗号）
参数三：该字典对象为该类绑定类变量和方法
"""

def fn(self):
    print('fn函数')

Dog = type('Dog',(object,),dict(walk=fn,age =6))
d = Dog()
print(type(d))
print(type(Dog))
d.walk()
print(d.age)
print("**********************8")

class ItemMetaClass(type):
    #cls代表被动态修改的类
    #name代表被动态修改的类名
    #bases代表被动态修改的类的所有父类
    #attrs代表被动态修改的类的所有属性，方法组成的字典
    def __new__(cls, name,bases, attrs):
        attrs['cal_price'] = lambda self:self.price*self.discount
        return type.__new__(cls,name,bases,attrs)

class Book(metaclass=ItemMetaClass):
    __slots__ = ('name','price','_discount')
    def __init__(self,name,price):
        self.name = name
        self.price = price
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self,discount):
        self._discount =  discount

class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ('price','_discount')
    def __init__(self,price):
        self.price = price

    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self,discount):
        self._discount = discount

b = Book('it',89)
b.discount = 0.76
print(b.cal_price())
cp = CellPhone(2399)
cp.discount = 0.85
print(cp.cal_price())
