
def funA(fn):
    print('A')
    fn()
    return 'abc'


@funA
def funB():
    print('B')

print(funB)

def foo(fn):
    def bar(*args):
        print("===1===",args)
        n = args[0]
        print("===2===",n*(n-1))
        print(fn.__name__)
        fn(n*(n-1))
        print("*"*15)
        return fn(n*(n-1))
    return bar

@foo
def my_test(a):
    print("==my_test函数==",a)
print(my_test)
my_test(10)
my_test(6,5)

def auth(fn):
    def auth_fn(*args):
        print("----模拟执行权限检查---")
        fn(*args)
    return auth_fn

@auth
def test(a,b):
    print("执行test函数，参数a:%s，参数b:%s"%(a,b))
test(20,15)
print(test)

print('+++++++++++++++++++++')

import functools

def log(text):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(x,y):
            print('参数1为：%s，参数2为：%s' %(x,y),f.__name__)
            return f(x,y)
        return wrapper
    return decorator

@log("python之装饰器")
def add(x,y):
    print(add.__name__)
    return x + y

print(add(2,3))

print('000000000000000')

import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print('Running "%s" in  %.3f seconds' %(func.__name__,(end-start)))
        return result
    return wrapper

def better_time_it(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print('Running "%s" in  %.3f seconds' %(func.__name__,(end-start)))
        return result
    return wrapper

@time_it
def foo():
    print('Foo!')

@better_time_it
def yeah():
    print('Yeah')


print(foo)
print(yeah)

# if __name__ =='__main__':
#     help(foo)
#     help(yeah)