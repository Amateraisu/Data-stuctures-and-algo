/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int universal = 0;

int isUnival(struct TreeNode *root)
{
    if (root == NULL)
    {
        return 1;
    }
    int left = isUnival(root->left);
    int right = isUnival(root->right);
    if (root->val != universal)
    {
        return 0;
    }

    if (left && right)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

bool isUnivalTree(struct TreeNode *root)
{
    universal = root->val;
    int boolean = isUnival(root);
    if (boolean)
    {
        return true;
    }
    else
    {
        return false;
    }
}