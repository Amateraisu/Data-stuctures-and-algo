bool isMirror(struct TreeNode *root, struct TreeNode *root2)
{
    if (root == NULL && root2 == NULL)
    {
        return true;
    }
    if (root == NULL && root2 != NULL)
    {
        return false;
    }
    else if (root != NULL && root2 == NULL)
    {
        return false;
    }

    if (isMirror(root->left, root2->right) && isMirror(root->right, root2->left))
    {
        if (root->val == root2->val)
        {
            return true;
        }
    }

    return false;
}

bool isSymmetric(struct TreeNode *root)
{
    if (root == NULL)
    {
        return true;
    }

    return isMirror(root->left, root->right);
}