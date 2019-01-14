'''
冒泡
每个数据都需要排列，i表示当前位置元素
j表示的是列表下标，第j个元素需要对比元素个数，n-1-i表示每行需要对比的最多次数，时间复杂度为O(n²)
'''
# def bubbleSort(list,n):
#     if n <= 1:
#         return list
#     for i in range(n):  #表示行
#         flag = False        #表示是否有数据交换
#         for j in range(n-1-i):  #表示每行的下标
#             if list[j] > list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]
#                 flag = True
#         if flag == False:
#             break
#     return list

# list = [8,1,9,3,4,2,6,7]
# n = len(list)
#
# f = bubbleSort(list,n)
# print(f)

def bubbleSort(ll):
    if len(ll) <= 1:
        return ll
    for i in range(len(ll)):
        for j in range(len(ll)-i-1):
            if ll[j] > ll[j+1]:
                ll[j],ll[j+1] = ll[j+1],ll[j]
    return ll

ll = [8,1,9,3,4,2,6,7]
n = len(ll)

f = bubbleSort(ll)
print(f)
