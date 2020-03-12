"""
python是动态语言，动态语言的典型特征就是：类，对象的属性，方法都可以动态增加和修改
"""
class Cat:
    def __init__(self,name):
        self.name = name
def walk_func(self):
        print('%s慢慢地走过一片草地'%self.name)
d1 = Cat('Garfield')
d2 = Cat('Kitty')
#为Cat动态添加walk()方法，该方法的第一个参数会自动绑定
Cat.walk = walk_func
d1.walk()

"""
使用type()函数定义类
使用type()定义一个Dog类，在使用type()定义类时可指定三个参数
参数一：创建的类名
参数二：该类继承的父类集合，由于Python支持多继承，因此此处使用元组指定它的多个父类，即使只有一个父类，也需要使用元组语法（必须多一个逗号）
参数三：该字典对象为该类绑定的类变量和方法，key是变量或者方法名
"""
class Role:
    pass

r = Role()
print(type(r))
print(type(Role))


def fn(self):
    print('fn函数')
#使用type()定义Doglei
Dog = type('Dog',(object,),dict(walk = fn,age=6))
d = Dog()
print(type(d))
print(type(Dog))
d.walk()
print(Dog.age)
print('******************')

"""
如果希望创建某一批类全部具有某种特征，则可通过metaclass来实现，使用metaclass可以在创建类时动态修改类定义
程序需要先定义metaclass，metaclass应该继承type类，并重写__new__()方法
metaclass类的__new__方法的作用是：当程序使用class定义新类时，如果指定了metaclass,那么metaclass的__new__方法就会被自动执行
"""
class ItemMetaClass(type):
    #cls代表被动态修改的类
    #name代表被动态修改的类名
    #bases代表被动态修改的类的所有父类
     #attr代表被动态修改的类的所有属性，方法组成的字典
    def __new__(cls,name,bases,attrs):
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
        self._discount = discount
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

b = Book("crazy python",89)
b.discount = 0.76
print(b.cal_price())
cp = CellPhone(2399)
cp.discount =0.1
print(cp.cal_price())






