class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = initializeGraph(numCourses, prerequisites)


        return isAbleToFinish(graph)
    
    
    
def isAbleToFinish(graph):
    
    while graph.nodes:
        currentNode = graph.nodes.pop()
        contains = dfs(currentNode, graph)
        if contains:
            return False 
        
    return True 

def dfs(node, graph):
    if node.visited:
        return False  
    if node.visiting:
        return True 
    
    node.visiting = True 
    
    for prereq in node.prereqs:
        nextNodeToVisit = graph.dictionary[prereq]
        
        contains = dfs(nextNodeToVisit, graph)
        if contains:
            return True 
        
    node.visited = True
    node.visiting = False 
        
        
        
def initializeGraph(numCourses, prerequisites):
    graph = courseGraph(numCourses)
    # [job, prereq]
    for course, prereq in prerequisites:
        currentCourse = graph.getNode(course)
        currentCourse.prereqs.append(prereq)
        
    return graph
        
        
        

class courseGraph:
    def __init__(self, numCourses):
        self.nodes = deque()
        self.dictionary = {}
        for i in range(numCourses):
            self.createNode(i)
            
    def createNode(self, nodeValue):
        node = graphNode(nodeValue)
        self.dictionary[nodeValue] = node 
        self.nodes.append(node)
        
    def getNode(self, nodeValue):
        if nodeValue not in self.dictionary:
            self.dictionary[nodeValue] = graphNode(nodeValue)
            
        return self.dictionary[nodeValue]
        
        
        
class graphNode:
    def __init__(self, nodeValue):
        self.value = nodeValue 
        self.prereqs = deque()
        self.visited = False 
        self.visiting = False