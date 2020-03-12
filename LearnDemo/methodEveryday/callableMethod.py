"""
callable(object)
检查对象object是否是可调用，如果返回true，object仍然可能调用失败，但如果返回false，调用对象object觉得不会成功
注意：类是可调用的，而类的实例实现_call_()方法才可调用
"""

print(callable(0))

print(callable("mystring"))

def add(a,b):
    return  a+b

print(callable(add))

class A :
    def method(self):
        return 0

a = A()
print(callable(a))

class B:
    def __call__(self):
        return 0

b = B()
print(callable(b))