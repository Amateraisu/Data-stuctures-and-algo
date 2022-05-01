class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        
        s1Count = [0 for num in range(26)]
        s2Count = [0 for num in range(26)]
        
        for charIndex in range(len(s1)):
            currentChar1 = s1[charIndex]
            currentChar2 = s2[charIndex]
            index1 = ord(currentChar1) - ord('a')
            index2 = ord(currentChar2) - ord('a')
            s1Count[index1] +=1
            s2Count[index2] +=1
            
        matches = 0
        
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches +=1
        
        left = 0 
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            currentChar = s2[i]
            index = ord(currentChar) - ord('a')
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                matches +=1
            elif s2Count[index] - 1 == s1Count[index]:
                matches -=1
            
            index = ord(s2[left]) - ord('a')
            s2Count[index]-=1
            if s2Count[index] == s1Count[index]:
                matches +=1
            elif s2Count[index] + 1 == s1Count[index]:
                matches -=1
            left+=1
            
        return matches == 26