"""
delattr(object,name)
删除object对象名为name的属性，这个函数命名真是简单易懂，和juery里面差不多，但是功能一样
"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age



tom = Person('Tom',20)
print(dir(tom))

delattr(tom,'age')

print(dir(tom))

#print(tom.age)  报错，AttributeError: 'Person' object has no attribute 'age'