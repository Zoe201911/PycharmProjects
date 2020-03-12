#字典和字符串的转换
a ='''{
    "aa": True,
    "bb": "cccc"
}'''
print(a)
print(type(a))
print(str(a))
print(type(str(a)))

c = eval(a)

print(c)
print(type(c))