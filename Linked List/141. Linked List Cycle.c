/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) 
{
    struct ListNode* ptr1 = head;
    struct ListNode* ptr2 = head;
    if (!head)
    {
        return false;
    }
    if (ptr1->next == NULL)
    {
    
        return false;
    }
    ptr2 = ptr2->next->next;
    if (ptr2 == NULL)
    {
        return false;
    }
    
    while (ptr2 != NULL && ptr2->next != NULL)
    {
        if (ptr1!=ptr2)
        {
            ptr1= ptr1->next;
            ptr2= ptr2->next->next;
            
        }
        else 
        {
            return true;
        }
        
        
    }
    return false;
    
}