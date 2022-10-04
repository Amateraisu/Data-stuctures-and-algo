class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        # I must go to a node whose distance to the last node is smaller than the current distance from here 
        if n == 1:
            return 0
        
        # find the shortest distance from n to any other nodes 
        graph = defaultdict(lambda : [])
        for edge in edges:
            x, y , weight = edge 
            graph[x].append([weight, y])
            graph[y].append([weight, x])
            
            
            
        # dijkstra's calculates the shortest distance from a node to any other nodes
        
        minHeap = [(0, n)]
        dist = [float("inf")] * (n + 1)
        dist[n] = 0 
        visited = set()
        while minHeap:
            distance, node1 = heapq.heappop(minHeap)
            if node1 in visited:
                continue
            visited.add(node1)

                # here that means we have already visited it 
            for weight, node2 in graph[node1]:
                if dist[node2] > dist[node1] + weight:
                    dist[node2] = dist[node1] + weight 
                    heapq.heappush(minHeap,[dist[node2], node2])
        
        # [inf, 4, 2, 1, 6, 0]
        cache = {}

        def dfs(currentNode):
            if currentNode == n:
                return 1 
            if currentNode in cache:
                return cache[currentNode]

            temp = 0 

            for weight, node2 in graph[currentNode]:
                if dist[node2] < dist[currentNode]:
                    temp += dfs(node2)
            cache[currentNode] = temp  

            
            return temp
        
        


        return dfs(1) % 1000000007