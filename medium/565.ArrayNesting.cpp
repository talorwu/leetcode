 class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int n = nums.size();
        bool used[n];
        memset(used,false,sizeof(used));
        int res = 0;
        
        for(int i=0;i<n;i++){
            if(used[i]) continue;
            int tmp = 0;
            int j = nums[i];
            do{
                used[j] = true;
                tmp+=1;
                j = nums[j];
            }while(j!=nums[i]);
            res = max(res,tmp);
            
        }
        return res;
    }
};
