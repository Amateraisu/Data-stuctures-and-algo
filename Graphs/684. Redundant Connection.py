class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for j in range(len(edges) + 1)]

        def find(node):
            currentParent = parent[node]
            while currentParent != parent[currentParent]:
                parent[node] = parent[currentParent]
                currentParent = parent[node]
            return currentParent 
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:

                return True 
            else:
                if rank[parent1] > rank[parent2]:
                    rank[parent1] += rank[parent2]
                    parent[parent2] = parent[parent1]
                else:
                    rank[parent2] += rank[parent1]
                    parent[parent1] = parent[parent2]

            return False 
            
        for edge in edges:
            node1, node2 = edge 

            
            if union(node1, node2):
                return [node1, node2]