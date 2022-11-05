class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trieGraph = createTrie(words)
        
        numRows = len(board)
        numCols = len(board[0])
        seen, visited = set(), set()

        # print("============")
        def dfs(board, row, col, node, word):
            if row < 0 or row == len(board) or col < 0 or col == len(board[0]) or (row, col) in visited or board[row][col] not in node.chars:
                return

            currentChar = board[row][col]
            
            node = node.chars[currentChar]
            flag = True
            
            

            word += currentChar

            
            if node.endOfWord:
                # print(currentPtr.word)
                seen.add(word)
                if len(node.chars) == 0:
                    del node
                    flag = False
                    

            
            if flag:
                visited.add((row, col))

                dfs(board, row + 1, col, node, word)
                dfs(board, row - 1, col, node, word)
                dfs(board, row, col + 1, node, word)
                dfs(board, row, col - 1, node, word)
                            
                visited.remove((row, col))

        
        
        
        
        for row in range(numRows):
            for col in range(numCols):
                
                dfs(board, row, col, trieGraph, "")
                # print("finish")

        return list(seen)
    
    

    
    
    
    

        
        
        
        
        
        
        
        
        
        
def createTrie(words):
    trie = Trie()
    
    for word in words:
        trie.insertWord(word)
        
    return trie
        
        
        
class Trie:
    def __init__(self):
        self.chars = {}
        self.endOfWord = False
        self.word = ""
    
    def insertWord(self, word):
        currentPtr = self
        for char in word:
            if char not in currentPtr.chars:
                currentPtr.chars[char] = Trie()
            currentPtr = currentPtr.chars[char]
            
        currentPtr.endOfWord = True 
        currentPtr.word = word

        return 
    