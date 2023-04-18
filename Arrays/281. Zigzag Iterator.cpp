class ZigzagIterator {
private:
    vector<int> res;
    int total;
    int ptr;

public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        int m = v1.size();
        int n = v2.size();
        total = m + n;
        ptr = 0;

        int ptr1 = 0;
        int ptr2 = 0;

        while (ptr1 < m || ptr2 <n) {
            if (ptr1 < m) {
                res.push_back(v1[ptr1++]);
            }
            if (ptr2 < n) {
                res.push_back(v2[ptr2++]);
            }
        }



    }

    int next() {
        int result = res[ptr++];
        return result;
        
    }

    bool hasNext() {
        return ptr < total;

    }
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */