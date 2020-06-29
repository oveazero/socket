#-*- codeing = utf-8 -*-
#@Time: 2020/5/12 0012 11:07
#@Author: orea
#@File:testGeometry.py
#@Software: PyCharm
import tkinter
# from tkinter import Tk,mainloop,TOP
from tkinter.ttk import Button
root = tkinter.Tk()   #创建界面对象
root.title('orea')  #设置界面名称，默认是tk
# root.geometry('300x400')  #长X宽，注意乘号是英文小写的'x',而不是'*'
root.geometry('300x400+400+100') #‘长乘宽+横轴+纵轴’  后面两个指标用于确定界面出现的初始位置（默认是左上角）
# button = Button(root,text = 'China') #设置按钮
# button.pack(side = TOP,pady = 10) #按钮的位置
root.mainloop()   #启动界面
