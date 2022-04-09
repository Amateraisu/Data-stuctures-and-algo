class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can sort and just compare it right 
        # or we can use a hashmap 
        # O(n) time complexity 
        # but the space complexity of this is O(1) because s and t contains only a-z letters 
        if len(s) != len(t):
            return False
        hashmap = {}
        for charIndex in range(len(s)):
            char = s[charIndex]
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        for charIndex in range(len(t)):
            char = t[charIndex]
            if char not in hashmap:
                return False
            else:
                hashmap[char] -=1
        print(hashmap)
        for key in hashmap:
            if hashmap[key] != 0:
                return False
            
        return True