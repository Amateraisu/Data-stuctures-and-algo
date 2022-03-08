// I want to get eveything into an array and compare the leaf array;

int countNodes(struct TreeNode *root)
{
    if (root == NULL)
    {
        return 0;
    }

    int left = countNodes(root->left);
    int right = countNodes(root->right);

    return 1 + left + right;
}

void getarray(struct TreeNode *root, int *arra, int *index)
{
    if (root == NULL)
    {
        return;
    }
    getarray(root->left, arra, index);
    getarray(root->right, arra, index);

    if (root->left == NULL && root->right == NULL)
    {
        arra[*index] = root->val;
        *index += 1;
    }

    return;
}

bool leafSimilar(struct TreeNode *root1, struct TreeNode *root2)
{
    int numberOfRoot1 = countNodes(root1);
    int numberOfRoot2 = countNodes(root2);
    int index1 = 0;
    int index2 = 0;
    int *arra1 = (int *)malloc(numberOfRoot1 * sizeof(int));
    int *arra2 = (int *)malloc(numberOfRoot2 * sizeof(int));

    getarray(root1, arra1, &index1);
    getarray(root2, arra2, &index2);
    // printf("arra1 %d\n", arra1[0]);
    // printf("arra2 %d\n", arra2[0]);
    // printf("This is index1 %d\n", index1);

    for (int i = 0; i < index1; i++)
    {
        // printf("arra1 %d\n", arra1[i]);
        // printf("arra2 %d\n", arra2[i]);
        index2--;
        if (arra1[i] != arra2[i])
        {
            return false;
        }
    }
    if (index2 != 0)
    {
        return false;
    }

    return true;
}