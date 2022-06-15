class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #O(j + e) where j is the number of nodes and e is the number of edges 
        #O(j + e) because we need to store the node sand graphs 
        graph = createGraphHelper(n, edges)
        res = 0
        def dfs(node):
            
            if node.visited == True:
                return 
            if node.visiting == True:
                return 
            
            node.visiting = True 
            for neighbourValue in node.neighbours:
                neighbour = graph.dictionary[neighbourValue]
                dfs(neighbour)
            
            node.visited = True 
            node.visiting = False
            
            return 
            
        for i in range(n):
            
            currentNode = graph.dictionary[i]

            if currentNode.visited == False:
                res += 1 
                dfs(currentNode)
        
    
        
        return res
    
    
def createGraphHelper(numberOfNodes, edges):
    graph = graphDirectory(numberOfNodes)
    for startNode, endNode in edges:
        # starting Node, ending Node 
        graph.dictionary[startNode].neighbours.append(endNode)
        graph.dictionary[endNode].neighbours.append(startNode)
    return graph
        
    
class graphDirectory:
    def __init__(self, numberOfNodes):
        self.dictionary = {}
        self.nodes = []
        for i in range(numberOfNodes):
            self.addNode(i)
            
    def addNode(self, nodeValue):
        node = Node(nodeValue)
        self.dictionary[nodeValue] = node 
        self.nodes.append(node)
        return 
        
class Node:
    def __init__(self, nodeValue):
        self.visited = False 
        self.visiting = False 
        self.nodeValue = nodeValue 
        self.neighbours = []