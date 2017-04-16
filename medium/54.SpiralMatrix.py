"""
思路：恶心
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        if rows==0:return []
        cols = len(matrix[0])
        res = [0]*rows*cols
        row,col = rows-1,cols-1
        k = 0
        loop=0
        while row >= 0 and col >= 0:
            if row==col and row == 0:
                res[k] = matrix[rows/2][cols/2]
                break
            if row == 0:
                for i in range(col+1):
                    res[k] = matrix[rows/2][i+loop]
                    k+=1
                break
            if col == 0:
                for i in range(row+1):
                    res[k] = matrix[i+loop][cols/2]
                    k+=1
                break
            for i in range(col):
                res[k] = matrix[loop][i+loop]
                k+=1
            for i in range(row):
                res[k] = matrix[i+loop][cols-loop-1]
                k+=1
            for i in range(col):
                res[k] = matrix[rows-loop-1][cols-1-loop-i]
                k+=1
            for i in range(row):
                res[k] = matrix[rows-1-loop-i][loop]
                k+=1
            row-=2
            col-=2
            loop+=1
        
        return res
        
