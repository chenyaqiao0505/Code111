'''
将列表中的数据分成两个区间，已排序区间和为排序区间。初始已排序区间只有一个元素，就是第一个。
取未排序区间元素，分别向已排序区间里插入，并且保证已排序区间元素永远排序。重复这个过程，直到未排序为空，算法结束


插入排序的工作方式像许多人排序一手扑克牌.开始时,我们的左手为空并且桌子上的牌面向下.然后,我们每次从桌子上拿走一张牌并将它插入左手中正确的位置.
为了找到一张牌的正确位置,我们从右向左将它与已在手中的每张牌进行比较,拿在左手中的牌总是排序好的.

时间复杂度为O(n²)
'''

def insertSort(list,n):
    if n <= 1:
        return list
    for i in range(1,n):        #未排序区间
        value = list[i]
        for j in range(i,-1,-1):    #排序过程
            if value < list[j-1]:       #如果value小于它前面的数。
                list[j] = list[j-1]     #就和它前面的数字换位置
            else:       #若没有，表示当前value为已排序区间最大值
                break
        list[j] = value
    return list

list1 = [1,9,4,23,11,56,8,43,6,7]
print(list1)
n = len(list1)

a = insertSort(list1,n)
print(a)

def insertSort(ll):
    if len(ll) <= 1:
        return ll
    for i in range(1,len(ll)):
        value = list[i]
        for j in range(i,-1,-1):