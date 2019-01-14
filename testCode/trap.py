class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:  # 边界检查
            return 0
        result = 0
        temp_max = None  # 首先从左到右遍历
        for id, i in enumerate(height):
            if temp_max is None:
                temp_max = [id, i]  #一个存id 一个存高度
            else:
                if i > temp_max[1]:
                    if id - temp_max[0] != 1:
                        result += (id - temp_max[0] - 1) * temp_max[1] - sum(height[temp_max[0] + 1: id])
                    temp_max = [id, i]
        temp_max = None # 然后从右到左遍历
        for j in range(len(height) - 1, -1, -1):
            if temp_max is None:
                temp_max = [j, height[j]]
            else:
                if height[j] >= temp_max[1]:
                    if temp_max[0] - j != 1:
                        result += (temp_max[0] - 1 - j) * temp_max[1] - sum(height[j + 1: temp_max[0]])
                    temp_max = [j, height[j]]
        return result

solution = Solution()
a = [0,1,0,2,1,0,1,3,2,1,2,1]
print(solution.trap(a))