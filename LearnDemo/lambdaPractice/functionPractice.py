"""
Python声明函数必须使用def关键字，对函数语法格式如下：
函数名：从语法角度来看，函数名只是一个合法的标识符即可，从程序的可读性角度来看，函数名由一个或多个有意义的单词连缀而成，每个单词的字母全部小写，单词与单词之间使用下划线分隔
形参列表：用于定义该函数可以接受的参数，形参列表由多个形参名组成，多个形参名之间以逗号分隔。谁调用，谁负责赋值
"""
def my_max(x,y):
    z = x if x>y else y
    return z

def say_hi(name):
    print("===正在执行say_hi（）函数===")
    return name + ",hello "
a = 6
b = 9
result = my_max(a,b)
print("result:",result)
print(say_hi("lily"))

#help(my_max(a,b))

 #当返回值为多个值时将会被自动封装成元组，因此程序中可以看到result包含两个元素的元组
def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        if isinstance(e,int) or isinstance(e,float):
            count +=1
            sum +=e
    return sum,sum/count
list1 = ['abc',1,2,3,-1,-9,10,'xsx']
result = sum_and_avg(list1)
print(result)
#收到多个返回值时，Python使用序列解包来获取多个返回值
s,avg = sum_and_avg(list1)
print("sum:",s)
print("avg:",avg)


def say_hi(name='monkey',message = 'welcome to crazyit'):
    print(name,",hello")
    print("message is :",message)
say_hi()
say_hi("白骨精")#如果只传入一个位置参数，由于该参数位于第一位，系统会将该参数值传递给name参数
say_hi("lilu","welcome to python")
say_hi(message="welcome to python lesson")
#say_hi("欢迎学习Python",name='lily')报错TypeError关键字参数必须位于位置参数的后面
say_hi("lily",message="dolalala")

def test(x,y,z=3,*books,**scores):
    print(x,y,z)
    print(books)
    print(scores)
test(1,2,4,"crazyit",'bababa',yuwen=80)

#逆向参数收集指的是程序已有列表，元组，字典等对象的前提下，把他们的元素"拆开"后传给函数的参数
#逆向参数收集需要在传入的列表、元组参数之前添加一个星号，在字典参数之前添加两个星号
def test(name,message):
    print("user is :",name)
    print("welcome message:",message)
my_list = ['Tom','welcome to crazyit']
test(*my_list)
#上面粗体字定义了一个需要两个参数的函数，而程序中的my_list列表包含两个元素，为了让程序将my_list列表的两个元素传给test()函数
#程序在传入的my_list参数之前添加一个星号，如果传入三个参数，程序报错：TypeError
def foo(name,*nums):
    print("name参数：",name)
    print("nums参数:",nums)
my_tuple = (1,2,3,4,5)
foo('lily',*my_tuple)
foo(*my_tuple)
foo(my_tuple)

def bar(book,price,desc):
    print(book,"这本书的价格是:",price)
    print('描述信息',desc)
my_dict = {'price':89,'book':'crazyit Python','desc':'这是一本系统全面的Python学习图书'}
bar(**my_dict)

def swap(a,b):
    a,b = b,a
    print('在swap函数里，a的值是：',a,"b的值是：",b)
a = 6
b = 9
swap(a,b)
print("交换结束后，变量a的值是：",a,"变量b的值是：",b)


def swap(dw):
    dw['a'],dw['b'] = dw['b'],dw['a']
    print("在swap函数里，a元素的值是：",\
          dw['a'],":b元素的值是",dw['b'])
dw = {'a':6,'b':9}
swap(dw)
print("交换结束后，a元素的值是",\
          dw['a'],":b元素的值是",dw['b'])