# from tkinter import *
#
# master = Tk()
#
# def test():
#     if e1.get() == '我爱学习':
#         print('继续努力！')
#         return True
#     else:
#         print('你在说什么鬼话')
#         e1.delete(0, END)
#         return False
#
#
# v = StringVar()
#
# e1 = Entry(master, textvariable=v, validate='focusout', validatecommand=test)  #当焦点移出的时候调用validatecommand设置的函数test
# e2 = Entry(master)
# e1.pack(padx=10, pady=10)
# e2.pack(padx=10, pady=10)
#
# mainloop()


class Solution(object):
    def twoSum(self, nums, target):
        # 定义一个字典
        d={}
        # 设置一个变量
        size=0
        # 当size小于列表nums的长度的时候，进行循环
        while size < len(nums):
            # 如果target减去nums的第size个值属于d的时候
            if target-nums[size] in d:
                # 如果字典d中的第（target-nums[size])个值小于size的时候
                if d[target-nums[size]] < size:
                    # 返回列表[d[target-nums[size]],size]
                    return [d[target-nums[size]],size]
            else:
                或者d的（nums中的第size个值）等于size
                d[nums[size]] = size

            size = size + 1
