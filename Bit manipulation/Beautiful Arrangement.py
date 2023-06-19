class Solution:
    def countArrangement(self, n: int) -> int:

        end = (1 << n + 1) - 1
        c = {}

        def dfs(mask, index):
            s = (mask, index)
            if s in c:
                return c[s]
            if mask == end:
                return 1
            res = 0
            for i in range(1, n + 1):
                if mask & (1 << i) == 0:  # unused
                    if i % index == 0 or index % i == 0:
                        new = mask ^ (1 << i)
                        res += dfs(new, index + 1)
            c[s] = res
            return res

        return dfs(1, 1)