class Solution:
    def maximumSumRectangle(self,R,C,matrix):
        # O(m n ^ 2)
        
        numRows = len(matrix)
        numCols = len(matrix[0])
        res = float("-inf")
        for col in range(numCols):
            left = col 
            # create the kandene array 
            kandeneArray = [0 for row in range(numRows)]
            for right in range(left, numCols):
                # populate the numbers 
                for row in range(numRows):
                    kandeneArray[row] += matrix[row][right]
                # find the best 
                bestSum = kandene(kandeneArray)
                res = max(res, bestSum)


        return res 
    
    
def kandene(array):
    preSum = 0 
    res = float("-inf")
    for i in range(len(array)):
        preSum += array[i]
        if preSum < 0:
            preSum =  0
        if preSum != 0:
            res = max(res, preSum)
        

    return res if res != float("-inf") else max(array)