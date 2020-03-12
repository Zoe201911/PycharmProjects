import xlrd

#打开文件
workbook = xlrd.open_workbook('/Users/zoe/Desktop/HairDrier.xlsx')

#获取所有sheet name
sheet_all = workbook.sheet_names()
sheet_1 = workbook.sheet_by_index(0)

print("all sheet names:",sheet_all)
print("获取第一个sheet的名称：",sheet_1.name)

#获取指定单元格里的值
cell_name = sheet_1.cell_value(2,2)
print("获取单元格值：",cell_name)

#获取sheet的一行数据
rows = sheet_1.row_values(1)
#获取sheet的一列数据
cols = sheet_1.col_values(2)
print("获取第二行值：",rows)
print("获取第三列值：",cols)

#获取sheet名，行数，列数
print(sheet_1.name,sheet_1.nrows,sheet_1.ncols)
arrayNum = 6
tables = []
newTable = []
listName = []
def read_excel():
    workbook = xlrd.open_workbook(r'/Users/zoe/Desktop/HairDrier.xlsx')
    sheet_name = workbook.sheet_names()
    sheet = workbook.sheet_by_index(2)
    print('sheet的名称%s,行数%s,列数%s'%(sheet_name,sheet.nrows,sheet.ncols))
    rows = sheet.row_values(1)
    cols = sheet.col_values(2)
    print('获取的第二行内容%s，获取的第三列数值%s'%(rows,cols))
    for coln in sheet.row_values(0):
        listName.append(coln)
    print(listName)
    for rown in range(1,sheet.nrows):
        array = {listName[0]:'',listName[1]:'',listName[2]:'',listName[3]:''}
        array[listName[0]] = sheet.cell_value(rown,0)
        array[listName[1]] = sheet.cell_value(rown, 1)
        array[listName[2]] = sheet.cell_value(rown, 2)
        array[listName[3]] = sheet.cell_value(rown, 3)
        tables.append(array)
    print(len(tables))
    print(tables)

if __name__ == '__main__':
    read_excel()
    print("读取成功")