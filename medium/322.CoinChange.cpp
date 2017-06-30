//https://leetcode.com/articles/coin-change/#approach-1-brute-force-time-limit-exceeded

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        //int ans = 0;
        int n = coins.size();
        sort(coins.begin(),coins.end());
        vector<int> dp(amount+1,INT_MAX-1);
        dp[0] = 0;
        for(int i=1;i<=amount;i++){
            for(int j=0;coins[j]<=i && j<n;j++){
                dp[i] = min(dp[i],dp[i-coins[j]]+1);
            }
        }
        if(dp[amount]>=INT_MAX-1)return -1;
        return dp[amount];
    }
};
