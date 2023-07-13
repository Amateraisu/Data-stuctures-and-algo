class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        unable = 0

        isVisiting = set()
        c = collections.defaultdict(set)
        for a, b in prerequisites:
            c[b].add(a)
        cache = {}
        def dfs(node):
            if node in isVisiting:
                return False

            if node in cache:
                return cache[node]
            if len(c[node]) == 0:
                return True

            can = True
            isVisiting.add(node)
            for pre in c[node]:
                can = can and dfs(pre)
            cache[node] = can
            isVisiting.discard(node)
            return can

        for i in range(n):
            if not dfs(i):
                return False

        return True