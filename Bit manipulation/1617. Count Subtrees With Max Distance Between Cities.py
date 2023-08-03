class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        for a, b in edges:
            g[a - 1].add(b - 1)
            g[b - 1].add(a - 1)
        res = [0 for i in range(n - 1)]
        def getMaxDist(mask):
            # if mask & (mask - 1) == 0:
            #     return 0
            ret = 0
            for i in range(n):
                if mask & (1 << i):
                    queue = deque([i])
                    t = mask
                    t ^= (1 << i) # mark it as visited
                    d = 0
                    while queue:
                        for _ in range(len(queue)):
                            node = queue.popleft()
                            for nei in g[node]:
                                if t & (1 << nei):
                                    queue.append(nei)
                                    t ^= (1 << nei)
                        d += 1

                    if t:
                        return 0
                    ret = max(ret, d)
            return ret - 1

        for mask in range(1 << n):
            d = getMaxDist(mask)
            if d > 0:
                res[d - 1] += 1

        return res