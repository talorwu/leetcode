"""
思路：输出每层的最右一个
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = []
        res = []
        if root is None:return []
        q.append(root)
        #res.append(root.val)
        while q:
            lenq = len(q)
            for _ in range(lenq):
                tmp = q.pop(0)
                if tmp.left:q.append(tmp.left)
                if tmp.right:q.append(tmp.right)
                if _ == lenq-1:res.append(tmp.val)
        return res
                
                
                
