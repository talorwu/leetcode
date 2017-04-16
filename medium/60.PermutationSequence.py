"""
思路：数学方法。
"""


import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = range(1,n+1)
        res = ''
        k-=1
        while n>0:
            n-=1
            index,k = divmod(k,math.factorial(n))
            #print index,k
            res+=str(numbers[index])
            numbers.remove(numbers[index])
            
        return res
