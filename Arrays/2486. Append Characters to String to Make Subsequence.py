class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptr2 = 0 
        
        
        for i in range(len(s)):
            currentChar = s[i]
            if ptr2 < len(t) and currentChar == t[ptr2]:
                ptr2 += 1 
            
            
        return len(t) - ptr2