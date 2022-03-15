int getNum(struct TreeNode* root)
{
    if (root == NULL)
    {
        return 0;
    }
    
    return 1+getNum(root->left) + getNum(root->right);
}
void treeToArray(struct TreeNode* root, int* arra, int* currentIndex)
{
    if (root == NULL)
    {
        return ;
    }
    
    treeToArray(root->left, arra, currentIndex);
    arra[*currentIndex]  = root->val;
    *currentIndex +=1;
    treeToArray(root->right, arra, currentIndex);
    
    
    return;
}
int* getAllElements(struct TreeNode* root1, struct TreeNode* root2, int* returnSize)
{
    int size1 = getNum(root1);

    int size2 = getNum(root2);
   
    int total = size1+size2;
    int root1arra[size1];
    int root2arra[size2];
    int* totalarra = (int*)malloc(total* sizeof(int));
    int index1 = 0;
    int index2 = 0;
    int index3 = 0;

    *returnSize = total;
    treeToArray(root1, root1arra, &index1);
    treeToArray(root2, root2arra, &index2);
    

    
    //now use 2 pointer to combine.
    
    index1 = 0;
    index2 = 0;
    
    while (index1 != size1 && index2  != size2)
    {
        if (root1arra[index1] < root2arra[index2])
        {

            totalarra[index3] =  root1arra[index1];

            index3++;
            index1++;
            
        }
        else
        {
            
            totalarra[index3] =  root2arra[index2];

            index3++;
            index2++;
            
        }
    }

    while (index1 != size1)
    {

        totalarra[index3] = root1arra[index1];

       
        index1++;
        index3++;

    }
    
    while (index2 != size2)
    {
        
        totalarra[index3] = root2arra[index2];
        index2++;
        index3++;
    }
    

    return totalarra;

    
}