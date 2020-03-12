"""
接下来我们写一个简单的客户端实例连接到以上创建的服务，端口号为12345
socket.connet(hostname,port)方法打开一个TCP连接到主机为hostname端口号为port的服务商，连接后我么就可以从服务的后期数据
操作完成后需要关闭连接
"""

import socket
import sys


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()

port = 8888

s.connect((host,port))

msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))