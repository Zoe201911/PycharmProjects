a = None
b = True
c = -10
f = ""
#三种情况装换成bool是false，0，None,""
print(bool(a))
h = [1,None,"aa",[1,2,3]]

for i in h:
    print(i)
h.append("xxx")
print(h)

k = {
    "a":1,
    "b":2,
    "c":"aaa"
}

k['abc']=90
print(k)
del(k["abc"])
print(k)

value = k.get("w","hello")

print(value)
print(k)