class Solution:
    def solve(self, matrix):

        # O(n) and O(1) time and space where n is the number of grids the matrix has 
        rowStart = 0 
        rowEnd = len(matrix) - 1 
        colStart = 0 
        colEnd = len(matrix[0]) - 1 

        while rowStart < rowEnd and colStart < colEnd:
            # rotate current Ring 
            topLeft = rowStart 
            bottomLeft = colStart 
            bottomRight = rowEnd
            topRight = colEnd


            # rotate the matrix 

            while topLeft < rowEnd:
                nums = [matrix[topLeft][colStart], matrix[rowEnd][bottomLeft], matrix[bottomRight][colEnd], matrix[rowStart][topRight]]
                final = rotateNums(nums)

                # then assign the respective numbers 
                matrix[topLeft][colStart] = final[0]
                matrix[rowEnd][bottomLeft] = final[1]
                matrix[bottomRight][colEnd] = final[2]
                matrix[rowStart][topRight] = final[3]


                topLeft += 1 
                bottomLeft += 1 
                bottomRight -= 1 
                topRight -= 1 






            rowStart += 1 
            rowEnd -= 1 
            colStart += 1 
            colEnd -= 1 

        return matrix 


def rotateNums(nums):
    res = [nums[-1]]
    for i in range(len(nums) - 1):
        res.append(nums[i])

    return res