import sys
import threading
import time
from tkinter import *
import tkinter.messagebox
import xlwt
import xlrd
from xlutils.copy import copy
import os
import datetime
from UDPdeviceDI import udpdevicedi
import tkinter.messagebox
import threading

aa = udpdevicedi()

book_name=''
time_stamp = datetime.datetime.now()
root = Tk()
root.title('绝缘耐压测试')
root.geometry('900x600')
root.resizable(0,0)

Label(root, text='IOM模块功能综合测试系统', fg='blue', font=('KaiTi', 35, 'bold'), anchor='n').pack()
Label(root, text='参数设置', fg="#1E90FF", font=('KaiTi', 20, 'bold')).place(x=30, y=60)
Label(root, text='测试类型: ', font=('KaiTi', 15, 'bold')).place(x=60, y=110)
Label(root, fg='green', text='DI输出', font=('KaiTi', 15, 'bold')).place(x=170, y=110)
Label(root, text='扫码框: ', font=('KaiTi', 15, 'bold')).place(x=60, y=160)
Label(root, text='测试信息', fg="#1E90FF", font=('KaiTi', 20, 'bold')).place(x=30, y=195)
Label(root, text='板卡扫码', fg="#1E90FF", font=('KaiTi', 20, 'bold')).place(x=400, y=150)
Label(root, text='故障通道', fg="#1E90FF", font=('KaiTi', 20, 'bold')).place(x=645, y=150)
Label(root, text='注意事项:', fg="#FF0000", font=('KaiTi', 10, 'bold')).place(x=400, y=50)
Label(root, text='1.程序加载完成前处于离线状态,连接正常3秒即可读取到插入的板卡数量.', fg="#FF0000", font=('KaiTi', 10, 'bold')).place(x=400, y=70)
Label(root, text='2.离线模式下可插入板卡,确保板卡插入正常,即可打开电源进行测试工作.', fg="#FF0000", font=('KaiTi', 10, 'bold')).place(x=400, y=90)
Label(root, text='3.扫码前请检查光标是否在左侧扫码文本框内,确认无误后开始扫码.', fg="#FF0000", font=('KaiTi', 10, 'bold')).place(x=400, y=110)
Label(root, text='4.点击扫描结束按钮后,方可点击开始按钮进行测试.', fg="#FF0000", font=('KaiTi', 10, 'bold')).place(x=400, y=130)

 

text = Text(root, bg='#E5E5E5' ,width=43, height=26)
text.place(x=60, y=240)

#判断工装是否在线
checknum = 0

#1正在扫描
scanningBar= 0

alive = 1
def runmethod():
    global scanningBar
    deviceOnlineprint = 1  # 1  online    
    while alive:
        time.sleep(0.1)
        if aa.DeviceOnline == 1 and deviceOnlineprint == 0:
            text.delete(0.0,END)
            deviceOnlineprint = 1
            resu = aa.DINumList
            text.insert(END, '读取到DI:', ' ', resu[0], ' ', '\n', ' ', '读取到DO:', ' ', resu[1], ' ', '\n')
        if aa.DeviceOnline == 0 and deviceOnlineprint == 1:
            deviceOnlineprint = 0
            text.insert(END, '设备处于离线状态~！','\n','\n')
            if scanningBar == 0:
                P_list = [ConfP1, ConfP2, ConfP3, ConfP4, ConfP5, ConfP6, ConfP7, ConfP8,
                          ConfP9, ConfP10, ConfP11, ConfP12, ConfP13, ConfP14, ConfP15, ConfP16]
                for i in range(len(P_list)):
                    P_list[i].set('')
                    
                list = [ConfM1,ConfM2,ConfM3,ConfM4,
                        ConfM5,ConfM6,ConfM7,ConfM8,
                        ConfM9,ConfM10,ConfM11,ConfM12,
                        ConfM13,ConfM14,ConfM15,ConfM16]
                for i in range(len(list)):
                    list[i].set('')
    for i in range(len(codelist)):
        codelist.pop()
      
