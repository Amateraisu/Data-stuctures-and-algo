/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// brute force way. 
// O(n*logn) = O(nlogn) O(logn) space 
// better approach 
// O(n + n) = O(2n) = O(n) time complexity. O(1); 

int getNumber(struct TreeNode* root)
{
    if (root == NULL)
    {
        return 0;
    }
    
    return 1+ getNumber(root->left) + getNumber(root->right);
}

void traverseToArray(struct TreeNode* root, int* arra, int* index)
{
    if (root == NULL)
    {
        return;
    }
    
    traverseToArray(root->left, arra, index);
    arra[*index] = root->val;
    *index +=1 ;
    traverseToArray(root->right, arra, index);
    
    return;
    
}


bool findTarget(struct TreeNode* root, int k)
{
    
    int size = getNumber(root);
    int* newarra = (int*)malloc(size*sizeof(int));
    int index = 0;
    traverseToArray(root,newarra, &index);
    int ptr1 = 0;
    int ptr2 = size-1;
    
    int target = k;
    int sum =0;
    
    while (ptr1 <ptr2)
    {
        sum = newarra[ptr1] + newarra[ptr2];
        if (sum<target)
        {
            ptr1++;
        }
        else if (sum>target)
        {
            ptr2--;
        }
        else if (sum == k)
        {
            return true;
        }
    }
    
    return false;
    
    

}