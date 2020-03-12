#coding:utf-8
board = []
# inputStr = input("请输入您下棋的坐标，应以x,y的格式:\n")
# while inputStr != None:
#     try:
#         #将用户输入的字符串以逗号作为分隔符，分割成两个字符串
#         x_str,y_str = inputStr.split(sep=',')
#         if board[int(y_str)-1][int(x_str)-1] !="+":
#             inputStr = input("您输入的坐标点已有棋子了，请重新输入\n")
#             continue
#
#         board[int(y_str)-1][int(x_str)-1] = "."
#     except Exception:
#         inputStr = input("您输入的坐标不合法，请您重新输入，下棋坐标应以x,y的格式\n")
#         continue
#


import sys
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    c = a/b

    print("你输入的两个数的结果是:",c)

except IndexError:
    print("索引错误：运行程序时输入的参数个数不够")

except ValueError:
    print('数值错误：程序只能接收证书参数')

except ArithmeticError:
    print("算术错误")

except Exception:
    print("未知错误")

except (IndexError,ValueError,ArithmeticError):
    print("程序发生了数组越界，数字格式异常，算术异常之一")
except:
    print("未知异常")