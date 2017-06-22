class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int count = 0;
        int add = 0;
        for(int i=2;i<A.size();i++){
            if(A[i-1]-A[i-2] == A[i]-A[i-1])
                count += ++add;
            else
                add = 0;
        }
        return count;
    }
};
