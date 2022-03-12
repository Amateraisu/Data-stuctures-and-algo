bool isSameTree(struct TreeNode *p, struct TreeNode *q)
{
    if (p == NULL && q == NULL)
    {
        return true;
    }
    else if (p == NULL && q != NULL)
    {
        return false;
    }
    else if (p != NULL && q == NULL)
    {
        return false;
    }

    if (p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right))
    {
        return true;
    }
    else
    {
        return false;
    }
}