"""
思路:pow(x,n) = pow(x*x,n/2)
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1.0
        if n<0:
            n,x=-n,1.0/x
        if n%2:
            return x*self.myPow(x*x,n/2)
        else:
            return self.myPow(x*x,n/2)
        
