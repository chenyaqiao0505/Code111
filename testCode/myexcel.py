import xlrd
import xlwt
import csv


def WriteExcel():
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建Excel
    worksheet = workbook.add_sheet('myworksheet')
    # 创建工作表
    # worksheet.write(0,0,label = '嗨~！')
    for i in OneRow(0, len(OneRow)):
        worksheet.write(0, i, OneRow[i])
    # 单元格创建内容
    workbook.save('myexcel.xls')
    # 保存
    print('创建成功！')

def ReadExcel():
    data = xlrd.open_workbook(u'订单行项汇总5月.xls')
    # 打开excel
    table = data.sheets()[0]
    # 打开第一张表
    nrows = table.nrows
    # 获取表行数
    ncols = table.ncols
    # 获取表列数
    for i in range(ncols):
        #     print(table.row_values(i))
        # 遍历全部元素，用的是row_values()
        print(table.col_values(i)[:1])
        输出行元素
        cell_a1 = table.cell(0, 0).value
        # 获取单元格内容
        # table(rowx,colx)(行，列)
        print(cell_a1)
        cell_f11 = table.cell(10, 5).value
        print(cell_f11)

    # worksheet.write(m_row, m_col, u'内容', body_style())
#  # 合并单元格，前四个参数分别是起止的行列位置
# worksheet.write_merge(1, 2, m_col, m_col+3, u'还好', body_style())

def MyConnection():
        # reader = []
        # with open('sale.orderok.csv','r') as f:
        #     reader.append(csv.reader(f))
    with open('sale.orderok.csv', 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        # print(rows[0])
    OneRow = rows[0]

    workbook = xlwt.Workbook(encoding='utf-8')
        #创建Excel
    worksheet1 = workbook.add_sheet('myworksheet')
        #创建工作表
        # worksheet.write(0,0,label = '嗨~！')
    col = 0
    for i in OneRow:
        worksheet1.write(0,col,i)
        col+=1
        #单元格创建内容
    workbook.save('myexcel.xls')
        #保存
    print('创建成功！')

if __name__ == '__main__':
    MyConnection()
        # print(OneRow)

# a = MyExcel()
# a.MyConnection()
# a.WriteExcel()
