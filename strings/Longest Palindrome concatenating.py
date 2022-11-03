from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        res = 0
        used = set()
        print(count)
        for key, val in count.items():
            if isPalindrome(key) and val % 2 != 0:
                # we can use this as a start
                res += 2 
                count[key] -= 1 
                
                break 
        
        for key, val in count.items():
            
            currentWord = key 
            reversedWord = currentWord[::-1]
            if reversedWord == currentWord and currentWord not in used:

                res += 2 * (val // 2) * 2 
                used.add(key)
            elif reversedWord in count and reversedWord not in used:

                res += 2 * min(val, count[currentWord[::-1]]) * 2 
        
                used.add(key)

        return res 
                

        
def isPalindrome(word):
    left = 0 
    right = len(word) - 1 
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1 
        right -=1 
    return True 