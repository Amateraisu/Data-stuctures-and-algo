class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        mod = 1e9 + 7
        s = []
        for i in range(n):
            if corridor[i] == "S":
                s.append(i)
        m = len(s)
        if m % 2 != 0:
            return 0

        @cache
        def dfs(i):
            res = 0
            new = i + 2
            if new > m:
                return 0
            if new == m:
                return 1

            res += (s[new] - s[new - 1]) * dfs(new)

            return int(res % mod)

        return dfs(0)