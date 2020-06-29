import tkinter    # 图形化界面
import threading  #多线程
from socket import *


class Server():
    def __init__(self):
        self.win = tkinter.Tk()  # 创建主窗口
        self.win.title('服务器')  # 主窗口名称
        self.win.geometry("380x300+0+30")  # 主窗口尺寸及显示位置
        self.users = {}  # 存放用户信息
        self.client_sockets = []  # 存放用户socket对象
        self.online_list = []    # 在线用户列表
        self.noExistTip = ""     # 当用户不存在时的提示信息

    #进行客户端之间的通信
    def run(self,client_socket):
        userName = client_socket.recv(1024) # 接受客户端发送的用户名
        self.users[userName.decode("utf-8")] = client_socket # 解码并储存用户的信息
        onlineTip = "用户 " + userName.decode("utf-8") + " 已上线\n" # 在连接显示框中显示是否连接成功

        #获取用户列表
        for item in self.users.keys():
            self.online_list.append(item)
            if item in self.text2.get("0.0","end"):
                continue
            self.text2.insert(tkinter.INSERT,item)
            self.text2.insert(tkinter.INSERT, " ")
        online_client = " "+"!".join(self.online_list)

        #发送给所有用户
        for socket in self.client_sockets:
            socket.send(onlineTip.encode("utf-8"))    # 每个客户端都显示上线提示
            socket.send(online_client.encode("utf-8"))  # 每个客户端都显示在线用户
            socket.send(self.noExistTip.encode("utf-8"))

        self.text1.insert(tkinter.INSERT, onlineTip)  # 显示上线提示

        while True: # 不断接受客户端发送的消息
            data = client_socket.recv(1024)
            data = data.decode("utf-8")
            infolist = data.split(":") # 分割字符串从而得到所要发送的用户名和客户端所发送的信息
            if  infolist[0] not in self.users:
                self.noExistTip = f'{infolist[0]}用户不存在\n'
                self.text3.insert(tkinter.INSERT, self.noExistTip)
                client_socket.send(self.noExistTip.encode("utf-8"))
                continue
            self.users[infolist[0]].send((userName.decode("utf-8") + ":" + infolist[1]).encode("utf-8")) #服务器将消息转发给相应的客户端
            msg = (userName.decode("utf-8") + " 对 " +infolist[0] + " 说 " + infolist[1]).encode("utf-8")
            self.text3.insert(tkinter.INSERT,msg.decode("utf-8"))
            self.text3.insert(tkinter.INSERT,"\n")

    #开启服务端socket
    def start(self):
        ip = "127.0.0.1"
        port = 8899
        server = socket(AF_INET,SOCK_STREAM)
        server.bind((ip, port)) # bind()的参数是一个元组的形式
        server.listen(5) # 同一时间最大排队数
        startTip = "服务器启动成功\n" # 提示是否连接成功
        self.text1.insert(tkinter.INSERT, startTip) # 显示在信息窗口中
        while True: # 这里用死循环是因为模拟的服务器要一直运行
            client_socket, client_info = server.accept()# 接受所连接的客户端的信息 >>> accept()->(socket_object,address_info),前者是ip和端口号组成的元组，后者时有关客户端的信息
            self.client_sockets.append(client_socket)
            t = threading.Thread(target=self.run, args=(client_socket,))# 每连接一个客户端就开启一个线程
            # 其中Thread函数中的传入函数的参数也是以元组的形式（args是target函数所调用的参数）
            t.start()#开启线程

    #通过按钮启动服务器
    def startServer(self):
        s = threading.Thread(target=self.start) # 启用一个线程开启服务器
        s.start() # 开启线程

    #界面设置
    def initUI(self):
        button = tkinter.Button(self.win,relief="raised",bd=0, height=1, width=7,text="启动",font="黑体" ,command=self.startServer,bg="#39C45D").grid(row=1,column=0)

        labeltext1 = tkinter.Label(self.win, text='连接状态', font="黑体").grid(row=5, column=0,padx=22)
        self.text1 = tkinter.Text(self.win, height=4, width=30,font="楷体",bd=0)
        self.text1.grid(row=5, column=1,pady=5)

        labeltext2 = tkinter.Label(self.win, text='在线用户', font="黑体").grid(row=6, column=0, padx=22)
        self.text2 = tkinter.Text(self.win, height=3, width=30, font="楷体", bd=0)
        self.text2.grid(row=6, column=1, pady=5)

        labeltext3 = tkinter.Label(self.win,text= "用户通信", font="黑体").grid(row=7,column=0,padx=5)
        self.text3 = tkinter.Text(self.win, height=5, width=30,font="楷体",bd=0)
        self.text3.grid(row=7,column=1,pady=5)

        self.win.mainloop()

if __name__ == '__main__':
    server = Server()
    server.initUI()