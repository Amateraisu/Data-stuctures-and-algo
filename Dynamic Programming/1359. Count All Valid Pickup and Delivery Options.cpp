// vector<vector<int>>dp(501, vector<int>(501, 0));

using ll = long long;
class Solution {
public:
    ll MOD = 1e9 + 7;
    vector<vector<ll>>dp =  vector<vector<ll>> (501, vector<ll>(501, 0));
    int countOrders(int n) {

        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            dp[0][i] += i * (dp[0][i - 1] % MOD) ;
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] += (dp[i - 1][j] % MOD) * i;
                dp[i][j] %= MOD;
                if (j - i > 0) dp[i][j] += (dp[i][j - 1] % MOD) * (j - i) ;
                dp[i][j] %= MOD;

            }
        }

        return dp[n][n];

    }
};

class Solution {
public:
    int countOrders(int n) {
        long ans = 1;
        int MOD = 1e9 + 7;

        for (int i = 1; i <= n; ++i) {
            // Ways to arrange all pickups, 1*2*3*4*5*...*n
            ans = ans * i;
            // Ways to arrange all deliveries, 1*3*5*...*(2n-1)
            ans = ans * (2 * i - 1);
            ans %= MOD;
        }

        return ans;
    }
};
// class Solution {
// public:
// ll MOD = 1e9 + 7;
// vector<vector<int>>dp =  vector<vector<int>> (501, vector<int>(501, 0));
// int dfs(int up, int ud) {

//     if (up == 0 && ud == 0) return 1;

//     if (up < 0 || ud < 0) return 0;
//     if (dp[up][ud] != 0) return dp[up][ud];
//     if (up > ud) return 0;
//     ll res = 0;
//     res += up * (dfs(up - 1, ud) % MOD);
//     res %= MOD;
//     res += (ud - up) * (dfs(up,ud - 1) % MOD);
//     res %= MOD;
//     dp[up][ud] = res;
//     return res;
// }
//     int countOrders(int n) {

//         return dfs(n, n);

//     }
// };