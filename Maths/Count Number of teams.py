class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        leftSmaller = [0 for i in range(N)]
        rightSmaller = [0 for i in range(N)]
        leftBigger = [0 for i in range(N)]
        rightBigger = [0 for i in range(N)]
        
        # left smaller 
        for i in range(N):
            currentNumber = rating[i]
            for j in range(i):
                if rating[j] < currentNumber:
                    leftSmaller[i] += 1 
                    rightBigger[j] += 1 

        # right smaller 
        for i in range(N):
            currentNumber = rating[i]
            for j in range(i, N):
                if rating[j] < currentNumber:
                    rightSmaller[i] += 1 
                    leftBigger[j] += 1 
        res = 0 
        for i in range(1, N - 1):
            # all the valid middle indexes
            res += leftSmaller[i] * rightBigger[i]
            res += rightSmaller[i] * leftBigger[i]
            
        return res