class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        p  = len(edgeList)
        q = len(queries)
        parents = [i for i in range(n)]
        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return
            parents[p2] = p1
            return

        res = [False for i in range(q)]

        queries_new = [(a, b, c, d) for d, (a, b, c) in enumerate(queries)]
        queries_new.sort(key = lambda x: x[2]) # sort according to the weight
        edgeList.sort(key = lambda x: x[2])
        ptr1 = 0
        ptr2 = 0

        for query in queries_new:
            while ptr1 < len(edgeList) and edgeList[ptr1][2] < query[2]:
                union(edgeList[ptr1][0], edgeList[ptr1][1])
                ptr1 += 1
            res[query[3]] = (find(query[0]) == find(query[1]))
        return res