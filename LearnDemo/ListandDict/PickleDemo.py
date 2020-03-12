"""
python的pickle模块实现了基本的数据序列和反序列化
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储
通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象
"""

import pickle,pprint
data1 = {'a':[1,2.0,3,4+6j],
         'b':('string',u'Unicode String'),
         'c':None}
selfref_list = [1,2,3]
selfref_list.append(selfref_list)
output = open('data.pkl','wb')

pickle.dump(data1,output)
pickle.dump(selfref_list,output,-1)
output.close()

pkl_file = open('data.pkl','rb+')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
# pkl_file.close()

print(pkl_file.tell())

print(pkl_file.truncate(14))
