/*
hashmap  也可以
*/

class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        int n = wall.size();
        int length = 0;
        for(int i=0;i<wall[0].size();i++)
            length+=wall[0][i];
        int rows[n];
        int steps[n];
        memset(rows,0,sizeof(rows));
        memset(steps,0,sizeof(steps));
        int k = 0;
        int res;
        int ans = n;
        
        while(k<length){
            k = help(rows,steps,wall,res,n,length);
            //cout<<k<<' '<<res<<endl;
            if(k==length)
                break;
            ans = min(res,ans);    
        }
        return ans;
    }
    int help(int row[],int steps[],vector<vector<int>>& wall,int &res,int n,int length){
        int ans = INT_MAX;
        for(int i=0;i<n;i++){
            ans = min(ans,row[i]);
        }
        if(ans == length)
            return ans;
        res = n;
        for(int i=0;i<n;i++){
            if(row[i] == ans){
                res-=1;
                row[i]+=wall[i][steps[i]];
                if(steps[i] < wall[i].size()-1)
                    steps[i]+=1;
            }
                
        }
        if(ans == 0)
            res = n;
        return ans;
    }
};
