/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int getTreeSize(struct TreeNode* root)
{
    if (root == NULL)
    {
        return 0;
    }
    return getTreeSize(root->left) + getTreeSize(root->right) + 1;
}

void arrayset(struct TreeNode* root, int* arr, int* index)
{
    if (root == NULL){
        return;
    }
    
    arrayset(root->left, arr, index);
    arr[*index] = root->val;
    *index+=1;
    arrayset(root->right, arr, index);
    
    
}
int* inorderTraversal(struct TreeNode* root, int* returnSize)
{
    int size = getTreeSize(root);
    *returnSize = size;
    int* arra = (int*)malloc(size* sizeof(int));
    int index = 0;
    arrayset(root, arra, &index );
    
    
    return arra;

}