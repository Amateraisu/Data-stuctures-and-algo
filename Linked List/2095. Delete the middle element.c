/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteMiddle(struct ListNode* head)
{
    struct ListNode* ptr1 = head;
    struct ListNode* ptr2 = head;
    
    struct ListNode* prev = NULL;
    
    if (head->next == NULL)
    {
        return NULL;
    }
    
    while (ptr2!= NULL && ptr2->next != NULL)
    {
        prev = ptr1;
        ptr1 = ptr1->next;
        ptr2 = ptr2->next->next;
    }
    prev->next = ptr1->next;
    return head;
}