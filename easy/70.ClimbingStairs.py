class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0]*(n+2)
        f[1] = 1
        f[2] = 2
        if n<=2:
            return f[n]
        for i in range(3,n+1):
            f[i]=f[i-1]+f[i-2]
        return f[n]
        
