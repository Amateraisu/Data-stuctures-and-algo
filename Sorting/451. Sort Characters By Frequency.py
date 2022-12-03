from collections import Counter 
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        
        chars = list(s)
        
        chars.sort(key = lambda x : (counter[x], x), reverse = True)
        
        
        return "".join(chars)