class Solution:
    def maxLength(self, arr: List[str]) -> int:
        states = [0 for i in ascii_lowercase]
        
        
        res = 0 
        
        
        cache = {}
        def dfs(currentIndex, states):
            if currentIndex == len(arr):
                return 0 
            
            tuplefied = tuple(states)
            if (currentIndex, tuplefied) in cache:
                return cache[(currentIndex, tuplefied)]
            
            best = 0 
            
            for i in range(currentIndex+ 1 , len(arr)):
                temp = states[:]
                currentWord = arr[currentIndex]
                valid = True
                for char in currentWord:
                    indexInState = ord(char) - ord("a")
                    # print("char", char, temp)
                    if temp[indexInState] != 0:
                        valid = False 
                        break
                    else:
                        temp[indexInState] += 1 
                        
                        
                if valid:
                    # print("valid")
                    best = max(best, dfs(i, temp) + len(currentWord))
            cache[(currentIndex, tuplefied)] = best 
            # print("best", best)
                               
            return best 
                             
        for i in range(-1, len(arr) - 1):
            res = max(res, dfs(i, states))
            
        return res