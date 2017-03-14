"""
思路：将其倒转到最后一位，比如1234321，q = 123432 , p=1,保证x/10 == q and x%10 == p
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        p = x
        q = 0
        while p >= 10:
            q = q * 10 + p%10
            p /= 10
        return p == x%10 and q == x/10
