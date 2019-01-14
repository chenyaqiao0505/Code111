import xlwt
import xlrd
import csv
import os

def  readexcel():
    data = xlrd.open_workbook(u'订单行项汇总5月.xls')  # 打开excel
    table = data.sheets()[0]  # 打开第一张表
    nrows = table.nrows  # 获取表行数
    ncols = table.ncols  # 获取表列数
    rightcol = []
    for i in range(nrows):
        # print(table.row_values(i))
        rightcol.append(table.row_values(i))

    workbook = xlwt.Workbook()
    xlsheet = workbook.add_sheet('myworksheet')

    for i, p in enumerate(rightcol):
        for j, q in enumerate(p):
            xlsheet.write(i, j, q)
        workbook.save('writein.xls')
    print('写入成功~!')


def judje():

    headlist = ['order_line/product_id/id','order_line/name','order_line/product_uom_qty',
    'order_line/create_date','pricelist_id/id','warehouse_id/id','partner_id/id','client_order_ref']
    workbook = xlwt.Workbook(encoding='utf-8')      #创建Excel表
    worksheet = workbook.add_sheet('myworksheet')      #创建工作表

    col = 0
    for i in headlist:
        worksheet.write(0, col, i)
        col += 1
        # 单元格创建内容
    workbook.save('16_27.xls')
    # 保存
    print('创建成功！')
    table = xlrd.open_workbook(u'16_27.xls')  # 打开excel
    worksheet2 = table.sheets()[0]  # 打开第一张表
    nrows = worksheet2.nrows  # 获取表行数
    ncols = worksheet2.ncols  # 获取表列数


    data = xlrd.open_workbook(u'订单行项汇总5月.xls')  # 打开excel
    table = data.sheets()[0]  # 打开第一张表
    nrows = table.nrows  # 获取表行数
    ncols = table.ncols  # 获取表列数


#worksheet1 创建的表
#table      数据源表
    for j in range(ncols):
        if worksheet2.cell(0,j).value == headlist[2]:
            for o in range(1,nrows):
                worksheet2.cell(j,o).value=table.cell(o,5).value
print('导入成功')

if __name__ == '__main__':
    judje()
