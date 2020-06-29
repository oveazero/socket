
from socket import *
from threading import Thread
import tkinter

win = tkinter.Tk()
win.title("客户端1")
win.geometry("400x400+200+20")


class Clinet():
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 8899
        self.client_socket = socket(AF_INET,SOCK_STREAM)

    def receive_msg(self):
        while True:
            data = self.client_socket.recv(1024)
            data = data.decode("utf-8")


    def connect_server(self):
        self.client_socket.connect((self.ip, self.port))
        t = Thread(target=self.receive_msg)
        t.start()


    def send_msg(self):
        msg = send.get()
        self.client_socket.send(msg)

if __name__ == '__main__':
    test = Clinet()
    test.connect_server()