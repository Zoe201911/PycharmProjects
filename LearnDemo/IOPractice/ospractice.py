"""
os.path模块下提供了一些操作目录的方法，这些函数可以操作系统的目录本身，该模块提供了exists()函数判断该目录是否存在，也提供了
getctime(）、getmtime(),getatime()函数来获取该目录的创建时间，最后一次修改时间，最后一次访问时间，还提供了getsize()
函数来获取指定文件的大小
"""
import os
import time

#获取绝对路径
print("获取绝对路径：",os.path.abspath("a_test.txt"))

#获取共同前缀名
print("获取共同前缀名：",os.path.commonprefix(['/usr/lib','usr/local/lib']))

# print("获取共同路径：",os.path.commonpath(['/usr/lib','usr/local/lib']))

print("获取目录：",os.path.dirname('abc/xyz/README.txt'))

print("判断指定目录是否存在：",os.path.exists('abc/xyz/README.txt'))

print("获取最近一次访问时间：",time.ctime(os.path.getatime('a_test.txt')))

print("获取最后一次修改的时间 ：",time.ctime(os.path.getmtime('a_test.txt')))

print("获取创建时间：",time.ctime(os.path.getctime('a_test.txt')))

print("获取文件大小:",os.path.getsize('a_test.txt'))

print("判断是否是文件",os.path.isfile('a_test.txt'))

print("判断是否是目录：",os.path.isdir('a_test.txt'))

print("判断是否为同一个文件：",os.path.samefile('ospractice.py','a_test.txt'))