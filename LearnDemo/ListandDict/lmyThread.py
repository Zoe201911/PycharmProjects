"""
_thread提供了低级别的，原始的线程以及一个简单锁，她相当于threading模块的功能还是比较有限的
threading模块除了包含_thread模块中的所有方法外，还提供了其他方法
threading.currentThread()返回当前的线程变量
threading.enumerate()返回一个包含正在运行线程的list，正在运行指线程启动后，结束前，不包括启动前和终止后的线程
thread.activeCount()返回正在运行的线程数量，与len(threading.enumerate())有相同的结果
run()用于表示线程活动的方法
start()启动线程活动
join(time)等待至线程中止，这阻塞调用线程直到线程的join方法被调用中止，正常退出或者抛出未处理的异常，或者是可选择的超时发生
isAlive()返回线程是否活动的
getName()返回线程名
setName()设置线程名
"""

import threading
import time

exitFlag = 0
class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("线程开始："+ self.name)
        print_time(self.name,self.counter,5)
        print("退出线程："+self.name)

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s:%s" % (threadName,time.ctime(time.time()),counter))
        counter -= 1

#创建新线程
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

#开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")