class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        length = len(s)
        count = 0 
        for i in range(length):
            if i >= length / 2 :
                if self.isVowel(s[i]):
                    count -= 1 
                    
            else:
                if self.isVowel(s[i]):
                    count += 1 
        return count == 0        
    def isVowel(self, char):
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
            
            return True 
        
        return False