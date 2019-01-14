# import tkinter as tk
import sys,threading,time
from tkinter import * 
from SerialTest import ComThread

#初始化串口实例
ck = ComThread(Port=int(1))

def comRead():
    while 1:
        # 接收间隔
        time.sleep(1)
        try:
            # 获取接收到的数据长度
            bv=ck.getValueOfID()
            if bv==b'' or bv ==None:
                v1.set('Null Device')
            else:
                v1.set(bv)
            bv=ck.getValueOfMode()
            if bv==b''  or bv ==None:
                v2.set('Null Device')
            else:
                v2.set(bv)
                #print(bv)
                #print(ConfInV1)
                #if bv==b'IR\r\n':
                #    ck.setModul(3)
                #    #print(lbl31.value)
            bv=ck.getValueOfStatus()
            #print(bv)
            if bv==b''  or bv ==None:
                v3.set('Null Device')
            else:
                v3.set(bv)
            bv=ck.getValueOfMeas()
            
            if bv==b'' or bv ==None:
                v4.set('Null Device')
            else:
                v4.set(bv)

            bv=ck.getValueOfConfig()
            if bv==b'' or bv ==None:
                ConfN1.set('Null Device')                                   
            else:
                if bv[0]=='':
                    ConfInV1.set('Null')
                else:
                    ConfInV1.set(bv[0])
                if bv[1]=='':
                    ConfInV2.set('Null')
                else:
                    ConfInV2.set(bv[1])
                if bv[2]=='':
                    ConfInV3.set('Null')
                else:
                    ConfInV3.set(bv[2])
                if bv[3]=='':
                    ConfInV4.set('Null')
                else:
                    ConfInV4.set(bv[3])
                if bv[4]=='':
                    ConfInV5.set('Null')                
                else:
                    ConfInV5.set(bv[4])
                ConfN1.set('VOLTage')
                ConfN2.set('RHISet ')
                ConfN3.set('RLOSet')
                ConfN4.set('TTIMe')
                ConfN5.set('REF')

                print(bv)
                
            
            if str(ck.getValueOfMode()) == str(b'ACW\r\n'):
                v.set(1)
            elif str(ck.getValueOfMode()) == str(b'DCW\r\n'):
                v.set(2)
            elif str(ck.getValueOfMode()) == str(b'IR\r\n'):
                v.set(3)
            elif str(ck.getValueOfMode()) == str(b'GB\r\n'):
                v.set(4)            
        except Exception as ex:
            print(str(ex))
            

def sel():
    # selection = "You selection the option" + str(v.get())
    # label.config(text = selection)
    modID=str(v.get())    
    label.config(text = modID)
    ck.setModul(v.get())    

# 按钮
def TestOnButton():
    ck.TestOn()
    print("Control!")
     
def ConfigButton():
    # 获取entry内容
    #print(ConfIn1.get())
    listConfig= []
    listConfig.append(ConfIn1.get())
    listConfig.append(ConfIn2.get())
    listConfig.append(ConfIn3.get())
    listConfig.append(ConfIn4.get())
    listConfig.append(ConfIn5.get())
    ck.setIRValueOfConfig(listConfig)
    
    print("配置！")

#ReadConfigButton
def ReadConfigButton():
    #ck.setReadConfig()
    print("Read配置！")   

#初始化窗口

# 显示框
root = Tk()
root.title('绝缘耐压测试')
root.geometry('800x600')
lbl1=Label(root,text='设备类型：').place(x=25,y=30)
lbl2=Label(root,text='工作模式：').place(x=25,y=70)
lbl3=Label(root,text='状    态：').place(x=25,y=110)
lbl4=Label(root,text='测量结果：').place(x=25,y=150)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()


