"""
思路：My idea is simple: store states of each row in the first of that row, and store states of each column in the first of that column. Because the state of row0 and the state of column0 would occupy the same cell, I let it be the state of row0, and use another variable "col0" for column0. In the first phase, use matrix elements to set states in a top-down way. In the second phase, use states to set matrix elements in a bottom-up way.

1.为什么有一个col0，因为第0行为0第0列不为0怎么表示？两者占一个cell,因此用matrix[0][0]表示第0行是否为0，用col0表示第0列是否为0
2.为什么倒叙填充，因为要保证我修改这一行或这一列的时候，matrix[i][0]和matrix[0][j]没有被修改，所以她们两个最后修改
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n==0:return
        m = len(matrix[0])
        col0=1
        for i in range(n):
            if matrix[i][0]==0:
                col0=0
            for j in range(1,m):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(n)[::-1]:
            for j in range(1,m)[::-1]:
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            if col0==0:
                matrix[i][0]=0
        
