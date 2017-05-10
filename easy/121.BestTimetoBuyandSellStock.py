"""
思路：dp，b[i]表示prices[0:i+1]的最小值，s[i]表示prices[i:]的最大值
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices==[]:return 0
        b = [9999]*len(prices)
        s = [0]*len(prices)
        b[0] = prices[0]
        s[-1] = prices[-1]
        res = 0
        
        for i in range(1,len(b)):
            if b[i-1] > prices[i]:
                b[i] = prices[i]
            else:b[i] = b[i-1]
        for i in range(0,len(b)-1)[::-1]:
            if s[i+1] < prices[i]:
                s[i] = prices[i]
            else:
                s[i] = s[i+1]
        #print b,s
        for i in range(len(b)-1):
            res = max(res,s[i+1]-b[i])
        return res
