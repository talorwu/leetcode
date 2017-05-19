class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        n-=1
        while True:
            res = t[n%26]+res
            n /= 26
            n-=1
            if n < 0:
                return res
