import os
import re
import xlrd
import xlwt
from xlutils.copy import copy

class HandleExcel:
    def __init__(self):
        self.root = ''
        self.dir = ''
        self.files = ''
        self.allFile_url = ''
        self.final_file_name = '测试数据清洗版.xls'
        self.title = ['条码内容', '故障通道', '测试时间']
        self.file_name = '测试数据汇总.xls'

    def get_allfile_msg(self,file_dir):
        for root, dirs, files in os.walk(file_dir):
            return root, dirs, files

    def get_allfile_url(self,root, files):
        allFile_url = []
        for f in files:
            file_url = root + '\\' + f
            allFile_url.append(file_url)
        return allFile_url

    def all_to_one(self,root, allFile_url, files, file_name='allExcel.xls', title=None):
        file_name = root + '\\' + file_name
        self.create_excel(file_name, title)

        list_row_data = []
        for f in allFile_url:
            excel = xlrd.open_workbook(f)
            table = excel.sheet_by_index(0)
            for i, j in zip(range(table.nrows), files):
                if i == 0:
                    continue
                row = table.row_values(i)
                k = re.sub("\D", "", j)
                row.append(k)
                list_row_data.append(row)
        self.add_row(list_row_data, file_name)

    def create_excel(self,file_name, title):
        a = xlwt.Workbook()
        table = a.add_sheet('sheet1', cell_overwrite_ok=True)
        for i in range(len(title)):
            table.write(0, i, title[i])
        a.save(file_name)

    file_name = '测试数据汇总.xls'
    title = ['条码内容', '故障通道', '测试时间']

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

    def clear_excel(self,file_dir,file_name):
        data = xlrd.open_workbook(file_dir + '\\' + file_name)
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
            if x not in clear_code_list and y == '\'PASS\'' or y == 'PASS' and x.startswith('A'):
                clear_code_list.append(x)
                clear_result_list.append(y)
                clear_time_list.append(z)


        a = xlwt.Workbook()
        table = a.add_sheet('sheet1', cell_overwrite_ok=True)
        # 写表头
        for i in range(len(self.title)):
            table.write(0, i, self.title[i])
        # 写内容
        for code_value, result_value, time_value in zip(range(len(clear_code_list)), range(len(clear_result_list)),
                                                        range(len(clear_time_list))):
            table.write(code_value + 1, 0, clear_code_list[code_value])
            table.write(result_value + 1, 1, clear_result_list[code_value])
            table.write(time_value + 1, 2, clear_time_list[code_value])

        a.save(file_dir + '\\' + self.final_file_name)
