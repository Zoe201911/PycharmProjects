"""
all(iterable),
该函数在Python2.5版本首次出现，使用于2.5以上版本，包括Python3版本
说明：如果iterable的所有元素不为0，''，False或者iterable为空，all(iterable)返回True,否则返回false

但是如果空元组，空列表作为参数，返回True
"""

def all(iterable):
    for element in iterable:
        if not element:
            return False

    return True

print(all(['a','b','q','c','r']))

print(all(()))

print(all([]))

print(all([1,0,9])) #返回False 因为列表元素中含有0

print(all(('',1,'e')))  #返回False，因为元组中含有''

print(all(dict()))