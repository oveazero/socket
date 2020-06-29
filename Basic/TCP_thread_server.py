#-*- coding = utf-8 -*-
#@Time: 2020/6/15 0015 15:54
#@Author: orea
#@File:TCP_thread_server.py
#@Software: PyCharm

from socket import *
from threading import Thread


class Server():
    def __init__(self):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(('', 8888))
        self.server_socket.listen(5)
        self.sockets = []

    def run(self):
            # 处理客户端的请求
        while True:
            client_socket, client_info = self.server_socket.accept()
            self.sockets.append(client_socket)
            # 开启线程处理信息
            t = Thread(target=self.sendMsg, args=(client_socket,))
            t.start()



    def sendMsg(self,client_socket):
        while True:
            recv_data = client_socket.recv(1024)
            if recv_data.decode("utf-8").endswith('bye'):
                self.sockets.remove(client_socket)
                client_socket.close()
            #将接收到的消息发送给所有在线用户
            for socket in self.sockets:
                socket.send(recv_data)
            pass

if __name__ == '__main__':
    test = Server()
    test.run()
