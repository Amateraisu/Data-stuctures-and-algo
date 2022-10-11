class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        numRows, numCols = len(matrix), len(matrix[0])
        
        # convert everything to int 
        for row in range(numRows):
            for col in range(numCols):
                matrix[row][col] = int(matrix[row][col])
        
        for row in range(1, numRows):
            for col in range(numCols):
                
                if matrix[row][col] == 0:
                    continue 
                else:
                    matrix[row][col] += matrix[row - 1][col]
                    
        # then find the largest rectangle for every single row 
        
        res = float("-inf")
        
        for row in range(numRows):
            largest = findLargest(matrix[row])
            res = max(res, largest)
            print(row, largest)
        return res
    
    
def findLargest(row):
    stack = []
    res = 0 
    rowLength = len(row)
    for index, height in enumerate(row):
        # keep trying to extend the height to the right 
        prevIndex = index
        if stack and stack[-1][1] > height: # that means we cannot extend the height of the top of  the stack any further, we have to pop it off, consider the height at 
            while stack and stack[-1][1] > height:
                # width = currentIndex - stackindex 
                stackIndex, stackHeight = stack.pop()
                width = index - stackIndex 

                area = width * stackHeight
                prevIndex = stackIndex
                res = max(res, width * stackHeight)
        if height != 0:
            
            stack.append([prevIndex, int(height)])
    # for the ones left inside the stack, that means they span across the entire row 
    
    for index, height in stack:
        res = max(res, height * (rowLength - index))
    # print(stack)
    # print(row, res, "result")
    return res