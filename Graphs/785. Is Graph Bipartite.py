import collections
class Solution:
    # dfs 
    def isBipartite(self, graph):
        colorings = {}
        def dfs(currentNode):
            for i in graph[currentNode]:
                if i in colorings:
                    if colorings[i] == colorings[currentNode]:
                        return False 
                else:
                    colorings[i] = colorings[currentNode] ^ 1 
                    if not dfs(i):
                        return False 
                    
            return True 
        
        for idx in range(len(graph)):
            if idx not in colorings:
                
                colorings[idx] = 1 
                if not dfs(idx):
                    return False
                
        return True