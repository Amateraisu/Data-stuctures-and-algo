class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True 
        L = len(s1)
        for k in range(1, L):
            if self.isScramble(s1[0:k], s2[0:k]) and self.isScramble(s1[k:], s2[k:]):
                return True 
            if self.isScramble(s1[0:k], s2[L - k:]) and self.isScramble(s1[k:], s2[0: L -k]):
                return True 
        return False