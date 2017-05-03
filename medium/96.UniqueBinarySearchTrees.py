
"""
思路：DP,
这道题要求可行的二叉查找树的数量，其实二叉查找树可以任意取根，只要满足中序遍历有序的要求就可以。从处理子问题的角度来看，
选取一个结点为根，就把结点切成左右子树，以这个结点为根的可行二叉树数量就是左右子树可行二叉树数量的乘积，
所以总的数量是将以所有结点为根的可行结果累加起来。写成表达式如下：


"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0]*(max(n+1,3))
        f[0] = 1
        f[1] = 1
        f[2] = 2
        if n < 3:
            return f[n]
        for i in range(3,n+1):
            for j in range(i):
                f[i] += f[j]*f[i-j-1]
        return f[n]
