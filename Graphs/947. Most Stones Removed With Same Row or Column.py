class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rank = [1 for stone in stones]
        parent = [i for i in range(len(stones))]
        
        def find(node):
            currentNode = parent[node]
            while currentNode != parent[currentNode]:

                currentNode = parent[currentNode]
            
            return currentNode 
        
        
        def union(node1, node2):
            par1 = find(node1)
            par2 = find(node2)
            
            if par1 == par2:
                return 
            
            if rank[par1] > rank[par2]:
                rank[par1] += rank[par2]
                rank[par2] = rank[par1]
                parent[par2] = par1 
            else:
                rank[par2] += rank[par1]
                rank[par1] = rank[par2]
                parent[par1] = par2 
            
            return 
                
            
        
        for i, stone in enumerate(stones):
            for j, stone2 in enumerate(stones):
                if i == j:
                    continue 
                if parent[i] == parent[j]:
                    continue 
                # check if they are valid 
                if stone[0] == stone2[0] or stone[1] == stone2[1]:
                    
                    union(i, j)
        res = 0 
        seen = set()    

        for i, stone in enumerate(stones):
            par = find(i)
            if par not in seen:
                res += rank[par] - 1 
                seen.add(par)
            
        return res

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rank = [1 for stone in stones]
        parent = [i for i in range(len(stones))]
        
        def find(node):
            currentNode = parent[node]
            while currentNode != parent[currentNode]:

                currentNode = parent[currentNode]
            
            return currentNode 
        
        
        def union(node1, node2):
            par1 = find(node1)
            par2 = find(node2)
            
            if par1 == par2:
                return 0
            
            if rank[par1] > rank[par2]:
                rank[par1] += rank[par2]
                rank[par2] = rank[par1]
                parent[par2] = par1 
            else:
                rank[par2] += rank[par1]
                rank[par1] = rank[par2]
                parent[par1] = par2 
            
            return -1
                
        res = len(stones)
        
        for i, stone in enumerate(stones):
            for j, stone2 in enumerate(stones):
                if i == j:
                    continue 
                if parent[i] == parent[j]:
                    continue 
                # check if they are valid 
                if stone[0] == stone2[0] or stone[1] == stone2[1]:
                    
                    res += union(i, j)


        return len(stones) - res