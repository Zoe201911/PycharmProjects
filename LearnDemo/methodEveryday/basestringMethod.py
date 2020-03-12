"""
basestring()方法是str和unicode的超类（父类），也是抽象类，因此不能被调用和实例化，但可以被用来判断一个对象是否为str
或者unicode的实例，isinstance(obj,basestring)等价于isinstance(obj,(str,unicode))
python2.3版本以后引入该函数，兼容Python2.3以后Python2个版本，注意：Python3中舍弃了该函数，所以该函数不能再Python3中使用
"""

print(isinstance('hello',str))

