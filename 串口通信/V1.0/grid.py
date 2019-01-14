from tkinter import *
root = Tk()
Button(root,text='A').pack(side=LEFT,expand=YES,fill=Y)
Button(root,text='B').pack(side=TOP,expand=YES,fill=BOTH)
Button(root,text='C').pack(side=RIGHT,expand=YES,fill=NONE)
Button(root,text='D').pack(side=LEFT,expand=NO,fill=Y)
Button(root,text='E').pack(side=TOP,expand=YES,fill=BOTH)
Button(root,text='F').pack(side=BOTTOM,expand=YES)
Button(root,text='G').pack(anchor=SE)
root.mainloop()





from Tkinter import *
root = Tk()
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=X,padx=10)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=X,padx=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X,padx=10)
mainloop()
