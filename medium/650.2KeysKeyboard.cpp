/*
if i%j==0,i/j = k;则dp[i]可以是dp[j]+一次复制+（k-1)次粘贴
*/

class Solution {
public:
    int minSteps(int n) {
        vector<int> dp(n+1,0);

        for (int i = 2; i <= n; i++) {
            dp[i] = i;
            for (int j = i-1; j > 1; j--) {
                if (i % j == 0) {
                    dp[i] = dp[j] + (i/j);
                    break;
                }
                
            }
        }
        return dp[n];
    }
//     int minSteps(int n) {
//         vector<int> minsteps(n+1,INT_MAX);
//         vector<vector<int> > paste(n+1,vector<int>(0,0));
//         if(n == 1)
//             return 0;
//         paste[2].push_back(1);
//         minsteps[2] = 2;
//         for(int i=3;i<=n;i++){
//             if(i%2 == 0){
//                 minsteps[i] = minsteps[i/2] + 2;
//                 paste[i].push_back(i/2);
//             }
//             for(int j=i/2;j<i;j++){
//                 for(int k=0;k<paste[j].size();k++){
//                     if((i-j)%paste[j][k] == 0 && minsteps[i] >= minsteps[j] + (i-j)/paste[j][k]){
//                         if(minsteps[i] > minsteps[j] + (i-j)/paste[j][k]){
//                             paste[i].clear();
//                             paste[i].push_back(paste[j][k]);
//                         }else{
//                             paste[i].push_back(paste[j][k]);
//                         }
//                         minsteps[i] = minsteps[j] + (i-j)/paste[j][k];
                        
//                     }
//                 }
//             }
//         }
//         return minsteps[n];
//    }
};
