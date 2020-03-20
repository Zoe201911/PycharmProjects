
def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2*fn(n-1) + fn(n-2)

print("fn(10）的结果是：",fn(10))

def test(a,*books):
    print(books)
    for b in books:
        print(b)
    print(a)

test(5,"lll","abc")

def test2(x,y,z=3,*books,**scores):
    print(x,y,z)
    print(books)
    print(scores)

test2(1,2,3,"abc","android",Chinese=90,Math=100)

#逆向参数收集是程序在已有列表，元组，字典等对象的前提下，把它们的元素"拆开"后传给函数的参数
def test3(name,message):
    print("用户是：",name)
    print("欢迎消息：",message)
my_list = ['abc','llllll']

test3(*my_list)

def bar(book,price,desc):
    print(book,"这本书的价格是：",price)
    print('描述信息：',desc)

my_dict = {'price':90,"book":"abc","desc":'lllll'}

bar(**my_dict)

lambda x,y:x+y

x = map(lambda x:x*x,range(8))
print([e for e in x])

