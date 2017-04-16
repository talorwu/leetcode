"""
思路：顺时针旋转以后a[i,j] = a[j,n-i-1],如果直接交换这两个会相互覆盖，所以分两步
      1.a[i,j] = a[n-i-1,j]  表示矩阵reserve
      2.a[i,j] = a[j,i]   按对脚线交换
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    
