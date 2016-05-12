# -*- coding:utf-8 -*-
from Tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.ip = Label(self,text='网址')
        self.ip.pack()
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
app = Application()
# 设置窗口标题:
app.master.title('图片爬虫')
# 主消息循环:
app.mainloop()
