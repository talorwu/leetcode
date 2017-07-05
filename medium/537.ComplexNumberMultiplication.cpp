class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        int a1=0,ai=0,b1=0,bi=0;
        bool flag = true;
        int i = 0;
        if(a[i] == '-'){
            flag = false;
            i++;
        }
        for(;a[i] != '+';i++)
            a1 = a1 * 10 + a[i]-'0';
        if(!flag)
            a1 = -a1;
        flag = true;
        if(a[i+1] == '-'){
            flag = false;
            i++;
        }
        for(i+=1;a[i]!='i';i++){
            ai = ai*10 + a[i]-'0';
        }
        if(!flag)
            ai = -ai;
        flag = true;
        i = 0;
        if(b[i] == '-'){
            flag = false;
            i++;
        }
        for(;b[i]!='+';i++)
            b1 = b1*10 + b[i]-'0';
        if(!flag)
            b1 = -b1;
        flag = true;
        if(b[i+1] == '-'){
            flag = false;
            i++;
        }
        for(i+=1;b[i]!='i';i++)
            bi = bi*10 + b[i]-'0';
        if(!flag)
            bi = -bi;
        //cout<<a1<<' '<<ai<<' '<<b1<<' '<<bi<<endl;
        return to_string(a1*b1-ai*bi)+'+'+to_string(ai*b1+a1*bi)+'i';
    }
};
