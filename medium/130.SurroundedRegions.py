"""
思路：DFS，先找出在边界上的'O'然后将和边界上的连起来的改成'S'，然后在处理
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:return
        n = len(board[0])
        if n == 0:return 
        q = []
        for i in range(m):
            for j in range(n):
                if i in [0,m-1] or j in [0,n-1] and board[i][j] == 'O':
                    q.append((i,j))
        while q:
            i,j = q.pop(0)
            if 0<=i<m and 0<=j<n and board[i][j] == 'O':
                board[i][j] = 'S'
                q.append((i-1,j))
                q.append((i,j+1))
                q.append((i+1,j))
                q.append((i,j-1))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':board[i][j] = 'X'
                if board[i][j] == 'S':board[i][j] = 'O'
            
            
            
            
            
