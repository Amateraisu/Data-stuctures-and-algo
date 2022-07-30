from collections import defaultdict

class Solution:
    def __init__(self):
        self.solution = []
        # self.cache = defaultdict(list) # index : []
    def expand(self, s: str) -> List[str]:
        endCondition = len(s)
        currentSolution = []
        currentIndex = 0
        self.dp(currentSolution, currentIndex, endCondition, s)
        
        return self.solution
    def dp(self, currentSolution, currentIndex, endCondition, string):
        if currentIndex == endCondition:
            finalSolution = "".join(currentSolution)
            self.solution.append(finalSolution)
            return 
        # if currentIndex in self.cache:
            # process all combinations here 
        
        if string[currentIndex] == "{":
            # find the next } 
            possibleOptions = []
            tempPtr = currentIndex + 1
            while string[tempPtr] != "}":
                if string[tempPtr] == ",":
                    pass
                else:
                    possibleOptions.append(string[tempPtr])
                    
                tempPtr += 1 
            possibleOptions.sort()
            for char in possibleOptions:
                self.dp(currentSolution + [char], tempPtr + 1, endCondition, string)
        else:
            self.dp(currentSolution + [string[currentIndex]], currentIndex + 1, endCondition, string)
            
        return 