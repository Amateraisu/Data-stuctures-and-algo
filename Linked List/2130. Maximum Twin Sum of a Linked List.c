/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int pairSum(struct ListNode *head)
{
    // lets do using a linked list
    // use floyd's algorithm to find the middle.

    struct ListNode *ptr1 = head;
    struct ListNode *ptr2 = head;

    while (ptr2 != NULL && ptr2->next != NULL)
    {
        ptr1 = ptr1->next;
        ptr2 = ptr2->next->next;
    }
    // ptr 1 will now be pointing at the first node of the 2ND linked list

    // reverse the 2nd half of the linked list, O(n);

    struct ListNode *prev = NULL;

    struct ListNode *next = NULL;

    while (ptr1 != NULL)
    {

        next = ptr1->next;
        ptr1->next = prev;
        prev = ptr1;
        ptr1 = next;
    }
    // prev will be the head of the 2nd linked list;
    struct ListNode *head2 = prev; // a head2 to REMEMBER the first node of the 2nd LL

    int max = 0;
    int sum = 0;
    struct ListNode *ptr3 = head;
    while (head2 != NULL) // since the number of nodes is even
    {

        sum = head2->val + ptr3->val;
        if (sum > max)
        {
            max = sum;
        }
        head2 = head2->next;
        ptr3 = ptr3->next;
    }

    return max;
}