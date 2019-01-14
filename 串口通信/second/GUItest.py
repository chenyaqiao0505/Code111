from tkinter import *
from UDPdevice import udpdevice
import tkinter.messagebox

root = Tk()
root.title('test2')
root.geometry('500x400')



def next(event):
    name = [n0,n1,n2,n3,n4,n5,n6,n7]
    for i in range(len(name)):
        if name[i].get() != '':
            name[i+1].focus_set()
            break


def touch(event):
    str = n9.get()
    name = [q0,q1,q2,q3,q4,q5,q6,q7]
    for i in range(len(name)):

        if name[i].get() == '':
            name[i].set(str)
            n9.delete(0,END)
            break
        if name[7].get()!='':
            tkinter.messagebox.showwarning('出错了', '扫码结束，请保存~！')
            break


def CheckValue():      #n就是DI+DO的值
    aa = udpdevice()
    qq = aa.init.buttonclick()
    list = []
    name = [n0,n1,n2,n3,n4,n5,n6,n7]
    if qq !=len(list):
        tkinter.messagebox.showwarning('出错了','扫码数量和板卡数量不一致，请重新扫码~！')
        for i in range(len(name)):
            name[i].delete(0,END)
            



Label(root,text='Hello,GUI').grid(row = 0,column = 0) #生成标签


q0 = StringVar()
q1 = StringVar()
q2 = StringVar()
q3 = StringVar()
q4 = StringVar()
q5 = StringVar()
q6 = StringVar()
q7 = StringVar()


n0 = Entry(root,textvariabl=q0)
n1 = Entry(root,textvariabl=q1)
n2 = Entry(root,textvariabl=q2)
n3 = Entry(root,textvariabl=q3)
n4 = Entry(root,textvariabl=q4)
n5 = Entry(root,textvariabl=q5)
n6 = Entry(root,textvariabl=q6)
n7 = Entry(root,textvariabl=q7)


n9 = Entry(root)

n0.grid(row = 1,column = 0)
n1.grid(row = 2,column = 0)
n2.grid(row = 3,column = 0)
n3.grid(row = 4,column = 0)
n4.grid(row = 5,column = 0)
n5.grid(row = 6,column = 0)
n6.grid(row = 7,column = 0)
n7.grid(row = 8,column = 0)

n9.grid(row = 1,column = 2)


b0 = Button(root,text = '开始',command =CheckValue)
b0.grid(row = 9,column = 1)




n0.bind('<Key-Return>',next)
n1.bind('<Key-Return>',next)
n2.bind('<Key-Return>',next)
n3.bind('<Key-Return>',next)
n4.bind('<Key-Return>',next)
n5.bind('<Key-Return>',next)
n6.bind('<Key-Return>',next)


n9.bind('<Key-Return>',touch)

n0.focus_set()

root.mainloop()      #进入消息循环（必需组件）
