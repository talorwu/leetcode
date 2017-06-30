/*
http://www.cnblogs.com/njufl/p/LeetCode.html
*/

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<int> nnums(n+2);
        for(int i=1;i<n+1;i++)
            nnums[i] = nums[i-1];
        nnums[0] = nnums[n+1] = 1;
        n = n + 2;
        int dp[n][n]; // dp[i][j]表示i开始的j结束的开区间(i,j)最大值
        memset(dp,0,sizeof(dp));
        for(int l = 2; l <= n; l++){
            for(int i = 0;i<=n-l ;i++){
                int j = i+l-1;
                for(int k = i+1;k<j;k++){  //k是最后一个被打破的
                    dp[i][j] = max(dp[i][j],nnums[i]*nnums[k]*nnums[j]+dp[i][k]+dp[k][j]);
                }
            }
        }
        return dp[0][n-1];
    }
    
};
