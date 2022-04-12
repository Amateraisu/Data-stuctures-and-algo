class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # O (m*n) time and space complexity, 
        # we can replace the value with -1 to signify if it was originally live or not
        
        duplicate = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                duplicate[i][j] = board[i][j]
                
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                neighbours = checkNeighbours(duplicate, i,j)
                sumOfNeighbours = sum(neighbours)
                if sumOfNeighbours == 2:
                    continue
                if sumOfNeighbours == 3:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        return board
                    
def checkNeighbours(duplicatedBoard,row,column):
    neighbours = []
    
    # if it is live cell then add to neighbours
    #check all surrounding 5~8 neighbours
    
    #check left and right 
    if column > 0 and duplicatedBoard[row][column-1] == 1:
        
        neighbours.append(1)
    
    if column < len(duplicatedBoard[0])-1 and duplicatedBoard[row][column+1] == 1:
        
        neighbours.append(1)
    
    #check top and bottom 
    
    if row > 0 and duplicatedBoard[row-1][column] == 1:
        
        neighbours.append(1)
        
    if row < len(duplicatedBoard)-1 and duplicatedBoard[row+1][column] == 1:
        neighbours.append(1)
    
    #check diagonals 
    
    # top diagonal 
    #top left diagonal
    
    if column > 0 and row > 0 and duplicatedBoard[row-1][column-1] == 1:
        neighbours.append(1)
    
    
    #top right diagonal
    if column < len(duplicatedBoard[0])-1 and row > 0 and duplicatedBoard[row-1][column+1] == 1:
        neighbours.append(1)
        
    
    #bottom left 
    if column > 0 and row < len(duplicatedBoard) -1 and duplicatedBoard[row+1][column-1] == 1:
        neighbours.append(1)
    
    #bottom right
    
    if column < len(duplicatedBoard[0])-1 and row < len(duplicatedBoard) -1 and duplicatedBoard[row+1][column+1] == 1:
        neighbours.append(1)
        
        
    
    return neighbours