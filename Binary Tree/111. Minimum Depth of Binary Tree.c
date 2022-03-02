/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#include <limits.h>
int mindepth = INT_MAX;

int getmin(struct TreeNode *root, int current)
{
    if (root == NULL)
    {
        return 0;
    }

    int left = getmin(root->left, current + 1);
    int right = getmin(root->right, current + 1);

    if (left == 0 && right == 0)
    {
        if (current < mindepth)
        {
            mindepth = current;
        }
    }

    return 1;
}

int minDepth(struct TreeNode *root)
{
    if (root == NULL)
    {
        return 0;
    }
    mindepth = INT_MAX;

    int min = getmin(root, 1);

    return mindepth;
}