/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int rangeSumBST(struct TreeNode* root, int low, int high)
{
    if (root == NULL)
    {
        return 0;
    }
    
    int left = rangeSumBST(root->left, low , high);
    int right = rangeSumBST(root->right, low, high);
    if (root->val <= high && root->val >= low)
    {
        return root->val+left+right;
    }
    else 
    {
        return left + right;
    }
    
    

    
}