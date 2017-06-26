/*
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
Going over all cells, we can count only those that are the "first" cell of the battleship. First cell will be defined as the most top-left cell. We can check for first cells by only counting cells that do not have an 'X' to the left and do not have an 'X' above them.
*/

class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        if(board.size() == 0)
            return 0;
        int m = board.size();
        int n = board[0].size();
        int count = 0;
        //int i = 0 , j = 0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(board[i][j] == '.') continue;
                if(i-1>=0 && board[i-1][j]=='X') continue;
                if(j-1>=0 && board[i][j-1]=='X') continue;
                count++;
            }
        }
        return count;
    }
};
