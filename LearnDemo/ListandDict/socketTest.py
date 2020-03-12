"""
socket成为套接字，，应用程序通常通过套接字向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯
使用socket()函数来创建套接字socket.socket([family[,type[,proto]]])
使用socket模块的socket函数来创建一个socket对象，socket对象可以通过调用其他函数来设置一个socket服务
现在我们可以通过调用bind(hostname,port)函数来指定服务的port
截止，我们调用socket对象的accpt方法，该方法等待客户端的连接，并返回connection对象，表示已连接到客户端

"""

import socket
import sys


#创建socket对象
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名
host = socket.gethostname()

port = 8888

#绑定端口
serverSocket.bind((host,port))

#设置最大连接数，超过后排队
serverSocket.listen(5)


while True:
    #建立客户端连接
    clientSocket,addr = serverSocket.accept()
    print("链接地址：%s" % str(addr))

    msg = '欢迎访问W3school教程'+"\r\n"
    clientSocket.send(msg.encode('utf-8'))
    clientSocket.close()