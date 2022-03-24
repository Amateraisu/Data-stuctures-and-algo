struct TreeNode *lowestCommonAncestor(struct TreeNode *root, struct TreeNode *p, struct TreeNode *q)
{
    // so for this question, look for where it converges
    if (root == NULL)
    {
        return NULL;
    }

    struct TreeNode *left = NULL;
    struct TreeNode *right = NULL;

    left = lowestCommonAncestor(root->left, p, q);
    right = lowestCommonAncestor(root->right, p, q);

    if (root->val == p->val || root->val == q->val)
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