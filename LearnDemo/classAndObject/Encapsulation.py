"""
如果程序希望将python类中的某些成员隐藏起来，那么只要让该成员的名字以双下划线开头即可，
即使通过这种机制实现隐藏，其实依然可以绕过去，使用对象._类名__方法名（u._User__name)
"""

class User:
    def __hide(self):
        print('示范隐藏的hide方法')
    def getname(self):
        return self.__name
    def setname(self,name):
        if len(name)<3 or len(name)>8:
            raise ValueError('用户名长度必须在3~8之间')
        self.__name = name
    name = property(getname,setname)
    def setage(self,age):
        if age < 18 or age >70:
            raise ValueError('用户年龄必须在18~70之间')
        self.__age = age
    def getage(self):
        return self.__age
    age = property(getage,setage)
u = User()
u.name = 'fkih'
#u.__hide() AttributeError: 'User' object has no attribute '__hide'
u._User__hide()
u._User__name = 'fk'
u.age = 20
print(u.name,u.age)