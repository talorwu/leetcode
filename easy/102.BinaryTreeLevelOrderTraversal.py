"""
思路：BFS+Queue
方法二：见代码
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = Queue.Queue()
        res = []
        if not root:
            return res
        q.put(root)
        while not q.empty():
            levelnums = q.qsize()
            subres = []
            for i in range(levelnums):
                p = q.get()
                subres.append(p.val)
                if p.left : q.put(p.left)
                if p.right : q.put(p.right)
            res.append(subres)
        return res




def levelOrder(self, root):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])
        LRpair = [(node.left, node.right) for node in level]
        level = [leaf for LR in LRpair for leaf in LR if leaf]
    return ans

