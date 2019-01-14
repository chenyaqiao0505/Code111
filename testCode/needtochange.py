from tkinter import *
import tkinter.filedialog






root = Tk()
root.title('数据格式转化')
root.geometry('430x180')


def change_odoo():
    selectFileName = tkinter.filedialog.askopenfilename(title='选择文件').place(x=100, y=30, anchor='nw')#选择文件
    pass
    tkinter.messagebox.showerror(title='Hi', message='有警告！')

def change_advantech():
    pass
    tkinter.messagebox.showerror(title='Hi', message='有警告！')

lab1 = Label(root,text="选取文件转化为研华格式:",font=('Arial', 15),).place(x=10, y=50, anchor='nw')
lab2 = Label(root,text="选取文件转化为odoo格式:",font=('Arial', 15),).place(x=10, y=90, anchor='nw')


btn1 = Button(root,text='文件选取', command=change_odoo).place(x=250, y=50, anchor='nw')
btn2 = Button(root,text='开始转化').place(x=330, y=50, anchor='nw')


btn1 = Button(root,text='文件选取', command=change_odoo).place(x=250, y=90, anchor='nw')
btn2 = Button(root,text='开始转化').place(x=330, y=90, anchor='nw')

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
