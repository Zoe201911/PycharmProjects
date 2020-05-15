import pandas as pd

#loc:通过行标签索引数据，例如取index为a的行；location的缩写
#iloc:通过行号索引行数据，例如取第2行数据；Integer and location的缩写
#ix:通过行标签或行号索引数据（基于loc和iloc的混合）pandas 20以后的版本就很少用了
#提取多行数据，所以是a和c的行，索引必须放入一个list中

city_data = {'城市':pd.Series(['北京','上海','深圳','成都','杭州'],
                            index=['a','b','c','d','e']),
             '人口/千万':pd.Series([2171,2415,1191,901,899],
                               index=['a','b','c','d','e']),
             '年份':pd.Series([2015,2016,2015,2016,2015],
                            index=['a','b','c','d','e'])}
df1 = pd.DataFrame(city_data)
print(df1)

#利用loc,iloc提取行数据
#提取单行数据。提取索引为a的行
df2 = df1.loc['a']
print('=========分割线 ===========')
print(df2)

#获取第一行数据，所以为'a'的行就是第一行，所以结果相同
df3 = df1.iloc[0]
print('=========分割线 ===========')
print(df3)

#提取多行数据，所以是a和c的行，索引必须放入一个list中
df4 = df1.loc[['a','c']]
print('=========分割线 ===========')
print(df4)
#获取第一行，第三行的数据
df5 = df1.iloc[[0,2]]
print('=========分割线 ===========')
print(df5)

#利用loc ,iloc提取列数据
df6 = df1.loc[:,['城市']]
df7 = df1.loc[:,['城市','年份']]
print('=========分割线 ===========')
print(df7)
df8 = df1.iloc[:,0:2]
print('=========分割线 ===========')
print(df8)

#使用loc ,iloc获取所有数据
df9 = df1.loc[:,:]
df10 = df1.iloc[:,:]
print('=========分割线 ===========')
print(df10)

#利用loc函数，根据某个数据值来提取数据所在的行
df11 = df1.loc[df1['城市']=='杭州']
print('=========分割线 ===========')
print(df11)

print(df1['城市']=='杭州')