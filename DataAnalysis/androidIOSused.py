"""
统计Android和IOS手机使用占比
"""
import pandas as pd
from matplotlib import pyplot
from matplotlib import font_manager
class PhoneUsed:
    def __init__(self,excelName,newExcelName):
        self.excelName = excelName
        self.newExcelName = newExcelName

    def dealWithData(self):
        pdData = pd.read_excel(self.excelName)
        dictData = dict(pdData.loc[:,:].values)
        for i in list(dictData.keys())[::-1]:
            if i == 'debug':
                dictData['c_huawei']+= dictData['debug']
                del(dictData['debug'])
            if i == 'google_play':
                dictData['c_huawei'] += dictData['google_play']
                del(dictData['google_play'])
        return dictData
    def setNewExcel(self):
        dictData = self.dealWithData()
        pdData = pd.DataFrame(dictData)
        with pd.ExcelWriter(self.newExcelName) as writer:
            pdData.to_excel(writer)
        writer.save()

    def drawChart(self):
        dictData = self.dealWithData()
        labels = dictData.keys()
        data = dictData.values()
        my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc', size=12)
        pyplot.title('Android & IOS市场占比', fontproperties=my_font)
        pyplot.axes(aspect='equal')#讲横、纵坐标轴标准化处理，保证饼图是一个正圆
        pyplot.xlim(0,8)
        pyplot.ylim(0,8)
        #绘制饼图
        pyplot.pie(x=data,labels=labels,autopct='%.2f%%',startangle=180,counterclock=False)
        pyplot.show()

if __name__ == '__main__':
    pu = PhoneUsed('fileExcel/AndroidIOS.xlsx','fileExcel/AndroidIOSMix')
    pu.drawChart()


"""
plt.pie(x=data, #绘制数据
labels=labels,#添加编程语言标签
explode=explode,#突出显示Python
colors=colors, #设置自定义填充色
autopct='%.3f%%',#设置百分比的格式,保留3位小数
pctdistance=0.8, #设置百分比标签和圆心的距离
labeldistance=1.0,#设置标签和圆心的距离
startangle=180,#设置饼图的初始角度
center=(4,4),#设置饼图的圆心(相当于X轴和Y轴的范围)
radius=3.8,#设置饼图的半径(相当于X轴和Y轴的范围)
counterclock= False,#是否为逆时针方向,False表示顺时针方向
wedgeprops= {'linewidth':1,'edgecolor':'green'},#设置饼图内外边界的属性值
textprops= {'fontsize':12,'color':'black','fontproperties':my_font},#设置文本标签的属性值
frame=1) #是否显示饼图的圆圈,1为显示
"""