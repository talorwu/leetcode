
/*
对于N>7,最后结尾的一定是ctrl-A,ctrl-C,加上一些个ctrl-V,找到那个breakpoint就可以了
*/
class Solution {
public:
    int maxA(int N) {
        vector<int> dp(N+1,0);
        if(N < 7)
            return N;
        for(int i=1;i<=6;i++) dp[i] = i;
        for(int i = 7 ;i<=N;i++){
            for(int j = i-3;j>0;j--){
                dp[i] = max(dp[i],dp[j]*(i-j-1));
            }
        }
        return dp[N];
    }
};
