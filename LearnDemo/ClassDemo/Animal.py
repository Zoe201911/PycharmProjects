"""
@property:简化方法的访问，像访问属性一样访问函数，装饰过的函数返回的不再是一个函数，而是一个property对象
装饰过后的方法不再是可调用的对象，可以看做数据属性直接访问
@classmethod：定义类方法，可以通过类.方法直接访问方法，而不用实例的对象访问，简化实例化过程
既能被类调用又能被实例调用。注意参数是cls代表这个类本身。
@staticmethod：静态方法，可以理解为单纯的在类中定义一个与该类完全无关的方法
"""

class Animal():
    leg = 1
    def __init__(self,name,food):
        self.name = name
        self.food = food

    @property #属性方式访问方法：dogs.legs，不能是dog.legs()
    def legs(self):
        print("Animal all have {} head".format(Animal.leg))

    @classmethod #类方法，可以直接通过类访问实例 Class.say(instance)
    def say(cls,self):
        print("my name is {0},I like eat {1}".format(self.name,self.food))

    @staticmethod #静态方法，就是一个函数，可以和实例无关
    def count():
        print("Just a function and no relation with class")

dog = Animal("erha",'bone')
cat = Animal('mimi','fish')

dog.legs
Animal.say(dog)
dog.count()
Animal.count()