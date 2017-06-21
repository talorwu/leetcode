/*
思路：left[i]记录i左边的最小值，right[i]记录i右边比left[i]大的最小值
*/

class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int len = nums.size();
        if (len < 3)
            return false;
        int left[len],right[len];  //左边最小值和右边最小值
        left[1] = nums[0];
        for(int i=2;i<len-1;i++){
            left[i] = min(left[i-1],nums[i-1]);
        }
        right[len-1] = INT_MIN;
        for(int i=len-2;i>=1;i--){
            //right[i] = INT_MIN;
            if(right[i+1] > left[i] && nums[i+1] > left[i])
                right[i] = min(right[i+1],nums[i+1]);
            else if(right[i+1] > left[i])
                right[i] = right[i+1];
            else if(nums[i+1] > left[i])
                right[i] = nums[i+1];
            else
                right[i] = INT_MIN;
            
        }
        for(int i=1;i<len-1;i++){
            //cout<<i<<' '<<left[i]<<' '<<nums[i]<<' '<<right[i]<<endl;
            if(nums[i]>left[i] && nums[i]>right[i] && right[i] != INT_MIN)
                return true;
                
        }
        return false;
    }
};
