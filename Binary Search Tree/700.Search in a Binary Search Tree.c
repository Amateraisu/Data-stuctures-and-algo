/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* searchBST(struct TreeNode* root, int val)
{
    if (root == NULL)
    {
        return NULL;
    }
    
    if (root->val == val)
    {
        return root;
    }
    
    struct TreeNode* left = searchBST(root->left, val); //searching left and right trees
    struct TreeNode* right = searchBST(root->right, val); 
    
    if (left != NULL && right == NULL) //exit conditions 
    {
        return left;
    }
    else if (right != NULL && left == NULL)
    {
        return right;
    }
    else 
    {
        return NULL;
    }

}