#读取内容
lbl11=Label(root,textvariable= v1).place(x=100,y=30)
lbl12=Label(root,textvariable= v2).place(x=100,y=70)
lbl13=Label(root,textvariable= v3).place(x=100,y=110)
lbl14=Label(root,textvariable= v4).place(x=100,y=150)


   
# 单选框
v = IntVar()
#要实现单选互斥的效果，
#variable选项共享一个整型变量，
#value需要设置不同的值
r1 = Radiobutton(root,text = 'ACW',variable = v,value = 1, command=sel)
r2 = Radiobutton(root,text = 'DCW',variable = v,value = 2, command=sel)
r3 = Radiobutton(root,text = 'IR',variable = v,value = 3, command=sel)
r4 = Radiobutton(root,text = 'GB',variable = v,value = 4, command=sel)

r1.place(x=40, y=200)
r2.place(x=100, y=200)
r3.place(x=160, y=200)
r4.place(x=220, y=200)

#参数设置部分
#VOLTage
ConfN1=StringVar()
ConfN2=StringVar()
ConfN3=StringVar()
ConfN4=StringVar()
ConfN5=StringVar()

ConfInV1=StringVar()
ConfInV2=StringVar()
ConfInV3=StringVar()
ConfInV4=StringVar()
ConfInV5=StringVar()
#i=0
#for i in range(5):
#    ConfN.append('')
#    Label(root,textvariable= ConfN[i]).place(x=25,y=290+i*40)
#    ConfN[i]=('ConfN'+str(i))


lbl21=Label(root,textvariable= ConfN1).place(x=25,y=290)
lbl22=Label(root,textvariable= ConfN2).place(x=25,y=330)
lbl23=Label(root,textvariable= ConfN3).place(x=25,y=370)
lbl24=Label(root,textvariable= ConfN4).place(x=25,y=410)
lbl25=Label(root,textvariable= ConfN5).place(x=25,y=450)

ConfN1.set('ConfN1')
ConfN2.set('ConfN2')
ConfN3.set('ConfN3')
ConfN4.set('ConfN4')
ConfN5.set('ConfN5')

ConfIn1=StringVar()
ConfIn2=StringVar()
ConfIn3=StringVar()
ConfIn4=StringVar()
ConfIn5=StringVar()

ConfOut1=StringVar()
ConfOut2=StringVar()
ConfOut3=StringVar()
ConfOut4=StringVar()
ConfOut5=StringVar()

e11 = Entry(root,textvariable=ConfIn1, width=20)
e12 = Entry(root,textvariable=ConfIn2, width=20)
e13 = Entry(root,textvariable=ConfIn3, width=20)
e14 = Entry(root,textvariable=ConfIn4, width=20)
e15 = Entry(root,textvariable=ConfIn5, width=20)

e11.place(x=100,y=290)
e12.place(x=100,y=330)
e13.place(x=100,y=370)
e14.place(x=100,y=410)
e15.place(x=100,y=450)

e11.config(state='normal')
#e12.config(state=DISABLED)
#e3.config(state=DISABLED)
#e4.config(state=DISABLED)

lbl31=Label(root,textvariable= ConfInV1).place(x=250,y=290)
lbl32=Label(root,textvariable= ConfInV2).place(x=250,y=330)
lbl33=Label(root,textvariable= ConfInV3).place(x=250,y=370)
lbl34=Label(root,textvariable= ConfInV4).place(x=250,y=410)
lbl35=Label(root,textvariable= ConfInV5).place(x=250,y=450)

ConfInV1.set('ConfN1')
ConfInV2.set('ConfN2')
ConfInV3.set('ConfN3')
ConfInV4.set('ConfN4')
ConfInV5.set('ConfN5')

b1 = Button(root, text="Test On", command=TestOnButton)
# 点击按钮的时候
b2 = Button(root, text="Config", command=ConfigButton)
#b3 = Button(root, text="ReadConfig", command=ReadConfigButton)

b1.place(x=60, y=240)
b2.place(x=60, y=490)
#b3.place(x=120, y=490)

label = Label(root)
label.pack()

#e15.pack_forget()

ck.start()

thread_read = None
thread_read = threading.Thread(target=comRead)
thread_read.setDaemon(1)
thread_read.start()

root.mainloop()
