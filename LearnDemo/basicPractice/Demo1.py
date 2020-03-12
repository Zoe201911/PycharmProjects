
def jisuan(a):
    s = (a-50000)/550
    return s

def listJisuan(list1):
    list2 = []
    for i in list1:
        b = jisuan(i)
        list2.append(b)
    print(list2)

if __name__ == '__main__':
    listJisuan([80000,80000,83000,85000,90000,90000])
