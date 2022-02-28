/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseBetween(struct ListNode* head, int left, int right)
{
    struct ListNode* prev = NULL;
    struct ListNode* current = head;
    struct ListNode* next = NULL;
    struct ListNode* p1 = NULL;
    struct ListNode* p2 = NULL;
    
    
    //counter 
    int counter = 1;
    //reverse right - left times 
    
    if (head == NULL || left==right)
    {
        return head;
    }
    
    while (counter<left)
    {
        prev = current;
        current = current->next;
        counter++;
    }
    
    p1 = prev;
    prev = NULL;
    
    p2 = current;

    for (int i = 0 ; i <= (right - left);i++)
    {
        next = current -> next;
        current->next = prev;
        prev = current;
        current = next;      

    }
    if (counter == 1)
    {
        head = prev;
    }
    else 
    {
        p1->next = prev;
    }
    p2->next = current;
    
    
    return head;
    
    

}