
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def getPositionOfNonAttackingQueens(row, columnPlacements, boardSize):
            if row == boardSize:
                res = createBoard(columnPlacements,boardSize)
                KAI.append(res)
                return 

            for possibleColumn in range(boardSize):
                if isValidNonAttackingQueenPlacements(row,possibleColumn,columnPlacements,boardSize):
                    columnPlacements[row] = possibleColumn
                    getPositionOfNonAttackingQueens(row+1, columnPlacements, boardSize)


            return

        def isValidNonAttackingQueenPlacements(row,col, columnPlacements, boardSize):
            for previousRow in range(row):
                columnToCheck = columnPlacements[previousRow]
                sameColumn = columnToCheck == col
                sameDiagonal = abs(columnToCheck - col) == row - previousRow
                if sameColumn or sameDiagonal:
                    return False
            return True 
        def createBoard(columnPlacements,boardSize):
            res = []
            
            for columnPlacement in columnPlacements:
                toAppend = ["." for col in range(boardSize)]
                toAppend[columnPlacement] = "Q"
                row = "".join(toAppend)
                
                
                res.append(row)
                
            return res
            
                    
                    
                
        
        columnPlacements = [0 for num in range(n)]
        KAI = []
        getPositionOfNonAttackingQueens(0, columnPlacements, n)
        print(KAI)
        return KAI