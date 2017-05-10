"""
思路：
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxValue = -999999
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathDown(root)
        return self.maxValue
    def maxPathDown(self,root):
        if root is None:return 0
        l = max(0,self.maxPathDown(root.left))
        r = max(0,self.maxPathDown(root.right))
        self.maxValue = max(self.maxValue,l+r+root.val)
        return max(l,r)+root.val
