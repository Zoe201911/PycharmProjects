"""
python提供了非常丰富的I/O支持，他即提供了pathlib和os.path来操作各种路径，也提供了全局的open()函数来打开文件
在打开文件后，程序即可以读取文件的内容，也可以向文件输出内容。而且Python提供多种方式来读取文件内容
Python还提供了tempfile模块来创建临时文件和临时目录，tempfile模块下的高级API会自动管理临时文件的创建和删除
当程序不再使用临时文件和临时目录时，程序会自动删除临时文件和临时目录

path:代表访问实际文件系统的"真正路径"，path对象可用于判断对应的文件是否存在，是否为文件、是否为目录等，path
同样由两个子类，即PosixPath和WindowsPath

程序使用PurePath或它的两个子类创建PurePath对象，如果在Unix或者Mac os系统上使用PurePath创建对象，程序
实际返回PurePosixPath对象，如果在Windows系统上使用PurePath创建对象，程序实际返回PureWindowsPath对象
程序在创建PurePath和Path时，既可以传入单个路径字符串，也可以传入多个路径字符串，PurePath会将他们拼成一个字符串
"""

from pathlib import *

#创建PurePath，实际上使用PurePosixPath
pp = PurePath('setup.py')
print("pp的类型是：",type(pp))
pp = PurePath('crazyit','some/path','info')

#看输出Windows风格的路径
print(pp)

pp = PurePath(Path('Crazyit'),Path('info'))

print(pp)

pp = PurePosixPath('crazyit','some/path','info')

print(pp)

pp = PurePath()#系统默认创建代表当前路径的PurePath，相当于传入点号

print(pp)

pp = PurePosixPath('/etc','/usr','lib64')
print(pp)
pp = PureWindowsPath('c:/Windows','d:info')
print(pp)

#如果在创建PurePath时传入的路径字符串中包含多余的斜杠和点号，系统会直接忽略他们，但是不会忽略亮点，因为亮点在路径中有实际意义（两点电表上一级路径）
pp = PurePath('foo/bar')
print(pp)
pp = PurePath('foo/./bar')
print(pp)
pp = PurePath('foo/../bar')
print(pp)

print("比较两个UNIX风格的路径，区分大小写：",PurePosixPath('info') == PurePosixPath("INFO"))
print("比较两个Windows风格的路径，不区分大小写:",PureWindowsPath('info') == PureWindowsPath('INFO'))

pp = PureWindowsPath('abc')
print(pp/'xyz'/'wawa')

pp2 = PurePosixPath('haha','hehe')
print(pp / pp2)

#PurePath的本质其实就是字符串，因此程序可使用str()将它们恢复成字符串对象，在恢复成字符串对象时会转换为对应平台风格的字符串

pp = PureWindowsPath('abc','xyz','wawa')
print(str(pp))

pp = PurePosixPath('abc','xyz','wawa')
print(str(pp))