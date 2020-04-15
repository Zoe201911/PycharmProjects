import pandas as pd
import warnings
import math
warnings.filterwarnings('ignore')

def blowerNum(excelName):
    pMd = pd.read_excel(excelName)
    count1 = 0.1
    counta = 1
    count2 =0.1
    count3 =  0.1
    count4 =0.1
    count5 =0.1
    count6 =0.1
    count7=0.1
    count8=0.1
    count9=0.1

    for i in range(0,len(pMd['product_id'])):

        for j in range(i+1,len(pMd['product_id'])):
            if pMd['product_id'][i] == pMd['product_id'][j]:
                if pMd['智能运行时间'][j]>0.1:
                    count1+=1
                else:
                    counta = 0
                if pMd['MAX档运行时间'][j] >0.1:
                    count2+=1
                else:
                    counta=0
                if pMd['冷风运行时间'][j] >0.1:
                    count3+=1
                else:
                    counta=0
                if pMd['APP手动运行时间'][j]>0.1:
                    count4+=1
                else:
                    counta=0
                if pMd['APP个性智能运行时间'][j]>0.1:
                    count5+=1
                else:
                    counta=0
                if pMd['APP冷风运行时间'][j]>0.1:
                    count6+=1
                else:
                    counta=0
                if pMd['APP温和卷发运行时间'][j]>0.1:
                    count7+=1
                else:
                    counta=0
                if pMd['APP本次宠物运行时间'][j]>0.1:
                    count8+=1
                else:
                    counta=0
                if pMd['APP儿童运行时间'][j]>0.1:
                    count9+=1
                else:
                    counta=0
        if count1 <=1:
            pMd['智能运行时间'][i] = counta
            counta = 1
        else:
            pMd['智能运行时间'][i] = math.ceil(count1)
            count1=1
        if count2 <=1:
            pMd['MAX档运行时间'][i]=counta
        else:
            pMd['MAX档运行时间'][i] = math.ceil(count2)
            count2=1
        if count3<=1:
            pMd['冷风运行时间'][i]=counta
        else:
            pMd['冷风运行时间'][i] = math.ceil(count3)
            count3=1
        if count4<=1:
            pMd['APP手动运行时间'][i]=counta
        else:
            pMd['APP手动运行时间'][i] = math.ceil(count4)
            count4 =1
        if count5<=1:
            pMd['APP个性智能运行时间'][i] = counta
        else:
            pMd['APP个性智能运行时间'][i] = math.ceil(count5)
            count5=1
        if count6<=1:
            pMd['APP冷风运行时间'][i] =counta
        else:
            pMd['APP冷风运行时间'][i] = math.ceil(count6)
            count6=1
        if count7<=1:
            pMd['APP温和卷发运行时间'][i] = counta
        else:
            pMd['APP温和卷发运行时间'][i] = math.ceil(count7)
            count7=1
        if count8<=1:
            pMd['APP本次宠物运行时间'][i] = counta
        else:
            pMd['APP本次宠物运行时间'][i] = math.ceil(count8)
            count8=1
        if count9<=1:
            pMd['APP儿童运行时间'][i] =counta
        else:
            pMd['APP儿童运行时间'][i] = math.ceil(count9)
            count9=1

    pMd.drop_duplicates(subset=['product_id'],keep='first',inplace=True)
    # print(pMd)
    pMd.to_excel('blower.xlsx')



if __name__ == '__main__':
    blowerNum('吹风机.xlsx')

# import math
# df = pd.DataFrame({'name':['草莓','苹果','梨','苹果','梨','苹果','苹果','苹果'], 'price':[0,8,1,8,3,0,0,1], 'cnt':[3,4,5,4,1,1,1,1]})
# print(df)
# # # print(df['name'][0])
# # df['price'][0] = 1
# count = 0.1
# count2 = 1
# for i in range(0,len(df['name'])):
#     for j in range(i+1,len(df['name'])):
#         if df['name'][i] == df['name'][j]:
#             if df['price'][j] >0.1:
#                 count +=1
#         else:
#             count2 = 0
#     if count<=1:
#         df['price'][i]=count2
#         count2 = 1
#     else:
#         df['price'][i]=math.ceil(count)
#         count = 0.1
#
# print(df)
# print('------------')
# df.drop_duplicates(subset=['name'],keep='first',inplace=True)
# print(df)
