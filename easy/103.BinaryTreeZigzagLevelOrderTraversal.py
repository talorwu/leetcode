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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        res = []
        if not root:
            return res
        q.append(root)
        j=0
        while q != []:
            levelnums = len(q)
            subres = []
            for i in range(levelnums):
                p = q.pop(0)
                subres.append(p.val)
                if p.left : q.append(p.left)
                if p.right : q.append(p.right)
            if j%2:subres.reverse()
            res.append(subres)
            j+=1
        return res
        
        
