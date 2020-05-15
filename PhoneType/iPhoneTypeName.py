import pandas as pd


def convertPhone(phoneMode,phoneName):
    pMdDataA = getAExcelData(phoneMode,'设备型号','名称')
    pNdCountListB, pNdCountTypeListB, pNdListB = getBExcelData(phoneName,'手机型号','总量','手机系统版本号')
    dataDict = convertABcolumn(pMdDataA, pNdListB)
    dataDcitConvert = getExcelABconnect(dataDict, pNdCountListB, pNdCountTypeListB,'手机型号','手机名称','总数量','手机系统版本号')
    getNewExcel(dataDcitConvert)
    # dataDcitConvert.to_excel("iPhone123.xlsx",encoding='UTF-8',index=False,header=True)使用csv

def convertABcolumn(pMdDataA, pNdListB):
    """
    把B中字段按照A Excel字典中的对应关系，重新对应
    :param pMdDataA:
    :param pNdListB:
    :return:
    """
    dataDict = {}
    for i in pNdListB:
        if i in pMdDataA.keys():
            dataDict[i] = pMdDataA.get(i)
        if i not in pMdDataA.keys():
            print(i)  # 如果字典Excel中没有该字段，打印该字段
    return dataDict


def getNewExcel(dataDcitConvert):
    """
    生成新的excel
    :param dataDcitConvert:
    :return:
    """
    with pd.ExcelWriter('iPhone123.xlsx') as writer:
        dataDcitConvert.to_excel(writer, sheet_name='工作表1')
    writer.save()


def getExcelABconnect(dataDict, pNdCountListB, pNdCountTypeListB,*args):
    """
    获取到AB Excel的各列名，然后找到自己需要的进行拼接
    :param dataDict:
    :param pNdCountListB:
    :param pNdCountTypeListB:
    :param args:
    :return:
    """

    dataDcitConvert = {args[0]: list(dataDict.keys()), args[1]: list(dataDict.values())}
    dataDcitConvert = pd.DataFrame(dataDcitConvert)
    dataDcitConvert[args[2]] = pNdCountListB
    dataDcitConvert[args[3]] = pNdCountTypeListB
    return dataDcitConvert


def getBExcelData(phoneName,*args):
    """
    获取Excel B需要的数据内容
    :param phoneName: excel B的名称
    :param args: Excel的列名称
    :return:
    """
    pNdB = pd.read_excel(phoneName)
    pNdDataNdarryB = pNdB.loc[:, args[0]].values
    pNdListB = pNdDataNdarryB.tolist()
    if len(args)>=2:
        pNdCountNdarrayB = pNdB.loc[:, args[1]].values
    if len(args)>=3:
        pNdTypeCountNdarrayB = pNdB.loc[:, args[2]].values
    pNdCountListB = pNdCountNdarrayB.tolist()
    pNdCountTypeListB = pNdTypeCountNdarrayB.tolist()
    return pNdCountListB, pNdCountTypeListB, pNdListB



def getAExcelData(phoneMode,*args):
    """
    获取主Excel的数据内容
    :param phoneMode: Excel名称
    :param args: excel 列明
    :return:
    """
    pMdA = pd.read_excel(phoneMode)
    pMdDataNdarrayA = pMdA.loc[:,[args[0],args[1]]].values
    pMdDataA = dict(pMdDataNdarrayA)
    # print(pMdDataA)
    return pMdDataA


if __name__ == '__main__':
        convertPhone("国际手机型号对应表.xlsx","国际手机登录.xlsx")


