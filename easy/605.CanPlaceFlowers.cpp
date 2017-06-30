class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        flowerbed.insert(flowerbed.begin(),0);
        flowerbed.push_back(0);
        int start = 0;
        int len = flowerbed.size();
        int ans = 0;
        while(start < len){
            //cout<<start<<"!!!"<<endl;
            int count = 0;
            if(flowerbed[start] == 1){
                start++;
                continue;
            }
            while(start<len && flowerbed[start] == 0){
                count ++;
                start ++;
            }
            ans += (count-1)/2;
            //cout<<count<<"###"<<endl;
        }
        return ans>=n;
    }
};
