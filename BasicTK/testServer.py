import tkinter    #图形化编程
import socket     #网络编程
import threading  #多线程

win = tkinter.Tk()  # 创建主窗口
win.title('模拟服务器') #主窗口名称
win.geometry("400x400+200+20")  #主窗口尺寸
users = {}#用户字典，也可以连接数据库

#获取客户端信息，及进行客户端之间的通信
def run(ck, ca):
    userName = ck.recv(1024)#接受客户端发送的信息以1k作为单位这里接受到的信息为byte类型
    users[userName.decode("utf-8")] = ck#解码并储存用户的信息
    #print(users)
    printStr = "" + userName.decode("utf-8") + "连接\n"#在连接显示框中显示是否连接成功
    text.insert(tkinter.INSERT, printStr)

    while True:
        rData = ck.recv(1024)#接受客户端发送的信息以1k作为单位这里接受到的信息为byte类型
        dataStr = rData.decode("utf-8")
        infolist = dataStr.split(":")#分割字符串从而得到所要发送的用户名和客户端所发送的信息
        print(infolist)
        users[infolist[0]].send((userName.decode("utf-8") + ":" + infolist[1]).encode("utf"))
        #要发送信息的客户端向目标客户端发送信息（服务器转发的过程）

#建立socket套接字，并开启通信服务
def start1():
    ipStr = eip.get()#从输入端中获取ip
    portStr = eport.get()#从输入端中获取端口，注意端口取得时候不能被占用（可以取8080，9876，等）
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socked所准守ipv4或ipv6，和相关协议的
    server.bind((ipStr, int(portStr)))#绑定ip和端口号！！！1:注意输入的端口号是str型而这里的要传入int型
    #2:bind()的参数是一个元组的形式
    server.listen(10)#设置监听，和设置连接的最大的数量
    printStr = "服务器启动成功\n"#，是否连接成功
    text.insert(tkinter.INSERT, printStr)#显示在信息窗口中
    while True:#这里用死循环是因为模拟的服务器要一直运行
        ck, ca = server.accept()#接受所连接的客户端的信息 >>> accept()->(scoket object,address info),故要安排一个对象来接收address info
        # 其中ca是ip和端口号组成的元组，ck有关客户端的信息
        t = threading.Thread(target=run, args=(ck, ca))#每连接一个客户端就开启一个线程
        #其中Thread函数中的传入函数的参数也是以元组的形式（args是target函数所调用的参数）
        t.start()#开启线程

#开启服务器也是需要一个进程的（下面这个不可少）
def startServer():
    s = threading.Thread(target=start1)#启用一个线程开启服务器
    s.start()#开启线程

#下面是关于界面的操作
labelIp = tkinter.Label(win, text='ip').grid(row=0, column=0)
labelPort = tkinter.Label(win, text='port').grid(row=1, column=0)
eip = tkinter.Variable()
eport = tkinter.Variable()
entryIp = tkinter.Entry(win, textvariable=eip).grid(row=0, column=1)
entryPort = tkinter.Entry(win, textvariable=eport).grid(row=1, column=1)
button = tkinter.Button(win, text="启动", command=startServer).grid(row=2, column=0)
text = tkinter.Text(win, height=5, width=30)
labeltext = tkinter.Label(win, text='连接消息').grid(row=3, column=0)
text.grid(row=3, column=1)
win.mainloop()
