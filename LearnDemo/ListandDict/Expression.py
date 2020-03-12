"""
python中运算符的种类：赋值运算符，算术运算符，位运算符，索引运算符，逻辑运算符
"""
bookName = 'crazy python'
price = 79
version = "normal version"
if bookName.endswith('python') and (price <50 or version == 'normal version'):
    print("打算购买这本Python图书")
else:
    print("不打算购买")


#三目运算  True_statements if expression else False_statements
#三目运算符的规则：先对逻辑表达式expression求值，如果逻辑表达式返回True,则执行并返回True_statements的值，如果逻辑表达式返回false，则
#执行并返回False_statements的值
a = 5
b = 3
st = "a大于b" if a>b else "a不大于b"
print(st)

st = print('crazyit'),'a大于b' if a>b else 'a大于b'
print(st)

c = 5
d = 5
print("c大于d")if c>d else (print('c小于d')if c>d else print('c等于d'))



a = 'abcaxabxbabdcxxabsxaxab'
b = 'ab'
count = 0
h = 0
for i in range(len(a)):
    if(a.find(b,h)>=h):
        h = a.find(b,h)+len(b)
        count += 1

print(count)

a = 'abac-aab*abac zza-ab'
print(a.replace('-','0'))
print(a.replace(a[2],'9'))
print(a)
