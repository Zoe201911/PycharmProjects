class Player:
    def __init__(self,atk):
        self.atk = atk
    def attack(self,other):
        print('玩家攻击敌人')

class Enemy:
    def damage(self,value):
        self.hp -= value
        if self.hp <=0:
            print('死亡')
