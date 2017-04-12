"""
思路：DFS，每次在一个位置加入一个数字，如果这个数字之前在这个位置出现过，就跳过
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.DFS([],nums,res)
        return res
    def DFS(self,step,nums,res):
        if len(nums)==0:
            res.append(step)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:continue
            self.DFS(step+[nums[i]],nums[:i]+nums[i+1:],res)
            
        
        
        
