class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        # build the adjacency list representation of the graph
        graph = [set() for i in range(len(edges)+1)]
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)

        def bfs(start):
            """
             return the farthest node from the 'start' node
               and the distance between them.
            """
            visited = [False] * len(graph)

            visited[start] = True
            queue = deque([start])
            distance = -1
            last_node = None
            while queue:
                next_queue = deque()
                while queue:
                    next_node = queue.popleft()
                    for neighbor in graph[next_node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            next_queue.append(neighbor)
                            last_node = neighbor
                distance += 1
                queue = next_queue

            return last_node, distance

        # 1). find one of the farthest nodes
        farthest_node, distance_1 = bfs(0)
        # 2). find the other farthest node
        #  and the distance between two farthest nodes
        another_farthest_node, distance_2 = bfs(farthest_node)

        return distance_2