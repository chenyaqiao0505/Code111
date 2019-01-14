# import tkinter as tk
from tkinter import *
# import scratch


# aa = scratch.mytest()


# 显示框
root = Tk()
root.title('tkinter')
root.geometry('300x400')
Label(root,text='设备类型：').place(x=25,y=30)
Label(root,text='工作模式：').place(x=25,y=70)
Label(root,text='状    态：').place(x=25,y=110)
Label(root,text='测量结果：').place(x=25,y=150)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()


e1 = Entry(root,textvariable=v1)
e2 = Entry(root,textvariable=v2)
e3 = Entry(root,textvariable=v3)
e4 = Entry(root,textvariable=v4)
e1.place(x=100,y=30)
e2.place(x=100,y=70)
e3.place(x=100,y=110)
e4.place(x=100,y=150)
e1.config(state=DISABLED)
e2.config(state=DISABLED)
e3.config(state=DISABLED)
e4.config(state=DISABLED)

# 单选框
v = IntVar()
v.set(1)     #要实现单选互斥的效果，
             #variable选项共享一个整型变量，
             #value需要设置不同的值
Radiobutton(root,text = 'ACM',variable = v,value = 1).pack(side = LEFT)
Radiobutton(root,text = 'DCW',variable = v,value = 2).pack(side = LEFT)
Radiobutton(root,text = 'IR',variable = v,value = 3).pack(side = LEFT)
Radiobutton(root,text = 'GB',variable = v,value = 4).pack(side = LEFT)

# 按钮
def StartButton():
    print("start!")

def StopButton():
    print("stop!")

Button(root, text="start", command=StartButton).pack(side=LEFT)
Button(root, text="stop", command=StopButton).pack(side=LEFT)



# def show():
#     print('账号：%s' % v1.get())
#     print('密码：%s' % v2.get())
#     e1.delete(0,END)    #获取完信息，清楚掉输入框的
#     e2.delete(0,END)    #0,END，表示从第0个到最后一个
# Button(root,text='获取信息',width=10,command=show).place(x=20,y=120)
# Button(root,text='退出',width=10,command=root.quit).place(x=180,y=120)


root.mainloop()
