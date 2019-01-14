'''
  该段代码作用是使用实现tkinter来操作excel表格的追加操作
'''


import xlrd
import xlwt
from xlutils.copy import copy

def write_excel(path, sheet_name, value):#写表头
  index = len(value)
  workbook = xlwt.Workbook()
  sheet = workbook.add_sheet(sheet_name)
  for i in range(0, index):
    for j in range(0, len(value[i])):
      sheet.write(i, j, value[i][j])
  workbook.save(path)
  print("写入表头成功！")

def write_excel_append(path, value):#追加
  index = len(value)
  workbook = xlrd.open_workbook(path)
  sheets = workbook.sheet_names()
  worksheet = workbook.sheet_by_name(sheets[0])
  rows_old = worksheet.nrows
  new_workbook = copy(workbook)
  new_worksheet = new_workbook.get_sheet(0)
  for i in range(0, index):
    for j in range(0, len(value[i])):
      new_worksheet.write(i + rows_old, j, value[i][j])
  new_workbook.save(path)

if __name__ == '__main__':

  book_name = 'Result.xls'
  sheet_name = 'sheet1'
  value_title = [['条形码','工作模式','是否通过','测试电压','测试电流','时间']]

  ss ='ACW,PASS,1.500Kv,0.019mA,T=002.0s'   #接受结果
  num = '413213543251,'   #接受条形码
  s1 = num+ss
  value1 = [(s1.split(','))]
  try:
    # write_excel(book_name, sheet_name, value_title)   #开始写表格
    write_excel_append(book_name, value1)   #追加具体操作
  except Exception as ex:
    print('请关掉Excel再试一次！')
