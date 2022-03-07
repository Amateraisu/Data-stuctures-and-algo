/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


bool isPalindrome(struct ListNode* head)
{
    int counter = 0;
    
    struct ListNode* ptr = head;
    
    while (ptr != NULL)
    {
        
        counter+=1;
        ptr= ptr->next;
        
    }
    ptr = head;
    int* arra = (int*)malloc(counter* sizeof(int));
    // printf("This is counter %d\n", counter);
    counter = 0;
    while (ptr != NULL)
    {
        // printf("This is stored %d\n", ptr->val);
        arra[counter] = ptr->val;
        // printf("This is stored confirm %d\n", arra[counter]);
        counter+=1;
        ptr= ptr->next;
        
    }
    
    
    
    
    int ptr1 = 0;
    int ptr2 = counter -1;
    
    while (ptr1 <ptr2 && ptr1 != ptr2)
    {
        // printf("Test ptr1 %d\n", arra[ptr1]);
        // printf("Test ptr2 %d\n", arra[ptr2]);
        
        if (arra[ptr1] != arra[ptr2])
        {
            return false;
        }
        ptr1++;
        ptr2--;
    }
    
    return true;

}