#coding:utf-8    #设置Python文件的编码为utf-8，这样就可以写入中文注释了


#-----Python可以根据参数名传递参数----
def foo(ip,port):
    print("%s:%d"%(ip,port))

#没有指定参数名，按照顺序传参数
foo("192.168.0.0",0)
#指定参数名，可以按照参数名传参数
foo(port = 8000,ip = "192.168.0.0")

#----可变参数----
def foo1(arg1,*tupleArg,**dictArg):
    print("arg1=",arg1)
    print("tupleArg=",tupleArg)
    print('dictArg=',dictArg)

foo1("kitty","kitty1","kitty2",key1=123,key2=456)

print("*********************88t")

"""
上面函数中的参数，tupleArg前面"*'表示这个参数是一个元组参数，从程序的输出可以看出，默认值为(),
"**"表示这个字典参数（键值对参数）。可以把tupleArg，dictArg看成两个默认参数，多余的非关键字
参数，函数调用时被放在元组参数tupleArg中，多余的关键字参数，函数调用时被放字典参数dictArg中
"""
def foo2(arg1,arg2="ok",*tupleArg,**dictArg):
    print("arg1=",arg1)
    print("arg2=",arg2)
    for i ,element in enumerate(tupleArg):
        print("tupleArg%d--->%s"%(i,str(element)))

    for key in dictArg:
        print("dictArg %s--->%s"%(key,dictArg(key)))

myList = ['my1','my2']
myDict = {"name":"kitty","age":12}

foo2(123,myList,myDict)

print("--------------------------------")

def test(a,*books):
    print(books)
    for b in books:
        print(b)
    print(a)

test(5,"疯狂IOS讲义","疯狂Android讲义")

def test(*books,num):
    print(books)
    for b in books:
        print(b)
    print(num)
test("疯狂IOS讲义","疯狂Android讲义",num=20)

def test(x,y,z=3,*books,**scores):
    print("x = {},y = {},z = {} ".format(x,y,z))
    print(books)
    print(scores)

test(1,2,3,"crazy IOS","crazy android",yuwen=99,shuxue=99,yingyu=100)


