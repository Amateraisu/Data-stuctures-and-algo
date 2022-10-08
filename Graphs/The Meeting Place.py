from collections import deque

class Solution:
    def solve(self, matrix):
        # we can do a bfs for every single node and calculate the min of the sum of those distances 
        # O(m * n) where m is the height and n is the width of the matrix 
        numRows, numCols = len(matrix), len(matrix[0])
        persons = 0 
        # count how many persons for a node to be valid 
        for row in range(numRows):
            for col in range(numCols):
                if matrix[row][col] == 2:
                    persons += 1 

        cache = {}
        res = float("inf")
        for row in range(numRows):
            for col in range(numCols):
                # search if it is an empty cell 
                #
                if (row, col) in cache:
                    cost = cache[(row, col)]

                elif matrix[row][col] != 1 and (row, col) not in cache:
                    cost =  bfs(row, col, matrix, persons)
                    cache[(row, col)] = cost 

                    res = min(res, cost)
                    print(row, col, cost, res)

                

        return res


def bfs(row, col , matrix, persons):

    cost = 0 
    seen = 0 
    queue = deque()
    queue.append([row, col, 0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    visited.add((row, col))
    while queue:
        currentNode = queue.popleft()

        currentRow, currentCol, dist = currentNode 
        
        if matrix[currentRow][currentCol] == 2:
            seen += 1 
            cost += dist
        # get neighbours 
        for direction in directions:
            newRow = currentRow + direction[0]
            newCol = currentCol + direction[1]

            if newRow >= 0 and newRow < len(matrix) and newCol >= 0 and newCol < len(matrix[0]) and matrix[newRow][newCol] != 1 and (newRow, newCol) not in visited:
                visited.add((newRow, newCol))
                queue.append([newRow, newCol, dist + 1])
    if seen != persons:
        cost = float("inf")
    return cost