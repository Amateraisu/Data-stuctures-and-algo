class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        
        rows = len(board)
        columns = len(board[0])
        
        for i in range(rows):
            for j in range(columns):
                # perform dfs 
                if visited[i][j]:
                    continue
                if dfs(visited, board, word, i, j, 0):
                    return True 
                
        return False 
    
    
def dfs(visited, board, word, row, col, wordIndex):
    
    if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or word[wordIndex] != board[row][col] or visited[row][col]:
        return False 
    
    if word[wordIndex] == board[row][col] and wordIndex == len(word) - 1:
        return True 
    # set current node as visited 
    visited[row][col] = True 
    
    
    res = (
    dfs(visited, board, word, row + 1, col, wordIndex + 1) or 
    dfs(visited, board, word, row - 1, col , wordIndex + 1) or
    dfs(visited, board, word, row, col + 1, wordIndex +1) or 
    dfs(visited, board, word, row, col - 1 , wordIndex + 1) )
    
    visited[row][col] = False
    
    
    return res