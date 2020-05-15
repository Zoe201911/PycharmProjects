import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# 使图形中的中文正常编码显示
myfont = matplotlib.font_manager.FontProperties(fname = '/System/Library/Fonts/STHeiti Light.ttc')
readFile = pd.read_excel('read.xlsx')
# readFile['DATE'] = pd.to_datetime(readFile['DATE'])
# print(readFile.head(10))
# plt.plot()#如果没有参数，画布画出来是空的
# # plt.show()
# first_ten = readFile[0:10]
# plt.plot(first_ten['DATE'],first_ten['VALUE'])#表示X轴和Y轴的含义
# plt.xticks(rotation = 45)#X轴的标记倾斜45度，rotation=90倾斜90度
# plt.xlabel('时间')
# plt.ylabel('取值')
# plt.title('年份转换率',fontproperties = myfont)
# plt.show()
#
# print(matplotlib.matplotlib_fname())#获取matplotlib包所在的文件夹

# fig = plt.figure()
fig = plt.figure(figsize=(3,3))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
# ax3 = fig.add_subplot(2,2,4)
ax1 .plot(np.random.randint(1,5,5),np.arange(5))
ax2.plot(np.arange(10)*3,np.arange(10))
# plt.show()

fig = plt.figure(figsize=(6,6))
plt.plot(readFile[0:10]['DATE'],readFile[0:10]['VALUE'],c='red')
plt.plot(readFile[11:20]['DATE'],readFile[11:20]['VALUE'],c='blue')
# plt.show()

fig = plt.figure(figsize=(6,6))
colors = ['red','blue','green','orange','black']
for i in range(5):
    start_index = i*10
    end_index = (i+1)*10
    subset = readFile[start_index:end_index]
    #每条折现代表的含义
    label = str(1948+i)
    #生成折现，每条折现代表的含义，以及颜色对应
    plt.plot(subset['DATE'],subset['VALUE'],c= colors[i],label=label)
#标签框放在哪个位置
plt.legend(loc='best')
print(help(plt.legend))
plt.show()