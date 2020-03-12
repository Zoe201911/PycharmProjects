"""
re.match(pattern,string,flag=0)尝试从一个字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
参数:pattern匹配的正则表达式，string要匹配的字符串，flags标志位，用于控制正则表达式的匹配方式，例如：是否区分大小写，多行匹配等待
匹配成功re.match方法返回一个匹配的对象，否则返回None
可以使用group(num)或者groups（）匹配对象函数来获取匹配表达式
group(num=0)匹配的整个表达式的字符串，group（）可以一次输入多个租号，在这种情况下它将返回一个包含哪些组所对应的值的元组

"""
import re
print(re.match('www','www.w3cshool.cn').span())
print(re.match('cn','www.w3school.cn'))
line = "Cats are smarter than dogs"
matcObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
if matcObj:
    print("matchObj.group():",matcObj.group())
    print("matchObj.group(1):",matcObj.group(1))
    print("matchObj.group(2):",matcObj.group(2))

else:
    print("No match")


"""
re.search扫描整个字符串并返回第一个成功的匹配
re.search(pattern,string,flags = 0)
pattern 匹配的正则表达式，string 要匹配的字符串，flags标志位，用于控制正则表达式的匹配方式
匹配成功re.search()方法返回一个匹配的对象，否则返回None
我们可以使用group(num)或者groups()匹配对象函数来获取匹配表达式
group(num=0)匹配的整个表达式的字符串，group()可以一次输入多个组号，在这种情况下它将返回一个包含哪些组所对应值的元组
groups()返回一个包含所有小组字符串的元组，从1到所含的小组号
"""
print(re.search('www','www.w3cshool.cn').span())
print(re.search('cn','www.w3cshool.cn').span())

"""
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None，而re.search匹配整个字符串，直到找到一个匹配
"""
line = "Cats are smarter than dogs"
matcObj = re.match(r'dogs',line,re.M|re.I)
if matcObj:
    print("match-->matchObj.group()：",matcObj.group())
else:
    print("No match!!")

matcObj = re.search(r'dogs',line,re.M|re.I)
if matcObj:
    print("search-->matchObj.group():",matcObj.group())
else:
    print("No match")


phone = "2004-959-599 # 这是一个电话号码"
#移除注释
num = re.sub(r'#.*$',"",phone)
print("电话号码：",num)

#移除非数字的内容
num = re.sub(r'\D',"",phone)
print("电话号码:",num)