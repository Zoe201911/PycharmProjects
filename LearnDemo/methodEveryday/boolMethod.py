"""
将x转换为Boolean类型，如果x缺省，返回False,bool也为int的子类
参数x：任意对象或者缺省，x参数是可有可无的，如果不给任何参数返回False

该函数在Python2.3以上使用，Python3中也可以正常使用
"""

print(bool())

print(bool(0))

print(bool(1))

print(bool(''))

print(bool(()))

print(bool([]))

print(bool('ba'))

print(issubclass(bool,int))