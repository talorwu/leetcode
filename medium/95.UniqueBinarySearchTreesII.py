"""
思路：深度搜索
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        results = []
        if n == 0:
            return []
        nums = range(1,n+1)
        results = self.DFS(nums)
        return results
        
    def DFS(self,nums):
        
        if nums == []:
            return None
        results = []
        for i in range(len(nums)):
            left = self.DFS(nums[:i])
            right = self.DFS(nums[i+1:])
            for l in left or [None]:
                for r in right or [None]:
                    node = TreeNode(nums[i])
                    node.left = l
                    node.right = r
                    results.append(node)
        return results
            
            
        
