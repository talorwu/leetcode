"""
思路：分析完以后发现，如果是上升序列比如[1,2,4]那么1买2卖，2买4卖和1买4卖一样。所以只需要每次遇见prices[i]>prices[i-1]就加上，否则不变
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:return 0
        res = 0
        pre = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > pre:
                res += (prices[i] - pre)
            pre = prices[i]
        return res
        
