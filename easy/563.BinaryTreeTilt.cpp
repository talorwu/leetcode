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
    int tilt = 0;
public:
    int findTilt(TreeNode* root) {
        calSum(root);
        return tilt;
        
    }
    int calSum(TreeNode* node){
        if(node == NULL)
            return 0;
        int left = calSum(node->left);
        int right = calSum(node->right);
        tilt += abs(left-right);
        return left+right+node->val;
    }
    
};
