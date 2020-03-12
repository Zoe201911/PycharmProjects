#clear()用于清空字典中所有的key-value对，对一个字典执行clear()方法之后，该字典就会变成一个空字典
cars = {'BMW':7.5,'BENS':8.3,'AUDI':9.0}
print(cars)
cars.clear()
print(cars)
#get()方法其实就是根据key来获取value，它相当于方括号语法的增强版，当使用方括号语法访问并不存在的key时，字典会引发keyError错误
#但是如果使用get()方法访问不存在的key，方法会简单返回none
cars = {'BMW':7.5,'BENS':8.3,'AUDI':9.0}
print(cars.get('BMW'))
print(cars.get('hello'))#返回none
#print(cars['hello'])直接报错KeyError
#update()方法可以使用一个字典所包含的key-value对来更新已有的字典，在执行update()方法时，如果被更新的字典中已包含对应的key-value对，那么远value会被覆盖
#如果被更新的字典中不包含对应的key-value，则该key-value对被添加进去

cars = {'BMW':7.5,'BENS':8.3,'AUDI':9.0}
cars.update({'BMW':99,'BENS':123})
print(cars)
cars.update({'ll':00})
print(cars)

#items()，keys(),values()分别用于获取字典中的所有key-value对，所有key，所有value这三个方法一次返回dict_items,dict_keys和dict_values
#Python不希望用户直接操作这几个方法，但可通过list()函数把他们转换成列表，
cars = {'BMW':7.5,'BENS':8.3,'AUDI':9.0}
items = cars.items()
print(type(items))
print(list(items))

keys = cars.keys()
print(type(keys))
print(list(keys))

values = cars.values()
print(type(values))
print(list(values))

#pop()方法用于获取指定的key对应的value，并删除这个key-value对,且pop函数里的参数必须是字典里对应的key值，否知报错TypeError
cars = {'BMW':7.5,'BENS':8.3,'AUDI':9.0}
print(cars.pop('AUDI'))
print(cars)


"""
#popitem()方法用于随机弹出字典中的一个Key-value对，此处的随机其实是假的，正如列表的pop()方法总是弹出列表中最后一个元素，实际上字典的popitem()
其实也是弹出字典中最后一个key-value对，由于字典存储key-value对的顺序是不可知的，一次开发者感觉字典的popitem()方法是随机弹出的，但是实际上字典de
popitem()方法总是弹出底层存储的最后一个key-value对
"""
cars = {'BMW':7.5,'BENS':8.3,'AUDI':9.0}
print(cars.popitem())
print(cars)

"""
setdefault()方法也用于根据key来获取对应的value值，但该方法有一个额外的功能，当程序要获取的key在字典中不存在时，该方法会先为这个不存在的key只设置
一个默认的value，然后再返回该key对应的value。总之，setdefault()方法总能返回指定key对应的value-如果该key-value对存在，直接返回key对应的value
如果该key-value对不存在，则先为该key设置默认的value，然后再返回该key对应的value
"""
cars = {'BMW':7.5,'BENS':8.3,'AUDI':9.0}
print(cars.setdefault('PORSCHE',9.8))
print(cars.setdefault('BMW',4.4))
print(cars.setdefault('BMW'))
print(cars)

"""
fromkeys()方法使用给定的多个key创建字典，这些key对应的value默认都是None，也可以额外传入一个参数作为默认的value，该方法一般不会使用字典对象
调用（没有实际意义）通常会使用dict类直接调用
"""
a_dict = dict.fromkeys(['a','b'])
print(a_dict)
a_dict = dict.fromkeys((13,17),'good')
print(a_dict)
a_dict = dict.fromkeys((13,17),('bye','lll'))
print(a_dict)

tmp = '书名是:%(name)s,价格是:%(price)010.2f,出版社是：%(publish)s'
book = {'name':'疯狂的Python讲义','price':88.9,'publish':'电子社'}
print(tmp%book)