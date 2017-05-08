"""
思路：DFS
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        results = []
        self.DFS(root,[],results,sum)
        return results
    def DFS(self,root,res,results,sum):
        if root is None : return
        if not root.left and not root.right:
            if sum == root.val:
                results.append(res+[root.val])
            else:return
        self.DFS(root.left,res+[root.val],results,sum-root.val)
        self.DFS(root.right,res+[root.val],results,sum-root.val)
        
        
