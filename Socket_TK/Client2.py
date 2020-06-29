import tkinter
import threading
from socket import *


class Client():
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title("客户端2")
        self.win.geometry("350x400+1080+30")

    # 接收服务端发送的消息
    def getMsg(self):
        while True:
            data = client.recv(1024)
            data = data.decode("utf-8")
            # 显示上线提醒
            if "上线" in data:
                self.text1.insert(tkinter.INSERT, data)
                continue
            # 显示在线用户
            if " " in data:
                online_client = data.strip().split("!")
                for item in online_client:
                    if item in self.text2.get("0.0", "end"):
                        continue
                    self.text2.insert(tkinter.INSERT, item)
                    self.text2.insert(tkinter.INSERT, " ")
                continue
            # 提示用户不存在
            if "不存在" in data:
                self.text3.insert(tkinter.INSERT, data)
                continue

            self.text3.insert(tkinter.INSERT, data)  # 显示在信息框上
            self.text3.insert(tkinter.INSERT, '\n')

    # 连接服务端（通过按钮启动）
    def connectServer(self):
        global client
        ip = "127.0.0.1"
        port = 8899
        userName = self.user_name.get()
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((ip, port))
        client.send(userName.encode("utf-8"))  # 向服务器发送用户名
        t = threading.Thread(target=self.getMsg)  # 开启线程处理消息
        t.start()

    # 发送消息（通过按钮启动）
    def sendMsg(self):
        Receiver = self.receiver.get()  # 获取接收者对象
        Msg = self.msg.get()  # 获取发送消息内容
        Msg = Receiver + ":" + Msg  # 将接受对象和消息一块儿打包发送
        client.send(Msg.encode("utf-8"))

    # 界面设置
    def initUI(self):
        labelUse = tkinter.Label(self.win, text="用户名", font="黑体").grid(row=0, column=0, pady=5)
        self.user_name = tkinter.Variable()
        entryUser = tkinter.Entry(self.win, textvariable=self.user_name, font="楷体", bd=0).grid(row=0, column=1)

        button = tkinter.Button(self.win, text="启动", bd=0, font="黑体", bg="#39C45D", command=self.connectServer).grid(
            row=3, column=0)

        labeltext1 = tkinter.Label(self.win, text="上线提醒", font="黑体").grid(row=4, column=0)
        self.text1 = tkinter.Text(self.win, height=4, width=30, font="楷体", bd=0)
        self.text1.grid(row=4, column=1, pady=5)

        labeltext2 = tkinter.Label(self.win, text="在线用户", font="黑体").grid(row=5, column=0)
        self.text2 = tkinter.Text(self.win, height=3, width=30, font="楷体", bd=0)
        self.text2.grid(row=5, column=1, pady=5)

        labeltext3 = tkinter.Label(self.win, text="消息记录", font="黑体").grid(row=6, column=0)
        self.text3 = tkinter.Text(self.win, height=5, width=30, font="楷体", bd=0)
        self.text3.grid(row=6, column=1, pady=5)

        self.msg = tkinter.Variable()
        labelesend = tkinter.Label(self.win, text="消息输入框", font="黑体").grid(row=7, column=0)
        entrySend = tkinter.Entry(self.win, textvariable=self.msg, bd=0).grid(row=7, column=1, pady=5)

        self.receiver = tkinter.Variable()
        labelefriend = tkinter.Label(self.win, text="发给谁", font="黑体").grid(row=8, column=0)
        entryFriend = tkinter.Entry(self.win, textvariable=self.receiver, bd=0).grid(row=8, column=1, pady=5)

        button2 = tkinter.Button(self.win, text="发送", font="黑体", bd=0, bg="#39C45D", command=self.sendMsg).grid(row=9,
                                                                                                                column=0)
        self.win.mainloop()


if __name__ == '__main__':
    client = Client()
    client.initUI()

