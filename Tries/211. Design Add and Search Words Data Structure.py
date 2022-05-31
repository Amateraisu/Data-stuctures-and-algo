class WordDictionary:

    def __init__(self):
        self.endSymbol = "*"
        self.root = {}
        
        
    def addWord(self, word: str) -> None:
        currentNode = self.root
        for index in range(len(word)):
            currentCharacter = word[index]
            if currentCharacter not in currentNode:
                currentNode[currentCharacter] = {}
            currentNode = currentNode[currentCharacter]
            
        currentNode[self.endSymbol] = True
        
    def search(self, word: str) -> bool:
        
        def dfs(root, currentWord):
            if root == True:
                return False 
            currentNode = root
            for index in range(len(currentWord)):
                currentCharacter = currentWord[index]
                if currentCharacter == ".":
                    newWord = currentWord[index+1:]
                    for char in currentNode:
                        newRoot = currentNode[char]
                        if dfs(newRoot, newWord):
                            return True 
                    return False 
                elif currentCharacter not in currentNode:
                    return False 
                currentNode = currentNode[currentCharacter]
            if type(currentNode) == bool :
                return False 
            elif type(currentNode) == dict :
                return "*" in currentNode
                
        
        return dfs(self.root, word)