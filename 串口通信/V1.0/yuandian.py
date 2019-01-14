from Tkinter import *
#导入tk模块
top = Tk()
#初始化Tk
top.title('label test')
#标题显示为label test
label = Label(top, text = 'this is my first label')
#创建一个label，它属于top窗口，文本显示内容为.....
label.pack()
bm = PhotoImage(file = '/home/fangxu/图片/4.png')
label2 = Label(top, image = bm)
label2.bm = bm
label2.pack()
top.mainloop()
