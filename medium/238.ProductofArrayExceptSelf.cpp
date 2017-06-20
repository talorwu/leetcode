class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n,1);
        int fromBegin = 1,fromEnd = 1;
        for(int i=0;i<n;i++){
            res[i] *= fromBegin;
            fromBegin *= nums[i];
            res[n-1-i] *= fromEnd;
            fromEnd *= nums[n-1-i];
        }
        return res;
    }
};
