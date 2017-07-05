

/*
使用139 word break
*/
class Solution { 
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        unordered_set<string> dict(words.begin(),words.end());
        if(words.size()<=2)
            return {};
        vector<string> ans;
        for(auto word : words){
            dict.erase(word);
            int n = word.size();
            if(n == 0)
                continue;
            vector<bool> dp(n+1,false);
            dp[0] = true;
            for(int i=1;i<=n;i++){
                for(int j=0;j<i;j++){
                    if(dp[j] && dict.count(word.substr(j,i-j))){
                        dp[i] = true;
                        break;
                    }
                        
                }
            }
            if(dp[n])
                ans.push_back(word);
            dict.insert(word);
        }
        return ans;
    }
};
