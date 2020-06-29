
import socket
import threading
from PyQt5.QtWidgets import *
import sys
from Socket_QT.serverwin import Ui_server_win



class ServerWin(QWidget):
    def __init__(self):
        super(ServerWin, self).__init__()
        self.ui = Ui_server_win()
        self.ui.setupUi(self)
        self.users = {}  # 用户字典

    #获取客户端信息，及进行客户端之间的通信
    def run(self,ck, ca):
        userName = ck.recv(1024)#接受客户端发送的信息以1k作为单位这里接受到的信息为byte类型
        self.users[userName.decode("utf-8")] = ck#解码并储存用户的信息
        #print(users)
        printStr = "" + userName.decode("utf-8") + "连接\n"#在连接显示框中显示是否连接成功
        self.ui.status.setText(printStr)

        while True:
            rData = ck.recv(1024)#接受客户端发送的信息以1k作为单位这里接受到的信息为byte类型
            dataStr = rData.decode("utf-8")
            infolist = dataStr.split(":")#分割字符串从而得到所要发送的用户名和客户端所发送的信息
            print(infolist)
            self.users[infolist[0]].send((userName.decode("utf-8") + ":" + infolist[1]).encode("utf"))
            #要发送信息的客户端向目标客户端发送信息（服务器转发的过程）

    #建立socket套接字，并开启通信服务
    def start1(self):
        ipStr = self.ui.ip_edit.text()#从输入端中获取ip
        portStr = self.ui.port_edit.text()#从输入端中获取端口，
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socked所准守ipv4或ipv6，和相关协议的
        server.bind((ipStr, int(portStr)))#绑定ip和端口号！！！1:注意输入的端口号是str型而这里的要传入int型
        #2:bind()的参数是一个元组的形式
        server.listen(10)#设置监听
        printStr = "服务器启动成功\n"#是否连接成功
        self.ui.status.setText(printStr)#显示在信息窗口中
        while True:#这里用死循环是因为模拟的服务器要一直运行
            ck, ca = server.accept()#接受所连接的客户端的信息 >>> accept()->(scoket object,address info),故要安排一个对象来接收address info
            # 其中ca是ip和端口号组成的元组，ck有关客户端的信息
            t = threading.Thread(target=self.run, args=(ck, ca))#每连接一个客户端就开启一个线程
            #其中Thread函数中的传入函数的参数也是以元组的形式（args是target函数所调用的参数）
            t.start()#开启线程

    #开启服务器也是需要一个进程的（下面这个不可少）
    def startServer(self):
        s = threading.Thread(target=self.start1)#启用一个线程开启服务器
        s.start()#开启线程


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ServerWin()
    win.show()
    sys.exit(app.exec())

