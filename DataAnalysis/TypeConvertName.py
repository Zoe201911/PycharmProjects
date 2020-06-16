"""
数据库里拉出来的都是机器type，需要把type跟机器名称替换
"""
import pandas as pd
from matplotlib import pyplot
from matplotlib import font_manager


class TypeConvertName:
    def __init__(self, filename):
        self.filename = filename

    def getDictData(self):
        pdData = pd.read_excel(self.filename)
        dataType = dict(pdData.loc[:, :].values)
        return dataType

    def getTypeData(self, colunmName):
        pdData = pd.read_excel(self.filename)
        dataType = pdData.loc[:, colunmName].values
        return dataType

    def getNameList(self, listData):
        dictData = dict(self.getDictData())
        listNameData = []
        for i in listData:
            if i in dictData.keys():
                listNameData.append(dictData[i])
        return listNameData

    def dealWithData(self):
        dataType = self.getDictData()
        listkeys = list(dataType.keys())[::-1]  # 必须把dataType.keys()转为list类型才能遍历
        for i in listkeys:
            if i == 'A12':
                dataType['q5ez2q'] += dataType['A12'] + dataType['PURE ONE系列']
                del (dataType['A12'])
            elif i == 'PURE ONE系列':
                del (dataType['PURE ONE系列'])
            elif i == 'PURE ONE J1':
                dataType['ibw0sj'] += dataType['PURE ONE J1']
                del (dataType['PURE ONE J1'])
            elif i == 'FLOOR ONE M':
                dataType['mnee8b'] += dataType['FLOOR ONE M']
                del (dataType['FLOOR ONE M'])
            elif i == '星悦P1':
                dataType['04l3g3'] += dataType['星悦P1']
                del (dataType['星悦P1'])
            elif i == 'PURE ONE M C1':
                del (dataType['PURE ONE M C1'])
            elif i == 'PURE ONE M P1':
                del (dataType['PURE ONE M P1'])
        return dataType

    def setNewExcel(self, excelName, pdSheet):
        with pd.ExcelWriter(excelName) as writer:
            pdSheet0.to_excel(writer, sheet_name='工作表1')
        writer.save()


def setNewConvert():
    global pdSheet0
    tcn01 = TypeConvertName('fileExcel/机器类型名称匹配表.xlsx')
    tcn02 = TypeConvertName('fileExcel/123.xlsx')
    listType = tcn02.getTypeData('机器类型')  # 获取机器类型
    listName = tcn01.getNameList(listType)  # 获取机器类型对应的名称
    dictData = tcn02.dealWithData()  # 获取到123表中的数据整合
    # 必须把dictData.keys()转成list的类型才能作为列值
    dictDatac = {'机器类型': list(dictData.keys()), '机器名称': listName, '总数量': list(dictData.values())}
    pdSheet0 = pd.DataFrame(dictDatac)
    # pdSheet0 = pd.DataFrame(dictData.items(),columns=['type','count'])#字典转DataFrame
    tcn02.setNewExcel('fileExcel/newTypeNameConvert.xlsx', pdSheet0)


def drawChart():
    # 支持中文
    my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc', size=12)
    DataFrame = pd.read_excel("fileExcel/newTypeNameConvert.xlsx")
    x = DataFrame.loc[:, "机器名称"].values
    y = DataFrame.loc[:, '总数量'].values
    autolabel(pyplot.bar(range(len(y)), y,  tick_label=x))

    pyplot.xlim(-1, 15)
    # 设置y轴从0开始
    pyplot.ylim(0,3800)
    pyplot.xticks(fontproperties=my_font, rotation=45,size=7)  # x轴标签45度倾斜
    pyplot.xlabel('机器名称', fontproperties=my_font)
    pyplot.ylabel('总数量', fontproperties=my_font)
    pyplot.title('机器绑定类型图', fontproperties=my_font)
    pyplot.show()


def autolabel(rects):
    """
    设置柱状图形式
    :param rects:
    :return:
    """
    for rect in rects:
        height = rect.get_height()
        pyplot.text(rect.get_x() + rect.get_width() / 2. - 0.2, 1.03 * height, '%s' % int(height))


if __name__ == '__main__':
    setNewConvert()
    drawChart()
