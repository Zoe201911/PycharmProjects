"""
迭代器
迭代器是Python最强大的功能之一，是访问集合元素的一种方式
迭代器是一个可以记住遍历的位置的对象
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束，迭代器只能往前不会后退
迭代器有两个基本方法：iter()和next()
字符串，列表或元组对象都可以用于创建迭代器

"""
import sys

# list = [1,2,3,4]
# it = iter(list)
# for x in it:
#     print(x,end=" ")
# print("xxxxxxxxxxx")
#
# i = iter(list)
# while True:
#     try:
#         print(next(i))
#     except StopIteration:
#         sys.exit()

"""
在Python中，使用yield的函数被称为生成器（generator）
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器是一个迭代器
在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next()方法时从当前位置
继续运行
"""

def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if(counter > n):
            return
        yield a
        a,b = b,a+b
        counter +=1

def main():
    f = fibonacci(10)
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()
if __name__ == '__main__':
    main()


