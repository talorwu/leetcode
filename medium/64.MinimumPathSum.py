"""
思路：DP
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m==0:return 0
        n = len(grid[0])
        
        f = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                t1,t2 = 9999999,9999999
                if i-1<0 and j-1<0:
                    f[i][j] = grid[i][j]
                else:
                    if i-1>=0:
                        t1 = f[i-1][j]+grid[i][j]
                    if j-1>=0:
                        t2 = f[i][j-1]+grid[i][j]
                    f[i][j] = min(t1,t2)
        #print f
        return f[m-1][n-1]
        
