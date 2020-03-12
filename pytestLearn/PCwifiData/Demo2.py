#!/usr/bin/python
# -*- coding: UTF-8 -*-


import serial
import serial.tools.list_ports
import json


def str2hex(s):
    return ' '.join([hex(ord(c)).replace('0x', '') for c in s])


def hex2str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])

#重置WiFi模块信息
def factory_reset():
    js = {}
    name = 'FactoryReset\0'
    print(name)
    print(name.encode('utf-8'))
    print(str2hex(name))
    client_id = '\0'
    print(client_id)
    print(client_id.encode('utf-8'))
    print(str2hex(client_id))
    resp_id = 'q0009\0'
    print(resp_id)
    print(resp_id.encode('utf-8'))
    print(str2hex(resp_id))
    payload = json.dumps(js)
    print(payload)
    print(payload.encode('utf-8'))
    print(str2hex(payload))
    packet = '`FP' + name + client_id + resp_id + 'j' + payload + '\0' + '\n'
    print(packet)
    print(packet.encode('utf-8'))
    print(str2hex(packet))
    return packet.encode('utf-8')

#发射WiFi模块热点
def wifi_info_response():
    js = {}
    name = 'GetDeviceCap\0'
    client_id = '\0'
    resp_id = 'pdcap\0'
    d = json.loads(json.dumps(js))
    d['ret'] = 'ok'
    d['sc'] = 1
    d['ssidPrefix'] = 'Tineco_'
    d['name'] = '0123456789012345a001'
    d['type'] = 'q5ez2q'
    payload = json.dumps(d)
    packet = '`FP' + name + client_id + resp_id + 'j' + payload + '\0' + '\n'
    print(packet)
    print(packet.encode('utf-8'))
    print(str2hex(packet))
    return packet.encode('utf-8')

#获取WiFi设备状态
def wifi_infomation():
    js = {}
    name = 'GetWIFIStat'
    client_id = '\0'
    resp_id = 'q006\0'
    payload = json.dumps(js)
    packet = '`FP' + name + client_id + resp_id + 'j' + payload + '\0' + '\n'
    print(packet.encode('utf-8'))
    print(str2hex(packet))
    return packet.encode('utf-8')


if __name__ == '__main__':
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) == 0:
        print('无可用串口')
    else:
        for i in range(0, len(port_list)):
            print(port_list[i][0])
    com = serial.Serial('/dev/cu.SLAB_USBtoUART', 115200, timeout=1)
    com.write(factory_reset())
    data = com.readline()

    for i in range(0,10):
        com.write(wifi_info_response())
        print("**************************")

        print(data)

    com.write(wifi_infomation())
    print(data)



