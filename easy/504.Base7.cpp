class Solution {
public:
    string convertToBase7(int num) {
        string ans = "";
        bool flag = false;
        if(num == 0)
            return "0";
        if(num < 0){
            flag = true;
            ans += "-";
        }
        num = abs(num);
        while(num){
            ans+=to_string(num%7);
            num /= 7;
        }
        if(flag)
            reverse(ans.begin()+1,ans.end());
        else
            reverse(ans.begin(),ans.end());
        return ans;
    }
};
