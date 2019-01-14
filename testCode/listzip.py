'''
列表压缩操作
注：zip()的结果是一个可迭代的zip类对象。并不是二维列表
'''

resultlist = ['pass1', 'pass2', 'pass3', 'pass4', 'pass5',
        'pass6', 'pass7', 'pass8', 'pass9', 'pass10',
        'pass11', 'pass12', 'pass13', 'pass14', 'pass15',
        'pass16', 'pass17', 'pass18', 'pass19', 'pass20',
        'pass21', 'pass22', 'pass23', 'pass24', 'pass25',
        'pass26', 'pass27', 'pass28', 'pass29', 'pass30',
        'pass31', 'pass32', 'pass33', 'pass34', 'pass35',
        'pass36', 'pass37', 'pass38', 'pass39']

print(len(resultlist))
list0 = []
for i in range(0,len(resultlist),2):
    list0.append(resultlist[i])


list1 = []
for j in range(1,len(resultlist),2):
    list1.append(resultlist[j])
list1.append(None)

l = []
for j,k in zip(list0,list1):
    l.append(str(j)+'|'+str(k))
print(l)

print(list1,len(list1))

list2=[]
heng=zip(list0,list1)
for i in heng:
    list2.append(i)

print(list2[5])


