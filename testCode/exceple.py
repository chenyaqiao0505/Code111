import xlwt

workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('test', cell_overwrite_ok=True)
# 生成sheet：test，如下图1：
data = {
    "1": [u"张三", 150, 120, 100],
    "2": ["wang", 90, 99, 95],
    "3": ["wu", 60, 66, 68] }
num = [a for a in data]
ldata = []
num.sort()
for x in num:
    t = [int(x)]
    for a in data[x]:
        t.append(a)

    ldata.append(t)
for i, p in enumerate(ldata):
    for j, q in enumerate(p):
        sheet1.write(i, j, q)
    workbook.save('E:\\test3.xls')
print('ok')