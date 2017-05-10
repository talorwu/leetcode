"""
思路：1.pre[i]表示prices[0:i+1]的最大值,表示第一次交易,post[i]表示prices[i:]的最大值，表示第二次交易
      2.
    states[0]: one buy
    states[1]: one buy, one sell
    states[2]: two buys, one sell
    states[3]: two buy, two sells
The states transistions occurs when buy/sell operations are executed. For example, state[][0] can move to state[][1] via one sell operation.

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        if prices==[]:return 0
        pre = [0]*len(prices)
        minPrice = prices[0]
        for k in range(1,len(prices)):
            minPrice = min(minPrice,prices[k])
            pre[k] = max(pre[k-1],prices[k]-minPrice)
            
        post = [0]*len(prices)
        maxPrice = prices[-1]
        for k in range(len(prices)-1)[::-1]:
            maxPrice = max(maxPrice,prices[k])
            post[k] = max(post[k+1],maxPrice - prices[k])
        print pre,post
        for i in range(len(prices)-1):
            result = max(result,pre[i]+post[i+1])
        result = max(result,post[0])
        return result



     def maxProfit(self, prices):
	state = [-999999,0,-999999,0]
        for p in prices:
            state[3] = max(state[3],state[2]+p)
            state[2] = max(state[2],state[1]-p)
            state[1] = max(state[1],state[0]+p)
            state[0] = max(state[0],-p)
        return state[3]
