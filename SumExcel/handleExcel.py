import xlwt
import xlrd

file_dir = 'E:\\Foxmail\\20181119发货输出板卡测试记录\\20181115'
file_name = 'DO测试数据汇总.xls'


data = xlrd.open_workbook(file_dir+'\\'+file_name)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols

first_ncol = []
second_ncol = []
thrid_ncol = []

for i in range(1,nrows):
    first_ncol_value = table.cell(i, 0).value
    first_ncol.append(first_ncol_value)

for j in range(1,nrows):
    second_ncol_value = table.cell(j,1).value
    second_ncol.append(second_ncol_value)

for k in range(1,nrows):
    thrid_ncol_value = table.cell(k,2).value
    thrid_ncol.append(thrid_ncol_value)

clear_code_list = []
clear_result_list = []
clear_time_list = []

for x,y,z in zip(first_ncol,second_ncol,thrid_ncol):
    if x not in clear_code_list and y == 'PASS' and x.startswith('A'):
        clear_code_list.append(x)
        clear_result_list.append(y)
        clear_time_list.append(z)

final_file_name = 'DO测试数据清洗版.xls'
title = ['条码内容', '故障通道','测试时间']
a = xlwt.Workbook()
table = a.add_sheet('sheet1', cell_overwrite_ok=True)
#写表头
for i in range(len(title)):
    table.write(0, i, title[i])
#写内容
for code_value,result_value,time_value in zip(range(len(clear_code_list)),range(len(clear_result_list)),range(len(clear_time_list))):
    table.write(code_value+1,0, clear_code_list[code_value])
    table.write(result_value+1,1, clear_result_list[code_value])
    table.write(time_value+1,2, clear_time_list[code_value])

a.save(file_dir+'\\'+final_file_name)
print('数据清洗完成~！')