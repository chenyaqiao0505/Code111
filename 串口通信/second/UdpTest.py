import time
from tkinter import *
import tkinter.messagebox
import datetime
from UDPdevice import udpdevice
import tkinter.messagebox


aa = udpdevice()
time_stamp = datetime.datetime.now()
book_name = 'Result'+time_stamp.strftime('%Y-%m-%d') +'.xls'
sheet_name = 'sheet1'
value_title = [['条形码','是否通过','时间']]

def StartButton():
    ww = aa.control1()
    list = [ConfM1,ConfM2,ConfM3,ConfM4,
            ConfM5,ConfM6,ConfM7,ConfM8,
            ConfM9,ConfM10,ConfM11,ConfM12,
            ConfM13,ConfM14,ConfM15,ConfM16]
    for i in range(len(list)):
        list[i].set(ww[i])




def ScanButton(event):
    # m = e12.get()
    m = ConfIn2.get()
    P_list = [ConfP1, ConfP2, ConfP3, ConfP4, ConfP5, ConfP6, ConfP7, ConfP8,
    ConfP9, ConfP10, ConfP11, ConfP12, ConfP13, ConfP14, ConfP15, ConfP16]
    for i in range(len(P_list)):
        if P_list[i].get() == '':
            P_list[i].set(m)
            time.sleep(0.5)
            e12.delete(0, END)
            break
def touch(event):
    qq = aa.init.CheckNum()
    list = []
    name = [ConfP1, ConfP2, ConfP3, ConfP4,
            ConfP5, ConfP6, ConfP7, ConfP8,
            ConfP9, ConfP10, ConfP11, ConfP12,
            ConfP13, ConfP14, ConfP15, ConfP16]
    if qq != len(list):
        tkinter.messagebox.showwarning('出错了', '扫码数量和板卡数量不一致，请重新扫码~！')
        for i in range(len(name)):
            name[i].delete(0, END)






# 显示框
root = Tk()
root.title('绝缘耐压测试')
root.geometry('1200x900')

Label(root, text='IOM模块功能综合测试系统', fg='blue', font=('KaiTi', 35, 'bold'), anchor='n').pack()
Label(root, text='参数设置', fg="#1E90FF", font=('KaiTi', 20, 'bold')).place(x=30, y=60)
Label(root, text='测试类型: ', font=('KaiTi', 15, 'bold')).place(x=60, y=110)
Label(root, fg='green', text='DI', font=('KaiTi', 15, 'bold')).place(x=170, y=110)
Label(root, text='循环测试次数: ', font=('KaiTi', 15, 'bold')).place(x=60, y=160)
Label(root, text='扫码框: ', font=('KaiTi', 15, 'bold')).place(x=60, y=210)
Label(root, text='测试信息', fg="#1E90FF", font=('KaiTi', 20, 'bold')).place(x=30, y=260)
Label(root, text='扫码显示', fg="#1E90FF", font=('KaiTi', 20, 'bold')).place(x=630, y=60)
Label(root, text='结果显示', fg="#1E90FF", font=('KaiTi', 20, 'bold')).place(x=950, y=60)


text = Text(root, bg='#E5E5E5' ,width=60, height=40)
text.place(x=60, y=310)
text.config(state=DISABLED) 


ConfIn1 = StringVar()
ConfIn2 = StringVar()

ConfP1 = StringVar()
ConfP2 = StringVar()
ConfP3 = StringVar()
ConfP4 = StringVar()
ConfP5 = StringVar()
ConfP6 = StringVar()
ConfP7 = StringVar()
ConfP8 = StringVar()
ConfP9 = StringVar()
ConfP10 = StringVar()
ConfP11 = StringVar()
ConfP12 = StringVar()
ConfP13 = StringVar()
ConfP14 = StringVar()
ConfP15 = StringVar()
ConfP16 = StringVar()

ConfM1 = StringVar()
ConfM2 = StringVar()
ConfM3 = StringVar()
ConfM4 = StringVar()
ConfM5 = StringVar()
ConfM6 = StringVar()
ConfM7 = StringVar()
ConfM8 = StringVar()
ConfM9 = StringVar()
ConfM10 = StringVar()
ConfM11 = StringVar()
ConfM12 = StringVar()
ConfM13 = StringVar()
ConfM14 = StringVar()
ConfM15 = StringVar()
ConfM16 = StringVar()

e11 = Entry(root, textvariable=ConfIn1, width=20)
e12 = Entry(root, textvariable=ConfIn2, width=29)

e12.focus_set()
e12.bind('<Key-Return>', ScanButton)

