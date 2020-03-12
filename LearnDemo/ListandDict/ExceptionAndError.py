"""
异常以不同的类型出现，这些类型都作为信息的一部分打印出来，例子中的类型有ZeroDivisionError,NameError,TypeError
错误信息的前面部分显示了异常发生的上下文，并以调用栈的形式显示具体信息
try语句按照如下方式工作：
1、首先，执行try子句（在关键字try和关键字except之间的语句）
2、如果没有异常发生，忽略except子句，try子句执行后结束
3、如果在执行try子句的过程中发生异常，那么try子句余下的部分将被忽略，如果异常的类型和except之后的名称相符，那么对应的except子句将被执行。
最后执行try语句之后的代码
4、如果一个异常没有任何的except匹配，那么这个异常将会传递给上层的try中
1）一个try语句可能包含多个except子句，分别来处理不同的特定异常，最多只有一个分支会被执行
2）处理程序将只针对对应的try子句中的异常进行处理，而不是其他的try的处理程序中的异常
3）一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
"""
import sys
while True:
    try:
        x = int(input("please enter a number"))
        break
    except ValueError:
        print("Oops! That was no valid number.try again")


try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('OS error:{0}'.format(err))
except ValueError:
    print('Could not convert data to an integer')
except:
    print("Unexpected error:",sys.exc_info()[0])
    raise

#try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后，这个子句将在try子句没有发生任何异常的时候执行。
for arg in sys.argv[:]:
    try:
        f = open(arg,'r')
    except IOError:
        print('cannot open',arg)
    else:
        print(arg,'has',len(f.readlines()),'lines')
        f.close()
#使用else子句比把所有的语句都放在try子句里面要好，这样可以避免一些意想不到的而except又没有捕获到的异常
#异常处理不仅仅处理那些直接发生在try子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常
def this_fails():
    x = 1/0
def main():
    try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handling run-time error:',err)
if __name__ == '__main__':
    main()

#Python使用raise语句抛出一个指定的异常,raise唯一的一个参数指定了要被抛出的异常，它必须是一个异常的实例或者是异常的类（也就是Exception的子类）
#如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的raise语句就可以再次把它抛出

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

#无论try子句里面有没有发生异常，finally子句都会执行
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye,world')



