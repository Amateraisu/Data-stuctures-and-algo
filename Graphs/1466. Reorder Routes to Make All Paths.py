from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # I need to make every node point to my current node 
        # so like starting from node 0, do a dfs 
        
        graph = defaultdict(list)
        outgoing = defaultdict(set)
        
        
        
        for connect in connections:
            source, dest = connect
            graph[source].append(dest)
            graph[dest].append(source)
            outgoing[source].add(dest)
        visited = set()
        
        cost = 0 
        def dfs(currentNode):
            
            nonlocal cost
            visited.add(currentNode)
            # check through surrounding nodes. 
            # if not visited, check if direction is correct 
            
            for neighbour in graph[currentNode]:
                if neighbour not in visited:
                    # check if the direction is correct 
                    if neighbour in outgoing[currentNode]:
                        # print(neighbour, currentNode, "changed")
                        cost += 1 
                    dfs(neighbour)
   
            return 
        dfs(0)
        return cost 