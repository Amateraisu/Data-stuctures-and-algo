class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        vector<ListNode*>res;
        ListNode* ptr = head;
        int cnt=  0;
        while (ptr) cnt++, ptr = ptr->next;
        int t = ceil(double(cnt) / k); // 4
        // so the ideal is t
        // at every segment, try to have at least t counts
        ptr = head;
        cout << t << '\n';
        // maybe I need to update it as I go
        for (int i = 0 ; i < k; i++) {
            ListNode* prev = NULL;
            res.push_back(ptr);
            t = ceil((double)cnt / (k - i));
            int t2 = 0;
            while (t2 < t) {
                prev = ptr;
                if (ptr) ptr = ptr->next;
                t2++;
            }
            if (prev) prev->next = NULL;
            cnt -= t2;
        }
        return res;

    }
};