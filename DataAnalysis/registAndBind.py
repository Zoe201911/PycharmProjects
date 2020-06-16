"""
绘制绑定注册量走势图表

"""
import pandas as pd
from matplotlib import pyplot
from matplotlib import font_manager

def getData(file1,*sheet):
    """
    获取到每一个sheet中想要的列，把这些列合并到一个Excel中去
    :param file1:
    :param sheet:
    :return:
    """
    pdSheet0 = pd.read_excel(file1,sheet[0])
    for i in sheet:
        pdSheet = pd.read_excel(file1,i)
        #获取列名为i的一列数据，Series类型
        bindData = pdSheet.pop(i)
        bindData = dealWithMissData(bindData, i)
        pdSheet0[i] = bindData
    print(pdSheet0)
    setNewExcel(pdSheet0)



def setNewExcel(pdSheet0):
    """
    生成一个新的Excel
    :param pdSheet0: 要生成Excel对应的数据集合
    :return:
    """
    with pd.ExcelWriter("fileExcel/绑定注册1.xlsx") as writer:
        pdSheet0.to_excel(writer, sheet_name='工作表1')
    writer.save()


def dealWithMissData(bindData, i):
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

def drawChart(listColName):
    #支持中文
    my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc',size=12)
    DataFrame = pd.read_excel("fileExcel/绑定注册1.xlsx",'工作表1')
    #时间在Excel中是文本的格式，否则取出来的会默认带上时间点
    x = DataFrame.loc[:, "时间"].values
    pyplot.figure(figsize=(15, 8), dpi=80)
    for i in listColName:
        y = DataFrame.loc[:,i].values
        pyplot.plot(x,y,label = i)
        #设置图例为中文显示在左上方
        pyplot.legend(prop = my_font,loc = 'upper left')

    pyplot.xlim(-1,15)
    #设置y轴从0开始
    pyplot.ylim(bottom=0.)
    pyplot.xticks(x,fontproperties=my_font)
    pyplot.xlabel('时间',fontproperties = my_font)
    pyplot.ylabel('每月总数量',fontproperties =  my_font)
    pyplot.title('注册绑定走势图',fontproperties = my_font)
    pyplot.show()


if __name__ == '__main__':
    getData("fileExcel/绑定注册.xlsx",'注册量','机器绑定总量','吸尘器绑定总量','水机绑定总量','吹风机绑定总量')
    drawChart(['注册量','机器绑定总量','吸尘器绑定总量','水机绑定总量','吹风机绑定总量'])





"""


#真实用户每月注册量
select FROM_UNIXTIME(create_time / 1000, '%Y-%m')  as '时间',
       count(id)                                            as '注册量'
from `tek-ecosystem-cn`.gl_user_info
where status = 'ENABLED'
  and create_time < unix_timestamp('2020-06-1 00:00:00') * 1000
group by FROM_UNIXTIME(create_time / 1000, '%Y-%m')
order by FROM_UNIXTIME(create_time / 1000, '%Y-%m');
#每月绑定设备量
select  FROM_UNIXTIME(create_time / 1000, '%Y-%m')  as '时间',
       count(id)                                            as '机器绑定总量'
from `tek-ecosystem-cn`.gl_product_bind_info
where gl_product_bind_info.user_id
    in (select id from `tek-ecosystem-cn`.gl_user_info where status = 'ENABLED')
  and product_id is not null
  and create_time < unix_timestamp('2020-06-01 00:00:00') * 1000
group by FROM_UNIXTIME(create_time / 1000, '%Y-%m')
order by FROM_UNIXTIME(create_time / 1000, '%Y-%m');


#水机每月绑定量(水机='9rotkh'，吹风机='f284us'，吸尘器绑定总量，水机绑定总量，吹风机绑定总量）
select FROM_UNIXTIME(create_time / 1000, '%Y-%m')  as '时间',
       count(id)                                            as '吸尘器绑定总量'
from `tek-ecosystem-cn`.gl_product_bind_info
where gl_product_bind_info.user_id
    in (select id from `tek-ecosystem-cn`.gl_user_info where status = 'ENABLED')
  and product_id is not null
  and product_type  not in ('f284us','9rotkh')
#   and product_type = 'f284us'
and create_time < unix_timestamp('2020-06-01 00:00:00')*1000
group by FROM_UNIXTIME(create_time / 1000, '%Y-%m')
order by FROM_UNIXTIME(create_time / 1000, '%Y-%m');

#注册的真实用户绑定的机器类型的数量（某个时间段）
select product_type as '机器类型', count(product_type) as '机器总数量'
from `tek-ecosystem-cn`.gl_product_bind_info
where gl_product_bind_info.user_id
          in (select id from `tek-ecosystem-cn`.gl_user_info where status = 'ENABLED')
and unix_timestamp('2020-04-08 00:00:00')*1000> create_time and create_time> unix_timestamp('2020-03-01 00:00:00')*1000
group by product_type
order by count(product_type) desc ;

"""