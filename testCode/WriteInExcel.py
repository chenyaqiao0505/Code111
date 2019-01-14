from tkinter import *
import tkinter.messagebox #导入tkinter模块
import xlwt
import xlrd
from time import *
ytm=tkinter.Tk() #创建Tk对象
ytm.title("login") #设置窗口标题
ytm.geometry("300x600") #设置窗口尺寸
l1=tkinter.Label(ytm,text="请扫码:") #标签
l1.pack() #指定包管理器放置组件
user_text=tkinter.Entry() #创建文本框
user_text.focus_set()
user_text.pack()
Result_text=tkinter.Entry() #创建第二个文本框，用于存储结果。
Result_text.pack()


def CBwrong():
    if user_text.get() == '':
        tkinter.messagebox.showinfo('出错了~！', '请先扫描，再存入数据~！')
def CMwrong():
    if Result_text.get() == '':
        tkinter.messagebox.showinfo('出错了~！', '请先扫描，再存入数据~！')
def listout():
    tkinter.messagebox.showinfo('出错了~！', '这张表存满了！~')
def repete():
    tkinter.messagebox.showinfo('出错了~！', '该数据已存在！~')



def CreateBarCode():       #存条形码
    data = xlrd.open_workbook('BarCode.xls')
    table = data.sheets()[0]
    textcon=user_text.get()     #获取文本框内容
    CBwrong()
    nrows = table.nrows     # 获取行数
    Result=CheckValues(0, textcon)     #检查数据是否正确
    if Result==1:
        user_text.delete('0', 'end')
    else:
        worksheet.write(nrows, 0, textcon)
        workbook.save('BarCode.xls')
        print(textcon, '写入成功')
        user_text.delete('0', 'end')


def CreateMeasurement():        #存结果
    data = xlrd.open_workbook('BarCode.xls')
    table = data.sheets()[0]
    textRe=Result_text.get() #获取文本框内容
    CMwrong()
    row = 0
    result = CheckValues(3, textRe)
    if result ==1:
        Result_text.delete('0', 'end')
    else:
        list = table.col_values(3)      # 将目标列的值存入列表
        while '' in list:
            list.remove('')     #遍历列表，删除列表中的空元素
        ditnum = len(list)
        worksheet.write(ditnum, 3, textRe)      # 按列写入
        workbook.save('BarCode.xls')
        print(textRe,'写入成功')
        Result_text.delete('0', 'end')

def Find_list():        #获取扫码值到列表
    list = []
    for i in range(5):
        textcom = user_text.get()
        list.append(textcom)
        user_text.delete('0','end')
    print(list)
    return list

def Save_16():
    com = textarea.get(0.0,END)
    if com.strip() == '':
        tkinter.messagebox.showinfo('出错了~！', '请先扫描，再存入数据~！')
    else:
        NumList = com.split('\n')
        while '' in NumList:
            NumList.remove('')  # 遍历列表，删除列表中的空元素
        print('NumList',NumList)
        setNumlist = set(NumList)
        print('setNumlist',setNumlist)
        setNumlist = list(setNumlist)
        if len(NumList) != len(setNumlist):
            print('???')
            tkinter.messagebox.showinfo('出错了~！', '扫入数据有重复项，请检查！')
            textarea.delete(0.0,END)
        else:
            print('!!!')
            data = xlrd.open_workbook('BarCode.xls')
            table = data.sheets()[0]
            ExcelRowsNum = 1
            for Num in range(len(NumList)):
                worksheet.write(ExcelRowsNum,2, NumList[Num])  # 按列写入
                workbook.save('BarCode.xls')
                ExcelRowsNum += 1
            print('条形码保存成功！')


def CheckValues(RowNum,values):     #检查数据是否正确
    data = xlrd.open_workbook('BarCode.xls')
    table = data.sheets()[0]
    listValue = table.col_values(RowNum)
    for value in listValue:
        while  values == value:
            repete()
            return 1

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet("sheets1")
# TableHeads = ['条形码','设备类型号','工作模式','测量结果']
TableHeads = ['BarCode','Device type number','Work mode','Measurement result']

col = 0
for i in TableHeads:
    worksheet.write(0,col,i)
    col+=1

workbook.save('BarCode.xls')
tkinter.Button(ytm,text="存条码",command=CreateBarCode).pack() #command绑定获取文本框内容方法
tkinter.Button(ytm,text="存结果",command=CreateMeasurement).pack() #command绑定获取文本框内容方法
tkinter.Button(ytm,text="存入条形码",command=Save_16).pack() #command绑定获取文本框内容方法
textarea = tkinter.Text(ytm,height=16,width=30)
textarea.pack()



ytm.mainloop() #进入主循环
