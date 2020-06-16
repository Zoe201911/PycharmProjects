"""
excel 文件处理
"""

import pandas as pd
class DealWithExcel:
    def __init__(self,excelName,*sheetName):
        self.excelName = excelName
        self.sheetName = sheetName

    def getData(self,newExcelName,newExcelSheet):
        pdSheet = pd.read_excel(self.excelName,self.sheetName[0])
        for i in self.sheetName:
            pdSheet0 = pd.read_excel(self.excelName,i)
            bindData = pdSheet0.pop(i)
            bindData = self.dealWithMissData(bindData, i)
            pdSheet[i] = bindData
            self.setNewExcel(pdSheet,newExcelName,newExcelSheet)

    def dealWithMissData(self,bindData, i):
        """
        处理月份不够15个月的数据
        :param bindData: 获取到这个sheet的列的合集
        :param i: 这个sheet的列名
        :return:
        """
        if (i == '水机绑定总量' or i == '吹风机绑定总量'):
            listData = []
            for j in range(12):
                listData.append(None)
            listBind = bindData.values.tolist()
            listData[len(listData):len(listData)] = listBind
            dictData = {i: listData}
            bindData = pd.DataFrame(dictData)
        return bindData

    def setNewExcel(self,pdSheetName,newExcelName,newExcelSheet):
        """
        生成一个新的Excel
        :param pdSheet0: 要生成Excel对应的数据集合
        :return:
        """
        with pd.ExcelWriter(newExcelName) as writer:
            pdSheetName.to_excel(writer, sheet_name=newExcelSheet)
        writer.save()

if __name__ == '__main__':
    dwe = DealWithExcel("fileExcel/绑定注册.xlsx",'注册量','机器绑定总量','吸尘器绑定总量','水机绑定总量','吹风机绑定总量')
    dwe.getData('fileExcel/注册绑定2.xlsx','工作表')