import xlrd
import xlwt
import csv


def writecsv():
    filename = u'C:\\Users\\admin\\Desktop\\mycode\\sale.orderok.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        OneRow = rows[0]
        # print(OneRow)
        writecsv = open('test.csv', 'w',newline='')
        write = csv.writer(writecsv)
        write.writerow(OneRow)
        print("写文件完成！")

def readexcel():
    data = xlrd.open_workbook(u'订单行项汇总5月.xls')  # 打开excel
    table = data.sheets()[0]    # 打开第一张表
    nrows = table.nrows     # 获取表行数
    ncols = table.ncols     #获取表列数


    # readlist = []
    writecsv = open('test1.csv', 'w', newline='')
    write = csv.writer(writecsv)
    for i in range(nrows):
        # print(table.row_values(i))
        # 遍历全部元素，用的是row_values()
        # print(table.row_values(i+1))
        # readlist.append(table.row_values(i+1))    #将excel中的内容存到readlist中
        write.writerow(table.row_values(i))

    print('写入成功！')


    # writecsv = open('test1.csv', 'w', newline='')
    # print(readlist)

        # 输出行元素
        # cell_a1 = table.cell(0, 0).value      #输出单元格(1,1)
        # rows = sheet2.row_values(3)     #第四行的元素
        # 获取单元格内容
        # table(rowx,colx)(行，列)
        # print(cell_a1)
        # cell_f11 = table.cell(10, 5).value
        # print(cell_f11)


    # datas = [['name', 'age'],
    #          ['Bob', 14],
    #          ['Tom', 23],
    #          ['Jerry', '18']]
    #
    # with open('example.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)
    #     for row in datas:
    #         writer.writerow(row)

if __name__ == '__main__':
    readexcel()