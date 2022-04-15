class Solutioclass Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0 
        res = 0 
        
        for i in range(len(s)):
            right = i 
            if s[right] in hashmap:
                hashmap[s[right]] +=1
            else:
                hashmap[s[right]] = 1

            while (right - left + 1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left+=1
                
            res = max(res, right-left+1)
            
        return resn:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0 
        res = 0 
        
        for i in range(len(s)):
            right = i 
            if s[right] in hashmap:
                hashmap[s[right]] +=1
            else:
                hashmap[s[right]] = 1

            while (right - left + 1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left+=1
                
            res = max(res, right-left+1)
            
        return res