'''
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
'''
class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        standard = {5,10,20}
        if bills == None | bills[0] != 5 and set(bills) not in standard:
            return False
        remain = 5
        for i in range(len(bills)-1):
            if bills[i] == 5:
                remain += 5
            elif bills[i] == 10:
                if bills[i] <= remain or bills[i] - remain == 5:
                    remain += 5
                else:
                    return False
            elif bills[i] == 20:
                if bills[i] <= remain or bills[i] - remain == 5:
                    remain += 5
                else:
                    return False

a = Solution()
list = [5,5,10,10,20]
print(a.lemonadeChange(list))


class Solution:
    def lemonadeChange(self, bills):
        if not bills: return True
        count = [0, 0]

        # 如果给5元就拿过来，如果给10元则找5元，如果给20元则找回3个5元或者1个5元1个10元
        # for item in bills:
        #     if item == 5:
        #         count[0] += 1
        #     elif item == 10:  # 此时需要找还5元
        #         if count[0] > 0:  # 5元的还有
        #             count[0] -= 1
        #             count[1] += 1
        #         else:
        #             return False
        #     elif item == 20:  # 找回3个5元或者1个5元1个10元
        #         if count[1] > 0 and count[0] > 0:
        #             count[1] -= 1
        #             count[0] -= 1
        #         elif count[0] >= 3:
        #             count[0] -= 3
        #         else:
        #             return False
        # return True

        for item in bills:
            if item == 5:
                count[0] += 1
            elif item == 10:
                if count[0] > 0:
                    count[0] -= 1
                    count[1] += 1
                else:
                    return False
            elif item == 20:
                if count[1] > 0 and count[0] > 0:
                    count[1] -= 1
                    count[0] -= 1
                elif count[0] >= 3:
                    count[0] -= 3
                else:
                    return False
        return True
