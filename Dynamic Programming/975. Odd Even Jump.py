class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        sortedAsc = sorted([i for i in range(len(arr))], key = lambda x : (arr[x], x))

        sortedDesc = sorted([i for i in range(len(arr))], key =lambda x: (-arr[x], x))

        validOdd = [float("inf")] * len(arr)
        validEven = [float("inf")] * len(arr)
        stack = [] 
        for i in range(len(sortedAsc)):
            while stack and stack[-1] <= sortedAsc[i]:
                top = stack.pop()
                validOdd[top] = sortedAsc[i]
            stack.append(sortedAsc[i])
        stack = [] 

        for j in range(len(sortedDesc)):
            while stack and stack[-1] <= sortedDesc[j]:
                top = stack.pop()
                validEven[top] = sortedDesc[j]
            stack.append(sortedDesc[j])
            
            

        @cache
        def dfs(currentIndex, isOdd):
            if currentIndex == len(arr) - 1:
                return 1 
            if currentIndex > len(arr) - 1:
                return 0 
            
            res = 0 
            if isOdd:
                res += dfs(validOdd[currentIndex], not isOdd)
            else:
                res += dfs(validEven[currentIndex], not isOdd)
            return res 
        res = 0
        for i in range(len(arr)):
            res += dfs(i, True)
            
        return res