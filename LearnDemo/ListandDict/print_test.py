print(40,'\t',end='')
print(50,'\t',end='')
print(60,'\t',end='')

f = open('poem.txt','w')
print('沧海月明珠有泪',file = f)
print('蓝田日暖玉生烟',file = f)
f.close()

af1 = 5.2345556
print("af1:",af1)
af2 = 25.2345
print("af2:",af2)

s1 = 'hello'

s2 = 99

s = str(s2)
print(s,type(s))

print(s+s1)

a = str(10/3)
print(a ,type(a))
print(repr(10/3))

#无论用户输入哪种type的内容，input（）函数返回字符串，程序总会将用户输入的内容转换成字符串
msg = input("please enter a number:",)
print(type(msg))
print(msg)

#三个引号（单引号，双引号都行）来包含多行注释内容，其实这是长字符串写法，只是由于在长字符串可以防止任何内容，包括放置单引号，双引号都可以。
#如果所定义的长字符串没有赋值给任何变量，那么这个字符串就相当于被解释器忽略了，也就是相当与注释掉了
s = ''' "Let's go fishing",said Mary.
"Ok,Let's go",said her brother
they walked to a lake
'''

print(s)

s = 'the quick brown fox\
 jumps over the lazy dog'
print(s)

num = 20+3/4+\
    2*3
print(num)

s = 'I\\M'
print(s)

s = r'G:\public\coder\02\03'
print(s)

s = r'Let\'s go'
print(s)

s = r"Let's go"
print(s)