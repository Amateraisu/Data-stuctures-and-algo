class Trie:

    def __init__(self):
        self.root = {}
        self.endSymbol = "*"
        

    def insert(self, word: str) -> None:

        self.insertSubStringStartingAt(0, word)
            
    def insertSubStringStartingAt(self, index, word):
        node = self.root
        for j in range(index, len(word)):
            letter = word[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
            
        node[self.endSymbol] = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for index in range(len(word)):
            currentLetter = word[index]
            if currentLetter not in node:
                return False
            node = node[currentLetter]
            
        return self.endSymbol in node
    # when I see an endsymbol, it is a word 
    # when I dont see an endsymbol, it is not a word 
            

    def startsWith(self, word: str) -> bool:
        print("here")
        node = self.root
        for index in range(len(word)):
            currentLetter = word[index]
            if currentLetter not in node:
                return False
            node = node[currentLetter]
            
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)