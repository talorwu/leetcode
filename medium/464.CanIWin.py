class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1+maxChoosableInteger)/2*maxChoosableInteger < desiredTotal:
            return False
        memo = {}
        return self.dfs(range(1,maxChoosableInteger+1),desiredTotal,memo)
        
    def dfs(self,nums,desiredTotal,memo):
        h = str(nums)
        if h in memo:
            return memo[h]
        if nums[-1] >= desiredTotal:
            return True
        for i in range(len(nums)):
            if not self.dfs(nums[:i]+nums[i+1:],desiredTotal-nums[i],memo):
                memo[h] = True
                return True
        memo[h] = False
        return False
        
