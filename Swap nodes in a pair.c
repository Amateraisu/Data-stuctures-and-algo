/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *swapPairs(struct ListNode *head)
{

    struct ListNode *ptr2 = NULL;
    struct ListNode *ptr1 = NULL;
    struct ListNode *last = NULL;
    struct ListNode *next = NULL;
    struct ListNode *prev = NULL;

    int counter = 0;

    if (head == NULL)
    {
        return NULL;
    }

    if (head->next == NULL)
    {
        return head;
    }

    ptr1 = head;
    ptr2 = head;
    next = ptr1->next;

    // if there are only 2 nodes in the list

    if (ptr2->next->next == NULL)
    {
        // just swap the 2 nodes;
        next->next = ptr1;
        ptr1->next = NULL;
        head = next;

        return head;
    }

    while (ptr2 != NULL)
    {
        // for odd numbered list nodes

        if (ptr2->next != NULL)
        {
            ptr1 = ptr2;
            next = ptr1->next;

            // remember the node to link to after reversing

            // this is setting the next 2 nodes
            ptr2 = ptr2->next->next;

            // reverse 2 nodes here;

            next->next = ptr1;

            // setting new head
            if (counter == 0)
            {
                head = next;
            }

            // linking the current 2 reversed nodes to the next node

            if (ptr2 != NULL && ptr2->next != NULL)
            {
                ptr1->next = ptr2->next;
                // ptr1 = ptr2;
                // next = ptr1->next;
            }

            else
            {
                ptr1->next = ptr2; // because ptr2 is already NULL;
            }

            counter += 1;
        }
        else
        {
            ptr1->next = ptr2; // for odd lists
            ptr2 = ptr2->next; // to  break out of the while loop
        }
    }

    return head;
}