class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        int i = 0,j=0;
        int m = matrix.size();
        vector<int> ans;
        if(m == 0)
            return ans;
        int n = matrix[0].size();
        if(n == 0)
            return ans;
        
        bool dir = false;
        ans.push_back(matrix[i][j]);
        while(true){
            //cout<<i << ' '<< j <<' '<< dir << endl;
            if(!dir){
            if(i-1 >= 0 && j+1<n){
                i-=1;j+=1;
                ans.push_back(matrix[i][j]);
            }else if(j+1 < n){
                j++;
                ans.push_back(matrix[i][j]);
                dir = !dir;
            }else if(i+1 < m){
                i++;
                ans.push_back(matrix[i][j]);
                dir = !dir;
            }
            }else{
                if(i+1 < m && j-1>=0){
                i+=1;j-=1;
                ans.push_back(matrix[i][j]);
            }else if(i+1 < m){
                i++;
                ans.push_back(matrix[i][j]);
                dir = !dir;
            }else if(j+1 < n){
                j++;
                ans.push_back(matrix[i][j]);
                dir = !dir;
            }
            }
            if(i == m-1 && j== n-1)
                return ans;
                
        }
    }
};
