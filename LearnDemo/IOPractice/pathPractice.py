"""
path是PurePath的子类，它除了支持PurePath的各种操作、属性和方法之外，还会真正访问底层的文件系统，
包括判断Path对应的路径是否存在，获取Path对应路径的各种属性（如是否只读、是文件还是文件夹等）甚至可以对文件进行读写
PurePath和Path最根本的区别在于：PurePath的本质依然是字符串，而Path则会真正访问底层的路径，因此它提供了属性和
方法来访问底层的文件系统
"""

"""
path同样提供了两个子类：PosixPath和WindowsPath,前者代表UNIX风格的路径，后者代表Windows风格的路径
path对象包含了大量is_xxx()方法，用于判断该path对应的路径是否为xxx，path包含一个exists()方法，用户判断path对应的目录是否存在
path还包含一个很常用的iterdir()方法，该方法可返还Path对应目录下的所有子目录和文件，此外，path还包含一个glob()方法，用于获取
path对应目录以及子目录下匹配指定模式的所有文件，借助于glob()方法，可以非常方便地查找指定的文件
"""

from pathlib import *
#获取当前目录
p = Path('.')
#遍历当前目录下的所有文件和子目录
for x in p.iterdir():
    print(x)

#获取上一级目录
p = Path('../')
print("获取当前目录的上级目录：",p)
#获取上级目录以及所有子目录下的.py文件
for x in p.glob('**/*.py'):
    print(x)


#获取g:/publish/codes对应的目录
p = Path('g:/publish/codes')
#获取上级目录以及所有子目录下的.py文件
for x in p.glob('**/*test.py'):
    print(x)



"""
path还提供了read_bytes()和read_text(encoding = None,errors = None)方法，分别用于读取该path对应文件的字节数据（二进制数据）
和文本数据，也提供了write_bytes(data)和Path.write_text(data,encoding=None,errors = None)方法来输出字节数据（二进制数据）
和文本数据

"""
from pathlib import *

p = Path('a_test.txt')
result = p.write_text("""有一个美丽的新世界
它在远方等我
哪里有美丽的花朵
还有天真的孩子
""",encoding='UTF-8')
print(result)

content = p.read_text(encoding='UTF-8')
print(content)
bb = p.read_bytes()
print(bb)