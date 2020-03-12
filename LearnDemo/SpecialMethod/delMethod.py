"""
与__init__()方法对应的是__del__()方法，__init__()方法用于初始化Python对象，而__del__()则用于
销毁Python对象，在任何Python对象将要被系统回首之时，系统都会自动调用该对象的__del__()方法
需要说明的是，不要以为对一个变量执行del操作，该变量所引用的对象就会被回收，只有当对象的引用计数变成0时，
该对象才会被回收。
"""
class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __del__(self):
        print('del删除对象')

im = Item('mouse',29.8)
x = im
del im
print('===============')

"""

"""