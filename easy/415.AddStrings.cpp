class Solution {
public:
    string addStrings(string num1, string num2) {
        int len1 = num1.length()-1;
        int len2 = num2.length()-1;
        int carry = 0;
        string ans = "";
        while(len1>=0 || len2>=0 || carry){
            int tmp = carry;
            if(len1 >= 0) {tmp+=num1[len1]-'0';len1--;}
            if(len2 >= 0) {tmp+=num2[len2]-'0';len2--;}
            carry = tmp/10;
            tmp %= 10;
            ans += to_string(tmp);
            
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
