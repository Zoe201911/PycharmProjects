import serial
import re
import time
import threading
from multiprocessing import Process
from threading import Thread
import os

class Converter():
    @staticmethod
    def to_ascii(h):
        list_s = []
        for i in range(0,len(h),2):
            list_s.append(chr(int(h[i:i+2].upper(),16)))
        return ''.join(list_s)
    @staticmethod
    def to_hex(s):
        list_h = []
        for c in s:
            list_h.append(str(hex(ord(c)))[-2:]) #取hex转换16进制的后两位
        return ''.join(list_h)

class SerialPort:
    message = ''
    def __init__(self, port, buand):
        super(SerialPort, self).__init__()
        self.port = serial.Serial(port, buand)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self):
        data = input("请输入要发送的数据（非中文）并同时接收数据: ")
        n = self.port.write((data + '\n').encode())
        return n

    def read_data(self):
        while True:

            for k in range(100000):
                print('-----k', k)
                self.message = self.port.readline()
                #self.message = self.port.reset_input_buffer()
                print(self.message)
                hexmessage = self.message.hex()
                print(hexmessage)
                # print('\n')
                # print(Converter.to_ascii(hexmessage))
                # str = bytearray.fromhex(hexmessage)
                # print(str)
                #print("....................................................................................................................................")


# def zhubanpost():
#     serialPort = "COM10"  # 串口
#     baudRate =115200  # 波特率
#     print("post to IOT.....................")
#     mSerial = SerialPort(serialPort, baudRate)
#     t1 = threading.Thread(target=mSerial.read_data)
#     t1.start()
#     while True:
#         time.sleep(1)
#         mSerial.send_data()
#
# def zhubanget():
#     serialPort = "COM7"  # 串口
#     baudRate = 115200  # 波特率
#     print("get from IOT.......................")
#     mSerial = SerialPort(serialPort, baudRate)
#     t1 = threading.Thread(target=mSerial.read_data)
#     t1.start()
#     while True:
#         time.sleep(1)
#         mSerial.send_data()

    def mainboardpost():
        serialPort = "/dev/tty.SLAB_USBtoUART"  # 串口
        baudRate =115200  # 波特率
        print("post to IOT.....................")
        mSerial = SerialPort(serialPort, baudRate)
        mSerial.read_data()
    def mainboardget():
        serialPort = "COM8"  # 串口
        baudRate = 9600  # 波特率
        print("app post to IOT , mainboard get from IOT.......................")
        mSerial = SerialPort(serialPort, baudRate)
        mSerial.read_data()

if __name__=='__main__':
    threads = []
    t1=threading.Thread(target=SerialPort.mainboardpost())#创建线程1
    threads.append(t1)
    t2=threading.Thread(target=SerialPort.mainboardget())#创建线程2
    threads.append(t2)
    #t2 = Process(target=SerialPort.zhubanget())  # 创建进程
    #t2.start()
    for t in threads:
        t.setDaemon(True)
        t.start()