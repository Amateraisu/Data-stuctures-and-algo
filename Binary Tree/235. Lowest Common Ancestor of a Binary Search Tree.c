/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// Time complexity is O(n) space complexity O(n)

struct TreeNode *lowestCommonAncestor(struct TreeNode *root, struct TreeNode *p, struct TreeNode *q)
{
    if (root == NULL)
    {
        return NULL;
    }

    struct TreeNode *left = lowestCommonAncestor(root->left, p, q);
    struct TreeNode *right = lowestCommonAncestor(root->right, p, q);

    if (root == p || root == q)
    {
        return root;
    }

    if (left != NULL && right != NULL)
    {
        return root;
    }
    else if (left != NULL && right == NULL)
    {
        return left;
    }
    else if (right != NULL && left == NULL)
    {
        return right;
    }

    return NULL;
}