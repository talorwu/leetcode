"""
思路：
中序遍历，找到逆序的位置
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        mistake = []
        pre,cur= None,None
        p = root
        while p or len(stack) > 0:
            if p:
                stack.append(p)
                p = p.left
            else:
                cur = stack.pop()
                p = cur.right
                if pre and cur.val < pre.val:
                    if mistake == []:       #处理两个挨着的直接交换
                        mistake.append(pre)
                        mistake.append(cur)
                    else:
                        mistake.pop()
                        mistake.append(cur)
                pre = cur
        #print mistake[0].val
        tmp = mistake[0].val
        mistake[0].val = mistake[1].val
        mistake[1].val = tmp
        
                
                
                
                
                
                
                
        
