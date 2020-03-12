"""
如果程序需要在except块中访问异常对象的相关信息，则可通过异常对象声明变量来实现，当Python解释器决定调用某个except块来处理该
异常对象时，会将异常对象赋值给except块后的异常变量，程序即可通过该变量来获取异常对象的相关信息
所有的异常对象都包含如下几个常用属性和方法
args:该属性返回异常的错误编码和描述字符串
errno:该属性返回异常的错误编码
strerror：该属性返回异常的描述字符串
with_traceback()：通过该方法可处理异常的传播轨迹信息
"""

def foo():
    try:
        fis = open("a.txt")
    except Exception as e:
        print(e.args)
        print(e.errno)
        print(e.strerror)

foo()

#python 的异常处理流程中还可以添加一个else块，当try块没有出现异常时，程序会执行else块

s = input("please input a chushu:")
try:
    result = 18/int(s)
    print('18 chuyi %s result is %g :'%(s,result))
except ValueError:
    print("zhicuowu ,shu zheng shu ")
except ArithmeticError:
    print('chushu buneng wei 0')
else:
    print("no exception")

"""
如果希望某段代码的异常能被后面的except块捕获，那么就应该将这段代码放在try块的代码之后，如果希望某段代码的
异常能向外传播（不被except块捕获）那么就应该将这段代码放在else块中
"""


print("9999999999999999999999999999")
def else_test():
    s = input('请输入除数：')
    result = 20/ int(s)
    print("20除以%s的结果是:%g"%(s,result))
def right_main():
    try:
        print('try块的代码，没有异常')
    except:
        print('程序出现异常')
    else:
        else_test()
def wrong_main():
    try:
        print('try块的代码，没有异常')
        else_test()
    except:
        print('程序出现异常')

wrong_main()
right_main()

