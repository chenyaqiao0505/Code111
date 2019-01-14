'''
tkinter text值的插入
'''


from tkinter import *
import tkinter.messagebox #导入tkinter模块
import xlwt
import xlrd
from tkinter import ttk


ytm=tkinter.Tk() #创建Tk对象
ytm.title("login") #设置窗口标题
ytm.geometry("900x600") #设置窗口尺寸




# tkinter.Button(ytm,text="存入结果",command=Save_16).pack() #command绑定获取文本框内容方法
textarea = tkinter.Text(ytm,height=16,width=30)
textarea.pack()

def iii():
    textarea.insert(END,'iii'+'\n')

btu = Button(ytm,text = '请点击',command = iii)
btu.pack()
user_text=tkinter.Entry() #创建文本框
user_text.focus_set()
user_text.pack()


# user_text.bind('<Key-Return>',find_values)



ytm.mainloop() #进入主循环

