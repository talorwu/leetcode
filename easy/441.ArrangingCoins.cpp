class Solution {
public:
    int arrangeCoins(int n) {
        int res = 0;
        int step = 1;
        while(n>0){
            n-=step;
            res+=1;
            step+=1;
        }
        return n==0?res:res-1;
    }
};
