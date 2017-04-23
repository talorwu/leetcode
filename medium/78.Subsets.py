"""
思路：DFS
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = [[]]
        self.DFS(nums,[],results)
        return results
    def DFS(self,nums,res,results):
        for i in range(len(nums)):
            results.append(res+[nums[i]])
            self.DFS(nums[i+1:],res+[nums[i]],results)
