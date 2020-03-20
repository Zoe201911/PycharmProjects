from types import MethodType

class Student(object):
    pass

def set_name(self,name):
    self.name = name

def set_age(self,age):
    self.age = age

def set_sc(self,x,y):
    self.x = x
    self.y = y

x1 = Student()
x2 = Student()

x1.set_age = MethodType(set_age,x1)
x2.set_age = MethodType(set_age,x2)

Student.setsc = MethodType(set_sc,Student)
Student.set_name = MethodType(set_name,Student)

x1.set_age(12)
x2.set_age(13)

x1.setsc("xmc","xu")

Student.set_name("hhh")

print(x1.age)
print(x2.age)
print(x1.x,x1.y)
print(x1.name)
print(x2.name)


class Dog:
    def jump(self):
        print("正在执行jump方法")

    def run(self):
        self.jump()
        print("正在执行run方法")


class ReturnSelf:
    def grow(self):
        if hasattr(self,'age'):
            self.age +=1
        else:
            self.age = 1
        return self

rs = ReturnSelf()
rs.grow().grow().grow()

print("rs的age属性值是:",rs.age)

ReturnSelf.grow(rs)


