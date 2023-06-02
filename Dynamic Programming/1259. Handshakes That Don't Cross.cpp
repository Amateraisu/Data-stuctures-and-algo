class Solution {
    int MOD = 1e9 + 7;
public:
    int numberOfWays(int numPeople) {
        int n = numPeople;

        vector<int> dp(n + 1, -1);

        return dfs(dp, numPeople) % MOD;

    }

    long long dfs(vector<int>& cache, int num) {
        if (num == 0) return 1;
        if (cache[num] != -1) return cache[num];
        long long res = 0;
        for (int i = 0; i < num; i+=2) {
            int left = num - 2 - i;
            res = (res % MOD + ((dfs(cache, left) % MOD) * (dfs(cache, i) % MOD))) % MOD;
            res %= MOD;
        }
        cache[num] = res % MOD;
        return res % MOD;
    }
};