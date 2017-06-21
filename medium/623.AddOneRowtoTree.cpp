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
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if(d == 1){
            TreeNode *node = new TreeNode(v);
            node->left = root;
            return node;
        }
        deque<TreeNode *> queue;
        queue.push_back(root);
        for(int i=1;i<d-1;i++){
            int len = queue.size();
            for(int j=0;j<len;j++){
                TreeNode* tmp = queue.front();
                queue.pop_front();
                if (tmp->left){
                    queue.push_back(tmp->left);
                }
                if(tmp->right)
                    queue.push_back(tmp->right);
                    
            }
        }
        while(!queue.empty()){
            TreeNode* tmp = queue.front();
            queue.pop_front();
            TreeNode *left = new TreeNode(v);
            left->left = tmp->left;
            tmp->left = left;
            TreeNode *right = new TreeNode(v);
            right->right = tmp->right;
            tmp->right = right;
        }
        return root;

    }
};
