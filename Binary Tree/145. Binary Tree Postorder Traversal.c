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
int getNumberNodes(struct TreeNode *root)
{
    if (root == NULL)
    {
        return 0;
    }

    return 1 + getNumberNodes(root->left) + getNumberNodes(root->right);
}

void traversal(struct TreeNode *root, int *arra, int *index)
{
    if (root == NULL)
    {
        return;
    }

    traversal(root->left, arra, index);
    traversal(root->right, arra, index);
    arra[*index] = root->val;
    *index += 1;

    return;
}
int *postorderTraversal(struct TreeNode *root, int *returnSize)
{
    // create an array here

    int numberNodes = getNumberNodes(root);
    *returnSize = numberNodes;
    int index = 0;

    int *arra = (int *)malloc(numberNodes * sizeof(int));
    traversal(root, arra, &index);

    return arra;
}