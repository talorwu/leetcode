/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        queue<TreeNode*> q;
        vector<double> ans;
        //ans.push_back(root->val);
        q.push(root);
        while(!q.empty()){
            int len = q.size();
            double sum = 0.0;
            for(int i=0;i<len;i++){
                TreeNode* node = q.front();
                sum += node->val;
                q.pop();
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
                
            }
            ans.push_back(sum/len);
        }
        return ans;
    }
};
