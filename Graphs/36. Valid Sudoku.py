from collections import defaultdict 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for every empty box, try to fill with a number 
        numRows = len(board)
        numCols = len(board[0])
        boxes = defaultdict(set)
        directions = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1),(1, 0), (1, -1), (1, 1), (0,0)]
        print("6".isnumeric())
        for i in range(1, numRows, 3):
            for j in range(1, numCols, 3):
                # parse through every 8-direction 
                for direction in directions:
                    newX = i + direction[0]
                    newY = j + direction[1]

                    if board[newX][newY] in boxes[(i, j)]:

                        return False 
                    if board[newX][newY].isnumeric():
                        boxes[(i, j)].add(board[newX][newY])
                    
        rows = defaultdict(set)
        cols = defaultdict(set)
        # 
        for i in range(numRows):
            for j in range(numCols):
                if board[i][j] in rows[i] or board[i][j] in cols[j]:

                    return False 
                
                if board[i][j].isnumeric():
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                
        return True