This is test
没有do...while循环
"""
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("Sum of 1 until %d:%d"%(n,sum))

languages = ['C','C++','Perl','Python']
for x in languages:
    if x == 'Perl':
        break
    print(x)


#如果你需要遍历数字序列，可以使用内置range()函数，他会生成一个数列
for i in range(5):
    print(i)
print("xxxxxxxxxx")
for i in range (4,9):
    print(i)
print("xxxxxxxxxx")
#也可以使用range以制定数字开始并指定不同的增量（甚至可以是负数，这个也叫'步长'
for i in range(0,10,3):
    print(i)
print("xxxxxxxxxx")
for i in range(-10,-100,-30):
    print(i)
print("x************x")

a = ['Marry','Cindy','kitty','Zoe']
for i in range(len(a)):
    print(i,a[i])
print("            ")
"""
break和continue语句以及循环中的else子句
1、break语句可以跳出for和while的循环体，如果你从for或者while循环中终止，任何对应的循环else块将不执行
2、continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
3、循环语句可以有else字句，它在穷尽列表或条件变为假循环终止时被执行，但循环被break终止时不执行
"""
for n in range(2,10):
    for x in range(2,n):
        if n%x == 0:
            print(n,'equals',x,'*',n//x)

        else:
            print(n,'is a prime number')
        breakThis is test
This is test
This is test