P21 = Entry(root, textvariable=ConfP1, width=30)
P22 = Entry(root, textvariable=ConfP2, width=30)
P23 = Entry(root, textvariable=ConfP3, width=30)
P24 = Entry(root, textvariable=ConfP4, width=30)
P25 = Entry(root, textvariable=ConfP5, width=30)
P26 = Entry(root, textvariable=ConfP6, width=30)
P27 = Entry(root, textvariable=ConfP7, width=30)
P28 = Entry(root, textvariable=ConfP8, width=30)
P29 = Entry(root, textvariable=ConfP9, width=30)
P30 = Entry(root, textvariable=ConfP10, width=30)
P31 = Entry(root, textvariable=ConfP11, width=30)
P32 = Entry(root, textvariable=ConfP12, width=30)
P33 = Entry(root, textvariable=ConfP13, width=30)
P34 = Entry(root, textvariable=ConfP14, width=30)
P35 = Entry(root, textvariable=ConfP15, width=30)
P36 = Entry(root, textvariable=ConfP16, width=30)

print(type(ConfP1), type(P21))

M21 = Entry(root, textvariable=ConfM1, width=30)
M22 = Entry(root, textvariable=ConfM2, width=30)
M23 = Entry(root, textvariable=ConfM3, width=30)
M24 = Entry(root, textvariable=ConfM4, width=30)
M25 = Entry(root, textvariable=ConfM5, width=30)
M26 = Entry(root, textvariable=ConfM6, width=30)
M27 = Entry(root, textvariable=ConfM7, width=30)
M28 = Entry(root, textvariable=ConfM8, width=30)
M29 = Entry(root, textvariable=ConfM9, width=30)
M30 = Entry(root, textvariable=ConfM10, width=30)
M31 = Entry(root, textvariable=ConfM11, width=30)
M32 = Entry(root, textvariable=ConfM12, width=30)
M33 = Entry(root, textvariable=ConfM13, width=30)
M34 = Entry(root, textvariable=ConfM14, width=30)
M35 = Entry(root, textvariable=ConfM15, width=30)
M36 = Entry(root, textvariable=ConfM16, width=30)

e11.place(x=210, y=163)
e12.place(x=145, y=213)

P21.place(x=575, y=110)
P22.place(x=575, y=160)
P23.place(x=575, y=210)
P24.place(x=575, y=260)
P25.place(x=575, y=310)
P26.place(x=575, y=360)
P27.place(x=575, y=410)
P28.place(x=575, y=460)
P29.place(x=575, y=510)
P30.place(x=575, y=560)
P31.place(x=575, y=610)
P32.place(x=575, y=660)
P33.place(x=575, y=710)
P34.place(x=575, y=760)
P35.place(x=575, y=810)
P36.place(x=575, y=860)

M21.place(x=895, y=110)
M22.place(x=895, y=160)
M23.place(x=895, y=210)
M24.place(x=895, y=260)
M25.place(x=895, y=310)
M26.place(x=895, y=360)
M27.place(x=895, y=410)
M28.place(x=895, y=460)
M29.place(x=895, y=510)
M30.place(x=895, y=560)
M31.place(x=895, y=610)
M32.place(x=895, y=660)
M33.place(x=895, y=710)
M34.place(x=895, y=760)
M35.place(x=895, y=810)
M36.place(x=895, y=860)

P21.config(state=DISABLED)
P22.config(state=DISABLED)
P23.config(state=DISABLED)
P24.config(state=DISABLED)
P25.config(state=DISABLED)
P26.config(state=DISABLED)
P27.config(state=DISABLED)
P28.config(state=DISABLED)
P29.config(state=DISABLED)
P30.config(state=DISABLED)
P31.config(state=DISABLED)
P32.config(state=DISABLED)
P33.config(state=DISABLED)
P34.config(state=DISABLED)
P35.config(state=DISABLED)
P36.config(state=DISABLED)

M21.config(state=DISABLED)
M22.config(state=DISABLED)
M23.config(state=DISABLED)
M24.config(state=DISABLED)
M25.config(state=DISABLED)
M26.config(state=DISABLED)
M27.config(state=DISABLED)
M28.config(state=DISABLED)
M29.config(state=DISABLED)
M30.config(state=DISABLED)
M31.config(state=DISABLED)
M32.config(state=DISABLED)
M33.config(state=DISABLED)
M34.config(state=DISABLED)
M35.config(state=DISABLED)
M36.config(state=DISABLED)

B1 = Button(root, text="开始", font=('KaiTi', 20), bd=3, bg='black', fg='#FFFFFF', command=StartButton)
B2 = Button(root, text="扫码结束", font=('KaiTi', 15), bd=3, bg='black', fg='#FFFFFF', command=touch)

B1.place(x=400, y=90)
B2.place(x=390, y=204)

root.mainloop()
