

class ICBC:
    """

    """
    #表示总行的钱
    total_money = 100000000 #类变量，会被所有对象共享
    def __init__(self,name,money):
        self.name = name
        self.money = money
        ICBC.total_money -= money #从总行中扣除当前支行使用的金额
    @classmethod #类方法,修饰的目的是调用方法时可以自动传递类
    def print_total_money(cls,age):
        print("总行剩下的钱%d" % cls.total_money)
        # print(cls.name)#报错，因为类方法没有对象地址self,所以不能访问实例成员
#类方法中不能访问实例成员，实例方法中可以访问类成员
i01 = ICBC("EC",100000)
i02 = ICBC('AH',100000)
ICBC.print_total_money(12)