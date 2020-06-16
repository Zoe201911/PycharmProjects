"""
APP注册归属地，绑定归属地占比
"""
import pandas as pd

class Address:
    def __init__(self,excelName,sheetName):
        self.excelName = excelName
        self.sheetName = sheetName

    def getDictData(self):
        pdDictData = pd.read_excel(self.excelName,self.sheetName)
        dictData = dict(pdDictData.loc[:,:].values)
        return dictData

    def dealWithData(self,dictDataA,dictDataB):
        listAB = []
        listPer = []
        listKeyA = list(dictDataA.keys())[::-1]
        listKeyB = list(dictDataB.keys())[::-1]
        for i in listKeyA:
            if i in listKeyB:
                listAB.append(dictDataB[i])
                m = dictDataB[i]/dictDataA[i]
                listPer.append('{:.2%}'.format(m))#换算成百分比保留两位小数
            else:
                del(dictDataA[i])
        return listAB[::-1],listPer
    def setNewExcelData(self,excelName,dictDataA,dictDataB,*columnName):
        listA,listB = self.dealWithData(dictDataA,dictDataB)
        dictData = {columnName[0]:list(dictDataA.keys()),columnName[1]:list(dictDataA.values()),
                    columnName[2]:listA,columnName[3]:listB}
        pdsheet = pd.DataFrame(dictData)
        self.setNewExcel(excelName,pdsheet)

    def setNewExcel(self, excelName, pdSheet):
        with pd.ExcelWriter(excelName) as writer:
            pdSheet.to_excel(writer, sheet_name='工作表1')
        writer.save()


if __name__ == '__main__':
    addA = Address('fileExcel/归属地.xlsx','注册数量')
    addB = Address('fileExcel/归属地.xlsx','绑定数量')
    dictDataA = addA.getDictData()
    dictDataB = addB.getDictData()
    addA.setNewExcelData('fileExcel/归属地注册绑定率.xlsx',dictDataA,dictDataB,'城市名称','注册数量','绑定数量','占比')



