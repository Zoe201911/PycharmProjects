"""
联系：定义对象计算器
"""

class Wifi:

    total_num = 0

    @classmethod
    def print_num(cls):
        print("一共%d个" % cls.total_num)

    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
        Wifi.total_num += 1




w01 = Wifi('Lily',18,90)
w02 = Wifi('Lucy',20,88)

Wifi.print_num()
print(Wifi.total_num)