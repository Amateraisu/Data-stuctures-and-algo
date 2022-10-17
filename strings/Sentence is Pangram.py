class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        mySet = set(ascii_lowercase)

        
        for char in sentence:
            if char in mySet:
                mySet.remove(char)
                
        return len(mySet) == 0