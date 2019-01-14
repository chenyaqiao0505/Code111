from tkinter import *



def key(event):
    entry1.delete('0.0',END)

root = Tk()
root.geometry('+200+300')
# 创建一个框架，在这个框架中响应事件
entry1 = Entry(root)
entry1.bind("<Up>",key)
entry1.pack()

# 当前框架被选中，意思是键盘触发，只对这个框架有效
entry1.focus_set()

mainloop()

