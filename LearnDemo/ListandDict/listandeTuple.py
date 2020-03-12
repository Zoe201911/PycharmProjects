my_list = ['crazylit',20,'python']
print(my_list)
my_tuple = ('crazyit',20,'python')
print(my_tuple)
"""
删除列表元素使用del语句，del语句是Python的一种语句，专门用于执行删除操作，不仅可用于删除列表的元素，也可以用户删除变量等
使用del语句既可以删除列表中的单个元素，也可直接删除列表中的中间一段
"""

a_list = ['crazyit',20,-2.4,(3,5),'fkit']
del a_list[2]
print(a_list)
a_list.extend((1,2,3,4))
del a_list[5:7]
print(a_list)
a_list = list(range(1,10))
del a_list[2:-1:2]
print(a_list)
name = 'crazyit'
print(name)
del name
#print(name)#name变量被删除后，接下来访问name变量时将会引发NameError错误
"""
除了使用del语句之外，Python还提供了remove()方法来删除列表元素，该方法并不是根据索引来删除元素的
而是根据元素本身来执行删除操作对的，该方法只删除第一个找到的元素，如果找不到该元素，方法将引发valueError错误
"""
a_list = [20,'crazyit',30,-4,'crazyit',3.4]
#删除第一个找到的30
a_list.remove(30)
print(a_list)
a_list.remove('crazyit')
print(a_list)
#a_list.remove(99)找不到元素报错ValueError
#列表还包含一个clear()方法，正如它的名字所暗示的，该方法用于清空列表的所有元素，
a_list.clear()
print(a_list)

a_list = [20,'crazyit',30,-4,'crazyit',3.4]
a_list[2] = 'fkit'
print(a_list)
a_list[-2]=9527
print(a_list)

a_list = list(range(1,5))
print(a_list)
a_list[1:3] = ['a','b']
print(a_list)
#将第三个到第三个元素赋值为新列表的元素，就是插入到某个位置元素
a_list[2:2]=['p','rr','00']
print(a_list)