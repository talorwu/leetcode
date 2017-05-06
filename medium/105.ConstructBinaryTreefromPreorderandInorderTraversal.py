"""
思路：1.递归算法
      2.非递归算法：使用stack，对于preorder扫描，记录前一个构造的节点pre，遇见一个新的先建立一个TreeNode，pre.left = 新的TreeNode
	然后放入栈里，当栈顶元素和inorder相等的时候，开始出栈，然后开始构造右子树（描述不清，看代码，模拟一遍就清楚了）
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == []:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        first = preorder[0]
        inIndex = -1
        for i in range(len(inorder)):
            if inorder[i] == first:
                inIndex = i
                break
        left = self.buildTree(preorder[1:inIndex+1],inorder[:inIndex])
        right = self.buildTree(preorder[inIndex+1:],inorder[inIndex+1:])
        node = TreeNode(preorder[0])
        node.left = left
        node.right = right
        return node

    def buildTree(self, preorder, inorder):	
	#非递归算法
	stack = []
        if preorder == []:return None
        root = TreeNode(preorder[0])
        stack.append(root)
        i,j = 1,0
        len_ = len(preorder)
        pre = root
        flag = 0
        while i < len_:
            if stack != [] and stack[-1].val == inorder[j]:
                pre = stack.pop()
                j+=1
                flag = 1
            elif flag==0:
                pre.left = TreeNode(preorder[i])
                pre = pre.left
                stack.append(pre)
                i+=1
            else:
                pre.right = TreeNode(preorder[i])
                pre = pre.right
                stack.append(pre)
                flag = 0
                i+=1
        return root
        
