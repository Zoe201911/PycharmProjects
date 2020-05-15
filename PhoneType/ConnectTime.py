import numpy as np
import pandas as pd

def convertTime(file1):
    pMd = pd.read_excel(file1)
    pdValues = pMd.loc[:, ['配网时间']].values.tolist()
    listTime = []
    for i in pdValues:
        for j in i:
            j = i[0].split('-')[1].split('=')[0]
            h = round(int(j)/1000/60,2)
            if(h<5):
                listTime.append(h)
    listNp = pd.DataFrame(listTime)
    with pd.ExcelWriter('connectTime.xlsx') as writer:
        listNp.to_excel(writer,sheet_name='工作表1')
    writer.save()

    print(listTime)


if __name__ == '__main__':
    convertTime('配网时间.xlsx')