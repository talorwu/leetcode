"""
https://leetcode.com/articles/number-1-bits/
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            res += n&1
            n >>= 1
        return res

	

	#方法2
	res = 0
        while n:
            res+=1
            n&=(n-1)
        return res
