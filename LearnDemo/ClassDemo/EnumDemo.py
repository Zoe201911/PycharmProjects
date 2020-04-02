"""
两种方式定义枚举类：
1、直接使用Enum列出多个枚举值来创建枚举类
2、通过继承Enum基类来派生枚举类
"""
import enum

# Season = enum.Enum(Season,('Spring','Summer','Auntum','Winter'))

from enum import Enum,unique,auto

@unique
class Mistake(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4

class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name



class Ordinal(AutoName):
    NORTH = auto()
    SOURTH = auto()
    EAST = auto()
    WEST = auto()

print(list(Ordinal))




class Gender(enum.Enum):
    MAIL = '男',"ll"
    FAMAIL = '女',"xxx"
    def __init__(self,cn_name,desc):
        self._cn_name = cn_name
        self._desc = desc

    @property
    def desc(self):
        return self._desc
    @property
    def cn_name(self):
        return self._cn_name

print(Gender.FAMAIL.desc)