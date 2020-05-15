import pandas as pd

def tongjiTime(excelFile):
    pdList = getExcelData(excelFile,'配网时长')
    dictConvert = convertList(*pdList)
    generateNewExcel(dictConvert,'时间段','总量','time.xlsx')


def generateNewExcel(dictConvert,*args):
    """
    生成新的Excel
    :param dictConvert:
    :param args:
    :return:
    """
    dataDictConvert = {args[0]: list(dictConvert.keys()), args[1]: list(dictConvert.values())}
    dataDictConvert = pd.DataFrame(dataDictConvert)
    with pd.ExcelWriter(args[2]) as writer:
        dataDictConvert.to_excel(writer, sheet_name='工作表1')
    writer.save()


def getExcelData(excelFile,*args):
    """
    获取Excel里的内容
    :param excelFile:
    :param args:
    :return:
    """
    pdNet = pd.read_excel(excelFile)
    if(len(args)>=1):
        pdList = pdNet.loc[:, args[0]].values
    return pdList


def convertList(*args):
    """
    统计配网区间在0-1，1-2，2-3，3以上的数据量
    list参数在传参时，如果传的是list，需要在list前面加*
    :param args:
    :return:
    """

    dictCount = {'0-1':0,'1-2':0,'2-3':0,'3~':0}
    for i in args:

        if i <= 1:
            dictCount['0-1']+=1
        elif i>1 and i<=2:
            dictCount['1-2']+=1
        elif i>2 and i<=3:
            dictCount['2-3']+=1
        else:
            dictCount['3~'] +=1
    dictCount = {"0-1": dictCount['0-1'], '1-2': dictCount['1-2'], '2-3': dictCount['2-3'], '3~': dictCount['3~']}
    return dictCount

tongjiTime('配网时长.xlsx')

