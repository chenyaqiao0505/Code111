from tkinter import *

root = Tk()

def key(event):
    print ("pressed", repr(event.char))
    if repr(event.char)==str('\r'):
        e2.focus_set()


def callback(event):
    e2.focus_set()
    print ("clicked at", event.x, event.y)


frame = Frame(root)

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry("{}x{}".format(int(w/3), int(h/2)))
v=StringVar()

e1 = Entry(root, textvariable=v, validate='focusout', validatecommand=key)  #当焦点移出的时候调用validatecommand设置的函数test
e2 = Entry(root)
# e1.focus_set()
e1.pack(padx=10, pady=10)
e2.pack(padx=10, pady=10)

#widget.bind(event,handler)
#
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
