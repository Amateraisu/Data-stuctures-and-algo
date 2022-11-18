class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        # 1234 
        # currentIndex = 3 
        # currentResult = [1 + 2 + 3]
        # currentSum = 6 
        # prev = 3 
        # 1 + 2 + 3 * 4 
        
        # 1 + 2 + 12 
        
        
        
        def dfs(currentIndex, currentResult, currentSum, prev):
            if currentIndex == len(num):
                if currentSum == target:
                    res.append("".join(currentResult))
                    
                return 
            
            for i in range(currentIndex, len(num)):
                currentString = num[currentIndex: i + 1]
                currentNum = int(currentString)
                
                if len(currentResult) == 0:
                    dfs(i + 1, [currentString], currentNum, currentNum)
                else:
                    dfs(i + 1, currentResult + ["+"] + [currentString], currentSum + currentNum, currentNum)
                    dfs(i + 1, currentResult + ["-"] + [currentString], currentSum - currentNum, -currentNum)
                    dfs(i + 1, currentResult + ["*"] + [currentString], currentSum - prev + currentNum * prev, currentNum * prev)
                    
                if num[currentIndex] == "0":
                    break
                    
        dfs(0, [], 0, 0)
        
        return res