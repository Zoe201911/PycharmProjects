class AuctionException(Exception):pass

class AuctionTest:
    def __init__(self,init_price):
        self.init_price = init_price
    def bid(self,bid_price):
        d =0.0
        try:
            d = float(bid_price)
        except Exception as e:
            print("转换出异常:",e)
            raise
            # raise AuctionException("竞拍价必须是数值，不能包含其他字符!")
        if self.init_price > d:
            raise AuctionException("竞拍价比起拍价低，不允许竞拍")
        initPrice = d
def main():
    at = AuctionTest(20.4)
    try:
        at.bid('df')
    except AuctionException as ae:
        print("main函数捕获的异常:",ae)

if __name__ == '__main__':
    main()


