class Solution {
public:
    int countArrangement(int N) {
        vector<int> a(N);
        bool visited[N];
        for(int i=0;i<N;i++){
            a[i] = i+1;
            visited[i] = false;
        }
        return dfs(N,1,a,visited);
    }
    
    int dfs(int N,int step,vector<int>& a,bool visited[]){
        if(step > N)
            return 1;
        int count = 0;
        for(int i=0;i<a.size();i++){
            if(!visited[i] &&(step%a[i]==0 || a[i]%step==0)){
                visited[i] = true;
                count += dfs(N,step+1,a,visited);
                //cout<<step<<' '<<count<<endl;
                visited[i] = false;
            }
        }
        return count;
    }
};
