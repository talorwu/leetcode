class Solution {
public:
    int distributeCandies(vector<int>& candies) {
        unordered_map<int,int> map;
        for(auto candy : candies){
            if(map.find(candy) == map.end()){
                map[candy] = 1;
            }else{
                map[candy] += 1;
            }
        }
        if(map.size() >= candies.size()/2)
            return candies.size()/2;
        return map.size();
    }
};
