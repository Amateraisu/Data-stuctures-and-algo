class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        left = 0 
        right = len(s) - 1 
        while left <= right:
            if isVowel(word[left]) and isVowel(word[right]):
                word[left], word[right] = word[right], word[left]
                left +=1 
                right -= 1 
                
            elif not isVowel(word[left]) and not isVowel(word[right]):
                left += 1 
                right -= 1 
            elif not isVowel(word[left]):
                left += 1 
            elif not isVowel(word[right]):
                right -= 1 
                
        return "".join(word)
                
def isVowel(kek):
    char = kek.lower()
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        return True 
    
    return False