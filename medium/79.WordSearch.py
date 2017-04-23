"""
思路：DFS+回溯,注意标记使用过的位置，并且如果最后不加入if res:return res剪枝会超时
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        words = list(word)
        n = len(board)
        if n==0:return word==""
        m = len(board[0])
        if m==0:return word==""
        res = False
        used = [[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j]==words[0]:
                    used[i][j] = True
                    res = res or self.DFS(board,used,i,j,words[1:])
                    used[i][j] = False
        return res
    def DFS(self,board,used,i,j,word):
        if word==[]:
            return True
        res = False
        if i-1>=0 and word[0]==board[i-1][j] and not used[i-1][j]:
            used[i-1][j] = True
            r1 = self.DFS(board,used,i-1,j,word[1:])
            used[i-1][j] = False
            res = res or r1
            if res:return res
        if j+1<len(board[0]) and word[0]==board[i][j+1] and not used[i][j+1]:
            used[i][j+1] = True
            r2 = self.DFS(board,used,i,j+1,word[1:])
            used[i][j+1] = False
            res = res or r2
            if res:return res
        if i+1<len(board) and word[0]==board[i+1][j] and not used[i+1][j]:
            used[i+1][j] = True
            r3 = self.DFS(board,used,i+1,j,word[1:])
            used[i+1][j]  = False
            res = res or r3
            if res:return res
        if j-1>=0 and word[0]==board[i][j-1] and not used[i][j-1]:
            used[i][j-1] = True
            r4 = self.DFS(board,used,i,j-1,word[1:])
            used[i][j-1] = False
            res = res or r4
            if res:return res
        return res
        
