"""
小明在银行取钱
"""

class Person:
    def __init__(self,name,money):
        self.name = name
        self.money = money
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,money):
        self.__money = money

    def get_money(self, name, bank,money):
        print("%s去%s取%s钱" % (name, bank.name,money))
        bank.getMoney(bank.name)





class Bank:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    def getMoney(self,name):
        print('去%s取钱'%name)

xm = Person('xiaoming','100W')
bk = Bank('ICBC')
xm.get_money('xiaoming',bk,'100W')

