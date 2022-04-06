class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        #O(n) time and #O(n) space complexity 
        newString = ['a' for character in range(len(s))]
        for index in range(len(s)):
            newIndex = indices[index]
            newString[newIndex] = s[index]
        
        return "".join(newString)