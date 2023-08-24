class MyCalendarThree {
public:
    map<int, int>mp;
    MyCalendarThree() {
    }

    int book(int startTime, int endTime) {

        mp[startTime]++;
        mp[endTime]--;
        int res = 0;
        int cur = 0;
        for (auto& [a, b] : mp) {
            cur += b;
            res = max(res, cur);
        }
        return res;
    }
};