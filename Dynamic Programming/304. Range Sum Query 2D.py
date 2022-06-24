class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = self.createSumMatrix(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        upperLeftRow, upperLeftCol = row1, col1
        bottomRightRow, bottomRightCol = row2, col2
        
        overlap = self.matrix[upperLeftRow - 1][upperLeftCol - 1] if upperLeftRow > 0 and upperLeftCol > 0 else 0 
        
        leftMinus = self.matrix[bottomRightRow][upperLeftCol - 1] if upperLeftCol > 0 else 0 
        topMinus = self.matrix[upperLeftRow - 1][bottomRightCol] if upperLeftRow > 0 else 0
        return self.matrix[bottomRightRow][bottomRightCol] - leftMinus - topMinus + overlap 
        
    def createSumMatrix(self, matrix):
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        # print(dp)
        dp[0][0] = matrix[0][0]
        for i in range(1, len(matrix)):
            dp[i][0] = dp[i - 1][0] + matrix[i][0]
        for j in range(1, len(matrix[0])):
            dp[0][j] = dp[0][j - 1] + matrix[0][j]
        # print(dp)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i][j]
        return dp
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)