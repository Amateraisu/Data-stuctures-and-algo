/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* oddEvenList(struct ListNode* head)
{
    if (head == NULL)
    {
        return NULL;
    }
    struct ListNode* oddPtr = head;
    struct ListNode* oddHead = head;
    struct ListNode* evenPtr = head;
    struct ListNode* evenHead = head;
    int firstOdd = 0;
    int firstEven =0;
    int index = 1;
    
    struct ListNode* current = head;
    
    while ( current != NULL)
    {

        if (index %2 ==0)//even index
        {
            if (firstEven ==0)
            {
                evenHead = current;
                evenPtr = current;
                firstEven++;
            }
            else 
            {
                evenPtr->next = current;
                evenPtr= evenPtr->next;
                
            }      
        }
        else //odd index 
        {
            if (firstOdd == 0)
            {

                oddHead = current;
                oddPtr = current;
                firstOdd++;
            }
            else 
            {
                oddPtr->next = current;
                oddPtr= oddPtr->next;
            }

        }
        current = current->next;
        
        index++;
    };
    //connect the odd FIRST then even
    oddPtr->next = evenHead;
    evenPtr->next = NULL;
    
    return head;
     
    
    

}