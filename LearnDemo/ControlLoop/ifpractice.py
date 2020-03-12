"""
循环语句的4个部分：
1）初始化语句：一条或者多条语句，用于完成一些初始化工作，初始化语句在循环开始之前执行
2）循环条件：这是一个布尔表达式，这个表达式能决定是否执行循环体
3）循环体：这部分是循环的主体，如果循环条件允许，这个代码块将被重复执行
4）迭代语句：这个部分在一次执行循环体结束后，对循环条件求值之前执行，通常用于控制循环条件中的变量，使得循环在合适的时候结束
在使用while循环时，一定要保证循环条件有变成假的时候，否则这个循环将成为一个死循环
"""

count_i = 0
while count_i<10:
    print("count:",count_i)
    count_i+=1
print("while loop is down")

a_tuple = ('abc','abw','uij','ppp')
i = 0
while  i<len(a_tuple):
    print("a_tuple",a_tuple[i])
    i +=1

src_list = [12, 45, 34,13, 100, 24, 56, 74, 109]
a_list = []
b_list = []
c_list = []
while len(src_list) > 0:
    num = src_list.pop()
    if num % 3 == 0:
        a_list.append(num)
    elif num % 3 == 1:
        b_list.append(num)
    else:
        c_list.append(num)
print("整除3的数：",a_list)
print("除以3余1的数：",b_list)
print("除以3余2的数：",c_list)


s_max = input("请输入您想计算的阶乘：")
mx = int(s_max)
result = 1
for num in range(1,mx+1):
    result *= num
print(result)

src_list = [12, 45, 3.4, 13,'a',4 ,56,'crazyit', 109.5]
my_sum = 0
my_count = 0
for src in src_list:
    if isinstance(src,int) or isinstance(src,float):
        print(src)
        my_sum += src
        my_count +=1
print('总和：',my_sum)
print('平均数:',my_sum/my_count)

for i in range(0,len(src_list)):
    print('第%d个元素是%s' % (i,src_list[i]))


my_dict={'语文': 89, '数学': 92, '英语': 80}
for key,value in my_dict.items():
    print("key:",key)
    print("value:",value)
print("*******************")
for key in my_dict.keys():
    print('key:',key)
    print('value:',my_dict[key])
print("*******************")
for value in my_dict.values():
    print('value:',value)

src_list = [12, 45, 3.4, 12,'fkit', 45, 3.4,'fkit', 45, 3.4]
src_dict = {}
for num in src_list:
    if num in src_dict.keys():
        src_dict[num]+=1
    else:
        src_dict[num]=1

count_i = 0
while count_i<5:
    print('count_i小于5',count_i)
    count_i+=1
else:
    print('count_i大于或者等于5：',count_i)

a_range = range(10)
b_list = [x*x for x in a_range if x%2==0]
print(b_list)

d_list = [(x,y) for x in range(5) for y in range(4)]
print(d_list)

print("xxxxxxxxxxxxxxxxxxxx")
dd_list = []
for x in range(5):
    for y in range(4):
        dd_list.append((x,y))
print(dd_list)

src_a = [30, 12, 66, 34, 39, 78, 36, 57, 121]
src_b =[3,7,5,11]
result = [(x,y) for x in src_a for y in src_b if x%y==0]
print(result)

a = ['a','b','c']
b = [1,2,3]
dict_a = [x for x in zip(a,b)]
print(dict_a)
#如果zip()函数压缩的两个列表长度不相等，那么zip()函数将以长度更短的列表为准
c = [0.1,0.2]
dict_c = [x for x in zip(a,b,c)]
print(dict_c)


books =['疯狂Kotlin讲义', '疯狂Swift讲义','疯狂Python讲义']
price = [79, 69, 89]
for book,price in zip(books,price):
    print("%s的价格是: %5.2f" %(book,price))

a = range(10)
list_a = [x for x in reversed(a)]
print(list_a)

c = 'hello kitty'
list_c = [x for x in reversed(c)]
print(list_c)

#sorted()函数也不会改变所传入的可迭代对象，该函数只是返回一个新的，排序好的列表，还可以传入一个reverse参数，如果将参数设置为true，则表示反向排序
#sorted()函数还可以传入一个key参数，该参数可指定一个函数生成排序的关键值
a = [1,3,2,5,6,3,7,-1]
print(sorted(a,reverse=True))

b = ['adgdsgs','ss','ass','a','ssaerwefqwegf','ab','sfsgr']
print(sorted(b,key=len))
"""
#break用于完全结束一个循环，跳出循环体，不管是哪种循环，一旦在循环体重遇到break，系统将完全结束该循环，开始执行循环之后的代码
#python的break语句不能像其他语言一样使用标签，因此它只可以结束其所在的循环，不可以结束嵌套循环的外层循环，为了使用break语句
跳出嵌套循环的外层循环，可先定义bool类型的变量来标志是否需要跳出外层循环，然后再内存循环、外层循环中分别使用两条break语句来实现
"""
for i in range(0,10):
    print("i的值是%s" % i)
    if i==2:
        break

for i in range(0,10):
    print("i的值是%i:"%i)
    if i == 2:
        break
    else:
        print('else块：',i)

print("00000000000000000")

exit_flag = False
for i in range(0,5):
    for j in range(0,3):
        print("i的值为：%d,j的值为：%d"%(i,j))
        if j == 1:
            exit_flag = True
            break
    if exit_flag:
        break
print("-----------------")
for i in range(0,5):
    for j in range(0,3):
        print("i的值为：%d,j的值为：%d"%(i,j))
        if j == 1:
            exit_flag = True
            break


"""
continue忽略本次循环声息的语句，continue跟break的区别是continue只是忽略档次循环的剩下语句，接着开始下一次循环，并不会终止循环，而break则是完全终止循环体
"""
for i in range(3):
    print("i的只是%i"%i)
    if i == 1:
        continue
    print("continue后的输出语句")

"""
使用return结束方法
return用于从包围它的最直接方法、函数或匿名函数返回。当函数或方法执行到一条return语句时，这个函数或方法将被结束
"""
def test():
    for i in range(10):
        for j in range(10):
            print("i的值是：%d，j的值是：%d"%(i,j))
            if j==1:
                return
            print("return后的输出语句")
test()