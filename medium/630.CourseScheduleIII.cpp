/*
思路：贪心，先按照结束时间排序，然后遍历，如果下一个course可以加入就加入，如果下一个course不可以加入，但是持续时间不是前面所有的最长的，
	那说明可以用这一个course替换之前加入的最长的course，这样做以后会使得前面所有的course结束时间提前，使得可能后面的更多的course可以加入进来
*/
class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        sort(courses.begin(),courses.end(),[](vector<int> a,vector<int> b){return a[1] < b[1];});
        priority_queue<int> heap;
        int time = 0;
        for(int i=0;i<courses.size();i++){
            heap.push(courses[i][0]);
            time += courses[i][0];
            if(time > courses[i][1]){
                time -= heap.top();
                heap.pop();
            }
        }
        return heap.size();
    }
};
