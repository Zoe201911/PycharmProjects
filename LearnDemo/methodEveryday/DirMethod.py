import struct
#当你为dir()提供一个模块名的时候，它返回模块定义的名称列表，如果不提供参数，它返回当前模块中定义的名称列表
print(dir())
print(dir(struct))


class Shape(object):
    def __dir__(self):
        return ['area','perimeter','location']

s = Shape()
print(dir(s))