class Solution {
public:
    ListNode* rev(ListNode* head) {

        ListNode* prev = NULL;
        ListNode* ptr = head;
        while (ptr) {
            ListNode* next = ptr->next;
            ptr->next = prev;
            prev = ptr;
            ptr = next;
        }
        return prev;
    }
    ListNode* doubleIt(ListNode* head) {
        ListNode* nhead = rev(head);
        int c = 0;
        ListNode* ptr = nhead;
        ListNode* prev = NULL;
        while (c || ptr) {
            int n = ptr->val * 2;
            int total = n + c;
            int nNumber = total % 10;
            ptr->val = nNumber;
            c = total / 10;

            if (c && !ptr->next) {
                ptr->next = new ListNode(0);
            }
            ptr = ptr->next;



        }



        return rev(nhead);

    }
};