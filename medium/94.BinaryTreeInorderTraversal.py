"""
思路：二叉树中序遍历非递归算法
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        p = root
        while p or len(stack) > 0:
            if p:
                stack.append(p)
                p = p.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                p = tmp.right
        return res
                
                
                
            
        
