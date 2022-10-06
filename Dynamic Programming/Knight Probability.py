class Solution:
    def knightProbability(self, n: int, k: int, x: int, y: int) -> float:
        numRows = n 
        numCols = n
        cache = {}
        nonvalids = 0 
        def dfs(currentRow, currentCol, stepsLeft):

            # if im outside of the box, do this 
            nonlocal nonvalids 

            if currentRow < 0 or currentRow >= n or currentCol < 0 or currentCol >= n:
                nonvalids += 1 
                return 0 
            if stepsLeft == 0:
                # it is a valid box 
                return 1



            if (currentRow, currentCol, stepsLeft) in cache:
                return cache[(currentRow, currentCol, stepsLeft)]
            temp = 0 
            directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1) , (2, 1), (1, 2)]
            # for each direction go each way 
            for direction in directions:
                newX = currentRow + direction[0]
                newY = currentCol + direction[1]
                temp += dfs(newX, newY, stepsLeft - 1)

            cache[(currentRow, currentCol, stepsLeft)] = temp / 8

            return cache[(currentRow, currentCol, stepsLeft)]
        valids = dfs(x, y, k)

        # then I need to find the total steps 
        return dfs(x, y, k)