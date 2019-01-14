import random
from itertools import combinations

possible = []		#未来10天的价格
Price = []              #差价列表
for x in range(10):
    possible.append(random.randint(10,100))        #写出来10个随机数

print('估算出来的价格是：',possible)
Price_list = []		

for x in range(1,10):
    Price.append(possible[x]-possible[x-1])     #后一天减前一天存入列表
for x in range(0,10):
    for y in range(x,10):
        a = possible[y]-possible[x]
        Price_list.append([x,y,a])
        print(str(y)+'天和'+str(x)+'天的利润差为'+str(a))


Price_zheng = []
print(Price_zheng)
for val in Price_list:
    if(val[2]>0):
        print(val[2])
        Price_zheng.append(val)

print(Price_zheng)
zh_li = list(combinations(Price_zheng, 2))
print(zh_li)
zuizhong_li = []
for val in zh_li:
    if val[1][0]>val[0][1]:
        zuizhong_li.append(val)

print(zuizhong_li)
zuidalirui = 0
zuida_li = []
for x in zuizhong_li:
    if (x[0][2]+x[1][2])>zuidalirui:
        zuidalirui = x[0][2]+x[1][2]
        zuida_li = x
print(str(zuida_li[0][0])+'天买入,'+str(zuida_li[0][1])+'天卖出,然后'+str(zuida_li[1][0])+'天买入,'+str(zuida_li[1][1])+'天卖出')
print('最大利润为:'+str(zuidalirui))
