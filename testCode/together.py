import xlrd
import xlwt
import csv


def readwrite():
    data = xlrd.open_workbook(u'订单行项汇总5月.xls')  # 打开excel
    table = data.sheets()[0]  # 打开第一张表
    nrows = table.nrows  # 获取表行数
    ncols = table.ncols  # 获取表列数
    readlist = []
    for i in range(nrows):
        # print(table.row_values(i))
        # 遍历全部元素，用的是row_values()
        # print(table.row_values(i+1))
        readlist.append(table.row_values(i))
    writecsv = open('test.csv', 'w',newline='')
    write = csv.writer(writecsv)
    write.writerows(readlist)
    print("写文件数据完成！")

    filename = u'C:\\Users\\admin\\Desktop\\mycode\\sale.orderok.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        OneRow = rows[0]
        # print(OneRow)
        writecsv = open('test.csv', 'w',newline='')
        write = csv.writer(writecsv)
        write.writerow(OneRow)
        print("写文件头部完成！")

if __name__ == '__main__':
    readwrite()