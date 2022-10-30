from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        return findShortest(grid, k)
        
def findShortest(grid, k):
    queue = deque()
    distance = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # [row, col, ks left]
    queue.append([0,0, k, distance])
    visited = set()
    res = float("inf")
    visited.add((0,0))
    while queue:
        currentNode = queue.popleft()
        row, col, k_left, dist = currentNode 
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            res = min(res, dist)
            # print(dist,"reached")
            continue
        for direction in directions:
            newX = row + direction[0]
            newY = col + direction[1]
            if newX < 0 or newX >= len(grid) or newY < 0 or newY >= len(grid[0]) or (grid[newX][newY] == 1 and k_left == 0) or (newX, newY, k_left) in visited:
                continue 
            if grid[newX][newY] == 1:
                queue.append([newX, newY, k_left - 1, dist + 1])
            else:
                queue.append([newX, newY, k_left, dist + 1])
            if newX == len(grid) - 1 and newY == len(grid[0]) - 1:
                continue 

            visited.add((newX, newY, k_left))
        # print(queue)

    return res if res != float("inf") else -1
        
#         numRows = len(grid) 
#         numCols = len(grid[0])
#         visited = set()
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#         @cache
#         def dfs(row, col, k_left):
#             if row == numRows - 1 and col == numCols - 1:
#                 print("reached")
#                 return 0

#             res = float("inf") 
#             visited.add((row, col))
#             for direction in directions:
#                 newX = row + direction[0]
#                 newY = col + direction[1]

#                 if newX < 0 or newX >= numRows or newY < 0 or newY >= numCols or (newX, newY) in visited:
#                     continue 
#                 if grid[newX][newY] == 1 and k_left > 0:
#                     new = k_left - 1
#                     res = min(res, dfs(newX, newY, new) + 1)
#                 elif grid[newX][newY] == 0:
                    
#                     res = min(res, dfs(newX , newY, k_left) + 1)
#             if row == 9 and col == 1:
#                 print(row, col, res, "left", k_left)
#             visited.remove((row, col))
#             return res
#         result = dfs(0,0, k) 
        
#         return result if result != float("inf") else -1
        
#         numRows = len(grid) 
#         numCols = len(grid[0])
#         visited = set()
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#         visited.add((0,0))
#         @cache
#         def dfs(row, col, k_left):
#             if row == numRows - 1 and col == numCols - 1:
#                 print("reached")
#                 return 0

#             res = float("inf") 
            
#             for direction in directions:
#                 newX = row + direction[0]
#                 newY = col + direction[1]

#                 if newX < 0 or newX >= numRows or newY < 0 or newY >= numCols or (newX, newY) in visited:
#                     continue 
#                 if grid[newX][newY] == 1 and k_left > 0:
#                     visited.add((newX, newY))
#                     res = min(res, dfs(newX, newY, k_left - 1) + 1)
#                     visited.remove((newX, newY))
#                 elif grid[newX][newY] == 0:
#                     visited.add((newX, newY))
#                     res = min(res, dfs(newX , newY, k_left) + 1)
#                     visited.remove((newX, newY))
#             if row == 9 and col == 1:
#                 print(row, col, res, "left", k_left)

#             return res
#         result = dfs(0,0, k) 
        
#         return result if result != float("inf") else -1
    
    

    
#     queue = deque()
#     distance = 0
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     # [row, col, ks left]
#     queue.append([0,0, k, distance])
#     visited = set()
#     res = float("inf")
#     visited.add((0,0))
#     while queue:
#         currentNode = queue.popleft()
#         row, col, k_left, dist = currentNode 
#         if row == len(grid) - 1 and col == len(grid[0]) - 1:
#             res = min(res, dist)
#             print(dist,"reached")
#             continue
#         for direction in directions:
#             newX = row + direction[0]
#             newY = col + direction[1]
#             if newX < 0 or newX >= len(grid) or newY < 0 or newY >= len(grid[0]) or (grid[newX][newY] == 1 and k_left == 0) or (newX, newY) in visited:
#                 continue 
#             if grid[newX][newY] == 1:
#                 queue.append([newX, newY, k_left - 1, dist + 1])
#             else:
#                 queue.append([newX, newY, k_left, dist + 1])
#             if newX == len(grid) - 1 and newY == len(grid[0]) - 1:
#                 continue 
                
#             visited.add((newX, newY))
#         # print(queue)
                
#     return res if res != float("inf") else -1
        