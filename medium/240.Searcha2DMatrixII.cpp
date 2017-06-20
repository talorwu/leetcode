class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty()) return false;
        int i = 0,j = matrix[0].size()-1;
        // return dfs(matrix,target,left,right,top,bottom);
        while(i < matrix.size() && j >= 0){
            if(matrix[i][j] == target) return true;
            if(matrix[i][j] > target)
                j--;
            else
                i++;
        }
        return false;
        
    }

	//下面的思路错了。
    bool dfs(vector<vector<int>>& matrix,int target,int left,int right,int top,int bottom){
        while(left <= right && top <= bottom){
            int mid1 = (left+right)/2;
            int mid2 = (top+bottom)/2;
            if(matrix[mid2][mid1] == target)
                return true;
            if(matrix[mid2][mid1] < target){
                return dfs(matrix,target,mid1+1,right,top,mid2-1) || dfs(matrix,target,left,mid1-1,mid2+1,bottom) || dfs(matrix,target,mid1+1,right,mid2+1,bottom) ||  binsearch(matrix,target,mid2,0,mid1+1,right) || binsearch(matrix,target,mid1,1,mid2+1,bottom);
            }
            return dfs(matrix,target,left,mid1-1,top,mid2-1) || binsearch(matrix,target,mid2,0,0,mid1-1)|| binsearch(matrix,target,mid1,1,0,mid2-1);
        }
        return false;
    }
    bool binsearch(vector<vector<int>>& matrix,int target,int c_or_r,int flag,int begin,int end){
        if(flag == 0){ // hang
            while(begin<=end){
                int mid = (begin+end)/2;
                if(matrix[c_or_r][mid] == target) return true;
                if(matrix[c_or_r][mid] > target)
                    end = mid - 1;
                else
                    begin = mid + 1;
            }
        }else{ //lie
            while(begin<=end){
                int mid = (begin+end)/2;
                if(matrix[mid][c_or_r] == target) return true;
                if(matrix[mid][c_or_r] > target)
                    end = mid - 1;
                else
                    begin = mid + 1;
            }
        }
        return false;
    }
};
