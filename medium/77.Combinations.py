"""
思路：DFS,如果单这样会超时，所以处理如果k较大，就先去k=n-k,然后去补集
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results=[]
        if k<=n/2:
            self.DFS(k,range(1,n+1),[],results)
        else:
            self.DFS(n-k,range(1,n+1),[],results)
            for i in range(len(results)):
                results[i] = list(set(range(1,n+1))^set(results[i]))
        return results
    def DFS(self,step,nums,res,results):
        if step==0:
            results.append(res)
            return
        for i in range(len(nums)):
            self.DFS(step-1,nums[i+1:],res+[nums[i]],results)
