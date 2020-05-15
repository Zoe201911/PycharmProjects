import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#whitegrid(去掉背景网格）,ticks（x,y 轴加线段）,dark（背景去掉横线）,
def sinplot(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*.5)*(7-i)*flip)
    plt.show()
#
# sns.set_style('dark')
# sns.despine(offset=50)
# sinplot()

sns.set_style('ticks')
data = np.random.normal(size=(20,6))+np.arange(6)/2
sns.boxplot(data = data,palette='deep')
sns.despine()#去掉上面和右面的线段
# sns.despine(left=True)#去掉左边的线段
plt.show()


with sns.axes_style('darkgrid'):
    plt.subplot(211)
    sinplot()
plt.subplot(212)
sinplot(-1)