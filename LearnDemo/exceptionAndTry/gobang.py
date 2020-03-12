"""
不管程序代码块是否处于try块中，甚至包括except块中的代码，只要执行该代码时出现异常，系统总会自动生成一个Error对象，
如果程序没有为这段代码块定义任何except块，则Python解释器无法找到处理异常的except块，程序就在此退出
先捕获小异常，再捕获大异常
"""
# inputStr = input("请您输入您的坐标，应以x,y的格式：\n")
# board = []
# while inputStr !=None:
#     try:
#         x_str,y_str = inputStr.split(sep = ',')
#         if board[int(y_str)-1][int(x_str)-1] != '+':
#             inputStr = input("您输入的坐标已有棋子，请重新输入\n")
#             continue
#         board[int(y_str-1)][int(x_str-1)] = '*'
#     except Exception:
#         inputStr = input("您输入的坐标不合法，请重新输入")
#         continue

# import sys
# try:
#     print(len(sys.argv))
#     a = int(sys.argv[1])
#     b = int(sys.argv[0])
#     c =a / b
#     print("您输入的两个数相除的结果是：",c)
# except IndexError:
#     print("索引错误：运行时输入的参数个数不够")
# except ValueError:
#     print("数值错误：程序只能接受整数参数")
# except ArithmeticError:
#     print("算术错误,被除数是0")
# except Exception:
#     print("未知错误")
"""
python的异常处理流程中还可添加一个else块，当try块没有出现异常时，程序会执行else块
当try块没有异常，而else块有异常，就能体现else块的作用了

"""

# s = input("请输入除数：")
# try:
#     result = 20/int(s)
#     print("20除以%s的结果是:%g"%(s,result))
# except ValueError:
#     print('值错误，您必须输入数值')
# except ArithmeticError:
#     print("算术错误，您不能输入0")
# else:
#     print('没有出现异常')


def else_test():
    s = input('请输入除数：')
    result = 20/int(s)
    print('20除以%s的结果是:%g'%(s,result))
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
print("******************************")

"""
为了保证一定能回收在try块中打开的物理资源，异常处理机制提供了finally块，不管try块中的代码是否出现异常
也不管哪一个except块被执行，甚至在try块或except块中执行了return语句，finally块总会被执行
如果不使用return，直接使用os._exit()来退出解释器，finally里的代码就不执行了
但是如果调用sys.exit()方法退出程序不能阻止finally块的执行，这是因为sys.exit()方法本身就是通过引发
SystemExit异常来退出程序的
"""
import os
def test():
    fis = None
    try:
        fis = open('a.txt')
    except OSError as e:
        print(e.strerror)
        return#虽然return语句也强制方法结束，但是一定会先执行finally块的代码
    finally:
        if fis is not None:
            try:
                fis.close()
            except OSError as ioe:
                print(ioe.strerror)
        print("执行finally块里的资源回收")


test()