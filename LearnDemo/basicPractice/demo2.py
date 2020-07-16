"""
封装变量，使用property(读取方法，写入方法），封装变量
"""
class Wife:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def get_age(self):
        return self.__age
    def set_age(self,age):
        if 21<age<=31:
            self.__age = age
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_weight(self):
        return self.__weight
    def set_weight(self,weight):
        self.__weight = weight

    age = property(get_age,set_age)#属性，拦截对age变量的读写操作
    name = property(get_name,set_name)
    weight = property(get_weight,set_weight)



w01 = Wife('Zoe',25,45)
w01.age = 25
print(w01.age)