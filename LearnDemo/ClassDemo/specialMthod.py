# class Item:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#
# im = Item('mouse',298)
# print(im)
# print(im.__repr__())
# im_str = im.__repr__()+"lll"
# print(im_str)
#
# class Apple:
#     def __init__(self,color,weight):
#         self.color = color
#         self.weight = weight
#     def __repr__(self):
#         return "Apple[color="+self.color+\
#             ",weight="+str(self.weight)+"]"
# a = Apple('red',5.48)
# print(a)
#
# class Item:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def __del__(self):
#         print('del删除对象')
#
# im = Item('lily',99)
# x = im
# print(im.__dir__())
# print(im.__dict__)
# print(im.__dict__['name'])
# print("xxxxxxxxxxxx")

# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def __setattr__(self, name, value):
#         print('----设置%s属性---'%name)
#         if name =='size':
#             self.width,self.height = value
#         else:
#             self.__dict__[name] = value
#     def __getattr__(self, name):
#         print('---读取%s属性---'%name)
#         if name == 'size':
#             return self.width,self.height
#         else:
#             raise AttributeError
#     def __delattr__(self, name):
#         print('---删除%s属性---'%name)
#         if name == 'size':
#             self.__dict__['width'] = 0
#             self.__dict__['height'] = 0
#
# rect = Rectangle(3,4)
# # print(rect.size)
# rect.size = 6,8
# print(rect.size)

# class User:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     #重写__setattr__()方法对设置的属性值进行检查
#     def __setattr__(self, name, value):
#         if name == 'name':
#             if 2< len(value)<=8 or len(value)>8:
#                 self.__dict__['name'] = value
#             else:
#                 raise ValueError('name长度必须在2~8之间')
#         elif name == 'age':
#             if 10< value <60:
#                 self.__dict__['age']=value
#             else:
#                 raise ValueError('age值必须在10~60之间')
#
#
# u = User('fkitxxxx',24)
# print(u.name)

class Comment:
    def __init__(self,detail,view_times):
        self.detail = detail
        self.view_times = view_times
    def info(self):
        print('一条简单的评论，内容是%s'%self.detail)

c = Comment('crazy python',20)
print(hasattr(c,'detail'))
print(getattr(c,'detail'))
setattr(c,'detail','weather is good')
print(c.detail)