import os
import shutil
import glob
import sys
import re
import math
import random
from datetime import date

os.getcwd()#返回当前工作目录
print(os.getcwd())

shutil.copyfile('myfile.txt','testfile.txt')

print(glob.glob('*.py'))#glob提供了一个函数用于从目录通配符搜索中生成文件列表

print(sys.argv)

#正则表达式工具，对于复杂的匹配和处理，正在表达提供了简洁、优化的解决方案
print(re.findall(r'\bf[a-z]*','which foot or hand fell fastest'))
print(re.sub(r'(/b[a-z]+) \1',r'\1','cat in the hat'))

str = 'tea for too'
str.replace('too','two')
print(str)

print(math.cos(math.pi/4))
print(math.log(1024,2))

print(random.choice(['apple','pear','banana']))
print(random.sample(range(100),10))

now = date.today()
print(now)
print(now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B'))

birthday = date(1990,5,2)
print((now-birthday).days)