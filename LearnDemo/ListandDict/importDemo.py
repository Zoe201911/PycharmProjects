"""
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py，模块可以被别的程序引入，以使用该模块中的函数等功能
"""

import sys
print("命令行参数如下：")
for i in sys.argv:
    print(i)

print('\n\nPython 路径为:',sys.path,'\n')


def fib(n):
    a,b = 0,1
    while b < n:
        print(b,end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    result = []
    a,b = 0,1
    while b < n:
        result.append(b)
        a,b = b,a+b
    return result


def main():
    fib(1000)
    print(fib2(100))


if __name__ == '__main__':
    main()