thread_read = threading.Thread(target=runmethod)
thread_read.setDaemon(1)
thread_read.start()


def StartButton():
    global checknum,scanningBar
    time.sleep(1)
    book_name = 'DO测试'+datetime.datetime.now().strftime("%Y%m%d%H%M%S") +'.xls'
    if P21.get() == '':
        tkinter.messagebox.showwarning('出错了', '请先扫描条形码，再点击开始按钮~！')
    elif len(codelist) == 0:
        tkinter.messagebox.showwarning('出错了', '请重新扫描条形码，再点击开始按钮~！')
    elif checknum == 1:
        aa.StartThread()
        result = aa.control1()
        list = [ConfM1,ConfM2,ConfM3,ConfM4,
                ConfM5,ConfM6,ConfM7,ConfM8,
                ConfM9,ConfM10,ConfM11,ConfM12,
                ConfM13,ConfM14,ConfM15,ConfM16]
        display = []
        for j in range(len(codelist)):
            display.append(result[2*j])
            display.append(result[2*j+1])

        finallist = finalhandle(display)
        finallist1 = finalhandle1(display)
        try:
            for i in range(len(display)):
                list[i].set(DealStr(finallist[i]))
        except Exception  as e:
            pass

        if os.path.exists(book_name):
                text.insert(END,'该文件已存在，可以直接进行测试~！ '+'\n')
                write_excel_append(book_name, finallist1)
        else:
            write_excel(sheet_name, value_title, book_name)
            write_excel_append(book_name, finallist1)
        #扫码结束
        scanningBar=0
        #存盘
        if os.path.exists(book_name):
            CodeBar(book_name, handle(codelist))
        else:
            write_excel(sheet_name, value_title, book_name)
            CodeBar(book_name, handle(codelist))
        for i in range(len(codelist)):
            codelist.pop()


def DealStr(aa):        #去掉[]
    bb = str(aa)
    b0 = bb.replace('[','')
    b1 = b0.replace(']','')
    b2 = b1.replace('pass, pass','PASS')
    b3 = b2.replace(', pass','')
    b4 = b3.replace('pass,','')
    return b4

codelist = []
def ScanButton(event):
    #正在扫码
    global scanningBar
    scanningBar=1
    m = ConfIn2.get()
    P_list = [ConfP1, ConfP2, ConfP3, ConfP4, ConfP5, ConfP6, ConfP7, ConfP8,
    ConfP9, ConfP10, ConfP11, ConfP12, ConfP13, ConfP14, ConfP15, ConfP16]
    for i in range(len(P_list)):
        if P_list[i].get() == '':
            P_list[i].set(m)
            codelist.append(m)
            time.sleep(0.5)
            e12.delete(0, END)
            break


def touch(event=None):
    try:
        global checknum
        ResuList = aa.DINumList
        qq = ResuList[0]
        name = [ConfP1, ConfP2, ConfP3, ConfP4,
                ConfP5, ConfP6, ConfP7, ConfP8,
                ConfP9, ConfP10, ConfP11, ConfP12,
                ConfP13, ConfP14, ConfP15, ConfP16]
        valuelist = [P21,P22,P23,P24,
                 P25,P26,P27,P28,
                 P29,P30,P31,P32,
                 P33,P34,P35,P36]
        if qq == len(codelist):
            text.insert(END,'板卡数量正确，可以进行测试~！'+'\n')
            checknum = 1    #修改状态位
        else:
            tkinter.messagebox.showwarning('出错了', '扫码数量和板卡数量不一致，请重新扫码~！')
            checknum = 0    #修改状态位
            for i in range(len(codelist)):
                valuelist[i].delete(0,END)
                for i in range(len(codelist)):
                    codelist.pop()
    except Exception as e:
        text.insert(END,'请先打开电源,再点击重试~!'+'\n')

sheet_name = 'sheet1'
value_title = [['条形码','是否通过']]


