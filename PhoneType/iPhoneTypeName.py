import pandas as pd
from itertools import chain


def convertPhone(phoneMode,phoneName):
    pMd = pd.read_excel(phoneMode)
    pMdDataNdarray = pMd.loc[:,['设备型号','名称']].values
    pMdData = dict(pMdDataNdarray)
    pNd = pd.read_excel(phoneName)
    pNdDataNdarry = pNd.loc[:,['手机型号']].values
    pNdERList = pNdDataNdarry.tolist()
    pNdList = list(chain.from_iterable(pNdERList))
    pNdCountNdarray = pNd.loc[:,['总量']].values
    pNdCountList = list(chain.from_iterable(pNdCountNdarray.tolist()))
    dataDict = {}
    for i in pNdList:
        if i in pMdData.keys():
            dataDict[i] = pMdData.get(i)
        if i  not in pMdData.keys():
            print(i)
    print(dataDict)

    dataDcitConvert = {'手机型号':list(dataDict.keys()),'手机名称':list(dataDict.values())}
    dataDcitConvert = pd.DataFrame(dataDcitConvert)
    dataDcitConvert['总数量'] = pNdCountList
    print(dataDcitConvert)
    with pd.ExcelWriter('iPhone123.xlsx') as writer:
        dataDcitConvert.to_excel(writer,sheet_name='工作表1')
    writer.save()
    # dataDcitConvert.to_excel("iPhone123.xlsx",encoding='UTF-8',index=False,header=True)使用csv


if __name__ == '__main__':
        convertPhone("iPhone型号对应表.xlsx","iPhone.xlsx")