"""
绘制绑定注册量走势图表

"""
import pandas as pd
from pandas import Series
import matplotlib as plt
import numpy as np
from matplotlib import pyplot
from matplotlib import font_manager

def getData(file1,sheet):
    """
    获取到每一个sheet中想要的列，把这些列合并到一个Excel中去
    :param file1:
    :param sheet:
    :return:
    """
    pdSheet0 = pd.read_excel(file1,sheet[0])
    for i in sheet:
        pdSheet = pd.read_excel(file1,i)
        #获取列名为i的一列数据，Series类型
        bindData = pdSheet.pop(i)
        bindData = dealWithMissData(bindData, i)
        pdSheet0[i] = bindData
    print(pdSheet0)
    getNewExcel(pdSheet0)


def getNewExcel(pdSheet0):
    """
    生成一个新的Excel
    :param pdSheet0: 要生成Excel对应的数据集合
    :return:
    """
    with pd.ExcelWriter("绑定注册1.xlsx") as writer:
        pdSheet0.to_excel(writer, sheet_name='工作表1')
    writer.save()


def dealWithMissData(bindData, i):
    """
    处理月份不够15个月的数据
    :param bindData: 获取到这个sheet的列的合集
    :param i: 这个sheet的列名
    :return:
    """
    if (i == '水机绑定总量' or i == '吹风机绑定总量'):
        listData = []
        for j in range(12):
            listData.append(0)
        listBind = bindData.values.tolist()
        listData[len(listData):len(listData)] = listBind
        dictData = {i: listData}
        bindData = pd.DataFrame(dictData)
    return bindData

def drawChart():
    #支持中文
    my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
    DataFrame = pd.read_excel("绑定注册1.xlsx",'工作表1')
    x = DataFrame.loc[:,"月"].values
    y = DataFrame.loc[:,"注册量"].values
    fig = pyplot.figure(figsize=(15,8),dpi =80)
    pyplot.plot(x, y)
    pyplot.xlim(-1,15)
    pyplot.xticks(x,fontproperties=my_font)
    pyplot.xlabel('时间',fontproperties = my_font)
    pyplot.ylabel('数量',fontproperties =  my_font)
    pyplot.title('注册绑定走势图',fontproperties = my_font)
    pyplot.show()


if __name__ == '__main__':
    getData("绑定注册.xlsx",['注册量','机器绑定总量','吸尘器绑定总量','水机绑定总量','吹风机绑定总量'])
    drawChart()