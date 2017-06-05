"""
http://blog.csdn.net/u012501459/article/details/46553139
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:return 0
        n = len(matrix[0])
        if n == 0:return 0
        dp = [[0]*n for _ in range(m)]
        if matrix[0][0] == '1':
            dp[0][0] = 1
        res = dp[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j==0:continue
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    if i>0 and j > 0:
                        dp[i][j] += min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                    res = max(res , dp[i][j])
        return res**2
            
