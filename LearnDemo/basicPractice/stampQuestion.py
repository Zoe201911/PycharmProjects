# coding:utf-8

a = 6
b = 7
c = 8
t = 50
s = []

for i in range(t+1):
    s1 = a * i
    s.append(s1)
    for j in range(t+1):
        s2 = a*i + b*j
        s.append(s2)
        for k in range(t+1):
            s3 = a*i + b*j + c*k
            s.append(s3)
new = list(set(s))
new.sort()
print(new[-1])

new_r = []
for i in range(6*t):
    if i in new:
        pass
    else:
        new_r.append(i)

print("组合不能生成的数据%s"%new_r)
print("不能生成的最大数字为%s"%new_r[-1])