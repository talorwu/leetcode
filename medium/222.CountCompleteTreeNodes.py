"""
思路：用暴力法, recursive求会超时 O(N).   如果从某节点一直向左的高度 = 一直向右的高度, 那么以该节点为root的子树一定是complete binary tree. 
	而 complete binary tree的节点数,可以用公式算出 2^h - 1. 如果高度不相等, 则递归调用 return countNode(left) + countNode(right) + 1.  复杂度为O(h^2)   
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #time limited
        # if not root: return 0
        # q = [root]
        # level = 0
        # res = 0
        # while q:
        #     lenq = len(q)
        #     if lenq != 2**level:
        #         res += lenq
        #         return res
        #     else:
        #         for i in range(lenq):
        #             tmp = q.pop(0)
        #             if tmp.left:q.append(tmp.left)
        #             if tmp.right:q.append(tmp.right)
        #         res += lenq
        #     level += 1
        # return res
        
        #time limited
        
        
    #     if not root:return 0
    #     level,right = self.findLast(root,0,1)
    #     #print level ,right
    #     return 2**(level)-1 + right
        
    # def findLast(self,root,level,right):
    #     #print root.val,level,right
    #     if not root.left:
    #         return level,right
    #     if not root.right:
    #         #print root.left.val,right
    #         return level+1, 2*right-1
    #     l1,right1 = self.findLast(root.right,level+1,right*2)
    #     l2,right2 = self.findLast(root.left,level+1,2*right-1)
    #     if l1 == l2:
    #         return l1,right1
    #     return l2,right2
        if not root:return 0
        l = self.findLevel(root,0)
        r = self.findLevel(root,1)
        
        if l == r:
            return 2**(l) - 1
        return self.countNodes( root.left) + self.countNodes(root.right)+1
    
    def findLevel(self,root,flag):
        level = 1
        if flag == 0:
            while root.left:
                level+=1
                root = root.left
        else:
            while root.right:
                level+=1
                root = root.right
        return level
                
                
                
            
        
