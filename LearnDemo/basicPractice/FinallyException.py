"""
python 的垃圾回收机制不会回收任何物理资源，只能回收堆内存中对象占用的内存.
为了保证一定能回收在try快中打开的物理资源，异常处理机制提供了finally块，不管try块中的代码是否出现异常，
也不管哪一个except块被执行，甚至在try块或者except块中执行了return语句，finally块总会被执行。

在异常处理语法结构中，只要try块时必须的，也就是说，如果没有try块，则不能有后面的except块和finally块；
except块和finally块都是可选的，但except块和finally块都是可选的，但except块和finally块至少出现其中之一
也可以同时出现。可以有多个except块，但捕获父类异常的except块应位于捕获子类异常的except块的后面；不能只有
try块，没有except块，也没有finally块。多个except块必须位于try块之后，finally块必须位于所有except块之后
"""

import os
def test():
    fis = None
    try:
        fis = open("a.txt")
    except OSError as e :
        print(e.strerror)
        return
        print("abc执行没")
    finally:
        if fis is not None:
            try:
                fis.close()
            except OSError as ioe:
                print(ioe.strerror)
        print('执行finally块里的资源回收')

# test()

"""
:except块里的return语句，该语句强制方法返回，在通常情况下，一旦在方法里执行到return语句，程序将立即结束该方法，现在不会了，虽然
return语句也强制方法结束，return之后的语句不再执行，但一定会先执行finally块的代码

遇到os_exit(1)强制退出，不在执行finally

"""

"""
在通常情况下，不要在finally块中使用如return或raise等导致方法中止的语句，一旦在finally块中用了return或raise语句，
将会导致try块，except块中的return，raise语句失效
"""
def test():
    try:
        return True
    finally:
        return False

a = test()
print(a)
"""
上面程序在finally块中定义了一条return False语句，这将导致try块中的return True失去作用。
如果Python程序在执行try块，except块时遇到了return或raise语句，这两条语句都会导致该方法立即结束，那么系统执行这两条语句并不会结束该方法
而是去寻找该异常处理流程中的finally块，如果没有找到finally块，程序立即执行return或raise语句，方法终止；如果找到finally块，系统立即
开始执行finally块，只有当finally块执行完成后，系统才会再次跳回来执行try块、except块里的return或raise语句，如果在finally块里也使用了
return或raise等导致方法终止的语句，finally块已经终止了方法，系统将不会跳回去执行try块，except块里的任何代码
"""