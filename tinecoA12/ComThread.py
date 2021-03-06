"""
创建串口助手手续要创建一个类，重构类的实现过程如下
"""
import threading
import time
import serial

class ComThread:
    def __init__(self,Port = '/dev/tty.SLAB_USBtoUART'):
    #构造串口的属性
        self.l_serial = None
        self.alive = False
        self.waitEnd = None
        self.port = Port
        self.ID = None
        self.data = None
    #定义串口等待的函数
    def waiting(self):
        if not self.waitEnd is None:
            self.waitEnd.wait()

    def setStopEvent(self):
        if not self.waitEnd is None:
            self.waitEnd.set()
        self.alive = False
        self.stop()

    #启动串口的函数
    def start(self):
        self.l_serial = serial.Serial()
        self.l_serial.port = self.port
        self.l_serial.baudrate = 115200
        #设置等待时间，超出时间停止等待
        self.l_serial.timeout = 2
        self.l_serial.open()
        #判断串口是否已经打开
        if self.l_serial.is_open():
            self.waitEnd = threading.Event()
            self.alive = True
            self.thread_read = None
            self.thread_read = threading.Thread(target=self.FirstReader)
            self.thread_read.setDaemon(1)
            self.thread_read.start()
            return True
        else:
            return False

    def SendDate(self,i_msg,send):
        lmsg = ''
        isOK = False
        if isinstance(i_msg):
            lmsg = i_msg.encode("gb18030")
        else:
            lmsg = i_msg
        try:
            #发送数据到响应的处理组件
            self.l_serial.write(send)
        except Exception as ex:
            pass
        return  isOK
    def FirstReader(self):
        while self.alive:
            time.sleep(0.1)
            data = ''
            data = data.encode('utf-8')
            n = self.l_serial.inWaiting()
            if n:
                data = data + self.l_serial.read(n)
                print('get data from serial port:',data)
                print(type(data))
            n = self.l_serial.inWaiting()
            if len(data)>0 and n==0:
                try:
                    temp = data.decode('gb18030')
                    print(type(temp))
                    print(temp)
                    car,temp = str(temp).split("\n",1)
                    print(car,temp)
                    String = str(temp).strip().split(":")[1]
                    str_ID, str_data = str(String).split("*", 1)
                    print(str_ID)
                    print(str_data)
                    print(type(str_ID),type(str_data))
                    if str_data[-1] == '*':
                        break
                    else:
                        print(str_data[-1])
                        print('str_data[-1]!=*')
                except:
                    print("读卡错误，请重试")
        self.ID = str_ID
        self.data = str_data[0:-1]
        self.waitEnd.set()
        self.alive = False


    def stop(self):
        self.alive = False
        self.thread_read.join()
        if self.l_serial.is_open():
            self.l_serial.close()







def main():
    rt = ComThread()
    rt.sendport = '**1*80*'
    try:
        if rt.start():
            print(rt.l_serial.name)
            rt.waiting()
            print("The data is:%s,The Id is:%s"%(rt.data,rt.ID))
            rt.stop()
        else:
            pass
    except Exception as ex:
        print(str(ex))
    if rt.alive:
        rt.stop()
    print('')
    print('End OK .')
    temp_ID = rt.ID
    temp_data = rt.data
    del rt
    return temp_ID,temp_data






if __name__ == '__main__':
    ID,data = main()
    print("********************")
    print(ID,data)
