class SmallestInfiniteSet {
    int current;
    std::priority_queue<int, std::vector<int>, less<int>> pq;
    unordered_set<int> visited;

public:
    SmallestInfiniteSet() {
        current = 1;

    }

    int popSmallest() {

        if (!pq.empty()) {
            int res = pq.top() * -1;
            visited.erase(res * -1);
            pq.pop();
            return res;
        }
        current++;
        return current -1 ;



    }

    void addBack(int num) {
        if (visited.find(num) == visited.end() && num < current) {
            visited.insert(num);

            pq.push(num * -1);
        }
        return;

    }
};
