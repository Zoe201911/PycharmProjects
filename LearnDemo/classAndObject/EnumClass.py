"""
程序有两种方式来定义枚举类
1）直接使用Enum列出多个枚举值来创建枚举
2）通过继承Enum基类来派生枚举类
使用Enum()函数来创建枚举值，该构造方法的第一个参数是枚举类的类名：第二个参数是一个元组，用于列出有所枚举值
1）定义枚举时，成员名称不允许重复
2）默认情况下，不同的成员值允许相同，但是两个相同值的成员，第二个成员的名称被视作第一个成员的别名
3)如果枚举中存在相同值的成员，在通过值获取枚举成员时，只能获取到第一个成员
4）如果要限制定义枚举时，不能定义相同的成员，可以使用装饰器@unique（需要导入unique模块）
5）
"""
from enum import Enum,unique
@unique
class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7
    #red_alias = 1  报错ValueError: duplicate values found in <enum 'Color'>: red_alias -> red


for color in Color:
    print(color.name,color.value)


#Python提供了一个__members__属性，该属性返回一个dict字典，字典包含了该枚举的所有枚举实例
#程序颗通过遍历__members__属性来访问枚举的所有实例
for color in Color.__members__.items():
    print(color)

#枚举成员可以进行同一性比较
print(Color.red is Color.red)
print(Color.red is Color.blue)
#枚举成员可以等值比较,但是不能进行大小比较
print(Color.blue == Color.red)

import enum
class Orientation(enum.Enum):
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH = '北'
    def info(self):
        print('这是一个代表方向【%s】的枚举'%self.value)
print(Orientation.SOUTH)
print(Orientation.SOUTH.value)
print(Orientation['WEST'])
print(Orientation('南'))
Orientation.EAST.info()
for name ,member in Orientation.__members__.items():
    print(name,">",member,",",member.value)



class Gender(enum.Enum):
    MALE = '男','阳刚之力'
    FEMALE = '女','柔顺之美'
    def __init__(self,cn_name,desc):
        self._cn_name = cn_name
        self._desc = desc
    @property
    def des(self):
        return self._desc
    @property
    def cn_name(self):
        return self._cn_name

print('FAMALE的name：',Gender.FEMALE.name)
print('FAMALE的value:',Gender.FEMALE.value)
print('FAMALE的cn_name：',Gender.FEMALE.cn_name)
print('FAMALE的desc:',Gender.FEMALE.des)