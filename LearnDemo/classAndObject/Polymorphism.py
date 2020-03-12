"""
同一个变量x在执行同一个move()方法时，由于x指向的对象不同，因此呈现的行为特征不同，这就是多态
"""

class Bird:
    def move(self,field):
        print('鸟在%s上自由地飞翔'%field)
class Dog:
    def move(self,field):
        print('狗在%s里飞快的奔跑'%field)
x = Bird()
x.move('天空')
x = Dog()
x.move('草地')

class Canvas:
    def draw_pic(self,shape):
        print('----开始绘图----')
        shape.draw(self)

class Rectangle:
    def draw(self,canvas):
        print('在%s上绘制矩形'%canvas)

class Triangle:
    def draw(self,canvas):
        print('在%s上绘制三角形'%canvas)

class Circle:
    def draw(self,canvas):
        print('在%s上绘制圆形'%canvas)

c = Canvas()
c.draw_pic(Rectangle())

"""
Python提供了两个函数来检查类型：
1）issubclass(cls,class_or_tuple):检查cls是否为后一个类或元组包含的多个类中任意类的子类
2）isinstance（obj,class_or_tuple):检查obj是否为后一个类或者元组包含的多个类中任意类的对象
通过使用上面两个函数，程序可以方便地执行检查，然后才调用方法，这样可以保证程序不会出现意外情况
两者的区别是issubclass()的第一个参数必须是类名，而isinstance（）的第一个参数是变量，这也与
两个函数的意义对应：issubclass判断是否为子类，而isinstance()判断是否为该类或子类实例

"""
hello = 'Hello'
print('"Hello"是否是str类的实例:',isinstance(hello,str))
print('"Hello"是否是object类的子类实例',isinstance(hello,object))
print('"str"是否是object类的子类',issubclass(str,object))
my_list = [1,2,3]
print('my_list是否是list类的实例：',isinstance(my_list,list))
print('my_list是否是list类的子类',issubclass(list,object))
my_tuple = (1,)
#print('my_tuple是否是tuple类的子类h',issubclass(my_tuple,tuple))

data = (20,'fkit')
#issubclass()和isinstance()的第二个参数可以使用元组
print('data是否为列表或元组的实例:',isinstance(data,(list,tuple)))
print('str是否为list或tuple的子类：',issubclass(str,(list,tuple)))
print('str是否为list或tuple或object的子类:',issubclass(str,(list,tuple,object)))


"""
python为所有类都提供了一个__bases__属性，通过该属性可以查看该类的所有直接父类，该属性返回所有直接父类组成的元组
"""
class A:
    pass
class B:
    pass
class C(A,B):
    pass
print('A类的所有父类：',A.__bases__)
print('B类的所有父类：',B.__bases__)
print('C类的所有父类：',C.__bases__)