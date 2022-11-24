class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # time complexity of O(3 ^ (Len of word) * MN)
        numRows = len(board)
        numCols = len(board[0])
        
        
        for i in range(numRows):
            for j in range(numCols):
                if self.doesExist(word, board, 0, i, j, set()):
                    return True

        return False
    
    def doesExist(self, word, board, currentIndex, row, column, visited):
        

        
        if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board[row][column] != word[currentIndex] or (row, column) in visited:
            return False 
        if currentIndex == len(word) - 1 and word[currentIndex] == board[row][column]:
            return True 
        
        visited.add((row, column))
        # print(row, column, word[currentIndex], visited)
        res = (
            self.doesExist(word, board, currentIndex + 1, row + 1, column, visited) or 
            self.doesExist(word, board, currentIndex + 1, row - 1, column, visited) or 
            self.doesExist(word, board, currentIndex + 1, row, column + 1, visited) or 
            self.doesExist(word, board, currentIndex + 1, row, column - 1, visited)
        )
        
        visited.remove((row, column))
        
        return res