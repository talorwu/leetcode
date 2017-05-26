"""
BFS
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:return 0
        n = len(grid[0])
        if m == 0:return 0
        res = 0
        used = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not used[i][j]:
                    res += 1
                    q=[(i,j)]
                    used[i][j] = True
                    while q:
                        ii,jj = q.pop(0)
                        if ii-1>=0 and grid[ii-1][jj]=='1' and not used[ii-1][jj]:
                            q.append((ii-1,jj))
                            used[ii-1][jj] = True
                        if jj+1<n and grid[ii][jj+1] == '1' and not used[ii][jj+1]:
                            q.append((ii,jj+1))
                            used[ii][jj+1] = True
                        if ii+1<m and grid[ii+1][jj] == '1' and not used[ii+1][jj]:
                            q.append((ii+1,jj))
                            used[ii+1][jj] = True
                        if jj-1>=0 and grid[ii][jj-1] == '1' and not used[ii][jj-1]:
                            q.append((ii,jj-1))
                            used[ii][jj-1] = True
        return res
                        
