"""
思路：记录曾经出现过的数字
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        Set = set()
        Set.add(n)
        while True:
            tmp = 0
            while n:
                tmp += (n%10)**2
                n = n/10
            if tmp == 1:return True
            if tmp in Set:return False
            Set.add(tmp)
            n=tmp
            
                
                
