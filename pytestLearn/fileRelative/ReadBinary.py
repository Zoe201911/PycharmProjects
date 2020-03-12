import struct

import os

def readFile():
    filepath = 'ZB1961A-01_WT588S_Mandarin_1.0.1.0.bin'
    binfile = open(filepath,'rb') #打开二进制文件
    size = os.path.getsize(filepath) #获得文件大小
    print("文件大小：",size)
    data = binfile.read()
    # print(data[-256:])
    list1 = []
    if size <= 0:
        print("该文件是空文件或者不存在")
    elif size >0 :
        if size%256 != 0:
            n = 256-size%256
            print("n的值是",n)
            binfile = open(filepath, 'a+')
            for i in range(0,n):

                binfile.writelines('F')
            binfile.close()
            binfile = open(filepath, 'rb')
            data = binfile.read()
            size = os.path.getsize(filepath)
            print("添加后的文件大小：",size)
            # print(type(data))

        print("%s个256段"%(int(size)/256))
        # print(data[-256:])
        for j in range(0,int(size/256) ):
            data_256 = data[j*256:(j+1)*256]
            list1.append(data_256)
            # print("第%s段的值是%a"%(j,data_256.hex().upper()))

        for i in range(0,11):
            print("第%s片段的值是%s"%(i,list1[i].hex().upper()))





    binfile.close()
if __name__ == '__main__':
    readFile()