#-*- codeing = utf-8 -*-
#@Time: 2020/6/15 0015 14:50
#@Author: orea
#@File:TCP_client.py
#@Software: PyCharm

from socket import *

client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(('127.0.0.1',8888))
while True:
    msg = input(">>>")
    client_socket.send(msg.encode("utf-8"))
    if msg == 'bye':
        break
    recv_data = client_socket.recv(1024)
    print(f'服务器说：{recv_data.decode("utf-8")}')
    pass
client_socket.close()