def write_excel( sheet_name, value,filepath):
    index = len(value)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheet_name)
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])
            workbook.save(filepath)
    text.insert(END,"写入表头成功！"+'\n')


def write_excel_append(path, value):
  workbook = xlrd.open_workbook(path)
  sheets = workbook.sheet_names() 
  worksheet = workbook.sheet_by_name(sheets[0])
  new_workbook = copy(workbook) 
  new_worksheet = new_workbook.get_sheet(0) 
  for j in range(0, len(value[0])):
      new_worksheet.write(j+1,1, DealStr(value[0][j]))
  new_workbook.save(path)
  text.insert(END,"结果保存成功~！"+'\n')



def CodeBar(path, value):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names() 
    worksheet = workbook.sheet_by_name(sheets[0])
    new_workbook = copy(workbook) 
    new_worksheet = new_workbook.get_sheet(0) 
    for j in range(0, len(value[0])):
        new_worksheet.write(j+1 , 0, value[0][j]) 
    new_workbook.save(path)
    text.insert(END,"条形码写入成功~！"+'\n')


def finalhandle(list):      #前后换位
    handlelist1 = []
    handlelist2 = []
    for o in range(len(list)):
        if o % 2 != 1 and type(list[o]) != type('pass'):
            for p, q in zip(range(len(list[o])), range(8, 0, -1)):
                list[o][p] += q
    for o in range(len(list)):
        if o % 2 != 0 and type(list[o]) != type('pass'):
            for p, q in zip(range(len(list[o])), range(16, 0, -1)):
                list[o][p] += q

    for i in range(0, len(list), 2):
        handlelist1.append(list[i])
    for j in range(1, len(list), 2):
        handlelist2.append(list[j])
    handlelist2.append(None)
    finallylist = []
    for j, k in zip(handlelist1, handlelist2):
        finallylist.append(str(j) + ', ' + str(k))
    return finallylist


def finalhandle1(list):
    handlelist1 = []
    handlelist2 = []
    for i in range(0, len(list), 2):
        handlelist1.append(list[i])

    for j in range(1, len(list), 2):
        handlelist2.append(list[j])

    finallylist = []
    finallylist1 = []
    for j, k in zip(handlelist1, handlelist2):
        finallylist.append(str(j) + ', ' + str(k))
    finallylist1.append(finallylist)
    return finallylist1


def handle(list):
    handlelist = []
    for i in range(len(list)):
        handlelist.append(str(list[i]))
    finallylist = []
    finallylist.append(handlelist)
    return finallylist


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

e12 = Entry(root, textvariable=ConfIn2, width=20)
e12.focus_set()
e12.bind('<Key-Return>', ScanButton)

P21 = Entry(root, textvariable=ConfP1, width=38)
P22 = Entry(root, textvariable=ConfP2, width=38)
P23 = Entry(root, textvariable=ConfP3, width=38)
P24 = Entry(root, textvariable=ConfP4, width=38)
P25 = Entry(root, textvariable=ConfP5, width=38)
P26 = Entry(root, textvariable=ConfP6, width=38)
P27 = Entry(root, textvariable=ConfP7, width=38)
P28 = Entry(root, textvariable=ConfP8, width=38)
P29 = Entry(root, textvariable=ConfP9, width=38)
P30 = Entry(root, textvariable=ConfP10, width=38)
P31 = Entry(root, textvariable=ConfP11, width=38)
P32 = Entry(root, textvariable=ConfP12, width=38)
P33 = Entry(root, textvariable=ConfP13, width=38)
P34 = Entry(root, textvariable=ConfP14, width=38)
P35 = Entry(root, textvariable=ConfP15, width=38)
P36 = Entry(root, textvariable=ConfP16, width=38)


