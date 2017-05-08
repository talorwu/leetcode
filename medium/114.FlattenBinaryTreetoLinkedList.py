# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#     :    self.right = None

#模拟一遍就清楚了，循环的右子树放在左子树，左子树放在右子树
def flatten(self, root):
    if root is None:return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.pre
        root.left = None
        self.pre = root


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.DFS(root)
    #返回root完成以后的叶节点
    def DFS(self,root):
        if root is None:return None
        if not root.left and not root.right:return root
        if root.left and root.right and self.check(root.left) and self.check(root.right):
            right = root.right
            root.right = root.left
            root.left = None
            root.right.right = right
            return right
        if root.left and not root.right and self.check(root.left):
            root.right = root.left
            root.left = None
            return root.right
        if not root.left and root.right and self.check(root.right):
            return root.right
        left = self.DFS(root.left)
        right = self.DFS(root.right)
        if left:
            tmp = root.right
            root.right = root.left
            root.left = None
            left.right = tmp
        if right:return right
        return left
        
    def check(self,root):
        return not root.left and not root.right
        
        
        
        
        
