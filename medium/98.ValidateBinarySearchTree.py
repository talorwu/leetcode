"""
思路：非递归算法，树的中序遍历
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        p = root
        res = []
        while p or len(stack)>0:
            if p:
                stack.append(p)
                p = p.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                p = tmp.right
        if len(res)==len(set(res)):
            return res == sorted(res)
        else:
            return False
