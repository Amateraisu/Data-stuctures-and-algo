class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        
        
        for edge in edges:
            start, end , dist = edge 
            graph[start].append([end,dist])
            graph[end].append([start, dist])
            
            
        # run dijkstra's algorithm on every single node 
        def dijkstra(node):
            seen = set()
            minHeap = []
            minHeap.append([0, node])
            res = [float("inf")] * n
             
            while len(seen) != n and minHeap:
                distance_so_far, currentNode = heapq.heappop(minHeap)
                res[currentNode] = min(distance_so_far, res[currentNode])
                seen.add(currentNode)
                for edge in graph[currentNode]:
                    end, dist = edge 
                    if end not in seen:
                        heapq.heappush(minHeap, [dist + distance_so_far, end])
            result = 0
            for dist in res:
                if dist <= distanceThreshold:
                    result += 1 
            # print(res, node)
            return result - 1 
        
        minimum_so_far = float("inf")
        res = 0 
        for i in range(n):
            # find the number of nodes away that are within distanceThreshold apart 
            visited = dijkstra(i)
            if visited < minimum_so_far:
                res = i 
                minimum_so_far = visited
            elif visited == minimum_so_far:
                res = max(res, i)
            print(i, visited)
        return res