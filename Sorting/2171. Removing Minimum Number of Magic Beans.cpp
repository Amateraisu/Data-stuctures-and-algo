using ll = long long;
class Solution {
public:
    ll minimumRemoval(vector<int>& beans) {
        sort(beans.begin(), beans.end());
        int n = beans.size();
        vector<ll>pref(n + 1, 0);
        for (int i = 1;  i <= n; i++) {
            pref[i] = pref[i - 1] + beans[i - 1];
        }
        ll res = 1e10;
        ll cur = 0;
        for (int i = 0; i < n; i++) {
            ll remain = n - i - 1;
            ll l = remain * beans[i];
            ll h = pref[n] - pref[i + 1];
            if ((cur + (h - l)) < res) {
                res = cur + ( h - l);

            }
            cur += beans[i];
        }
        return res;

    }
};
