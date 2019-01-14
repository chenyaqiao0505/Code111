import tkinter
import serial.tools.list_ports
from  tkinter  import ttk

def go(*args):   #处理事件，*args表示可变参数
    print(comboxlist.get()) #打印选中的值
    #print(comboxlist.index())

win=tkinter.Tk() #构造窗体
comvalue=tkinter.StringVar()#窗体自带的文本，新建一个值
comboxlist=ttk.Combobox(win,textvariable=comvalue) #初始化

pNameList=[]
port_list = list(serial.tools.list_ports.comports())
if len(port_list) == 0:
   print('找不到串口')
else:
    for i in range(0,len(port_list)):
        print(port_list[i])
        pNameList.append(port_list[i][0])
pNameList.sort()

comboxlist["values"]=tuple(pNameList)
comboxlist.set("5")
comvalue="5"
comboxlist.current(0)  #选择第一个
comboxlist.bind("<<ComboboxSelected>>",go)  #绑定事件,(下拉列表框被选中时，绑定go()函数)
comboxlist.pack()

#from Tkinter import *
#root = Tk()
#for i in range(1, 101):
#    val = str(i)
#    l=Label(win, textvariable = val)
#    l.pack(x=10,y=20)
#    win.update_idletasks()

win.mainloop() #进入消息循环
from tkinter import *
#
# root = Tk()
#
# text1 = Text(root,width=30,height=2)
# text1.pack()
# text1.insert(INSERT,'I love you')
#
# def show():
#      print('吆喝，我被点了一下')
# #text还可以插入按钮  图片等
# b1 = Button(text1,text='点我点我',command=show)
# #在text创建组件的命令
# text1.window_create(INSERT,window=b1)
#
# mainloop()

list = ['978750536729648652289787505367296\n9787505367296\n9787505367296\n9787505367296\n112231234323\n']
print(len(list))