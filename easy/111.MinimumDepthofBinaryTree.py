"""
思路：BFS
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = []
        if not root:return 0
        q.append(root)
        res = 0
        while q!=[]:
            lenq = len(q)
            res += 1
            for _ in range(lenq):
                tmp = q.pop(0)
                if not tmp.left and not tmp.right:return res
                if tmp.left : q.append(tmp.left)
                if tmp.right: q.append(tmp.right)

        return res        
        
