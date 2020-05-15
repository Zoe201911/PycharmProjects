import pandas as pd

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
    print(getAExcelData("每天清扫.xlsx",'时间','数量'))
