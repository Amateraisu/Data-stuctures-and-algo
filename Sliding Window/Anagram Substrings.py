class Solution:
    def solve(self, req, string):
        required = Counter(req)
        left = 0 
        res = 0 
        runningDict = defaultdict(int)
        for right in range(len(string)):
            currentChar = string[right]
            if currentChar not in required:
                runningDict = defaultdict(int)
                left = right  + 1
                continue 
            runningDict[currentChar] += 1 

            while left < right and runningDict[currentChar] > required[currentChar]:
                
                runningDict[string[left]] -= 1 
                if runningDict[string[left]] == 0:
                    runningDict.pop(string[left])
                left += 1 

            if runningDict == required:

                res += 1 

        return res