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
    vector<string> binaryTreePaths(TreeNode* root) {
        
        string res = "";
        vector<string> results;
        if(root == NULL)
            return results;
        dfs(root,res,results);
        //cout<<res<<endl;
        return results;
    }
    void dfs(TreeNode* node , string res , vector<string>& results){
        if(node->left == NULL && node->right == NULL){
            res+=to_string(node->val);
            results.push_back(res);
            return ;
        }
        if(node->left){
            string t = res+(to_string(node->val)+"->");
            dfs(node->left,t,results);
        }
        if(node->right){
            string t = res+(to_string(node->val)+"->");
            dfs(node->right,t,results);
        }
    }
};
