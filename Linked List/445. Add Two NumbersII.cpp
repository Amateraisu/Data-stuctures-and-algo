/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;
        ListNode* n1 = reverse(l1);
        ListNode* n2 = reverse(l2);
        int carry = 0;
        ListNode* dummy = new ListNode();
        ListNode* ptr = dummy;
        cout << n1->val << n2->val << '\n';
        int num1, num2;
        while (n1 || n2 || carry) {

            if (n1) {
                num1 = n1->val;
            } else {
                num1 = 0;
            }
            if (n2) {
                num2 = n2->val;
            } else {
                num2 = 0;
            }
            int num = num1 + num2 + carry;
            if (num >= 10) {
                carry = 1;
            } else {
                carry = 0;
            }
            int cur = num % 10;
            ptr->next = new ListNode(cur);
            ptr = ptr->next;
            if (n1) n1 = n1->next;
            if (n2) n2 = n2->next;

        }
        ListNode* start = dummy->next;
        dummy->next = NULL;
        return reverse(start);



    }

    ListNode* reverse(ListNode* root) {
        ListNode* prev = NULL;
        while (root) {
            ListNode* next = root->next;
            root->next = prev;
            prev = root;
            root = next;
        }

        return prev;
    }
};