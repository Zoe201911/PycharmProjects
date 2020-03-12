"""
使用str.format()函数格式化输出值
如果希望将输出值转化成字符串，可以使用repr()或则str()函数来实现
str()函数返回一个用户易读表达式
repr()产生一个解释器易读的表达式,可以转义字符串中的特殊字符,且repr()参数可以是Python的任何对象
"""

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    # print("###############")
    print(repr(x*x*x).rjust(4))

#rjust()方法将字符串靠右，并在左边填充空格，rjust()里的参数是几，就在左边添加几个空格

for x in range(1,11):
    print(repr(x).ljust(4),repr(x*x).ljust(6),end=' ')
    # print("###############")
    print(repr(x*x*x))


table = {'Sjoerd':4127,"Jack":4098,'Deab':7678}
for name,phone in table.items():
    print('{0:10}===>{1:10d}'.format(name,phone))


# f = open('importDemo.py','r')
# print(f.readline())#会从文件中读取单独的一行，换行符为'\n'  f.readline()如果返回一个空字符串，说明已经读取到最后一行
# print("$$$$$$$$$$$$$$")
# print(f.readlines())#将返回该文件中包含的所有行
# print("$$$$$$$$$$$$$$")
# print(f.read())#为了读取一个文件的内容，调用f.read(size),这将读取一定数目的数据，然后作为字符串或字节对象的返回，size是一个可选的数字类型的参数，当size被忽略了或者为负，那么该文件的所有的内容将被读取并且返回
# f.close()

m = open('Whileloop.py','r+')
for line in m:
    print(line, end=' ')
print("￥￥￥￥￥￥￥￥￥￥￥")
count = m.write('This is test\n')
print(count)
print("￥￥￥￥￥￥￥￥￥￥￥m.tell")
print(m.tell())
m.close()