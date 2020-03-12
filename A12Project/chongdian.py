"""
测试WiFi模块与手机的通讯
先发指令
主机发送配网指令，同时清除已配信息
b'`FPFactoryReset\x00\x00q0009\x00j{}\x00\n’
b'`FPFactoryReset\x00\x00q0009\x00j{}\x00\n'
604650466163746f7279526573657400007130303039006a7b7d000a

获取wifi设备信息,发射热点
b'`FPGetDeviceCap\x00\x00pdcap\x00j{"ret":"ok","sc":1,"ssidPrefix":"Tineco_","name":"0123456789012345a045","type":"q5ez2q"}\x00\n'
60465047657444657669636543617000007064636170006a7b22726574223a226f6b222c227363223a312c2273736964507265666978223a2254696e65636f5f222c226e616d65223a223031323334353637383930313233343561303435222c2274797065223a227135657a3271227d000a
让WiFi模块发射热点，手机配网成功，然后模拟发送数据
"""

import serial
import time
import json
import random
#ser=serial.Serial('COM14','115200',timeout=30)
ser = serial.Serial('/dev/tty.usbserial-AH06YBGR','115200',timeout=30)
ser1 = serial.Serial('/dev/tty.SLAB_USBtoUART','115200',timeout=30)

for bp in range (101) :
    listerror = ['64','128','256','512','0','240']
    i=random.randint(0,4)
    errornum = listerror[i]
    data = {
             "wm":2,    # 0 停机1 待机2 充电3 放电4 演示5 测试机6 其他7 配网成功（提示用户按下主机开关开始使用）
             "cds":0,   # 0 调速模式来源于手机触控屏   自动调速模式时，功率显示条来源于手机触控屏   手动调速模式时，功率显示条来源于主机       1 放电模式来源于主机，   任何调速模式下，功率显示条都来源于主机
             "smr":0,  # 0 主机要求自动调速模式   1 主机要求手动调速模式
             "vpr":0,  # 主机要求的功率显示条长度0~100
             "bp":bp,   # 电量百分比(BmsPercent) 0x00~0x64 显示0~100%，0xF0(240)不显示百分比
             "dv":0,   # 灰尘度(DustValue)0~100，默认值0
             "e":errornum,
                        # 二进制的每一个BIT表示一种故障，对应的BIT等于0表示没有故障，1表示有故障
                        # BIT0 (1)：主机吸尘电机状态：0)正常，1)自身故障
                        # BIT1 (2)：风道半堵：0)正常，1)堵塞
                        # BIT2 (4)：风道全堵：0)正常，1)堵塞
                        # BIT3 (8)：地刷状态：0)正常，1)堵转过流、短路
                        # BIT4 (16)：灰尘传感器状态：0)正常，1)电路故障、光路遮挡
                        # BIT5 (32)：触控屏2秒没有通信：0)通信正常，1)通信异常(这个不要在界面显示。可能是无屏幕的A12，也可能是有屏幕的但是屏幕坏了，无法区分)
                        # BIT6 (64)：  充电时电池包过温、过充等所有可以自行恢复的故障（不要显示）
                        # BIT7 (128)：充电时没有电池包
                        # BIT8 (256)：充电超时
                        # BIT9 (512)：充电时过流、过压等所有不可自行恢复的故障
             "dst":0,  #累计放电时间(DischargeSecondTotal)    dst>ds
             "ds":0,   #本次放电时间(DischargeSecond)
             "dntL":0,  #累计灰尘颗数(DustNumTotal)     dnt>dn
             "dntH":0,  # 累计灰尘颗数(DustNumTotal)     dnt>dn
             "dn":0,  #本次灰尘颗数(DustNum)
             "bc":2500  #电芯总容量(BmsCapacity)
             }
    time.sleep(0.1)
    #间隔时间
    str='`FRcft\x00j'+json.dumps(data)+'\x00\n'
    print(str)

    str = str.encode("utf-8")
    ser.write(str)

    print(ser1.readline())
    print(">>>>>>>>>>>>>>>>>>>")

ser.read()
ser.close()





"""

def batteryError(data):
    listerror = ['64', '128', '256', '512', '0', '240']
    for i in range(len(listerror)):
        data['e'] = i
"""


