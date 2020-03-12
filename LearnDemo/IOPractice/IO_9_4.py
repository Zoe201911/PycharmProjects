"""
PurePath的基本功能
程序可使用PurePath或者他的两个子类来创建PurePath对象，如果在UNIX或者Mac OS系统上使用PurePath创建对象，程序实际返回
PurePosixPath对象，如果在Windows系统上使用PurePath创建对象，程序实际返回PureWindowsPath对象
"""

from pathlib import *
pp = PurePath('setup.py')
print(type(pp))
pp = PurePath('crazyit','some/path','info')
print(pp)