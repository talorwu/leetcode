/*

记忆化搜索
*/

class Solution {
public:
    vector<int> diffWaysToCompute(string input){
        int n = input.size();
        vector<vector<vector<int> > > dp(n,vector<vector<int> >(n,vector<int>(0,0)));
        vector<int>res = diffWaysToCompute1(input,0,n-1,dp);
        // for(int i=0;i<dp.size();i++){
        //     for(int j=0;j<dp[i].size();j++){
        //         for(int k=0;k<dp[i][j].size();k++)
        //             cout<<i << ' ' << j<<' '<< dp[i][j][k]<< ' ';
        //         cout<<endl;
        //     }
        // }
        return res;
    }
    vector<int> diffWaysToCompute1(string input,int start,int end,vector<vector<vector<int>>>& dp) {
        //cout<<"************************"<<endl;
        //cout<<"start = "<<start<<"; end = "<<end<<"; dp[start][end].size() = "<<dp[start][end].size()<<endl;
        if(dp[start][end].size() != 0)
            return dp[start][end];
        vector<int> ret;
        for(int i = start; i <= end; i ++)
        {
            if(input[i] == '+' || input[i] == '-' || input[i] == '*')
            {
                vector<int> left = diffWaysToCompute1(input,start,i-1,dp);
                //if(dp[start][i-1].size() != 0) dp[start][i-1] = left;
                
                vector<int> right = diffWaysToCompute1(input,i+1,end,dp);
                //if(dp[i+1][end].size() != 0) dp[i+1][end] = right;
                for(int j = 0; j < left.size(); j ++)
                {
                    for(int k = 0; k < right.size(); k ++)
                    {
                        if(input[i] == '+')
                            ret.push_back(left[j] + right[k]);
                        else if(input[i] == '-')
                            ret.push_back(left[j] - right[k]);
                        else
                            ret.push_back(left[j] * right[k]);
                    }
                }
            }
        }
        
        if(ret.empty())
            ret.push_back(atoi(input.substr(start,end+1).c_str()));
        //cout<<"ret:"<<start<< ' '<<end<< '=';
        // for(int i =0;i<ret.size();i++)
        //     cout<<ret[i]<<' ';
        //cout<<endl;
        dp[start][end] = ret;
        return ret;
    }
};
