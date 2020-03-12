"""
any(iterable）
该函数适用于2.5以上版本，兼容Python3
说明：如果iterable里的元素有一个不是''，0，False时any(iterable）返回true，否则返回false
参数为空的列表和元组，返回false
比较函数all(iterable)和any(iterable)的区别，any是任意，而all是全部

"""

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

#参数iterable，可迭代对象

print(any(['a','b','c']))

print(any(['',3,1]))

print(any([]))

print(any((0,False)))

print(any((0,3)))