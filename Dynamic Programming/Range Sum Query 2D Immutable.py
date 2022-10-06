class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        numRows, numCols = len(matrix), len(matrix[0])

        self.cache = [[0 for i in range(numCols + 1)] for j in range(numRows + 1)]
        res = 0 
        current = 0 
        # assign the rows 
        # which is the first column
        for row in range(1, numRows + 1):
            # here the changing variable is rows 
            current += matrix[row - 1][0]
            self.cache[row][1] = current
            
        # assign the cols which is the first row 
        current = 0 
        for col in range(1, numCols + 1 ):
            print(matrix[0][col - 1])
            current += matrix[0][col - 1]
            
            self.cache[1][col] = current 
            
        for row in range(1, numRows + 1):
            for col in range(1, numCols + 1):
                self.cache[row][col] = self.cache[row - 1][col] + self.cache[row][col - 1] - self.cache[row - 1][col - 1] + matrix[row - 1][col - 1]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # take the bottom right corner - top - left + upper left 
        return self.cache[row2 + 1][col2 + 1] - self.cache[row1][col2 + 1] - self.cache[row2 + 1][col1] + self.cache[row1][col1]