"""
思路：n=d*2^k1+d*2^k2+....+d
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = (dividend < 0) is (divisor < 0)
        dividend,divisor = abs(dividend),abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp ,i = divisor,1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                tmp<<=1
                i<<=1
        if not flag:res = -res
        return min(max(-2147483648,res),2147483647)
