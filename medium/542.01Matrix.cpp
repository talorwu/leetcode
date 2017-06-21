/*
思路：dp 两遍，一遍左上->右下  一遍 右下->左上
*/
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        if (rows == 0)
            return matrix;
        int cols = matrix[0].size();
        vector<vector<int>> dict(rows , vector<int>(cols,INT_MAX-10010));
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if (matrix[i][j] == 0)
                    dict[i][j] = 0;
                else{
                    if (i-1>=0)
                        dict[i][j] = min(dict[i][j],dict[i-1][j] + 1);
                    if(j-1 >=0)
                        dict[i][j] = min(dict[i][j], dict[i][j-1] + 1);
                        
                }
            }
        }
        for(int i=rows-1;i>=0;i--){
            for(int j=cols-1;j>=0;j--){

                    if (i+1<rows)
                        dict[i][j] = min(dict[i][j],dict[i+1][j] + 1);
                    if(j+1<cols)
                        dict[i][j] = min(dict[i][j], dict[i][j+1] + 1);
                        
                
            }
        }
        return dict;
        
    }
};
