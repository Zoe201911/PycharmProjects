import serial
import time
import json
import random
# s =[ 'appCode','appVersion','authAppkey','authSign','authTimespan','authTimeZone','channel','country','deviceId','deviceType','lang','pageIndex','pageSize','productId','deviceid','requestid']
# print(s)
#
# s.sort(key=locale.strxfrm)
# for str in s:
#     print(str.encode('utf-8'))
# str="1538105560006appCode=global_eappVersion=1.0.1authTimespan=1547172053783authTimeZone=Asia/Shanghaichannel=appstorecountry=CNdeviceType=2lang=ZH_CNpageIndex=1pageSize=10productId=c3893c5e-d369-41c1-adac-998a6bb288b8fb7045ebb8ae5297bca45cbf5a5597ab"
# hash = hashlib.md5()
# hash.update(str.encode('utf-8'))
# res= hash.hexdigest()
# print(res)
# # utf-8 转成 Unicode，decode(解码)需要注明当前编码格式

# -*- coding: utf-8 -*-
# import binascii
# #16进制整数转ASCii编码字符串
# a = 0x665554
# b = hex(a) #转换成相同的字符串即'0x665554'
# b = b[2:]  #截取掉'0x'
# c = binascii.a2b_hex(b) #转换成ASCii编码的字符串
# print("a:%x, b:%s,c:%s" %(a,b,c))
# print type(a)
# print type(b)
# print type(c)

#选择设备（设备路径，端口号，连接超时时间
# ser=serial.Serial('/dev/tty.SLAB_USBtoUART','115200',timeout=30)
ser=serial.Serial('/dev/tty.SLAB_USBtoUART','115200',timeout=30)


bp=100
for n in range (100) :
    vpr = random.randint(0, 100)
    dv = random.randint(0, 100)
    bp=bp-1
    data = {
             "wm":3,    #  0 停机1 待机2 充电3 放电4 演示5 测试机6 其他7 配网成功（提示用户按下主机开关开始使用）
             "cds":1,   #  0 调速模式来源于手机触控屏   自动调速模式时，功率显示条来源于手机触控屏   手动调速模式时，功率显示条来源于主机       1 放电模式来源于主机，   任何调速模式下，功率显示条都来源于主机
             "smr":0,   #  0 主机要求自动调速模式   1 主机要求手动调速模式
             "vpr":vpr,  # 主机要求的功率显示条长度0~100
             "bp":bp,   # 电量百分比(BmsPercent) 0x00~0x64 显示0~100%，0xF0(240)不显示百分比
             "dv":dv,   #灰尘度(DustValue)0~100，默认值0
             "e":1,     #二进制的每一个BIT表示一种故障，对应的BIT等于0表示没有故障，1表示有故障
                        # BIT0 (1)：主机吸尘电机状态：0)正常，1)自身故障
                        # BIT1 (2)：风道半堵：0)正常，1)堵塞
                        # BIT2 (4)：风道全堵：0)正常，1)堵塞
                        # BIT3 (8)：地刷状态：0)正常，1)堵转过流、短路
                        # BIT4 (16)：灰尘传感器状态：0)正常，1)电路故障、光路遮挡
                        # BIT5 (32)：触控屏2秒没有通信：0)通信正常，1)通信异常(这个不要在界面显示。
                        #                   可能是无屏幕的A12，也可能是有屏幕的但是屏幕坏了，无法区分)
                        # BIT6 (64)：  充电时电池包过温、过充等所有可以自行恢复的故障（不要显示）
                        # BIT7 (128)：充电时没有电池包
                        # BIT8 (256)：充电超时
                        # BIT9 (512)：充电时过流、过压等所有不可自行恢复的故障
             "dst":3600000,#累计放电时间(DischargeSecondTotal)    dst>ds
             "ds":3600,   #本次放电时间(DischargeSecond)
             "dnt":3000000000,#累计灰尘颗数(DustNumTotal)     dnt>dn
             "dn":100000000,#本次灰尘颗数(DustNum)
             "bc":2500 #电芯总容量(BmsCapacity)
             }
    time.sleep(1)
    str='`FRcft\x00j'+json.dumps(data)+'\x00\n'

    print(str)
    # c = str
    # e = 0  #暂存结果
    # for i in c:
    #   d = ord(i) #单个字符转换成ASCii码
    #   e = e*256 + d  #将单个字符转换成的ASCii码相连
    #print("e:%x" %e)

    str=str.encode("utf-8")
    ser.write(str)
ser.read()
ser.close()











