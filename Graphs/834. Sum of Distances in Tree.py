class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        res = [0] * n
        count = [1] * n
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        def dfs(currentNode, parent): # postorder traversal 
            for kid in graph[currentNode]:
                if kid != parent:
                    dfs(kid, currentNode)
                    count[currentNode] += count[kid] # the number of nodes in every subtree
                    res[currentNode] += res[kid] + count[kid] # the distance of every node from its parent node 

        def dfs2(currentNode, parent): # preorder traversal 
            for kid in graph[currentNode]:
                if kid != parent:
                    res[kid] = res[currentNode] - count[kid] + n - count[kid]  # the result of a tree is equals to the distances of children nodes of the currentNode - count of the children node + n - count[child] because by moving downwards, the total distance of the childSubtree is discounted by 1, +(n - count[child]) because anything else other than that gets incremented by 1 
                    
                    dfs2(kid, currentNode)

        dfs(0, -1)
        dfs2(0, -1)

        return res
        