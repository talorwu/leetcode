/*
考虑好所有的情况
*/

class Solution {
public:
    int numDecodings(string s) {
        int n = s.length();
        const int MAX_ = 1000000000 + 7;
        //cout << MAX_<<endl;
        vector<long long> dp(n+1,0);
        dp[0] = 1;
        for(int i=1;i<=n;i++){
            if(s[i-1] == '*')
                dp[i] = (dp[i-1]*9)%MAX_;
            else if(s[i-1] != '0')
                dp[i] = dp[i-1];
            
            
            if(i<2 || s[i-2] == '0')
                continue;
            if(s[i-2] == '*' )
                if(s[i-1] == '*')
                    dp[i] = (dp[i] + dp[i-2]*15)%MAX_;
                else if(s[i-1] == '0')
                    dp[i] = (dp[i] + dp[i-2]*2)%MAX_;
                else if(s[i-1] <= '6')
                    dp[i] = (dp[i] + dp[i-2]*2)%MAX_;
                else
                    dp[i] = (dp[i] + dp[i-2])%MAX_;
            else if(s[i-2] == '1')
                if(s[i-1] == '*')
                    dp[i] = (dp[i] + dp[i-2]*9)%MAX_;
                else
                    dp[i] = (dp[i] + dp[i-2])%MAX_;
            else if(s[i-2] == '2')
                if(s[i-1] == '*')
                    dp[i] = (dp[i] + dp[i-2]*6)%MAX_;
                else if(s[i-1] <= '6')
                    dp[i] = (dp[i] + dp[i-2])%MAX_;
                    
                
        }
        return dp[n];
    }
};
