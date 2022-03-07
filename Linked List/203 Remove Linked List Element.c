struct ListNode* removeElements(struct ListNode* head, int val)
{
    if (head == NULL)
    {
        return NULL;
    }
    
    struct ListNode* ptr1 = head;
    struct ListNode* ptr2 = NULL;
    
    
    while (ptr1 != NULL)
    {
        if (head->val == val)
        {
            head = head->next; //remove this current node; and assign a new head;
            ptr1 = head;
        }
        else if (ptr1->val == val) 
        {
            struct ListNode* temp = ptr1->next;
            ptr2 ->next = temp;
            ptr1 = temp;
        }
        else 
        {
            ptr2 = ptr1;
            ptr1 = ptr1->next;
            
        }
    }
    
    return head;

}