/*
思路：寻找前两个数，然后迭代
*/
class Solution {
public:
    bool isAdditiveNumber(string num) {
        int len = num.length();
        if(len < 3) return false;
        int i = 1,j = 2;
        for(i = 1; i<=len/2;i++){
            for(j = i+1;j<=2*len/3;j++){
               // if(a3 == num.substr(j,a3.length()))
                    if(helper(num,i,j))
                        return true;
                
            }
        }
        return false;
    }
    bool helper(string num,int i,int j){
        int len = num.length(),pre = 0;
        long long a1,a2,a3;
        while(1){
            if(i-pre>1 && num[pre] == '0') return false;
            if(j-i>1 && num[i] == '0') return false;
            if(to_string(a1+a2).length()>1 && num[j] == '0') return false;
            a1 = stolong(num.substr(pre,i-pre));
            a2 = stolong(num.substr(i,j-i));
            if(to_string(a1+a2).length()+j>len) return false;
            a3 = stolong(num.substr(j,to_string(a1+a2).length()));
            //cout<<i<<' '<<j<<' '<<a1<<' '<<a2<<' '<<a3<<endl;
            if(a1+a2 != a3)
                return false;
            pre = i;
            i=j;
            j=to_string(a1+a2).length()+j;
            if(j==len)
                return true;
        }
        return false;
    }
    long long stolong(string str) //改一下函数名，变量类型，搞定  
    {  
        long long result;  
        istringstream is(str);  
        is >> result;  
        return result;  
    }  
};
