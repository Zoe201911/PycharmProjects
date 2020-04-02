# inputStr = input("请输入您的坐标，应以x,y格式：\n")
# board = 0
# while  inputStr != None :
#     try:
#         x_str,y_str = inputStr.split(sep = ',')
#         if board[int(y_str)-1][int(x_str)-1] != "+":
#             inputStr = input("您输入的坐标已有棋子，请重新输入\n")
#             continue
#         board[int(y_str)-1][int(x_str)-1] = "*"
#
#     except Exception:
#         inputStr = input("您输入的坐标不合法请重新输入")
#         continue

"""
先处理小异常，再处理大异常
"""
# import sys
# try:
#     a = int(sys.argv[1])
#     b = int(sys.argv[2])
#     c = a/b
#     print("您输入的两个数相除的结果是:",c)
# except(IndexError,ValueError,ArithmeticError):
#     print("程序发生了数组越界，数字格式异常，算术异常之一")
# except:
#     print("未知异常")
#
#
#
# def foo():
#     try:
#         fis = open("a.txt")
#     except Exception as e :
#         print(e.args)
#         print(e.errno)
#         print(e.strerror)
#
# foo()
# #当程序中的try块中没有出现异常时，程序就会执行else块
# s = input('请输入除数:')
# try:
#     result = 20/int(s)
#     print('20除以%s的结果是：%g'%(s,result))
# except ValueError:
#     print('值错误，您必须输入数值')
# except ArithmeticError:
#     print('算术错误，您不能输入0')
#
# else:
#     print('没有出现异常')


print('888888888888888888888888')
"""
放在else块汇总的代码所引发的异常不会被except块捕获，所以若果希望某段代码的异常能被
后面的except块捕获，那么就应该蒋这段代码放在try块的代码之后。如果希望某段代码的异常
能向外传播（不被except块捕获），那么就应该将这段代码放在else块中
"""
#
# def else_test():
#     s = input('请输入除数：')
#     result = 20/int(s)
#     print('20除以%s的结果是：%g'%(s,result))

# def right_main():
#     try:
#         print('try块的代码，没有异常')
#     except:
#         print('程序出现异常')
#     else:
#         else_test()
#
#
# def wrong_main():
#     try:
#         print('try块的代码，没有异常')
#         else_test()
#     except:
#         print('程序出现异常')


# right_main()0
# wrong_main()

"""
如果try块的某条语句引发了异常，该语句后的其他语句通常不会获得执行的机会，这将导致位于该语句之后的资源回收语句得不到执行
如果在except块里进行资源回收，因为except块完全可能得不到执行，这将导致不能及时收回这些物理资源
为了保证一定能回收try块中打开的物理资源，异常处理机制提供了finally快，不管try块中的代码是否出现异常，也不管哪一个except
块被执行，甚至在try块或者except块中执行了return语句，finally块总会被执行
"""

# import os
# def test():
#     fis = None
#     try:
#         fis = open("a.txt")
#     except OSError as e :
#         print(e.strerror)
#         # return #虽然return语句也强制方法结束了，但一定会先执行finally块的代码
#         os._exit(1)#如果异常处理的代码中使用os._exit(1)来退出，则finally块将失去执行的机会
#     finally:
#         if fis is not None:
#             try:
#                 fis.close()
#             except OSError as ioe:
#                 print(ioe.strerror)
#         print("执行finally块里的资源回收")
#
#
#
# test()

#不要在finally块中使用return或raise等导致方法终止的语句，一旦在finally块中使用了return或raise语句，将会
#导致try块，except块中的return、raise语句失效,所以尽量避免在finally里使用return或者raise等刀子方法终止的语句

def test1():
    try:
        return True
    finally:
        return False

a = test1()
print(a)

#使用raise触发异常
# x = 10
# if x>5:
#     raise Exception('x不能大于5，x值为：{}'.format(x))

class AuctionException(Exception):
    pass

class AuctionTest:
    def __init__(self,init_price):
        self.init_price = init_price
    def bid(self,bid_price):
        d =0.0
        try:
            d = float(bid_price)
        except Exception as e :
            print("转换出异常：",e)
            raise AuctionException('竞拍价必须是数值，不能包含其他字符！')
        if self.init_price > d :
            raise AuctionException('竞拍价比起拍价低，不允许竞拍')
        initPrice = d
def main():
    at = AuctionTest(20.4)
    try:
        at.bid('df')
    except AuctionException as ae:
        print('main函数捕获的异常：',ae)

main()