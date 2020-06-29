#-*- codeing = utf-8 -*-
#@Time: 2020/6/15 0015 15:54
#@Author: orea
#@File:TCP_thread_server.py
#@Software: PyCharm

import sys
from socket import *
from threading import Thread
from TCPserver import Ui_server
from PyQt5.QtWidgets import QApplication, QMainWindow



class ServerWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_server()
        self.ui.setupUi(self)
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(('127.0.0.1', 8888))
        self.server_socket.listen(5)
        self.sockets = []
        # self.run()

    def run(self):
            # 处理客户端的请求
        while True:
            client_socket, client_info = self.server_socket.accept()
            self.sockets.append(client_socket)
            self.ui.online_user.setText(self.sockets)
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

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = ServerWin()
    win.show()
    sys.exit(app.exec_())


