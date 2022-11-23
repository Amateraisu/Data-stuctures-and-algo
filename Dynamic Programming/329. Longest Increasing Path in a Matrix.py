class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # we can save space complexity by editing the matrix 
        
        numRows = len(matrix)
        numCols = len(matrix[0])
        
        res = 1 
        cache = {}
        for i in range(numRows):
            for j in range(numCols):
                # find longest increasing path 
                if (i, j) in cache:
                    res = max(res, cache[(i, j)])
                    
                else:
                    currentLongest = self.findLongest(i, j, matrix, float("-inf"), cache)
                    res = max(res, currentLongest)  

        return res
    
    def findLongest(self, row, column, matrix, previous, cache):
        if row < 0 or row >= len(matrix) or column < 0 or column >= len(matrix[0]) or matrix[row][column] <= previous:
            return 0 
        
        best = 1
        
        highest = max(
            self.findLongest(row + 1, column, matrix, matrix[row][column], cache),
            self.findLongest(row - 1, column, matrix, matrix[row][column], cache),
            self.findLongest(row, column + 1, matrix, matrix[row][column], cache),
            self.findLongest(row, column - 1, matrix, matrix[row][column], cache)
        )
        cache[(row, column)] = best + highest
        
        
        return best + highest