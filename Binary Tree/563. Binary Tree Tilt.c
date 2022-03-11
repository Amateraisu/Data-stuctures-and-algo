/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// O(n)
int getSumOfTree(struct TreeNode *root)
{
    if (root == NULL)
    {
        return 0;
    }

    int left = getSumOfTree(root->left);
    int right = getSumOfTree(root->right);

    return left + right + root->val;
}

// O(n)
void convertToTilt(struct TreeNode *root)
{
    if (root == NULL)
    {
        return;
    }

    int left = getSumOfTree(root->left);
    int right = getSumOfTree(root->right);
    root->val = abs(left - right);

    convertToTilt(root->left);
    convertToTilt(root->right);
}

// O(n^2)
// O(n^2);

int findTilt(struct TreeNode *root)
{
    convertToTilt(root);
    int ans = getSumOfTree(root);

    return ans;
}