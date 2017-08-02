/*
fa = max(left,right,left的深度+right深度+1)
*/


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
    int diameterOfBinaryTree(TreeNode* root) {
        if(root == NULL)
            return 0;
        vector<int> ans = dfs(root);
        
        return ans[0]-1;
    }
    
    vector<int> dfs(TreeNode *node){
        vector<int> ans(2,0); //ans[0] 长度，ans[1] 深度
        if(node == NULL)
            return ans;
        if(!node->left && !node->right){
            ans[0] = 1;
            ans[1] = 1;
            return ans;
        }
        vector<int> l = dfs(node->left);
        vector<int> r = dfs(node->right);
        ans[0] = max(max(l[0],r[0]),l[1]+r[1]+1);
        ans[1] = max(l[1],r[1])+1;
        return ans;
    }
};
