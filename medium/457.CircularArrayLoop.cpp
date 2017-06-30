/*
思路：先先处理数组变成0～n-1的数，然后处理，访问过得变为0
*/

class Solution {
public:
    bool circularArrayLoop(vector<int>& nums) {
        int n = nums.size();
        for(int i=0;i<n;i++)
            nums[i] = nums[i]%n;
        int flag = true;
        for(int i=0;i<n;i++){
            if(nums[i] == 0)
                continue;
            int start = i;
            int next = ((i+nums[i])%n+n)%n;
            //nums[i] = 0;
            flag = true;
            if(nums[next] == 0)
                flag = false;
            while(nums[next] != 0){
                if(nums[i]*nums[next]<=0)
                    flag = false;
                int tmp = nums[next];
                nums[next] = 0;
                next = ((next+tmp)%n+n)%n;
                
                
            }
            nums[i] = 0;
            //cout<<i<<' '<<flag<<endl;
            if(flag)
                return true;
        }
        return false;
    }
};
