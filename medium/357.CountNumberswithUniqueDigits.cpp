class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int f[11];
        if(n==0) return 1;
        f[1] = 10;
        f[2] = 9*9;
        int exp = 8;
        for(int i=3;i<11;i++){
            f[i] = f[i-1]*exp;
            exp --;
        }
        
        int ans = 0;
        for(int i = 1;i<=n&&i<=10;i++)
            ans += f[i];
        return ans;
    }
};
