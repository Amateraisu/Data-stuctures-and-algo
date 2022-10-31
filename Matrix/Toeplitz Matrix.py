class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])
        hashmap = collections.defaultdict(list)
        for row in range(numRows):
            for col in range(numCols):
                position = row - col

                if hashmap[position] and hashmap[position][-1] != matrix[row][col]:

                    return False 
                
                hashmap[position].append(matrix[row][col])
                
        return True 