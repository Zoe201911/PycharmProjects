import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# 使图形中的中文正常编码显示
myfont = matplotlib.font_manager.FontProperties(fname = '/System/Library/Fonts/STHeiti Light.ttc')
readFile = pd.read_excel('read.xlsx')
readFile['DATE'] = pd.to_datetime(readFile['DATE'])
print(readFile.head(10))
plt.plot()#如果没有参数，画布画出来是空的
# plt.show()
first_ten = readFile[0:10]
plt.plot(first_ten['DATE'],first_ten['VALUE'])#表示X轴和Y轴的含义
plt.xticks(rotation = 45)#X轴的标记倾斜45度，rotation=90倾斜90度
plt.xlabel('Date')
plt.ylabel('Values')
plt.title('年份转换率',fontproperties = myfont)
plt.show()

# print(matplotlib.matplotlib_fname())#获取matplotlib包所在的文件夹
