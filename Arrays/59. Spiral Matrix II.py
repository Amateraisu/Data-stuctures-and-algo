class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        spiral = [[0 for column in range(n)] for row in range(n)]
        startCol = 0 
        endCol = n-1
        startRow = 0 
        endRow = n-1
        count = 1
        while startCol <= endCol and startRow <= endRow:
            for col in range(startCol, endCol+1):
                spiral[startCol][col] = count
                print(count)
                count += 1
                if startCol == endCol:
                    break
            for row in range(startRow+1, endRow+1):
                spiral[row][endCol] = count
 
                count+=1
                if startRow == endRow:
                    break
            for col in reversed(range(startCol, endCol)):
                spiral[endRow][col] = count
                print(count)
                count+=1
            for row in reversed(range(startRow+1, endRow)):
                spiral[row][startCol] = count
                print(count)
                count+=1
                
            startCol +=1
            endCol -=1
            startRow +=1
            endRow -=1
        return spiral