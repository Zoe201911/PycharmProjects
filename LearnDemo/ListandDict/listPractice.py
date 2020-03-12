
import random


str = input("请输入多个字符串:",)
a_tuple = tuple(str)
print(a_tuple)
a_tuple3 = a_tuple*3
print(a_tuple3)
str4 = a_tuple3 + ('fkjava','crazyit')
print(str4)

list1 = [1,2,3,4,5]
listC = list1[0:]
print(listC)

#用户输入 一个整数 n，生成长度为 n 的列表，将 n 个随机数放入列表中 。
a = 10
my_randoms = random.sample(range(1,101),a)
print(my_randoms)
print("xxxxxxxxxxxxxxxx")

#用户输入 一个整数 n，生成长度为 n 的列表，将 n 个随机的奇数放入列表中 。
my_randoms_ji = random.sample(range(1,101),100)

list_a = []
count = 1
for i in my_randoms_ji:
    if count > 10:
        break

    if i%2 != 0:
        count += 1
        list_a.append(i)
print(list_a)
print('xxxxxlllllllllllll')

#用户输入 一个整数 n，生成长度为 n 的列表，将 n 个随机的大写字符放入列表中
random_cha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
my_random_cha =random.sample(random_cha,a)
print(my_random_cha)

#用户输入 N 个字符扇，将这些字符串收集到列表中，然后去除其中重复的宇符串后输出列表 。
#方法一：先把列表转为set，然后再把set转化为list
list_b = ['abc','abc','hello','kitty','xxxH','two','kitty','hello']
set_a = set(list_b)
print(set_a)
list_b = list(set_a)
print(list_b)

print("***********")
#方法二：直接通过循环删除
list_C = ['abc','abc','hello','kitty','xxxH','two','kitty','hello','kitty','kitty']
for val in list_C:
    if list_C.count(val) > 1:
        while i<list_C.count(val):
            list_C.remove(val)
            i += 1
print(list_b)

print("**************")

a_str = '12 34 1 3 4 56 78 9'
tuple_a = tuple(a_str.split( ))
print(tuple_a)

vals = 12,13,14,1,2,3
print(vals)
print(vals.__hash__())


#用户随机输入 N 个大写字母，程序使用 diet 统计用户输入的每个字母的次数 。
dict_a ={}
list_chab = ['A','B','A','C','A','B','D','D','A','B','F','C']
for val in list_chab:
    dict_a.setdefault(val,list_chab.count(val))
print(dict_a)