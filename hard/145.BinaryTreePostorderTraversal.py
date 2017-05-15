# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:return []
        stack = []
        res = []
        cur,pre = root,None
        while cur:
            stack.append(cur)
            cur = cur.left
        while stack:
            cur = stack.pop()
            if cur.right is None or pre==cur.right:
                res.append(cur.val)
                pre = cur
            else:
                stack.append(cur)
                cur = cur.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
                    
                    
        return res
            
            
            
            
            
            
            
