import pandas as pd

def convertRegistBind(excelName):
    pdCountry = getExcelData(excelName, "sheet1",'国家')
    pdCountryReCount = getExcelData(excelName,"sheet1",'总量')
    pdDictCountry = getExcelData(excelName,"sheet2",'国家','总量')
    newDictData = getCountryBind(pdCountry,pdDictCountry)
    generatorExcel(pdCountryReCount, newDictData)


def generatorExcel(pdCountryReCount, pdDictCountry):
    """
    生成新的Excel
    :param pdCountryReCount:
    :param pdDictCountry:
    :return:
    """
    pdDictCountrynew = {"国家":list(pdDictCountry.keys()),"注册总量":pdCountryReCount,"绑定总量":list(pdDictCountry.values())}
    pdCountryBindCount = pd.DataFrame(pdDictCountrynew)
    with pd.ExcelWriter("CountryBindRe.xlsx") as writer:
        pdCountryBindCount.to_excel(writer, sheet_name='工作表1')
    writer.save()


def getCountryBind(pdCountry, pdDictCountry):
    """
    把国家对应的绑定情况和注册情况整合在一起
    :param pdCountry:
    :param pdDictCountry:
    :return:
    """
    newDictData = {}
    newListData = []
    for i in pdCountry:
        if i in pdDictCountry.keys():
            newDictData[i] = pdDictCountry[i]
        else:
            newListData.append(i)
    print("下面这些国家没有绑定机器")
    print(newListData)
    print("这些国家绑定机器了")
    print(newDictData)
    return newDictData


def getExcelData(excelName, sheetName,*columns):
    """
    获取Excel每个sheet的内容
    :param excelName:
    :param sheetName:
    :param columns:
    :return:
    """
    pdData = pd.read_excel(excelName, sheet_name=sheetName)
    if 2>len(columns)>0:
        pdCountry = pdData.loc[:, columns[0]].values
    elif len(columns)>1:
        pdCountry = pdData.loc[:, [columns[0],columns[1]]].values
        pdCountry = dict(pdCountry)
    # print(pdCountry)
    return pdCountry


convertRegistBind("register.xlsx")