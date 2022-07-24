class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        numberOfStones = len(stones)
        
        rank = [1 for stone in range(numberOfStones)]
        parent = [stone for stone in range(numberOfStones)]
        
        
        def find(node):
            currentPtr = node 
            
            while currentPtr != parent[currentPtr]:
                parent[currentPtr] = parent[parent[currentPtr]]
                currentPtr = parent[currentPtr]
                
            return currentPtr
        
        def union(node1, node2):
            
            parent1 , parent2 = find(node1) , find(node2)
            
            if parent1 == parent2:
                return 
            
            if rank[parent1] > rank[parent2]:
                rank[parent1] += rank[parent2]
                rank[parent2] = rank[parent1]
                parent[parent2] = parent1
            else: # if rank[parent2] >= rank[parent1]
                rank[parent2] += rank[parent1]
                rank[parent1] = rank[parent2]
                parent[parent1] = parent2
            
            return 
        
        for i in range(numberOfStones):
            currentStone = stones[i]
            for j in range(numberOfStones):
                otherStone = stones[j]
                if i == j or parent[i] == parent[j]:
                    continue
                    
                    
                if currentStone[0] == otherStone[0] or currentStone[1] == otherStone[1]:
                    union(i, j)

            
            
        res = 0

        visited = set()
        for key in parent:
            parentNode = find(key)
            if parentNode in visited:
                continue
            res += rank[parentNode] - 1
            visited.add(parentNode)
            
        return res