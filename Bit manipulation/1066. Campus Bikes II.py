class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        m = len(workers)
        n = len(bikes)


        @cache
        def dfs(work, mask):
            if work == m:
                return 0

            cur = float('inf')
            for i in range(n):
                if (1 << i) & mask == 0:
                    dist = calc(workers[work], bikes[i])
                    new = (1 << i) | mask
                    cur = min(cur, dist + dfs(work + 1, new))
            return cur

        return dfs(0, 0)

def calc(work, bike):
    return abs(work[0] - bike[0]) + abs(work[1] - bike[1])