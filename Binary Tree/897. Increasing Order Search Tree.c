/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int countNodes(struct TreeNode *root)
{

    if (root == NULL)
        return 0;
    else
        return 1 + countNodes(root->left) + countNodes(root->right);
}

void getInOrderArray(int *array, int *ind, struct TreeNode *root)
{

    if (root == NULL)
        return;

    else
    {

        getInOrderArray(array, ind, root->left);
        array[*ind] = root->val;
        *ind += 1;
        getInOrderArray(array, ind, root->right);
    }
}

struct TreeNode *createNewNode(int value)
{

    struct TreeNode *root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->val = value;
    root->left = NULL;
    root->right = NULL;
    return root;
}

struct TreeNode *createTreeFromArray(int *array, int arraySize)
{

    if (arraySize == 0)
        return NULL;

    else
    {

        int i = 0;
        struct TreeNode *currentRoot = createNewNode(0);
        struct TreeNode *refRoot = currentRoot;
        while (i < arraySize)
        {

            currentRoot->right = createNewNode(array[i]);
            currentRoot = currentRoot->right;
            i++;
        }

        return refRoot->right;
    }
}

struct TreeNode *increasingBST(struct TreeNode *root)
{

    if (root == NULL)
        return NULL;

    else
    {

        int index = 0;
        int count = countNodes(root);
        int *inOrderArray = (int *)malloc(count * sizeof(int));
        getInOrderArray(inOrderArray, &index, root);
        return createTreeFromArray(inOrderArray, count);
    }
}