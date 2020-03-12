"""
如果一个异常在try子句（或者在except和else子句里）被抛出，而又没有任何的except把它截住，那么这个异常会在finally子句执行后再次被抛出。
"""

#with关键字就可以保证文件之类的对象在使用完之后一定会正确的执行他的清理方法
#这段代码执行完毕后，就算在处理过程中出问题了，文件f总是会被关闭
def openfile():
    with open("myfile.txt") as f:
        for line in f:
            print(line,end="")


def devide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero")
    else:
        print("result is",result)
    finally:
        print("executing finally clause")


def main():
    # devide(1,'111')
    openfile()

if __name__ == '__main__':
    main()