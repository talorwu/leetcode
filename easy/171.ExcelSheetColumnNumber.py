class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        #t = '#ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = 0
        for n in s:
            res = res*26 + ord(n)-64
        return res