M21 = Entry(root, textvariable=ConfM1, width=35)
M22 = Entry(root, textvariable=ConfM2, width=35)
M23 = Entry(root, textvariable=ConfM3, width=35)
M24 = Entry(root, textvariable=ConfM4, width=35)
M25 = Entry(root, textvariable=ConfM5, width=35)
M26 = Entry(root, textvariable=ConfM6, width=35)
M27 = Entry(root, textvariable=ConfM7, width=35)
M28 = Entry(root, textvariable=ConfM8, width=35)
M29 = Entry(root, textvariable=ConfM9, width=35)
M30 = Entry(root, textvariable=ConfM10, width=35)
M31 = Entry(root, textvariable=ConfM11, width=35)
M32 = Entry(root, textvariable=ConfM12, width=35)
M33 = Entry(root, textvariable=ConfM13, width=35)
M34 = Entry(root, textvariable=ConfM14, width=35)
M35 = Entry(root, textvariable=ConfM15, width=35)
M36 = Entry(root, textvariable=ConfM16, width=35)

e12.place(x=145, y=163)

P21.place(x=410, y=190)
P22.place(x=410, y=215)
P23.place(x=410, y=240)
P24.place(x=410, y=265)
P25.place(x=410, y=290)
P26.place(x=410, y=315)
P27.place(x=410, y=340)
P28.place(x=410, y=365)
P29.place(x=410, y=390)
P30.place(x=410, y=415)
P31.place(x=410, y=440)
P32.place(x=410, y=465)
P33.place(x=410, y=490)
P34.place(x=410, y=515)
P35.place(x=410, y=540)
P36.place(x=410, y=565)


M21.place(x=650, y=190)
M22.place(x=650, y=215)
M23.place(x=650, y=240)
M24.place(x=650, y=265)
M25.place(x=650, y=290)
M26.place(x=650, y=315)
M27.place(x=650, y=340)
M28.place(x=650, y=365)
M29.place(x=650, y=390)
M30.place(x=650, y=415)
M31.place(x=650, y=440)
M32.place(x=650, y=465)
M33.place(x=650, y=490)
M34.place(x=650, y=515)
M35.place(x=650, y=540)
M36.place(x=650, y=565)


Label(root, text='1', font=('KaiTi', 15, 'bold')).place(x=387, y=185)
Label(root, text='2', font=('KaiTi', 15, 'bold')).place(x=387, y=210)
Label(root, text='3', font=('KaiTi', 15, 'bold')).place(x=387, y=235)
Label(root, text='4', font=('KaiTi', 15, 'bold')).place(x=387, y=260)
Label(root, text='5', font=('KaiTi', 15, 'bold')).place(x=387, y=286)
Label(root, text='6', font=('KaiTi', 15, 'bold')).place(x=387, y=310)
Label(root, text='7', font=('KaiTi', 15, 'bold')).place(x=387, y=335)
Label(root, text='8', font=('KaiTi', 15, 'bold')).place(x=387, y=360)
Label(root, text='9', font=('KaiTi', 15, 'bold')).place(x=387, y=385)
Label(root, text='10', font=('KaiTi', 15, 'bold')).place(x=377, y=410)
Label(root, text='11', font=('KaiTi', 15, 'bold')).place(x=377, y=435)
Label(root, text='12', font=('KaiTi', 15, 'bold')).place(x=377, y=460)
Label(root, text='13', font=('KaiTi', 15, 'bold')).place(x=377, y=485)
Label(root, text='14', font=('KaiTi', 15, 'bold')).place(x=377, y=510)
Label(root, text='15', font=('KaiTi', 15, 'bold')).place(x=377, y=535)
Label(root, text='16', font=('KaiTi', 15, 'bold')).place(x=377, y=560)


B1 = Button(root, text="开始", font=('KaiTi', 20), bd=3, bg='black', fg='#FFFFFF', command=StartButton)
B2 = Button(root, text="扫码结束", font=('KaiTi', 15), bd=3, bg='black', fg='#FFFFFF', command=touch)

B1.place(x=290, y=90)
B2.place(x=280, y=154)
root.mainloop()
