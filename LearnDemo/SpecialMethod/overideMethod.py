"""
__repr__()是Python类中的一个特殊的方法，由于object类已提供了该方法，而所有的Python类都是object类的子类
因此所有的Python对象都是具有__repr__()方法。因此当程序需要将任何对象与字符串进行连接时，都可以先调用__repr__()
方法将对象转换成字符串，然后将两个字符串连接在一起
__repr__()是一个非常特殊的方法，他是一个"自我描述"的方法，该方法通常用于实现这样一个功能：当程序员直接打印对象时，
系统将会输出该对象的"自我描述"信息，用来告诉外界，该对象具有的状态信息
object类提供的__repr__()方法总是返回该对象实现类的"类名+object at +内存地址"值，这个返回值并不能真正实现"自我描述"
功能，因此如果用户需要自定义类能实现"自我描述"的功能，就必须重写__repr__()方法
"""

class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
im = Item('mouse',29.9)
print(im.price,im.name)
print(im)
print(im.__repr__())
im_str = im.__repr__()+""
print(im_str)

class Apple:
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def __repr__(self):
        return "Apple[color = "+self.color+\
            ",weight="+str(self.weight)+"]"
a = Apple('红色',5.68)
print(a)
