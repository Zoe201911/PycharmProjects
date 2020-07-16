class Enemy:
    def __init__(self,name ,hp,atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def get_name(self):
        return self.__name
    def set_name(self,value):
        self.__name = value

    def get_hp(self):
        return self.__hp
    def set_hp(self,value):
        self.__hp = value

    def get_atk(self):
        return self.__atk
    def set_atk(self,value):
        self.__atk = value
    name = property(get_name,set_name)
    hp = property(get_hp,set_hp)
    atk = property(get_atk,set_atk)

e01 = Enemy('lily',1000,3000)
e01.name = 'Hanmeimei'
print(e01.name)

class Enemy1:
    def __init__(self,name,hp,atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,hp):
        self.__hp = hp
    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self,atk):
        self.__atk = atk

e02 = Enemy1('Zoe',1000,20)
print(e02.name)
e02.name = 'lily'
print(e02.name)