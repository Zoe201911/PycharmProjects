class Wife:
    def __init__(self,name,age,weight):
        self.__name = name
        #本质是个障眼法（实际是蒋变量名改为：_类名_age）
        self.set_age(age)#双下划线的是私有变量
        self.__weight = weight

    def get_age(self):
        return self.__age

    def set_age(self,value):
        if 21 <=value <31:
            self.__age = value
        else:
            raise ValueError('go out')



class Amry:
    def __init__(self,name,defent,blood):
        self.set_name(name)
        self.set_defent(defent)
        self.set_blood(blood)

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_defent(self,defent):
        if defent<80:
            self.__defent = defent
        else:
            raise ValueError('error')
    def get_defent(self):
        return self.__defent

    def set_blood(self,blood):
        if 10<blood<100:
            self.__blood = blood
        else:
            raise ValueError('ERROR')

    def get_blood(self):
        return self.__blood


a01 = Amry('Zoe',60,99)
a01.set_defent(88)
print(a01.get_defent())

"""
不建议使用
w01 = Wife('lily',80,80)
w01.age = 109
w01.__age = 108 #重新创建了新的实例变量（没有改变类中定义的__age）
w01._Wife__age = 106 #识破障眼法，修改定义中的私有变量
print(w01.__dict__)#python内置变量存储对象的实例变量
"""

w01 = Wife('lily',80,80)
w01.set_age(30)
print(w01.get_age())