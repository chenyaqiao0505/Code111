import xlrd
import os
import xlwt
from xlutils.copy import copy
from tkinter import *

file_dir = 'C:\\Users\\admin\\Desktop\\Excel'

def get_allfile_msg(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return root, dirs, files

root, dirs, files = get_allfile_msg(file_dir)
def get_allfile_url(root, files):
    i = 0       #文件数量
    allFile_url = []
    for f in files:
        i += 1
        if i == len(files):
            break
        file_url = root + '\\' + f
        allFile_url.append(file_url)
    return allFile_url

allFile_url = get_allfile_url(root, files)

def all_to_one(root, allFile_url, file_name='allExcel.xls', title=None):
    file_name = root + '\\' + file_name
    create_excel(file_name, title)

    list_row_data = []
    for f in allFile_url:
        e1.insert(END,'打开%s' % f,'\n','\n')
        excel = xlrd.open_workbook(f)
        table = excel.sheet_by_index(0)
        e1.insert(END,'该文件行数为：%d，列数为：%d' % (table.nrows,table.ncols),'\n','\n')
        for i in range(table.nrows):
            if i == 0:
                # i += 1
                continue
            row = table.row_values(i)
            list_row_data.append(row)

    e1.insert(END,'总数据量为%d' % len(list_row_data),'\n','\n')
    add_row(list_row_data, file_name)


def create_excel(file_name, title):
    e1.insert(END,'创建文件%s' % file_name,'\n','\n')
    a = xlwt.Workbook()
    table = a.add_sheet('sheet1', cell_overwrite_ok=True)
    for i in range(len(title)):
        table.write(0, i, title[i])
    a.save(file_name)
file_name = 'DO测试数据汇总.xls'
title = ['条码内容','故障通道']

def add_row(list_row_data, file_name):
    allExcel1 = xlrd.open_workbook(file_name)
    sheet = allExcel1.sheet_by_index(0)
    allExcel2 = copy(allExcel1)
    sheet2 = allExcel2.get_sheet(0)
    i = 0
    for row_data in list_row_data:
        for j in range(len(row_data)):
            sheet2.write(sheet.nrows + i, j, row_data[j])
        i += 1      #覆盖原文件
    allExcel2.save(file_name)
    e1.insert(END,'合并完成','\n','\n')

win = Tk()
win.title('Excel数据汇总')
btu = Button(win,text = '开始汇总',command = lambda :all_to_one(root, allFile_url, file_name=file_name, title=title)).grid(row=2, column=0,pady=5)
e1 = Text(win,width=50,height=25,bg = 'green')
e1.grid(row=1, column=0,pady=5)

win.resizable(0, 0)  # 阻止Python GUI的大小调整
win.mainloop()

e1.insert(END,'当前目录路径:',root,'当前路径下所有子目录',dirs,'当前路径下所有非目录子文件 ',files)
