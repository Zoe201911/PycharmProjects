"""
如果开发者需要实现迭代器，只要实现如下两个方法即可
__iter__(self)：该方法返回一个迭代器，迭代器必须包含一个__next__()方法，该方法返回迭代器的下一个元素
__reversed__(self)该方法主要为内建的reversed()反转函数提供支持，当程序调用reversed()函数对指定迭代
器执行反转时，实际上是由该方法实现的
"""

class Fibs:
    def __init__(self,len):
        self.first = 0
        self.sec = 1
        self.__len = len
    def __next__(self):
        if self.__len == 0:
            raise StopIteration
        self.first,self.sec = self.sec,self.first + self.sec
        self.__len -= 1
        return  self.first
    def __iter__(self):
        return self
fibs = Fibs(10)
# print(fibs.__next__())
for el in fibs:
    print(el,end=' ')

my_iter = iter([2,'kfit',4])
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())


class ValueDict(dict):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def getkeys(self,val):
        result = []
        for key ,value in self.items():
            if value == val:
                result.append(key)
        return result

my_dict = ValueDict(chinese = 99,math=99,English =89)
print(my_dict.getkeys(99))

def test(val,step):
    print('---函数开始执行----')
    cur = 0
    for i in range(val):
        cur += i*step
        print(cur,end=' ')
test(10,2)

#调用包含yield语句的函数并不会立即执行，它只是返回一个生成器，只有当程序通过next()函数调用生成器或者遍历生成器，函数才会真的执行
def test1(val,step):
    print('---函数开始执行----')
    cur = 0
    for i in range(val):
        cur += i*step
        yield cur
t = test1(10,2)
print(t.__next__())
print(list(t),type(t))
for ele in t :
    print(ele,end=' ')

print("xxxxxxxxxxxxxxxxxxxx")
def square_gen(val):
    i = 0
    out_val = None
    while True:
        #使用yield语句生成值，使用out_val结束send()方法发送的参数值
        out_val = (yield out_val**2)if out_val is not None else (yield  i ** 2)
        if out_val is not None:
            print("----%d"%out_val)
        i += 1

sg = square_gen(5)
print(sg.send(None))#生成器根本不能获取第一次调用send()方法发送的参数，这就是Python要求生成器第一次调用send()方法智能发送None参数
# print('-------------')
print(sg.send(9))
# print(sg.__next__())