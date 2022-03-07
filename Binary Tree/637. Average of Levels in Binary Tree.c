int finddepth(struct TreeNode *root)
{
    if (root == NULL)
    {
        return -1;
    }

    int left = finddepth(root->left);
    int right = finddepth(root->right);

    if (left > right)
    {
        return left + 1;
    }
    else
    {
        return right + 1;
    }
}

void findnumber(struct TreeNode *root, int *level, int *array)
{
    if (root == NULL)
    {
        return;
    }

    array[*level] += 1;

    *level += 1;
    findnumber(root->left, level, array);
    findnumber(root->right, level, array);
    *level -= 1;

    return;
}

void arrayfind(struct TreeNode *root, double *array, int *current)
{
    if (root == NULL)
    {
        return;
    }

    array[*current] += (double)root->val;

    *current += 1;

    arrayfind(root->left, array, current);

    arrayfind(root->right, array, current);
    *current -= 1;

    return;
}
double *averageOfLevels(struct TreeNode *root, int *returnSize)
{
    int depth = finddepth(root);
    int current = 0;
    int currents = 0;
    *returnSize = depth + 1;
    double *arra = (double *)malloc(*returnSize * sizeof(double));
    int *nodecount = (int *)malloc(*returnSize * sizeof(int));

    // initialize everything to 0;

    for (int j = 0; j < *returnSize; j++)
    {
        arra[j] = 0;
    }
    for (int j = 0; j < *returnSize; j++)
    {
        nodecount[j] = 0;
    }
    arrayfind(root, arra, &current);
    findnumber(root, &currents, nodecount);

    for (int j = 0; j < *returnSize; j++)
    {

        arra[j] /= nodecount[j];
    }

    return arra;
}