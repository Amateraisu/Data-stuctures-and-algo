class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        
        cache = {}
        
        def dfs(currentIndex, daysLeft):

            if currentIndex == len(jobDifficulty) and daysLeft == 0:

                return 0 
            if daysLeft == 0:
                # print("currentIndex", currentIndex, daysLeft)
                return float("inf")
            if currentIndex == len(jobDifficulty):
                return float("inf")
            if (currentIndex, daysLeft) in cache:
                return cache[(currentIndex, daysLeft)]
            
            

            

            
            temp = float("inf")
            biggest = jobDifficulty[currentIndex]
            for i in range(currentIndex, len(jobDifficulty)):
                biggest = max(biggest, jobDifficulty[i])
                # print("currentIndex", i, "currentBiggest", biggest, "days", daysLeft)
                
                temp = min(temp, dfs(i + 1, daysLeft - 1) + biggest)
                
            cache[(currentIndex, daysLeft)] = temp 
            # print(temp, "FINAL")
            return temp 

        return dfs(0, d)