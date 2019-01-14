# import tkinter as tk
import sys,threading,time
from tkinter import *
from SerialTest1 import ComThread


 # 使用tkinter编写登录窗口
 # Grid(网格)布局管理器会将控件放置到一个二维的表格里，主控件被分割为一系列的行和列
 # stricky设置对齐方式，参数N/S/W/E分别表示上、下、左、右
 # columnspan：指定控件跨越多列显示
 # rowspan：指定控件跨越多行显示
 # padx、pady分别设置横向和纵向间隔大小

# 显示框
root = Tk()
root.title('tkinter')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry("{}x{}".format(int(w), int(h)))
v=StringVar()

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
e4 = Entry(root,textvariable=v4, width=30)

# e1.grid(row=0)
# e2.grid(row=1)
# e3.grid(row=2)
# e4.grid(row=3)



#pady竖直方向外边距
#padx水平方向外边距

# e1.pack(padx=20, pady=33,side=TOP)
# e2.pack(padx=20, pady=5, side=TOP)
# e3.pack(padx=20, pady=5, side=TOP)
# e4.pack(padx=20, pady=5, side=TOP)




e1.place(x=100,y=30)
e2.place(x=100,y=70)
e3.place(x=100,y=110)
e4.place(x=100,y=150)


e1.config(state=DISABLED)
e2.config(state=DISABLED)
e3.config(state=DISABLED)
e4.config(state=DISABLED)

def comRead():
    while 1:
        # 接收间隔
        time.sleep(1)
        try:
            # 获取接收到的数据长度
            v1.set(ck.getValueOfID())
            v2.set(ck.getValueOfMode())
            v3.set(ck.getValueOfStatus())
            v4.set(ck.getValueOfMeas())

        except Exception as ex:
            print(str(ex))

ck = ComThread(Port=int(1))

def sel():
    # selection = "You selection the option" + str(v.get())
    # label.config(text = selection)
    label.config(text=v.get())

# 单选框
v = IntVar()
#要实现单选互斥的效果，
#variable选项共享一个整型变量，
#value需要设置不同的值
r1 = Radiobutton(root,text = 'ACW',variable = v,value = 1, command=sel)
r2 = Radiobutton(root,text = 'DCW',variable = v,value = 2, command=sel)
r3 = Radiobutton(root,text = 'IR',variable = v,value = 3, command=sel)
r4 = Radiobutton(root,text = 'GB',variable = v,value = 4, command=sel)

# r1.pack(fill=X,padx=10)
# r2.pack(fill=X,padx=10)
# r3.pack(fill=X,padx=10)
# r4.pack(fill=X,padx=10)

# r1.pack(padx=20, pady=40, side=LEFT)
# r2.pack(padx=20, pady=40, side=LEFT)
# r3.pack(padx=20, pady=40, side=LEFT)
# r4.pack(padx=20, pady=40, side=LEFT)


r1.place(x=40, y=200)
r2.place(x=100, y=200)
r3.place(x=160, y=200)
r4.place(x=220, y=200)




# 按钮
def StartButton():
    ck.start()
    thread_read = None
    thread_read = threading.Thread(target=comRead)
    thread_read.setDaemon(1)
    thread_read.start()
    print("start!")
    # 设定状态,当点击开始的时候,把获取到的后端的值设置给指定的label


def StopButton():
    print("stop!")
    root.quit()

b1 = Button(root, text="start", command=StartButton)
# 点击按钮的时候使用quit退出.
b2 = Button(root, text="stop", command=StopButton)
b1.place(x=60, y=240)
b2.place(x=180, y=240)


label = Label(root)
label.pack()
print(ck.getValueOfID())
root.mainloop()
