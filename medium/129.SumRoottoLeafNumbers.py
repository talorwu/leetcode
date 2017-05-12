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
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:return 0
        result = []
        self.DFS([],result,root)
        ans = 0
        for res in result:
            ans1 = 0
            for r in res:
                ans1 = ans1*10 + r
            #print ans1
            ans+=ans1
        #print result
        return ans
    def DFS(self,res,result,root):
        if not root.left and not root.right:
            result.append(res+[root.val])
            return 
        if root.left:self.DFS(res+[root.val],result,root.left)
        if root.right:self.DFS(res+[root.val],result,root.right)
        
        
        
        
        
        
