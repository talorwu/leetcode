"""
思路：
递归，判断左子树与右子树
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:return True

        return self.calHeight(root) != -1

    def calHeight(self,root):
        if not root : return 0
        left = self.calHeight(root.left)
        right = self.calHeight(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left,right)+1
        
        
