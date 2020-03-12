"""
定义子类的语法：在原来的类定义后增加圆括号，并在圆括号中添加多个父类，即可表明该子类继承了这些父类
object类是所有类的父类，要么是直接父类，要么是间接父类。父类包含的范围总比子类包含的范围要大，python支持多继承，推荐尽量不使用

"""
class Fruit:
    def info(self):
        print('我是一个水果！重%g'%self.weight)
class Food:
    def taste(self):
        print('不同食物的口感不同')

class Apple(Fruit,Food):
    def info(self):
        print("我是一只苹果，是%s色的"%self.color)

a = Apple()
a.weight = 5.6
a.color = '粉'
a.info()
a.taste()
"""
档一个子类有多个直接父类时，该子类会继承得到所有父类的方法，但是如果多个父类中包含了同名的方法，此时排在前面的
父类中的方法会'遮蔽'排在后面的父类中的同名方法
"""
class Item:
    def info(self):
        print("Item中方法:",'这是一个商品')
class Product:
    def info(self):
        print('Product中方法：','这是一个工业产品')
class Mouse(Item,Product):
    pass

m = Mouse()
m.info()#Item排在前面，具有更好的优先级，Python会优先到Item父类中搜寻方法，一旦在Item中搜寻到目标方法，Python就不会继续向下搜寻了


"""
重写父类的方法:子类包含与父类同名的方法的现象被称为方法重写（Override)，也被称为方法覆盖，可以说子类重写了父类的方法
也可以说子类覆盖了父类的方法

"""
class Bird:
    def fly(self):
        print("我在天空自由飞翔。。。。")
class Ostrich(Bird):
    def fly(self):
        print("我只能在地上奔跑.....")

os = Ostrich()
os.fly()

"""
使用未绑定方法调用被重写的方法
python类相当于类空间，因此Python类中的方法本质上相当于类空间内的函数。所以即使是实例方法，Python也允许通过类名调用，区别在于：
在通过类名调用实例方法时，Python不会为实例方法的第一个参数self自动绑定参数值，而是需要程序显试的绑定第一个参数self。这种机制
被称为未绑定方法
"""
class BaseClass:
    def foo(self):
        print("父类中定义的foo方法")
class SubClass(BaseClass):
    def foo(self):
        print('子类重写父类中的foo方法')
    def bar(self):
        print('执行bar方法')
        self.foo()
        BaseClass.foo(self)
sc = SubClass()
sc.bar()
sc.foo()

"""
使用super函数调用父类的构造方法，Python的子类也会得到父类的构造方法，如果子类有多个直接父类
那么排在前面的父类的构造方法会被优先使用
Python要求：如果子类重写了父类的构造方法，那么子类的构造方法必须调用父类的构造方法，子类的构造方法调用父类的构造方法有两种方式：
1）使用未绑定方法，这种方式很容易理解，因为构造方法也是实例方法，当然可以通过这种方式来调用
2）使用super()函数调用父类的构造方法
"""
class Employee:
    def __init__(self,salary):
        self.salary = salary
    def work(self):
        print("普通员工正在写代码，工资是:",self.salary)
class Customer:
    def __init__(self,favorite,address):
        self.favorite = favorite
        self.address = address
    def info(self):
        print('我是一个顾客，我的爱好是:%s，地址是%s'%(self.favorite,self.address))

class Manager(Employee,Customer):
    def __init__(self,salary,favorite,address):
        print('---manager的构造方法---')
        #通过super()函数调用父类的构造方法
        super().__init__(salary)
        #使用未绑定方法调用父类的构造方法
        Customer.__init__(self,favorite,address)

m = Manager(30000,'IT test','上海')
m.work()
m.info()
