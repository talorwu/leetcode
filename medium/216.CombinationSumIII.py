"""
思路：dfs,为了避免重复，只选择后面的
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [1,2,3,4,5,6,7,8,9]
        results = []
        self.dfs(nums,k,n,[],results)
        #results = set(results)
        return results
        
    def dfs(self,nums,k,n,res,results):
        if k==0 :
            if n==0:
                results.append(res)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i+1:],k-1,n-nums[i],res+[nums[i]],results)
