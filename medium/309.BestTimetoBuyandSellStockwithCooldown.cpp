//https://discuss.leetcode.com/topic/30421/share-my-thinking-process/2

class Solution {
public:
    int maxProfit(vector<int>& prices){
        // buy[i] = max(sell[i-2]-price, buy[i-1])
        // sell[i] = max(buy[i-1]+price, sell[i-1])
        int pbuy=INT_MIN,buy=INT_MIN,sell=0,psell=0;
        for(auto price : prices){
            pbuy = buy;
            buy = max(psell-price,buy);
            psell = sell;
            sell = max(pbuy+price,sell);
        }
        return sell;

    }

//超时
    // int maxProfit(vector<int>& prices) {
    //     int n = prices.size();
    //     return help(prices,0,n-1);
    // }
    
    // int help(vector<int>& prices,int left,int right){
    //     if(right - left < 1)
    //         return 0;
    //     int ans = prices[right] - prices[left];
    //     // if(check(prices,left,right))
    //     //     return ans;
    //     for(int cool = left;cool<=right;cool++){
    //         if(cool == right || prices[cool] >= prices[cool+1] || (prices[cool-1]>=prices[cool])){
    //             ans = max(ans,help(prices,left,cool-1)+help(prices,cool+1,right));
    //         }
    //     }
    //     return ans;
        
    // }

};	
