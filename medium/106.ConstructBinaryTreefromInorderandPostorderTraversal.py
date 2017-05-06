"""
思路：1.递归算法
      2.非递归算法
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder == []:return None
        if len(inorder) == 1: return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        inIndex = -1
        for i in range(len(inorder)):
            if inorder[i] == postorder[-1]:
                inIndex = i
                break
        root.left = self.buildTree(inorder[:inIndex],postorder[:inIndex])
        root.right = self.buildTree(inorder[inIndex+1:],postorder[inIndex:-1])
        return root



#非递归算法
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        stack = []
        len_ = len(inorder)
        if len_ == 0:
            return None
        root = TreeNode(postorder[-1])
        i ,j= len_ -2,len_-1
        pre = root
        stack.append(root)
        flag = 0
        while i>=0:
            if stack != [] and stack[-1].val == inorder[j]:
                pre = stack.pop()
                flag = 1
                j-=1
            elif flag:
                pre.left = TreeNode(postorder[i])
                pre = pre.left
                flag = 0
                stack.append(pre)
                i-=1
            else:
                pre.right = TreeNode(postorder[i])
                pre = pre.right
                stack.append(pre)
                i-=1
        return root
                
                
                
