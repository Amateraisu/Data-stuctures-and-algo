class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        numRows = len(board)
        numCols = len(board[0])
        seen = set()
        res = 0 
        
        def dfs(row, col):
            if row < 0 or row >= numRows or col < 0 or col >= numCols or board[row][col] != "X":
                return 
            
            seen.add((row, col))
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for direction in directions:
                newX = row + direction[0]
                newY = col + direction[1]
                if (newX, newY) not in seen:
                    
                    dfs(newX, newY)
                
            return
        for row in range(numRows):
            for col in range(numCols):
                if (row, col) not in seen and board[row][col] == "X":
                    # print(row, col)
                    res += 1 
                    dfs(row, col)
                    # print(seen, "seen")
                    
                    
                    
                    
        return res