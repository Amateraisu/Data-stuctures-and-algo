class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP algorithm 
        
        # first initialize the substring with -1 
        pattern = buildPattern(needle)
        # print(pattern)
        matchingIndex = findMatch(haystack, pattern, needle)
        
        
        return matchingIndex
    
def buildPattern(substring):
    pattern = [-1 for i in range(len(substring))]
    
    i = 0 
    j = 1 
    
    while j < len(substring):
        if substring[i] == substring[j]:
            pattern[j] = i
            i += 1 
            j += 1 
        elif i > 0:
            i = pattern[i - 1] + 1  
        else:
            j += 1 
            
    return pattern

def findMatch(haystack, pattern, needle):
    res = 0
    i = 0 
    j = 0 
    while i < len(haystack) and j < len(needle):
        if haystack[i] == needle[j]:
            i += 1 
            j += 1
            
            if j == len(needle):

                return res 
        elif j > 0:
            j = pattern[j - 1] + 1 
            res = i - j 
        else:
            res = i + 1 
            i += 1 
        # print(i, j)
            
    return res if j == len(needle) else -1
            

    
    return res 