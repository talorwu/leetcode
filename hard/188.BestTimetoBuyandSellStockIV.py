"""
思路：主要题目中要求，买卖股票必须交替进行！所以可以另buys[i]表示第i次购买时手中剩余的最大钱数，sales[i]表示第i次卖股票时手中剩余的最大钱数
"""
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n<2:return 0
        ans = 0
        if k >= n/2:
            for i in range(1,n):
                ans+=max(0,prices[i] - prices[i-1])
            return ans
        buys = [-999999]*(k+1)
        sales = [0]*(k+1)
        for p in prices:
            for i in range(1,k+1)[::-1]:
                sales[i] = max(sales[i],buys[i]+p)
                buys[i] = max(buys[i],sales[i-1]-p)
        return sales[k]
            
            
            
            
        
