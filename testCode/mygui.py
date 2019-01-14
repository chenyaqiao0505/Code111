from tkinter import *
import tkinter.filedialog
import xlrd
import xlwt
from datetime import date,datetime

def change():
    select = tkinter.filedialog.askopenfilename(title='选择文件').place(x=100, y=30, anchor='nw')#选择文件
    tkinter.messagebox.showerror(title='Hi', message='有警告！')

# def change_advantech():
#     selectAdvantech = tkinter.filedialog.askopenfilename(title='选择文件').place(x=100, y=30, anchor='nw')#选择文件
#
#
#     tkinter.messagebox.showerror(title='Hi', message='有警告！')



lab1 = Label(root,text="选择文件进行转化:",font=('Arial', 15),).place(x=10, y=20, anchor='nw')
lab2 = Label(root,text="您选择的文件是:",font=('Arial', 15),).place(x=10, y=51, anchor='nw')
text1 = Entry(root,width=10,bg='green',font=('Arial', 15),).place(x=160, y=53, anchor='nw')
text2 = Text(root,width=27,height=3,bg='green',font=('Arial', 14),).place(x=10, y=130, anchor='nw')

btn1 = Button(root,text='文件选取', command=change).place(x=249, y=50, anchor='nw')
btn2 = Button(root,text='开始转化',width=41,height=1).place(x=10, y=90, anchor='nw')

root.resizable(0,0)

# lab2 = Label(root,text="选取文件转化为odoo格式:",font=('Arial', 15),).place(x=10, y=90, anchor='nw')
# btn2 = Button(root,text='文件选取', command=change_advantech).place(x=250, y=90, anchor='nw')
# btn2 = Button(root,text='开始转化').place(x=330, y=90, anchor='nw')



# textarea = Text(root,height=i)
# row 为行，colum 为列，padx 就是单元格左右间距，pady 就是单元格上下间距，
#ipadx是单元格内部元素与单元格的左右间距，ipady是单元格内部元素与单元格的上下间距。
#参数 anchor='nw'，就是前面所讲的锚定点是西北角。
#place()精确坐标显示




# l = Label(root, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)

#
#
# e1 = Entry(root,width=0)
# e1.grid(row=0, column=0)


mainloop()
