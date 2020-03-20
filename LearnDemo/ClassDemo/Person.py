class Person:
    hair = 'black'
    def __init__(self,name='Jom',age = 8):
        self.name = name
        self.age = age
    def say(self,content):
        print(content)

    def info(self):
        print("----info函数----",self)


p = Person()

print(p.name,p.age)

p.name = 'Tom'

print(p.say("lllll"))
p.skills = ['sss','xxx']
print(p.skills)

p.bar = lambda self :print('--lambda---',self)
p.bar(p)

