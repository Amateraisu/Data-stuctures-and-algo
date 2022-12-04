from collections import defaultdict 
from collections import deque
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        print(roads)
        graph = defaultdict(list)
        for road in roads:
            source, dest, dist = road 
            graph[source].append([dist, dest])
            graph[dest].append([dist, source])
            
        # dfs
        # go through all the edges 
        res = float("inf")
        queue = deque()
        queue.append(1)
        visited = set()
        res = float("inf")
        while queue:
            currentNode = queue.popleft()
            # print(currentNode)
            currentCity = currentNode 
            
            for neighbour in graph[currentCity]:
                dist, nei = neighbour 
                # print(currentCity, dist, nei, "looping")
                
                if (currentCity, nei) not in visited:
                    # print(dist, nei, "went through")
                    visited.add((currentCity, nei))
                    visited.add((nei, currentCity))
                    
                    
                    res = min(res, dist)
                    queue.append(nei)
        return res 
            