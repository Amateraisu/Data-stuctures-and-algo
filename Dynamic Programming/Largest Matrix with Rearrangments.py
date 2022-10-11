class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # so here I need to sort each of the rows 
        # let m be the number of rows 
        # let n be the number of cols 
        
        # time complexity will be O(m * n log n)
        largest = 0 
        numRows = len(matrix)
        numCols = len(matrix[0])
        
        for row in range(1, numRows):
            for col in range(numCols):
                # if the box is 0, dont update it 
                if matrix[row][col] == 0:
                    continue 
                else:
                    matrix[row][col] += matrix[row - 1][col]

        # then go through every single row and sort them 
        for row in matrix:
            # sort them , and find the largest u can form 
            row.sort(reverse = True)

            for index, maximum in enumerate(row):
                largest = max(largest, maximum * (index + 1))
                print(largest, maximum, index + 1)
        
        return largest