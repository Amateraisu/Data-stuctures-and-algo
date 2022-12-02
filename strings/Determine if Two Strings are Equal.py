from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        Counter1 = Counter(word1)
        Counter2 = Counter(word2)
        
        
        if set(Counter1.keys()) != set(Counter2.keys()):
            return False
        if Counter(Counter1.values()) != Counter(Counter2.values()):
            return False
        
        return True 
