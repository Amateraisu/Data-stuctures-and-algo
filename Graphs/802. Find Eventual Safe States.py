class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        nodes = len(graph)
        cache = {}
        isVisiting = set()

        def dfs(node):
            if len(graph[node]) == 0:
                return True
            if node in isVisiting:
                return False
            if node in cache:
                return cache[node]

            can = True
            isVisiting.add(node)
            for nei in graph[node]:
                t = dfs(nei)
                can = can and t
            isVisiting.discard(node)
            cache[node] = can

            return can

        n = len(graph)
        for i in range(n):

            if dfs(i):
                res.append(i)
            # print(i)
            # print(cache)

        return res
