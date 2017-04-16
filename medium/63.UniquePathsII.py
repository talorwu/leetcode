"""
思路：DP，如果obstacleGrid[i][j]==1,f[i][j]=0
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m==0:return 0
        n = len(obstacleGrid[0])
        f = [[0]*n for _ in range(m)]
        f[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                else:
                    if i-1>=0:
                        f[i][j] += f[i-1][j]
                    if j-1>=0:
                        f[i][j]+=f[i][j-1]
        #print f
        return f[m-1][n-1]
