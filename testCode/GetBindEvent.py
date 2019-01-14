'''
获取绑定事件
'''


from tkinter import *
import time

def rtnkey(event=None):
    print(e.get())
    time.sleep(2)
    clear()


def clear():
	entry.delete(0,END)

def mydel(event=None):
    print('verystrange!~')

root = Tk()
e = StringVar()
entry = Entry(root, validate='key', textvariable=e, width=50)

button1 = Button(root,text='获取',  command=mydel,width=20,height=1)
button1.pack()
button1.bind('<F1>',mydel)

# 默认获取光标位置
entry.focus_set()

entry.pack()
entry.bind('<Return>', rtnkey)
root.title('测试回车获取文本框内容')

# # 获取全屏
# w = root.winfo_screenwidth()
# h = root.winfo_screenheight()
# print(w,h)
# root.geometry("%dx%d" %(w,h))
# # 置顶窗口,覆盖其他的窗口
# root.attributes("-topmost",True)

root.mainloop()
