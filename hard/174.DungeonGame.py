"""
思路：f[i][j]表示从（i，j)到（m-1,n-1)至少需要多少体力
"""

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        f = [[0]*n for _ in range(m)]
        f[-1][-1] = 1 if dungeon[-1][-1] >= 0 else -dungeon[-1][-1]+1
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                if i == m-1 and j == n-1:
                    continue
                if i+1 >= m:
                    f[i][j] = max(1,f[i][j+1]-dungeon[i][j])
                elif j+1 >= n:
                    f[i][j] = max(1,f[i+1][j] - dungeon[i][j])
                else:
                    f[i][j] = min(max(1,f[i][j+1]-dungeon[i][j]),max(1,f[i+1][j] - dungeon[i][j]))
        print f
        return f[0][0]
                    
                    
                    
                    
                        
