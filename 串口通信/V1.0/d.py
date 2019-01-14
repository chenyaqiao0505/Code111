__author__ = 'freedom'
from tkinter import *
class Reg (Frame):
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.lab1 = Label(frame,text = "User:")
        self.lab1.grid(row = 0,column = 0,sticky = W)
        self.ent1 = Entry(frame)
        self.ent1.focus_set()
        self.ent1.grid(row = 0,column = 1,sticky = W)
        self.lab2 = Label(frame,text = "Password:")
        self.lab2.grid(row = 1,column = 0)
        self.ent2 = Entry(frame,show = "*")
        self.ent2.grid(row = 1,column = 1,sticky = W)
        self.button = Button(frame,text = "Submit",command = self.Submit)
        self.button.grid(row = 2,column = 1,sticky = E)
        self.lab3 = Label(frame,text = "")
        self.lab3.grid(row = 3,column = 0,sticky = W)
        self.button2 = Button(frame,text = "Quit",command = frame.quit)
        self.button2.grid(row = 3,column = 3,sticky = E)

    def Submit(self):
        s1 = self.ent1.get()
        s2 = self.ent2.get()
        if s1 == 'freedom' and s2 == '123':
            self.lab3["text"] = "Confirm"
        else:
            self.lab3["text"] = "Error!"
        self.ent1.delete(0,len(s1))
        self.ent2.delete(0,len(s2))

    # def callback(event):
    #     self.ent1.focus_set()

root = Tk()
root.title("Register")
# root.bind('<Key>',callback)

app = Reg(root)
root.mainloop()



from tkinter import *
root = Tk()

def callback(event):
    # print('敲击位置：',repr(event.char))


frame = Frame(root,width=200,height=200)
frame.bind('<Key>',callback)
frame.focus_set()
frame.pack()
mainloop()
