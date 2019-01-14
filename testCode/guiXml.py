from tkinter import *
import tkinter.filedialog
'''
    这是一个使用tkinter实现的,可以进行文件上传下载的demo
'''

def Open():
    selectFileName = tkinter.filedialog.askopenfilename(title='???')#选择文件
    with open(selectFileName, 'r', encoding='UTF-8') as f:
        print(f.name)
        print('-------------------------------------------')
        print(f.read())
def Download():
    pass
    # path = tkinter.filedialog.asksaveasfilename()
    # print(files.content)

root = Tk()
root.title('数据格式转化')
root.geometry('500x400')

# e1 = Entry(root,width=50)
# e1.grid(row=0, column=0)

lab1 = Label(root,text='请选择Excel文件:',).grid(row=0, column=0)
lab1 = Label(root,text='点击生成XML文件:',).grid(row=1, column=0)

btn1 = Button(root,text='选择', command=Open).grid(row=0, column=1,pady=5)
btn2 = Button(root,text='生成', command=Download).grid(row=1, column=1,pady=5)

mainloop()
