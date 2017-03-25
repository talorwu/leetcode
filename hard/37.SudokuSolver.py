"""
思路：DFS+回溯
"""
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        s = set()
        for i in range(9):
            for j in range(9):
                s.add((i,board[i][j]))
                s.add((board[i][j],j))
                s.add((i/3,j/3,board[i][j]))
                
        nums = ['1','2','3','4','5','6','7','8','9']
        self.solve(board,0,0,s,nums)
        
    def solve(self,board,i,j,s,nums):
        if i>8:return True
        cur = board[i][j]
        if board[i][j] != '.':
            s.add((i,cur))
            s.add((cur,j))
            s.add((i/3,j/3,cur))
            return self.solve(board,i+(j+1)/9,(j+1)%9,s,nums)
        else:
            for c in nums:
                if self.check(i,j,c,s):
                    board[i][j] = c
                    if self.solve(board,i+(j+1)/9,(j+1)%9,s,nums):return True
                    else:
                        board[i][j] = '.'
                        s.remove((i,c))
                        s.remove((c,j))
                        s.remove((i/3,j/3,c))
            return False
                
            
        
        
    
    def check(self,i,j,cur,big):
        if (i,cur) in big or (cur,j) in big or (i/3,j/3,cur) in big:
            return False
        big.add((i,cur))
        big.add((cur,j))
        big.add((i/3,j/3,cur))
        return True
        
    
        
        
