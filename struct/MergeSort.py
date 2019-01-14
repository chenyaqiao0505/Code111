'''
如果要排序一个数组，我们先把数组从中间分成前后两部分，然后对前后两部分分别排序，再将排好序的两部分合并在一起，这样整个数组就都有序了

首先归并排序使用了二分法，归根到底的思想还是分而治之。拿到一个长数组，将其不停的分为左边和右边两份，然后以此递归分下去。
然后再将她们按照两个有序数组的样子合并起来。O(nlogn)

'''
# def merge(a, b):        #接受两个列表
#     c = []      #定义了一个新列表
#     h = j = 0   #两个变量
#     while j < len(a) and h < len(b):    #当j<列表a的长度。当h小于列表b的长度
#         if a[j] < b[h]:         #如果a的j小于b的h，c添加a[j]，j再+1
#             c.append(a[j])
#             j += 1
#         else:
#             c.append(b[h])      #反言之c添加b[h]，h+1
#             h += 1
#
#     if j == len(a): #当j到a的末尾了
#         for i in b[h:]:     #列表c添加列表b从h位到末尾的值
#             c.append(i)
#     else:
#         for i in a[j:]:     #反之列表c添加列表a从j位到末尾的值
#             c.append(i)
#
#     return c
#
# def merge_sort(lists):
#     if len(lists) <= 1:
#         return lists
#     middle = len(lists)//2  #将列表分成两份，放到merge中
#     left = merge_sort(lists[:middle])
#     right = merge_sort(lists[middle:])
#     return merge(left, right)
#
# if __name__ == '__main__':
#     a = [14, 2, 34, 43, 21, 19]
#     print(a)
#     print (merge_sort(a))


def merge(a,b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i == len(a):
        for _ in b[j:]:
            c.append(_)
    else:
        for _ in a[i:]:
            c.append(_)
    return c

def fen(l):
    if len(l) <= 1:
        return l
    middle = len(l)//2
    left = fen(l[:middle])
    right = fen(l[middle:])
    return merge(left,right)
if __name__ == '__main__':
    a = [14, 2, 34, 43, 21, 19]
    print(a)
    print(fen(a))
