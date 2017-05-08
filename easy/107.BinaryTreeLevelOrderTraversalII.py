"""
思路：和Binary Tree Level Order Traversal思路一样，最后结果reverse()
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        res = []
        if root is None:return res
        q.append(root)
        while q != []:
            len1 = len(q)
            subres = []
            for _ in range(len1):
                tmp = q.pop(0)
                subres.append(tmp.val)
                if tmp.left:q.append(tmp.left)
                if tmp.right:q.append(tmp.right)
            res.append(subres)
        res.reverse()
        return res
            
