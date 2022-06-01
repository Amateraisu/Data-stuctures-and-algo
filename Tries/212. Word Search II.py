from collections import deque

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. so I first store all the words in a Trie data structure, time complexity of this operation will be O(m*n) where m is the length of the longest word and n is the number of words 
        # 2. perform bfs on a node that matches the first letter 
        # 3. correct words, mark as used.
        # 4. traverse down the trie at the same time 
        # 5. if endSymbol is there, append the word to the final result 
        root = Node()
        for word in words:
            root.insert(word)

        result,visited=set(),set()
        ROWS,COLS=len(board),len(board[0])
    
        def dfs(row,col,node,word):
            if row<0 or row==ROWS or col<0 or col==COLS or (row,col) in visited or board[row][col] not in node.children:
                return
            ele=board[row][col]
            node = node.children[ele]
            word+= ele
            flag=True
            if node.endOfWord:
                result.add(word)
                if len(node.children)==0:
                    del node
                    flag=False
            if flag:
                visited.add((row,col))
                dfs(row+1,col,node,word)
                dfs(row-1,col,node,word)
                dfs(row,col+1,node,word)
                dfs(row,col-1,node,word)
                visited.remove((row,col))
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row,col,root,"")

        return list(result)
    
    
    
    
    
    
         
            
        
class Node:        
    def __init__(self):
        self.children={}
        self.endOfWord=False

    def insert(self,word):
        root = self
        for w in word:
            if w not in root.children:
                root.children[w]=Node()
            root=root.children[w]
        root.endOfWord = True