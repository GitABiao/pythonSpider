# -*- coding:utf-8 -*-
from Tkinter import *
root = Tk()
root.title("BiaoSpider")
root.geometry('400x200')

Frm = Frame(root)
Frm_L = Frame(Frm)
Label(Frm_L,text="网址",bg="#000",font=("Arial",12),width=4,height=2).pack(side=TOP)
Label(Frm_L,text="类型",bg="#000",font=("Arial",12),width=4,height=2).pack(side=TOP)
Frm_L.pack(side=TOP)

Frm_R = Frame(Frm)
Entry(root, textvariable = StringVar()).pack(side=TOP)
StringVar().set("网址")
Entry(root, textvariable = StringVar()).pack(side=TOP)
StringVar().set("网址")
Entry(root, textvariable = StringVar()).pack(side=TOP)
StringVar().set("网址")
Frm_R.pack(side=RIGHT)

Button(root, text="press").pack()
root.mainloop()