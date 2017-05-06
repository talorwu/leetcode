"""
思路：递归算法
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root == None or self.helpf(root.left,root.right)
    def helpf(self,left,right):
        if not left or not right:
            return left == right
        elif left.val != right.val:
            return False
        return self.helpf(left.left,right.right) and self.helpf(left.right,right.left)
