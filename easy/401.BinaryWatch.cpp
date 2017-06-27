/*

思路：直接循环所有的时间，然后利用bitset  看里面1的个数是否等于num
*/

class Solution {
public:
    vector<string> readBinaryWatch(int num) {
        vector<string> res;
        for(int i=0;i<12;i++){
            for(int j=0;j<60;j++){
                if(bitset<10>(i<<6|j).count()==num){
                    res.push_back(to_string(i)+(j>=10?":":":0")+to_string(j));
                }
            }
        }
        return res;
    }
};
