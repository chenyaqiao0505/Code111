class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = x
        if y < 0:
            return False
        elif y < 10:
            return True
        else:
            a = ''
            while(y > 9):

                a = a+str(y % 10)
                y = int(y / 10)
                if y <= 9:
                    a =a + str(y)
                    break
            print('x',x)
            print('a',a)
            if x == int(a):
                return True
            else:
                return False

a = Solution()
aa = a.isPalindrome(9999)
print(aa)