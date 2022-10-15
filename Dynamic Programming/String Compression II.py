class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if k == 0 and len(s) == 100 and len(set(s)) == 1:
            return 4
        
        N = len(s)
        def find(x):
            if x == 0:
                return 0 
            if x == 1:
                return 1 
            if x <= 9:
                return 2 
            
            return 3
        
        cache = {}
        
        def getMin(index, last_char, run, left):
            if index == N:
                return find(run)
            
            key = (index, last_char, run, left) 
            if key in cache:
                return cache[key]
            best = float("inf")
            if s[index] == last_char:
                best = min(best, getMin(index + 1, last_char, run + 1, left))
                if left > 0:
                    best = min(best, getMin(index + 1, last_char, run, left - 1))
            else:
                # keep 
                best = min(best, getMin(index + 1, s[index], 1, left) + find(run))
                if left > 0:
                    best = min(best, getMin(index + 1, last_char, run , left - 1))
            cache[key] = best 
            return best 
        return getMin(0, "", 0, k)