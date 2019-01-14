from tkinter import *

class MyGui:
    def __init__(self):
        self.url_vaule = ''
        self.btu_set = 0
        self.sub_set = 0

        self.win = Tk()
        self.win.geometry('400x550')
        self.win.title('Excel数据汇总工具')

        self.e1 = Text(self.win, width=57, height=33, bg='green')
        self.e1.place(x = 0,y = 0)

        self.btu = Button(self.win, text='开始汇总',command = self.set_btu_val)
        self.btu.place(x = 10,y = 490)

        self.lab = Label(self.win,text = '选择路径：')
        self.lab.place(x = 10,y = 450)

        self.sub_btn = Button(self.win,text = '提交',command = self.set_sub_val)
        self.sub_btn.place(x = 300,y = 445)

        self.url_entry = Entry(self.win,width = 30)
        self.url_entry.place(x = 70,y = 450)
        self.url_entry.focus_set()

        self.win.resizable(0, 0)


    def set_sub_val(self):
        self.sub_btn = 1

    def set_btu_val(self):
        self.btu_set = 1

    def display_e1(self,value):
        self.e1.insert(END,value,'\n', '\n')