"""
很多时候，系统是否要引发异常，可能需要根据应用的业务需求来决定，如果程序中的数据，执行与既定的业务需求不符，这就是一种异常
由于与业务需求不符而产生的异常，必须由程序员来决定引发，系统无法引发这种异常
如果需要在程序中自行引发异常，应使用raise语句，raise语句有如下三种常用的用法：
1）raise：单独一个raise，该语句引发当前上下文中捕获的异常（比如在except块中），或默认引发RuntimeError异常
2）raise异常类：raise后带一个异常类，该语句引发指定异常类的默认实例
3）raise异常对象：引发执行的异常对象
上面三种用法最终都是要引发一个异常实例（即使指定的异常类，实际上也是引发该类的默认实例），raise语句每次只能引发一个异常实例
"""
# def main():
#     try:
#         mtd(3)
#     except Exception as e:
#         print('程序出现异常',e)
#
#     mtd(3)
#
# def mtd(a):
#     if a > 0:
#         raise ValueError("a的值大于0，不符合要求")
#
#
# if __name__ == '__main__':
#     main()



"""
为了实现这种通过多个方法协作处理一个异常的情形，可以在except块中结合raise语句来完成
"""

class AuctionException(Exception):pass
class AuctionTest:
    def __init__(self,init_price):
        self.init_price = init_price
    def bid(self,bid_price):
        d =0.0
        try:
            d = float(bid_price)
        except Exception as e:
            print("转换出异常：",e)
            raise AuctionException("竞拍价必须是数值，不能包含其他字符")
        if self.init_price >d:
            raise  AuctionException("竞拍价比起拍价低，不许竞拍")
        init_price = d
def main():
    at = AuctionTest(20.4)
    try:
        at.bid('df')
    except AuctionException as ae:
        print("main函数捕获的异常",ae)

if __name__ == '__main__':
    main()
"""
上面程序中的bid方法里的异常，系统打印了该异常的字符串信息，接着引发一个AuctionException
"""
