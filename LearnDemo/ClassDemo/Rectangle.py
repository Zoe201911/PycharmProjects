class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def setsize(self,size):
        self.width,self.height = size

    def getsize(self):
        return self.width,self.height
    def delsize(self):
        self.width,self.height =0,0
    size = property(getsize,setsize,delsize,'用于描述矩形大小的属性')


print(Rectangle.size.__doc__)

help(Rectangle.size)
rect = Rectangle(4,3)
print(rect.size)
rect.size = 9,7
print(rect.height)

del rect.size

print(rect.width)

print("****************")

class Cell:
    @property #使用@property修饰方法，相当于为该属性设置getter方法
    def state(self):
        return self._state
    @state.setter #为state属性设置setter方法
    def state(self,value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'
    @property
    def is_dead(self):
        return  self._state.lower() == 'alive'
c = Cell()
c.state = 'Alive'
print(c.state)
print(c.is_dead)

class BaseClass:
    def foo(self):
        print('父类中定义的foo方法')
class SubClass(BaseClass):
    def foo(self):
        print('子类重写父类中的foo方法')
    def bar(self):
        print('执行bar方法')
        self.foo()
        BaseClass.foo(self)

sc = SubClass()
sc.bar()


class Employee:
    def __init__(self,salary):
        self.salary = salary
    def work(self):
        print('普通员工正在写代码，工资是：',self.salary)
class Customer:
    def __init__(self,favorite,address):
        self.favorite = favorite
        self.address = address
    def info(self):
        print('我是一名顾客，我的爱好是：%s，地址是%s'%(self.favorite,self.address))
class Manager(Employee,Customer):
    def __init__(self,salary,favorite,address):
        print('--Manager的构造方法')
        super().__init__(salary)
        Customer.__init__(self,favorite,address)

m = Manager(25000,'IT产品','广州')
m.work()
m.info()


