# from tkinter import *
#
# master = Tk()
#
# def test():
#     if e1.get() == '�Ұ�ѧϰ':
#         print('����Ŭ����')
#         return True
#     else:
#         print('����˵ʲô��')
#         e1.delete(0, END)
#         return False
#
#
# v = StringVar()
#
# e1 = Entry(master, textvariable=v, validate='focusout', validatecommand=test)  #�������Ƴ���ʱ�����validatecommand���õĺ���test
# e2 = Entry(master)
# e1.pack(padx=10, pady=10)
# e2.pack(padx=10, pady=10)
#
# mainloop()


class Solution(object):
    def twoSum(self, nums, target):
        # ����һ���ֵ�
        d={}
        # ����һ������
        size=0
        # ��sizeС���б�nums�ĳ��ȵ�ʱ�򣬽���ѭ��
        while size < len(nums):
            # ���target��ȥnums�ĵ�size��ֵ����d��ʱ��
            if target-nums[size] in d:
                # ����ֵ�d�еĵڣ�target-nums[size])��ֵС��size��ʱ��
                if d[target-nums[size]] < size:
                    # �����б�[d[target-nums[size]],size]
                    return [d[target-nums[size]],size]
            else:
                ����d�ģ�nums�еĵ�size��ֵ������size
                d[nums[size]] = size

            size = size + 1
