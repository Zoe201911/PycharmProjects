import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

reviews = pd.read_excel('test.xlsx')
num_clos = pd.read_excel('test.xlsx').columns.tolist()
num_reviews = reviews[num_clos]
print(num_reviews)
bar_height = reviews.iloc[[3,6,9],0]
print(bar_height)
#bar_position是第一个点离远点的距离
bar_position = np.arange(3)+0.5
print(bar_position)
fig,ax = plt.subplots()
#0.3表示柱的宽度ax.bar()画出来的是竖着的柱状图，ax.barh()画出来的是横向的柱状图
ax.bar(bar_position,bar_height,0.3)
# plt.show()

#绘画散点图
ax.scatter(num_reviews['月数据'],num_reviews['每月注册总量'])
ax.set_xlabel('month')
ax.set_ylabel('total count')
plt.show()
