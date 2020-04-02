"""
__len__(self）该方法的返回值决定序列中元素的个数
__getitem__(self,key)该方法获取指定的索引对应的元素，该方法的key应该是整数数值或者slice对象，否则该方法引发KeyError异常
__contains__(self,item)该方法判断序列是否包含指定元素
__setitem__(self,key,value)该方法设置指定索引对应的元素，该方法的key应该是整数值或者slice对象，否则该方法会引发KeyError值
__delitem__(self,key)该方法删除指定索引对应的元素
"""
def check_key(key):
    if not isinstance(key,int):
        raise TypeError('索引值必须是整数')
    if key < 0:
        raise IndexError('索引值必须是非负整数')
    if key >= 26**3:
        raise IndexError('索引值不能超过%d'% 26**3)

class StringSeq:
    def __init__(self):
        #用于存储被修改的数据
        self._changed = {}
        #用于存储已删除元素的索引
        self._deleted = []
    def __len__(self):
        return 26**3
    def __getitem__(self, key):
        #根据索引获取序列中元素
        check_key(key)
        #如果在self._changed中找到修改后的数据
        if key in self._changed:
            return self._changed[key]
        #如果key在self._deleted中，说明元素已被删除
        if key in self._deleted:
            return None
        three = key//(26*26)
        two = (key - three*26*26)//26
        one = key %26
        return chr(65+three)+chr(65+two)+chr(65+one)

sq = StringSeq()
print(len(sq))
print(sq[26*26])
