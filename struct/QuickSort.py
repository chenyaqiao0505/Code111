'''
快速排序
1、 算法描述：

1．先从数列中取出一个数作为基准数。

2．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。

3．再对左右区间重复第二步，直到各区间只有一个数。

时间复杂度：O(nlgn)
'''
import random
def getrandata(num):
    a = []
    i = 0
    while i <num:
        a.append(random.randint(0,100))
        i += 1
    return a

#
# def quicksort(num_list):
#     lenth = len(num_list)
#     if lenth <= 1:
#         return num_list
#     temp = random.randint(0,lenth-1)# 随便取的一个数，作为列表索引
#     tempval = num_list[temp]
#     left = []
#     right = []
#     for i in range(0,lenth):
#         if num_list[i] > tempval:
#             right.append(num_list[i])
#         else:
#             left.append(num_list[i])
#     return quicksort(left)+quicksort(right)

#
# if __name__ == '__main__':
#     a = getrandata(10)
#     print(a)
#     b = quicksort(a)
#     print(b)
def quicksort(l):
    if len(l) <= 1:
        return l
    indexval = random.randint(0,len(l)-1)
    val = l[indexval]
    left = []
    right = []
    for i in l:
        if i < val:
            left.append(i)
        else:
            right.append(i)
    return quicksort(left)+quicksort(right)
if __name__ == '__main__':
    a = getrandata(10)
    print(a)
    b = quicksort(a)
    print(b)