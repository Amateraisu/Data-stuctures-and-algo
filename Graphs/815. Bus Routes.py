class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        q = deque()
        g = collections.defaultdict(set)
        s_to_b = collections.defaultdict(set)
        for i, b in enumerate(routes):
            for s in b:
                s_to_b[s].add(i)
        visited = set()
        for b in s_to_b[source]:
            q.append([1, b])
            visited.add(b)
        while q:
            cost, bus = q.popleft()
            if bus in s_to_b[target]:
                return cost
            for s in routes[bus]:
                for j in s_to_b[s]:
                    if j not in visited:
                        visited.add(j)
                        q.append([cost + 1, j])
        return -1