'''
原理同插入排序。也分已拍区间和未拍区间，选择排序会从每次未排序的区间中找到最小元素，将其放到已排序区间末尾
选择排序刚开始没有已排序，找到最小元素，放到开始。或者末尾.时间复杂度为O(n²)
'''
# def selectionSort(list):
#     if len(list) <= 1:
#         return list
#
#     for i in range(len(list)-1):
#         min_index = i       #记录最小位置
#         for j in range(i+1,len(list)):
#             if list[j] < list[min_index]:
#                 min_index = j
#         if min_index != i:
#             list[i],list[min_index] = list[min_index],list[i]
#     return list
#
# list1 = [1,9,4,23,11,56,8,43,6,7]
# print(list1)
# a = selectionSort(list1)
# print(a)


def selectionSort(l):
    if len(l) <= 1:
        return l
    for i in range(len(l)-1):
        min_index = i
        for j in range(i+1,len(l)):
            if l[j] < l[min_index]:
                min_index = j
        if min_index != i:
            l[i],l[min_index] = l[min_index],l[i]
    return l
list1 = [1,9,4,23,11,56,8,43,6,7]
print(list1)
a = selectionSort(list1)
print(a)
