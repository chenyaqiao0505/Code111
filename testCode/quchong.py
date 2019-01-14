l=[[1,2,3,4],[4,5,6],[1,2,3,4]]


for i in range(len(l)):
    print('i',i)
    for j in range(i+1,len(l)):
        print('j', j)
        if l[i] == l[j]:
            print('delete')
            l.remove(l[j])
print(l)

# bol = True
# bol = (l[0] ==l[2])
# print(bol)