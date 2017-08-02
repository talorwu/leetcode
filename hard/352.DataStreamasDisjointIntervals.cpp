/*

思路：我们需要保存一个输入数据流的有序状态，排序的话是nlogn 如果用BST,每次插入只有logn时间
*/



/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class SummaryRanges {
    set<int> tree;
public:
    /** Initialize your data structure here. */
    SummaryRanges() {
        
    }
    
    void addNum(int val) {
        tree.insert(val);
    }
    
    vector<Interval> getIntervals() {
        vector<Interval> ans;
        int start = *tree.begin();
        int end = start;
        for(set<int>::iterator it=++tree.begin(); it!=tree.end(); ++it){
            if(end == *it-1){
                end++;
            }else{
                Interval in(start,end);
                ans.push_back(in);
                start = *it;
                end = start;
            }
        }
        cout<<start<<' '<<end<<endl;
        if(ans.size() == 0 || !(ans.back().start == start && ans.back().end == end)){
            Interval in(start,end);
            ans.push_back(in);
        }
        return ans;
    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * vector<Interval> param_2 = obj.getIntervals();
 */
