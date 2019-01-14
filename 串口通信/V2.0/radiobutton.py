#Radiobutton为单选按钮，即在同一组内只能有一个按钮被选中，每当选中组内的一个按钮时，其它的按钮自动改为非选中态，与其他控件不同的是：它有组的概念.
'''1.创建一个简单的Radiobutton'''
# from tkinter import *
# root = Tk()
# Radiobutton(root,text = 'python').pack()
# Radiobutton(root,text = 'tkinter').pack()
# Radiobutton(root,text = 'widget').pack()
# root.mainloop()
#不指定绑定变量，每个Radiobutton自成一组

'''2.创建一个Radiobutton组，使用绑定变量来设置选中的按钮'''
# from tkinter import *
# root = Tk()
# #创建一个Radiobutton组，创建三个Radiobutton，并绑定到整型变量v
# #选中value=1的按钮
# v = IntVar()
# v.set(1)
# for i in range(3):
#     Radiobutton(root,variable = v,text = 'python',value = i).pack()
#
# root.mainloop()
'''3.创建两个不同的组'''
# from tkinter import *
# root = Tk()
# vLang = IntVar()
# vOS = IntVar()
# vLang.set(1)
# vOS.set(2)
#
# for v in [vLang,vOS]:    #创建两个组
#     for i in range(3):    #每个组含有3个按钮
#         Radiobutton(root,
#                     variable = v,
#                     value = i,
#                     text = 'python' + str(i)
#                     ).pack()
# root.mainloop()
#不同的组，各个按钮互不影响。
# # ---------------------------------------
# '''小甲鱼的例子'''
# from tkinter import *
# root = Tk()
# v = IntVar()
# v.set(1)     #要实现单选互斥的效果，
#              #variable选项共享一个整型变量，
#              #value需要设置不同的值
# Radiobutton(root,text = '貂蝉',variable = v,value = 1).pack(anchor = W)
# Radiobutton(root,text = '王昭君',variable = v,value = 2).pack(anchor = W)
# Radiobutton(root,text = '杨玉环',variable = v,value = 3).pack(anchor = W)
# Radiobutton(root,text = '西施',variable = v,value = 4).pack(anchor = W)
# root.mainloop()
#
#
# '''还可以写成循环版的'''
# from tkinter import *
# root = Tk()
# girls = [('西施',1),('王昭君',2),('杨玉环',3),('貂蝉',4)]
# v = IntVar() #tkinter专用整型变量
# v.set(1) #设置v的值为1，值多少无所谓了,我的理解是第一组写1，第二组写2，一次递增
# for girl,num in girls:
#     #variable = v绑定了一个整型变量
#     b = Radiobutton(root,text = girl,variable = v,value = num)
#     b.pack(anchor = W)
# root.mainloop()
'''
Created on 2017年9月11日
@author: Nick
'''
'''
Tkinter之Radiobutton篇
Radiobutton为单选按钮，即在同一组内只能有一个按钮被选中，每当选中组内的一个按钮时，其它的按钮自动改为非选中态，与其他控件不同的是：它有组的概念
'''

#_*_coding:utf-8_*_
import tkinter as tk
from tkinter import *


#回调函数
def callRadiobutton():
    print('python is good!')

def callRadobuttonPrint(v):
    print(v)

if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('Radiobutton')
    root.geometry("1800x800+120+100")         #设置窗口大小  并初始化桌面位置
    root.resizable(width = True,height = True)  #宽不可变 高可变  默认True

    #不指定绑定变量，每个Radiobutton自成一组
    fram = Frame(root)
    Radiobutton(fram,text = 'python').pack(side = LEFT)
    Radiobutton(fram,text = 'python1').pack(side = LEFT)
    Radiobutton(fram,text = 'python2').pack(side = LEFT)

    fram.pack(side = TOP)

    #1、不指定绑定变量，每个Radiobutton自成一组
    fram1 = Frame(root)
    v = IntVar()
    v.set(1)
    for i in range(3):
        Radiobutton(fram1,variable = v,text = 'python',value = i).pack(side = LEFT)
    fram1.pack(side = TOP)

    #2、创建两个不同的组
    fram2 = Frame(root)
    v1 = IntVar()
    v2 = IntVar()
    v1.set(1)
    v2.set(2)
    for v in [v1,v2]:   #创建两个组
        for i in range(3):  #每个组含有3个按钮,不同的组，各个按钮互不影响。
            Radiobutton(fram2,variable = v,
                        text = 'python',
                        value = i,
                        command = callRadiobutton).pack(side = LEFT)
    fram2.pack(side = TOP)

    #3、如果同一个组中的按钮使用相同的value，则这两个按钮的工作方式完全相同
    fram3 = Frame(root)
    v = IntVar()
    v.set(1)
    for i in range(3):
        Radiobutton(fram3,variable = v,
                    text = 'value值是:' + str(1),
                    value = 1).pack(side = LEFT)

    for i in range(3):
        Radiobutton(fram3,variable = v,
                    text = 'value值是:' + str(i),
                    value = i).pack(side = LEFT)
    #上述的例子中共有4个value为1的值，当选中其中的一个时，其他三个也会被选中；选中除了这四个只外的按钮时，四个按钮全部取消
    fram3.pack(side = TOP)

    #4、与Checkbutton类似，每个Radiobutton可以有自己的处理函数，每当点击按钮时，系统会调用相应的处理函数
    fram4 = Frame(root)
    v = IntVar()
    v.set(1)
    for i in range(3):
        Radiobutton(fram4,variable = v,
                    text = 'python' + str(i),
                    value = i,
                    command = callRadobuttonPrint(i)).pack(side = LEFT)
    fram4.pack(side = TOP)

    fram5 = Frame(root)
    v = IntVar()
    v.set(0)

    def r1():
        print('call r1')
    def r2():
        print('call r2')
    def r3():
        print('call r3')
    def r4():
        print('call r4')

    i = 0
    # 创建8个按钮，其中两个两个的value值相同
    # 注意虽然同时可以选中两个按钮，但每次点击按钮，执行的代码只有一次
    for r in [r1,r2,r3,r4]:
        for i in range(3):
            Radiobutton(fram5,variable = v,
                        text = 'python' + str(i),
                        value = i,
                        bg = 'green',
                        command = r).pack(side = LEFT)

        for i in range(3):
            Radiobutton(fram5,variable = v,
                        text = 'python' + str(i),
                        value = i,
                        fg = 'red',
                        command = r).pack(side = LEFT)
        i += 1

    fram5.pack(side = TOP)
    #6、Radiobutton另一个比较实用的属性是indicatoron,缺省情况下为1，如果将这个属性改为0，则其外观是Sunken
    # Radiobutton表示按钮的弹起或按下两种状态
    fram6 = Frame(root)
    Radiobutton(fram6,indicatoron = 1,
                text = 'python1').pack(side = LEFT)
    Radiobutton(fram6,indicatoron = 0,
                text = 'python1').pack(side = LEFT)

    Radiobutton(fram6,indicatoron = 1,
                text = 'python1',
                width = 10,height = 5).pack(side = LEFT)


    fram6.pack(side = TOP)

    root.mainloop()
