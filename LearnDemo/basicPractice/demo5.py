"""
封装：
1、数据角度讲，将一些基本数据类型复合成一个自定义类型
2、行为角度讲，向类外提供必要的功能，隐藏实现的细节
3、设计角度讲:
1)分而治之：
----将一个大的需求分解为许多类，，每个类处理一个独立的功能
----拆分好处，便于分工，便于复用，可扩展性强
2）变则蔬之：(衡量哪里会变化）
----变化的地方独立封装，避免影响其他类
3）高内聚
----类中各个方法都在完成一项任务（单一职责的类）
4）低耦合
----类与类的关联性与依赖度要低（每个类独立），让一个类的功能独立
"""

class Person:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    def go_to(self,position,type):
        type.run(position,type.name)

lz = Person('laozhang')


class Cars:
    def __init__(self,name):
        self.name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    def run(self,position,name):
        print('驾驶%s去%s'%(name,position))

car = Cars('BMW')
lz.go_to('dongbei',car)