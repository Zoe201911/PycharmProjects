import  pandas as pd
import numpy as np

titanicFile = pd.read_csv('titanic_train.csv')
print(titanicFile)
cabin = titanicFile['Cabin']
cabin_null = pd.isnull(cabin)
print(cabin_null)
print(titanicFile.columns.tolist())
cabin_null_true = cabin[cabin_null]
print(cabin_null_true)
print(len(cabin_null_true))

age = titanicFile['Age']

age_null = pd.isnull(age)
agv_age = sum(titanicFile['Age'][age_null==False])/len(titanicFile['Age'][age_null==False])
print(agv_age)
print(titanicFile['Age'].mean())#mean()方法去掉缺失值后的求平均

passenger_classes = [1.2,3]
fares_by_class = {}
for this_class in passenger_classes:
    pclass_rows = titanicFile[titanicFile['Pclass'] == this_class]
    pclass_fares = pclass_rows['Fare']
    fare_for_class = pclass_fares.mean()
    fares_by_class[this_class] = fare_for_class
print(fare_for_class)
#按照index分类，每一类的values的平均值是多少，aggfunc=np.mean算取平均值
passenger_surv = titanicFile.pivot_table(index='Pclass',values='Survived',aggfunc=np.mean)
print(passenger_surv)

passenger_age = titanicFile.pivot_table(index='Pclass',values='Age')
print(passenger_age)

#统计一个变量跟对应两个变量之间的关系，按照index分类，求value各列值的和 aggfunc =np.sum
passenger_stat = titanicFile.pivot_table(index='Embarked',values=['Fare','Survived'],aggfunc=np.sum)
print(passenger_stat)

#fillna对缺失值填充，dropna对缺失值丢弃
drop_na_columns = titanicFile.dropna(axis=1)
print(drop_na_columns)
#找出subset内列值对应的行如果是空值，就把这行丢掉
drop_na_rows = titanicFile.dropna(axis=0,subset= ['Age','Sex'] )
print(drop_na_rows)

#huoqu di 101 hang de age zhi
row_83_age = titanicFile.loc[101,'Age']
print(row_83_age)


# sales =  [('account', ['Jones LLC', 'Alpha Co', 'Blue Inc', 'Mega Corp']),
#           ('Total Sales', [150, 200, 75, 300]),
#           ('Country', ['US', 'UK', 'US', 'US'])]
#
# df = pd.DataFrame.from_items(sales)
#
# print(df)
#
# indices = [True,False,True,True]
#
# print(df(indices))
#
# df.Country == 'US'
# print(df[df['Country'] == 'US'])

# print("******************************")
#
# arr = np.arange(7)
# print(arr)
# booling1 = [True,False,False,True,True,False,False]
# booling2 = np.array([True,False,False,True,True,False,False])
# print(arr[booling1])
# print(booling2)
#
#
# arr1 = np.arange(28).reshape(7,4)
# print(arr1)
# print("**********************")
# print(arr1[booling1])
# print(arr1[booling2])
#
# names = np.array(['Ben','Tom','Ben','Jeremy','Jason','Michael','Ben'])
# print(names)
# namebool = ([names == 'Ben',2])
# print(namebool)
# print(arr1)
# print(arr1[names == 'Ben',2:4])
# print(arr1[names != 'Ben'])
# print(arr1[~(names == 'Ben')])
#
# print(arr1[arr1>15])
# arr1[arr1>15] = 0
# print(arr1)