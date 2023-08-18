class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = collections.defaultdict(set)
        for a, b in roads:
            g[a].add(b)
            g[b].add(a)
        res = 0
        visited = set()
        # O(n^2)

        for i in range(n):
            for j in range(n):
                if i != j:
                    t = 0
                    a = len(g[i])
                    b = len(g[j])

                    if i in g[j]:
                        res = max(res, a + b - 1)
                    else:
                        res = max(res, a + b)
        return res
