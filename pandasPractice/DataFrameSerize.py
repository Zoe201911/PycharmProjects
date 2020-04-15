import pandas as pd
from pandas import Series

DataFile = pd.read_csv('titanic_train.csv')
series_file = DataFile['Name']
print(type(series_file))
print(series_file[0:5])

file_name = series_file.values
print(file_name)
print(type(file_name))

series_rt = DataFile['Age']
print(series_rt[0:5])
age_values = series_rt.values
# print(age_values)

