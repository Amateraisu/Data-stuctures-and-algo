class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        numRows = len(seats)
        numCols = len(seats[0])
        placedStudents = set()
        
        res = findMaximum(seats, numRows, numCols, 0, 0, placedStudents)

        return res
    
def findMaximum(seats, numRows, numCols, currentRow, currentCol, placedStudents):
    if currentRow == numRows:
        return 0 
    if currentCol == numCols:
        return findMaximum(seats, numRows, numCols, currentRow + 1, 0, placedStudents)
    num_students = 0 
    if seats[currentRow][currentCol] == "." and isValid(currentRow, currentCol, placedStudents):
        # try placing a seat here 
        placedStudents.add((currentRow, currentCol))
        num_students = max(num_students, findMaximum(seats, numRows, numCols, currentRow, currentCol + 1, placedStudents) + 1)
        placedStudents.remove((currentRow, currentCol))
        
    num_students = max(num_students, findMaximum(seats, numRows, numCols, currentRow, currentCol + 1, placedStudents))
    
    

    
    return num_students

def isValid(row, col, placed):
    if (row - 1, col - 1) in placed or (row - 1, col + 1) in placed or (row, col - 1) in placed or (row, col + 1) in placed:
        return False
    return True