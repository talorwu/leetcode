"""
res = n/5+n/25+n/125+...+n/x    x是5的多次方最接近n的
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        exp = 5
        while exp<=n:
            res += n/exp
            exp*=5
        return res
