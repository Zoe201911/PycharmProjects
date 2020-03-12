class User:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    def getfullname(self):
        return self.first+','+self.last
    def setfullname(self,fullname):
        first_last = fullname.rsplit(',')
        self.first = first_last[0]
        self.last = first_last[1]
    #使用property（）函数定义fullname属性，只传入两个参数，该属性是一个读写属性，但不能删除
    fullname = property(getfullname,setfullname)
u = User('悟空','孙')
print(u.fullname)
u.fullname = 'Zoe,Zhang'
u.setfullname('qin,shihuang')
print(u.fullname)
print(u.first)
print(u.last)


class Cell:
    #使用@property修饰方法，相当于为该属性设置getter方法
    @property
    def state(self):
        return self._state
    #为state属性设置setter方法
    @state.setter
    def state(self,value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'
    #为is_dead属性设置getter方法
    #只有getter方法的属性是只读属性
    @property
    def is_dead(self):
        return not self._state.lower()=='alive'
c = Cell()
#修改state属性
c.state = 'Alive'
#c.is_dead = True 程序执行报错，AttributeError: can't set attribute，因为is_dead没有setter方法，只有getter方法
#访问state属性
print(c.state)
#访问is_dead属性
print(c.is_dead)