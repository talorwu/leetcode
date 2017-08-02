/*

比较痛苦的是，优先队列lamda表达式的写法：    
priority_queue<State*,vector<State*>,function<bool(const State*,const State*)>> pq([](const State* s1, const State* s2){return s1->hValue>s2->hValue;});
*/


class Twitter {
    struct Tweet{
        int time;
        int id;
        Tweet(int time,int id): time(time),id(id) {};
    };
    unordered_map<int,vector<Tweet>> tweets;
    unordered_map<int,set<int>> followings;
    int time;
public:
    /** Initialize your data structure here. */
    Twitter() : time(0){
        
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        // if(tweets.find(userId) == tweets.end()){
        //     tweets[userId] = Vector(Tweet(time++,tweetId));
        // }else{
        //     tweets[userId].insert(tweets[userId].begin(),new Tweet(time++,tweetId));
        // }
        Tweet t(time++,tweetId);// = new Tweet(time++,tweetId);
        tweets[userId].insert(tweets[userId].begin(),t);
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        set<int> users = followings[userId];
        users.insert(userId);
        vector<int> ans;
        int n = 0;
        priority_queue<
            pair<Tweet *,Tweet *>,
            vector<pair<Tweet *,Tweet *>>, 
            function<bool(const pair<Tweet *,Tweet *>,const pair<Tweet *,Tweet *>)>> heap([](pair<Tweet *,Tweet *> a,pair<Tweet *,Tweet *> b){return a.first->time < b.first->time;});
        
        for(auto user : users){
            //cout<<tweets[user].empty()
            if(!tweets[user].empty())
                heap.push(make_pair(&(tweets[user][0]),&(tweets[user][tweets[user].size()-1])));
        }
        while(!heap.empty() && n < 10){
            pair<Tweet *,Tweet *> t = heap.top();
            heap.pop();
            ans.push_back(t.first->id);
            n++;
            if(++t.first <= t.second)
                heap.push(make_pair(t.first,t.second));
        }
        return ans;
        
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        if (followerId != followeeId)
            followings[followerId].insert(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        followings[followerId].erase(followeeId);
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * vector<int> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
