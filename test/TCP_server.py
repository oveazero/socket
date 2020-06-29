#-*- codeing = utf-8 -*-
#@Time: 2020/6/15 0015 14:40
#@Author: orea
#@File:TCP_server.py
#@Software: PyCharm

from socket import *

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('',8888))
server_socket.listen(5)
client_socket,client_info = server_socket.accept()
while True:
    recv_data = client_socket.recv(1024)
    print(f'客户端说：{recv_data.decode("utf-8")}')
    msg = input('>>>')
    client_socket.send(msg.encode("utf-8"))
    if msg == "bye":
        break
    pass
client_socket.close()
server_socket.close()