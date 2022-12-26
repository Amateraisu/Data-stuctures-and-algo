class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        for pre, node in relations:
            graph[node].append(pre)

        cache = {}
        res = float("-inf")

        visited = set()

        def dfs(currentNode, isVisiting):
            if currentNode in isVisiting:
                return float("inf")
            if currentNode in cache:
                return cache[currentNode]

            visited.add(currentNode)
            isVisiting.add(currentNode)

            cache[currentNode] = 1
            temp = 0
            for nei in graph[currentNode]:
                temp = max(dfs(nei, isVisiting), temp)

            isVisiting.remove(currentNode)
            cache[currentNode] += temp
            return cache[currentNode]

        for node in range(1, n + 1):
            if node not in visited:
                isVisiting = set()
                res = max(dfs(node, isVisiting), res)

        return res if res != float("inf") else -1
