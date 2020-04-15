import  pandas as pd

level_info = pd.read_excel('档位.xlsx')
print(type(level_info))
print(level_info.dtypes)
print(help(pd.read_excel))
print(level_info.head(6))#默认参数（急head())是显示5条数据，如果head有参数就按照参数来显示行数

print(level_info.tail())#默认显示后5行，如果有参数显示参数的行数
print(level_info.columns)#显示列名称
print(level_info.shape)#显示行数和列数

print(level_info.loc[200])#第多少行的数据

mdb_col = level_info['product_id']
print(mdb_col)
cols = ['本次auto模式时间','本次手动模式时间']
print(level_info[cols])
cols_info = level_info.columns.tolist()
print(cols_info)
level_info['a_product_id'] = level_info['product_id']+'b'
print(level_info.columns.tolist)
print("xxxxxxxxxxxxxxxxxxxxx")
print(level_info['本次手动模式时间'].max())
#sort_values排序默认是从小到大，指定升序还是降序用ascending
level_info.sort_values('本次auto模式时间',inplace=True,ascending=True)
print(level_info['本次auto模式时间'])
