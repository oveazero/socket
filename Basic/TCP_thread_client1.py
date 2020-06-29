#-*- coding = utf-8 -*-
#@Time: 2020/6/15 0015 17:33
#@Author: orea
#@File:TCP_thread_client1.py
#@Software: PyCharm

from socket import *
from threading import Thread

client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(('127.0.0.1',8888))
flag = True

def readMsg(client_socket):
    while flag:
        recv_data = client_socket.recv(1024)
        print(f"{recv_data.decode('utf-8')}")
        pass
def sendMsg(client_socket):
    global flag
    while flag:
        msg = input('>')
        msg = user_name + ':' + msg
        client_socket.send(msg.encode("utf-8"))
        if msg.endswith('bye'):
            flag = False
            break
        pass

user_name = input("请输入用户名：")
t1 = Thread(target=sendMsg,args=(client_socket,))
t1.start()
t2 = Thread(target=readMsg, args=(client_socket,))
t2.start()
t1.join()
t2.join()
client_socket.close()