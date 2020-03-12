import random

i = 1
a = random.randint(1,100)
b = int(input("输入一个0-100中的一个数字\n然后查看是否跟电脑上一样："))
while a!=b:
    if a>b:
        print('您第%d次输入的数字小于电脑随机数字'%i)
        b = int(input('请再次输入数字:'))
    else:
        print('您%d次输入的数字大于电脑随机数字'%i)
        b = int(input('请再次输入数字：'))
    i =+1

else:
    print('恭喜您，你第%d次输入的数字跟电脑输入的随机数字%d一样'%(i,b))