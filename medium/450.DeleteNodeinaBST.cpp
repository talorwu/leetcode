/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

//非递归
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        
        //memset(root,null,sizeof(root));
        //cout<<root<<' '<<root->val<<endl;
        TreeNode *pren = NULL,*node  = root;
        int flag = 0;//left;
        //search
        while(node){
            if(key == node->val)
                break;
            if(key > node->val){
                pren = node;
                node = node->right;
                flag = 1;
            }
            else{
                pren = node;
                node = node->left;
                flag = 0;
            }
        }
        if(node == NULL)
            return root;
        //delete
        if(node->right == NULL && node->left == NULL){  // it is a leaf
            if(pren == NULL)
                return NULL;
            if(flag == 0)
                pren->left = NULL;
            else
                pren->right = NULL;
        }else if(node->left == NULL){
            TreeNode *pre = node,*tmp = node->right;
            while(tmp->left){
                pre = tmp;
                tmp = tmp->left;
            }
            node->val = tmp->val;
            //tmp = tmp->right;
            if(pre != node)
                pre->left = tmp->right;
            else
                pre->right = tmp->right;
            
        }else{
            TreeNode *pre = node,*tmp = node->left;
            while(tmp->right){
                pre = tmp;
                tmp = tmp->right;
            }
            node->val = tmp->val;
            if(pre != node)
                pre->right = tmp->left;
            else
                pre->left = tmp->left;
            
        }
         return root;
    }
};
