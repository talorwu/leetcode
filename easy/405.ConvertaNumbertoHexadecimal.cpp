class Solution {
public:
    string toHex(int num) {
        string ans = "";
        if(num == 0) return "0";
        int count = 0;
        char map[] = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'};
        while(num != 0 && count < 8){
            //cout<< num<<endl;
            ans = map[num & 15] + ans;
            num >>= 4;
            count += 1;
        }
        return ans;
    }
};
