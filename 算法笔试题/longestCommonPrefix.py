class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        if strs == []:
            return ''
        else:
            minil = min(len(i) for i in strs)
            index = 0
            while index < minil:
                for i in range(1,len(strs)):
                    if strs[i][index] != strs[i - 1][index]:
                        return strs[0][:index]
                index  += 1
            return strs[0][:index]

a = Solution()
strs = ["flower","flow","flight"]
qq = a.longestCommonPrefix(strs)
print(qq)