/*
思路：dp[i][j]表示使用前j个硬币构造i的个数，dp[i][j] = sum{k}(dp[i-k*coins[j-1]][j-1])
*/

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        int n = coins.size();
        vector<vector<int>> dp(amount+1,vector<int>(n+1,0));
        for(int i=0;i<=n;i++)
            dp[0][i] = 1;
        for(int i=1;i<=amount;i++){
            for(int j = 1;j<=n;j++){
                for(int k=0;k*coins[j-1]<=i;k++){
                    dp[i][j] += dp[i-k*coins[j-1]][j-1];
                }
            }
        }
        return dp[amount][n];
    }
    
};
