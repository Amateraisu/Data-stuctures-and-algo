/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int sum = 0;

int getheight(struct TreeNode *root)
{
    if (root == NULL)
    {
        return 0;
    }

    int left = getheight(root->left);
    int right = getheight(root->right);

    if (left > right)
    {
        return left + 1;
    }
    else
    {
        return right + 1;
    }
}

void totalsum(struct TreeNode *root, int height, int current)
{
    if (root == NULL)
    {
        return;
    }

    totalsum(root->left, height, current + 1);
    totalsum(root->right, height, current + 1);

    if (current == height)
    {
        sum += root->val;
    }
}

int deepestLeavesSum(struct TreeNode *root)
{
    sum = 0;
    int height = getheight(root);

    totalsum(root, height, 1);

    return sum;
}