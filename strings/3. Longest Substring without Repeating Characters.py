class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentSet = set()
        maximumLength = 0
        left = 0
        for charIndex in range(len(s)):
            
            char = s[charIndex]
            while char in currentSet:
                currentSet.remove(s[left])
                left+=1
            currentSet.add(char)
            maximumLength = max(maximumLength, len(currentSet))
            
        return maximumLength