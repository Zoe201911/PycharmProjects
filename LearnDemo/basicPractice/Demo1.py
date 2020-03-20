
def jisuan(a):
    s = (a-50000)/550
    return s

def listJisuan(list1):
    list2 = []
    for i in list1:
        b = jisuan(i)
        list2.append(b)
    print(list2)



def test():
    for i in range(10):
        for j in range(10):
            print("i 的值是：%d,j的值是：%d" % (i,j))
            if j == 1:
                return
            print("return后的输出语句")

def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list :
        if isinstance(e,int) or isinstance(e,float):
            count +=1
            sum +=e
    return sum,sum/count



if __name__ == '__main__':
    listJisuan([80000,80000,83000,85000,90000,90000])
    test()
    print(sum_and_avg([1,'ss',2,4,9,'pp']))



