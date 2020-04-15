import pandas as pd
import numpy as np

#获取某一列的值，升序或者降序，ascending= True升序，ascending=False降序
titanicFile = pd.read_csv('titanic_train.csv')
new_titanicFile = titanicFile.sort_values('Age',ascending= False)
print(new_titanicFile['Age'])

#排序后重新生成一个index的值，reset_index(drop=True),drop=True是把之前index舍弃
renew_titanicFile = new_titanicFile.reset_index(drop=True)
print(renew_titanicFile['Age'])


#获取到第100行的所有信息
def hundredth_row(column):
    hundredth_item = column.loc[99]
    return hundredth_item

hundredth_row = titanicFile.apply(hundredth_row)
print(hundredth_row)

#获取到为空的行的总行数
def not_null_count(column):
    column_null = pd.isnull(column)
    null_1 = column[column_null]
    return len(null_1)
column_null_count = titanicFile.apply(not_null_count)
print(column_null_count)
column_null_count = titanicFile.apply(not_null_count)
print(column_null_count)

def generate_age(row):
    age = row['Age']
    if pd.isnull(age):
        return 'unknow'
    elif age > 18:
        return  "adult"
    else:
        return 'child'

generate_age = titanicFile.apply(generate_age,axis=1)
print(generate_age)

