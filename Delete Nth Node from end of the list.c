/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// Approach 1:
// first find the total number of nodes. Then take sum - n and delete the nth node from the start

// Approach 2: (2 ptr approach)
// maintain an nth distance between ptr 1 and ptr 2. Then keep iterating until ptr 2 == NULL
// remove the node that ptr 1 is pointing to

struct ListNode *removeNthFromEnd(struct ListNode *head, int n)
{

    struct ListNode *ptr1 = head;
    struct ListNode *prev = head;
    struct ListNode *ptr2 = head;
    struct ListNode *counter = head;
    int current_index = 0;
    int nodes = 0;

    int position = n;

    while (counter != NULL)
    {
        nodes++;
        counter = counter->next;
    }

    // if there is only 1 node

    if (nodes == 1)
    {
        return NULL;
    }
    while (n != 0)
    {
        ptr2 = ptr2->next;
        n--;
    }

    // start iterating here

    // for general cases

    while (ptr2 != NULL)
    {
        prev = ptr1;
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }

    // if remove from start of the list
    if (position == nodes)
    {

        prev = ptr1;

        ptr1 = ptr1->next;

        head = ptr1;
    }

    if (prev->next != NULL)
    {
        prev->next = prev->next->next;

        return head;
    }

    return head;
}