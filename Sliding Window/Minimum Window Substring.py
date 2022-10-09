from collections import defaultdict

class Solution:
    def solve(self, a, b):
        # to optimize more we could use an array instead of map but who cares right.... ? XD 
        res = float("inf")
        if not a:
            return -1
        
        left = 0 
        currentDict = defaultdict(int)
        requiredDict = Counter(b)
        need = len(requiredDict.keys())
        have = 0
        for right in range(len(a)):
            currentChar = a[right]
            currentDict[currentChar] += 1 
            if currentChar in requiredDict and requiredDict[currentChar] == currentDict[currentChar]:
                have += 1 
            
            while left < right  and  currentDict[a[left]] > requiredDict[a[left]]:
                # print(left, right, "testing here", currentDict, requiredDict)
                currentDict[a[left]] -= 1 
                if a[left] in requiredDict and requiredDict[a[left]] != currentDict[a[left]]:
                    have -= 1
                left += 1 
            # print(left, right, "outside here", currentDict, requiredDict, currentChar)
            if need == have:
                res = min(res, right - left + 1)


        return res if res != float("inf") else -1