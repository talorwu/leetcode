"""
思路：DFS，每次选取一个
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.DFS([],nums,res)
        return res
    def DFS(self,step,nums,res):
        if len(nums)==0:
            res.append(step)
        for i in range(len(nums)):
            self.DFS(step+[nums[i]],nums[:i]+nums[i+1:],res)
            
        
