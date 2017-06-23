/*
思路：dp[i][step]记录以A[i]结尾的 等差为step的长度
*/
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int n = A.size();
        vector<unordered_map<int,int>> dp(n);
        int res = 0;
        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                if((long)A[i] - (long)A[j] > INT_MAX || (long)A[i] - (long)A[j] < INT_MIN) continue;// do not ignore this st
                int step = A[i]-A[j];
                dp[i][step]+=1;
                if(dp[j].find(step) != dp[j].end()){
                    dp[i][step] += dp[j][step];
                    res += dp[j][step];
                }
            }
        }
        return res;
    }
};
