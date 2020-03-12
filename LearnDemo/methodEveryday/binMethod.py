"""
bin(x)将整数转换成二进制字符串，如果x不是Python中int类型，x必须包含方法_indx_()并且返回integer
参数x:整数或者包含_index_()方法且返回integer的类型
版本：bin函数是Python2.6中新增函数，使用时要注意版本问题
注意：Python版本号和参数类型
"""

print(bin(521))

class MyType:
    def __index__(self):
        return 35

mt = MyType()
print(bin(mt))