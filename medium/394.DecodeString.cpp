/*

stack
*/

class Solution {
public:
    string decodeString(string s) {
        string ans = "";
        stack<string> mystack;
        int i=0;
        while(i<s.length()){
            string tmp = "";
            if(s[i] != ']'){
                if(!isdigit(s[i])){
                    tmp = s[i];
                    i++;
                }else{
                    while(isdigit(s[i])){
                        tmp+=s[i];
                        i++;
                    }
                }
                
                mystack.push(tmp);
                //cout<<tmp<<endl;
            }else{
                string sstr = "";
                while(mystack.top() != "["){
                    sstr = mystack.top()+sstr;
                    mystack.pop();
                }
                mystack.pop();
                string k = mystack.top();
                //cout<<k<<endl;
                mystack.pop();
                sstr = helper(k,sstr);
                cout<<k<<' '<<sstr<<endl;
                mystack.push(sstr);
                i++;
            }
        }
        //string ans = "";
        while(mystack.size()>0){
            ans = mystack.top()+ans;
            mystack.pop();
        }
        return ans;
    }
    string helper(string k,string sstr){
        int n = stoi(k);
        string ans = "";
        while(n--){
            ans += sstr;
        }
        return ans;
    }
};
