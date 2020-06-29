#-*- coding = utf-8 -*-
#@Time: 2020/6/15 0015 16:09
#@Author: orea
#@File:TCP_thread_client.py
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

user_name = input('请输入用户名：')
#开启一个线程处理客户端发送消息
t1 = Thread(target=sendMsg,args=(client_socket,))
t1.start()
#开启一个线程处理客户端读取消息
t2 = Thread(target=readMsg, args=(client_socket,))
t2.start()
t1.join()  #等待，直到进程终止(target跳出死循环)，才会执行下一句，否则，会被锁住，下面的代码将不会被执行
t2.join()  #没有参数，则会一直等待下去，否则，过了等待时间，便会执行下面的代码
client_socket.close()