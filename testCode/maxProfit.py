'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        profit = 0
        for day in range(len(prices)-1):
            differ = prices[day+1] - prices[day]
            if differ > 0:
                profit += differ
        return profit

i = [44,67,98,34,12,35]
a = Solution()
print(a.maxProfit(i))

