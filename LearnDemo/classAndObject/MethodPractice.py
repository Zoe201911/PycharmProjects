def foo():
    print("全局空间的foo方法")
bar = 20
class Bird:
    def foo(self):
        print("Bird类里的foo方法")
    bar = 200
foo()
print(bar)
Bird.foo(Bird)
print(Bird.bar)

#python类可以调用实例方法，但使用类调用实例方法时，Python不会自动为方法的第一个参数self绑定参数值；程序必须显试的为第一个参数self传入方法调用者，被称为"未绑定方法"
class User:
    def walk(self):
        print(self,'正在慢慢的走')

u = User()
User.walk('Kitty')

"""
类方法和静态方法的区别：Python会自动绑定类方法的第一个参数，类方法的第一个参数（通常建议参数名为cls）会自动绑定到类本身，但对于静态方法则不会自动绑定
使用@classmethod修饰的方法时类方法，使用@staticmethod修饰的方法就是静态方法
Python编程中，一般不使用类方法或静态方法，程序完全可以使用函数来代替类方法或静态方法，但是在特殊场景（比如使用工厂模式下），类方法或静态方法也是不错的选择
"""
class Bird:
    @classmethod
    def fly(cls):
        print('类方法fly：',cls)
    @staticmethod
    def info(p):
        print("静态方法info：",p)

#无论是使用类本身Bird还是对象b调用类方法，Python始终都会将类方法的第一个参数绑定到类本身
Bird.fly()
#Bird.fly('kitty')如果强制再给类方法一个参数，程序将报错，TypeError: fly() takes 1 positional argument but 2 were given
Bird.info('crazyit')
#静态方法统一可以使用类调用静态方法，也可使用对象调用静态方法，不管是哪种调用方式，Python都不会为静态方法执行自动绑定
b = Bird()
b.fly()
b.info('crazyit')


"""
函数装饰器：例如@classmethod，staticmethod都是函数装饰器。当程序使用"@函数"函数A，装饰另一个函数（比如函数B）时，实际上完成如下两步：
1）将被修饰的函数（函数B）作为参数传给@符号引用的函数（函数A)
2)将函数B替换（装饰）成第1步的返回值
"""
def funA(fn):
    print('A')
    fn()
    return 'crazyit'

#下面的装饰效果相当于funA(funB),funB将会被替换成该语句的返回值，由于funA函数返回crazyit,因此funB就是crazyit
#1）将funB作为funA()的参数，也就是@funA相当于执行funA(funB)
#2）将funB替换成1）步执行的结果，funA()执行完成后返回crazyit，因此funB就不再是函数，而是被替换成一个字符串
#先执行@foo把my_test作为参数，然后再执行my_test，把它作为foo的返回值执行
@funA
def funB():
    print('B')
print(funB)

def foo(fn):
    print("hello kitty")
    def bar(*args):
        print("===1===",args)
        n = args[0]
        print("===2===",n*(n-1))
        #print(fn.__name__)
        #fn(n*(n-1))
        print("*"*15)
        return (n*(n-1))
    return bar
@foo
def my_test(a):
    print("===my_test函数===",a)
print(my_test)
print("&&&&&&&&&&&")
print(my_test(10))
my_test(5,6)

"""
通过@符号来修饰函数是Python的一个非常实用的功能，它既可以在被修饰函数的前面添加一些额外的处理逻辑（比如权限检查），也可以在被修饰函数的后面
添加一些额外的处理逻辑（比如记录日志）还可以在目标方法抛出异常时进行一些修复操作
"""
def auth(fn):
    def auth_fn(*args):
        print("----模拟执行权限检查-----")
        fn(*args)
    return auth_fn
@auth
def test(a,b):
    print("执行test函数，参数a:%s,参数b:%s"%(a,b))
test(20,15)