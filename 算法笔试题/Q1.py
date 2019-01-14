from itertools import combinations
a = input("请输入9个数字,以逗号为间隔")
b = a.split(',')        #输入的数组
c = 0       #输入9个数的和
lt = []
for x in b:
    lt.append(int(x))

# for x in lt:
#     c += x
c = sum(lt)

d = c/3     #每行值之和
e = d/3     #中值
status = False

for x in lt:
    if x == e:
        status = True

def hang(l):            #全排列，然后再遍历？
    zui_li = []
    hangli = list(combinations(l, 3))   #列出全部组合
    for x in hangli:
        if x[0]+x[1]+x[2]==d:
            # print(x)
            zui_li.append(x)
    return zui_li

if(status):
    ll_list = hang(lt)

    ll_list1 = []
    ll_2 = []
    ll_3 = []
    jiao_li=[]
    result = [[0,0,0],[0,0,0],[0,0,0]]

    if len(ll_list)>=8:
        for x in ll_list:
            ll_list1 += x

        for x in lt:
            if ll_list1.count(x)==2:
                ll_2.append(x)
            if ll_list1.count(x) == 3:
                ll_3.append(x)
        ll_3.append(e)

        for x in ll_list:
            aa_li = [i for i in ll_3 if i not in x]
            if len(aa_li)==2:
                jiao_li += aa_li

        result[1][1]=e
        result[0][0]=jiao_li[0]
        result[2][2] = jiao_li[1]
        result[0][2] = jiao_li[2]
        result[2][0] = jiao_li[3]
        result[0][1] = d - result[0][0]-result[0][2]
        result[1][0] = d - result[0][0]-result[2][0]
        result[1][2] = d - result[0][2]-result[2][2]
        result[2][1] = d - result[2][0]-result[2][2]
        print('ok')

    else:
        print('无解')
else:
    print('无解')
