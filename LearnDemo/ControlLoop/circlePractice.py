#使用循环输出九九乘法表，输出结果如下：
for i in range(1,10):
    result = 0
    for j in range(1,i+1):
        #print("%s * %s = %s" % (i,j,i*j),end= '   ')
        print("{} * {} = {}" .format(j, i, i * j), end='   ')
    print()

#给定循环输出等腰三角形
for i in range(0,4):
    for j in range(0,4-i):
        print((' '),end='')
    print((2*i+1)*('*'))

#给定奇数3，输出（横竖斜的总和相等）


#使用循环输出菱形 。例如用户输入 7(用户输入偶数，则提示不能打印〉
n = int(input("输入一个整数：",))
if n%2 ==0:
    print("输入数不是奇数")
else:
    for i in range(0,n):
        if (n+1)/2 > i:
            for j in range(0,int((n+1)/2-i-1)):
                print((' '),end='')
            print((2*i+1)*('*'))
        else:
            num = int(i-((n-1)/2))
            for k in range(0,num):
                print((' '), end='')
            print((2*(n-i)-1)*('*'))

#方法二：
n = int(input("请输入一个整数值："))
for i in range(-n,n+1):
    if i<0:
        j=-i
    else:
        j=i
    print(' '*j+'*'*(9-2*j))

