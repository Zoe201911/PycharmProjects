"""
time : 2019.1.19
function:list learning
"""


list =['google','runoob',2019,2020]
print("第三个元素为：",list[2])
list[2]=2021
print("更新后第三个元素为：",list[2])
del list[2]
print("删除后的list为:",list)
print("list的长度为：",len(list))

age = 20
if age >=18:
    print('your age is ',age)
    print('adult')
else:
    print('your age is ',age)
    print('teenager')


bmi = eval(input("请输入bmi:"))
if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")


sum = 0
for x in range(10):
    x +=1
    sum += x
print(sum)

sum = 0
n = 99
while n> 0:
    sum += n
    n = n-2
print(sum)

list = ['Bart','Kitty','Adam']
for name in list:
    print("hello,",name)


n = 1
while n <= 100:
    if n >10:
        break
    print(n)
    n += 1
print('END')

n = 0
while n < 10:
    n += 1
    if n%2 == 0:
        continue
    print(n)
print('END')
"""
break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本次循环，并且开始下一轮循环，这两个语句通常都必须配合if语句实用
特别注意：
不要滥用break和continue语句会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句。
"""




