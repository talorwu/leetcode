/*
贪心：每一次遇见R，他总会废掉下一个D，对于D一样的处理
*/

class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> q1,q2;
        int n = senate.size();
        for(int i=0;i<n;i++)
            senate[i] == 'R'?q1.push(i):q2.push(i);
        while(!q1.empty() && !q2.empty()){
            int r,d;
            r = q1.front();
            d = q2.front();
            q1.pop();q2.pop();
            r < d?q1.push(r+n):q2.push(d+n);
        }
        return q1.size() > q2.size()?"Radiant":"Dire";
    }
};
