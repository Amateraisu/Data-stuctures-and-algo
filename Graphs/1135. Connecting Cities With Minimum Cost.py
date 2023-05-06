class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # if it is impossible, then return -1
        # we can use kruskal's algorithm
        connections.sort(key=lambda x: x[2])
        parents = [i for i in range(n)]

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        def uf(n1, n2, cost):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return 0

            parents[p1] = p2
            return cost

        res = 0
        for a, b, cost in connections:
            res += uf(a - 1, b - 1, cost)
        visited = set()
        for par in parents:
            visited.add(find(par))

        if len(visited) != 1:
            return -1
        return res