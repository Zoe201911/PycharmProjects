"""
*args和**kwargs主要用于函数定义，可以将不定数量的参数传递给一个函数，预先并不知道，函数使用者会传递多少个参数给你
所以在这个场景下使用这两个关键字，*args用来发送一个非键值对的可变数据量的参数列表给一个参数
"""

def test_var_args(f_arg,*argv):
    print("first normal arg",f_arg)
    for arg in argv:
        print("another arg through *argv:",arg)


test_var_args('yasoob','python','django','eggs','test')

print("****************")
"""
**kwargs允许将不一定长度的键值对，作为参数传递给一个函数，如果你想要在一个函数里处理带名字的参数
应该使用**kwargs
"""

def great_me(**kwargs):
    for key,value in kwargs.items():
        print("{0}=={1}".format(key,value))

great_me(name = "yasoob",age = 12,weight = 40)


def test_args_kwargs(arg1,arg2,arg3):
    print("arg1:",arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ("two",3,4)
test_args_kwargs(*args)

kwargs = {"arg3":2,"arg2":1,"arg1":5}
test_args_kwargs(**kwargs)

#如果想在函数里同时使用所有这三种参数，顺序是这样的  some_func(fags,*args,**kwargs)


