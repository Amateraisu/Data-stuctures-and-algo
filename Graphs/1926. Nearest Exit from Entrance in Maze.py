from collections import deque 

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        visited = set()
        visited.add(tuple(entrance))
        queue.append([entrance, 0])
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while queue:
            currentNode, dist = queue.popleft()
            # print(currentNode, "here")
            if (currentNode[0] == 0 or currentNode[1] == 0 or currentNode[0] == len(maze) - 1 or currentNode[1] == len(maze[0]) - 1) and currentNode != entrance:
                # print(currentNode)
                return dist
            
            for direction in directions:
                newX = currentNode[0] + direction[0]
                newY = currentNode[1] + direction[1]
                if newX < 0 or newX > len(maze) - 1 or newY < 0 or newY > len(maze[0]) - 1:
                    continue 
                if (newX , newY) in visited or maze[newX][newY] == "+":
                    continue 
                visited.add((newX, newY))
                newDist = dist + 1
                queue.append([[newX, newY], newDist])
            
        return -1