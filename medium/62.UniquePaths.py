"""
思路：DP
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [[0]*n for _ in range(m)]
        for i in range(m):
            f[i][0] = 1
        for i in range(n):
            f[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                f[i][j] = f[i-1][j]+f[i][j-1]
        return f[m-1][n-1]
