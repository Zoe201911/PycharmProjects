"""
date : 2019.01.16
author:Zoe
function:模拟主机发送指令给WiFi芯片，到达控制手机的目的
"""


import serial
import json
import random
import time
import binascii
#连接串口设备，设置端口号，设置连接超时时长


ser1 = serial.Serial('/dev/tty.SLAB_USBtoUART', '115200', timeout=30)


#主机发送配网指令，同时清除已配网信息
def factoryReset():

    data = {}
    str1 = '`FPFactoryReset\x00\x00q0009\x00j'+json.dumps(data)+'\x00\n'
    print("主机发送的指令是：",str1.encode('gbk'))
    result = ser1.write(str1.encode('gbk'))
    print("*************",type())

#获取WiFi设备信息，发射热点
def  connectWifiInfo():
    data = {
        "ret": "ok",
        "sc": 1,
        "ssidPrefix": "Tineco_",
        "name": "0123456789012345a045",
        "type": "q5ez2q"
    }
    str = '`FPGetDeviceCap\x00\x00pdcap\x00j' + json.dumps(data) + '\x00\n'
    str = str.encode("gbk")

    ser1.write(str)
    # ser1.flush()
    print("主机发送的指令是：", str)
    # time.sleep(200)
    print("**************")

#主机获取WiFi设备状态
def  getWifiInfo():
    data = {}
    str1 = '`FPGetWIFIStat\x00\x00q0060\x00j'+json.dumps(data)+'\x00\n'
    str1 = str1.encode('utf-8')
    print("主机发送的指令：",str1)
    ser1.write(str1)
#主机获取设备连接状态
def getConnectionState():
    pass
#主机初始化
def getMainInit():
    data = {}
    str = 'FPGetWIFIStat\x00\x00q0060\x00j'+json.dumps(data)+'\x00\n'
    str = str.encode("utf-8")
    print("主机发送指令：",str)
    ser1.write(str)
def operation():
    n = 0
    dnt = 0
    dst = 0
    while n <100:

        n +=1 #循环的次数
        dv = n
        bp = 100 - n
        vpr = n
        dn = random.randint(0,100000000000)
        ds = random.randint(1,2700)
        dnt += dn
        dst += ds
        data = {
            "wm": 4,  # 0 停机1 待机2 充电3 放电4 演示5 测试机6 其他7 配网成功（提示用户按下主机开关开始使用）
            "cds": 1, # 0 调速模式来源于手机触控屏自动调速模式时，功率显示条来源于手机触控屏手动调速模式时，功率显示条来源于主机 1、放电模式来源于主机,任何调速模式下，功率显示条都来源于主机
            "smr": 0,  # 0 主机要求自动调速模式   1 主机要求手动调速模式
            "vpr": vpr,  # 主机要求的功率显示条长度0~100
            "bp": bp,  # 电量百分比(BmsPercent) 0x00~0x64 显示0~100%，0xF0(240)不显示百分比
            "dv": dv,  # 灰尘度(DustValue)0~100，默认值0
            "e": 0,  # 二进制的每一个BIT表示一种故障，对应的BIT等于0表示没有故障，1表示有故障
            "dst": dst,  # 累计放电时间(DischargeSecondTotal)    dst>ds
            "ds": ds,  # 本次放电时间(DischargeSecond)
            "dnt": dnt,  # 累计灰尘颗数(DustNumTotal)     dnt>dn
            "dn": dn,  # 本次灰尘颗数(DustNum)
            "bc": 2500  # 电芯总容量(BmsCapacity)
        }
        #json常用的两个函数dumps和dump函数，两个函数的唯一区别就是dump把Python对象转化成json对象生产一个fp得的文件流，而dumps则生成了一个字符串
        str = '`FRcft\x00j' + json.dumps(data) + '\x00\n'

        str = str.encode("utf-8")
        print("生成的字符串为：", str)
        # ser.write(str)

        time.sleep(0.2)
    # ser.read()
    # ser.close()


if __name__ == '__main__':
    # ser1.open()
    factoryReset()
    connectWifiInfo()
    # getWifiInfo()
    # operation()
    # catchPortData()
    ser1.close()

# https://www.cnblogs.com/attentle/p/7098408.html
