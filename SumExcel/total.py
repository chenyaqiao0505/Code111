import xlrd
import os
import xlwt
from xlutils.copy import copy
from tkinter import *
import re



class mygui:
    def __init__(self):
        self.file_dir = self.getuser()#'E:\\Foxmail\\20181119发货输出板卡测试记录\\20181114'
        self.root, self.dirs, self.files = self.get_allfile_msg(self.file_dir)
        self.allFile_url = self.get_allfile_url(self.root, self.files)
        self.win = Tk()
        self.win.title('Excel数据汇总')
        self.win.geometry('300x400')
        self.e1 = Text(self.win, width=50, height=25, bg='green')
        self.e1.place(height=300, width=400)
        self.e1.insert(END, '文件数量:', )
        self.e1.insert(END, sum_files, '\n', '\n')
        self.btu = Button(self.win, text='开始汇总', command=lambda: gui.all_to_one(gui.root,
                                                                      gui.allFile_url,
                                                                      file_dir=gui.file_dir,
                                                                      files=gui.files,
                                                                      file_name=gui.file_name,
                                                                      title=gui.title))
        self.btu.place(x=200, y=370)

        self.valuebtu = Button(self.win, text="写入地址", command=gui.getuser)
        self.valuebtu.place(x=200, y=340)

        label1 = Label(self.win, text='请将文件夹地址复制到文本框内:')
        label1.place(x=10, y=310)


    def getuser(self):
        url_value = user_text.get()  # 获取文本框内容
        print(url_value)
        return url_value


    def get_allfile_msg(self, file_dir):
        for root, dirs, files in os.walk(file_dir):
            return root, dirs, files

    # root, dirs, files = get_allfile_msg(file_dir)

    def get_allfile_url( self,root, files):
        allFile_url = []
        for f in files:
            file_url = root + '\\' + f
            allFile_url.append(file_url)
        return allFile_url

    # allFile_url = get_allfile_url(root, files)

    def all_to_one(self,root, allFile_url, file_dir,files, file_name, title=None):
        file_name = root + '\\' + file_name
        self.create_excel(file_name, title)

        list_row_data = []
        for f in allFile_url:
            e1.insert(END, '打开%s' % f, '\n', '\n')
            excel = xlrd.open_workbook(f)
            table = excel.sheet_by_index(0)
            e1.insert(END, '该文件行数为：%d，列数为：%d' % (table.nrows, table.ncols), '\n', '\n')
            for i, j in zip(range(table.nrows), files):
                if i == 0:
                    # i += 1
                    continue
                row = table.row_values(i)
                k = re.sub("\D","",j)
                row.append(k)
                list_row_data.append(row)

        e1.insert(END, '总数据量为%d' % len(list_row_data), '\n', '\n')
        self.add_row(list_row_data, file_name)
        self.clear_data(file_dir,file_name)


    def create_excel(self,file_name, title):
        self.e1.insert(END, '创建文件%s' % file_name, '\n', '\n')
        a = xlwt.Workbook()
        table = a.add_sheet('sheet1', cell_overwrite_ok=True)
        for i in range(len(title)):
            table.write(0, i, title[i])
        a.save(file_name)

    file_name = 'DO测试数据汇总.xls'
    title = ['条码内容', '故障通道','测试时间']

    def add_row(self,list_row_data, file_name):
        allExcel1 = xlrd.open_workbook(file_name)
        sheet = allExcel1.sheet_by_index(0)
        allExcel2 = copy(allExcel1)
        sheet2 = allExcel2.get_sheet(0)
        i = 0
        for row_data in list_row_data:
            for j in range(len(row_data)):
                sheet2.write(sheet.nrows + i, j, row_data[j])
            i += 1  # 覆盖原文件
        allExcel2.save(file_name)
        self.e1.insert(END, '合并完成', '\n', '\n')

    def clear_data(self,file_dir,file_name):
        # file_dir + '\\' +
        data = xlrd.open_workbook( file_name)
        table = data.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols

        first_ncol = []
        second_ncol = []
        thrid_ncol = []

        for i in range(1, nrows):
            first_ncol_value = table.cell(i, 0).value
            first_ncol.append(first_ncol_value)

        for j in range(1, nrows):
            second_ncol_value = table.cell(j, 1).value
            second_ncol.append(second_ncol_value)

        for k in range(1, nrows):
            thrid_ncol_value = table.cell(k, 2).value
            thrid_ncol.append(thrid_ncol_value)

        clear_code_list = []
        clear_result_list = []
        clear_time_list = []

        for x, y, z in zip(first_ncol, second_ncol, thrid_ncol):
            if x not in clear_code_list and y == 'PASS' and x.startswith('A'):
                clear_code_list.append(x)
                clear_result_list.append(y)
                clear_time_list.append(z)

        final_file_name = 'DO测试数据清洗版.xls'
        title = ['条码内容', '故障通道', '测试时间']
        a = xlwt.Workbook()
        table = a.add_sheet('sheet1', cell_overwrite_ok=True)
        # 写表头
        for i in range(len(title)):
            table.write(0, i, title[i])
        # 写内容
        for code_value, result_value, time_value in zip(range(len(clear_code_list)), range(len(clear_result_list)),
                                                        range(len(clear_time_list))):
            table.write(code_value + 1, 0, clear_code_list[code_value])
            table.write(result_value + 1, 1, clear_result_list[code_value])
            table.write(time_value + 1, 2, clear_time_list[code_value])

        a.save(file_dir + '\\' + final_file_name)
        self.e1.insert(END,'数据清理完毕~!','\n', '\n')

gui = mygui()
# win = Tk()
user_text = Entry(gui.win, width=25)
user_text.place(x = 10,y = 340)

# file_dir = getuser()
# win = Tk()
# win.title('Excel数据汇总')
# win.geometry('300x400')
# e1 = Text(win, width=50, height=25, bg='green')
# e1.place(height = 300,width = 400)
sum_files = len(gui.get_allfile_url(gui.root,gui.files))
# e1.insert(END, '文件数量:', )
# e1.insert(END,sum_files,'\n', '\n')
# valuebtu = Button(win, text="写入地址", command=gui.getuser)
# valuebtu.place(x=200, y=340)
#
#
# label1 = Label(win, text='请将文件夹地址复制到文本框内:')
# label1.place(x=10, y=310)

# user_text = Entry(win, width=25)
# user_text.place(x = 10,y = 340)

# btu = Button(win, text='开始汇总',command=lambda: gui.all_to_one(gui.root,
#                                                              gui.allFile_url,
#                                                              file_dir=gui.file_dir,
#                                                              files=gui.files,
#                                                              file_name=gui.file_name,
#                                                              title=gui.title))
# btu.place(x=200, y=370)

win.resizable(0, 0)  # 阻止Python GUI的大小调整
win.mainloop()

e1.insert(END, '当前目录路径:', gui.root, '当前路径下所有子目录', gui.dirs, '当前路径下所有非目录子文件 ', gui.files)
