class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        colStart = 0
        colEnd = n - 1
        rowStart = 0
        rowEnd = m - 1
        res = []
        while colStart <= colEnd and rowStart <= rowEnd:
            for i in range(colStart, colEnd + 1):
                res.append(matrix[rowStart][i])

            if rowStart == rowEnd:
                break
            for j in range(rowStart + 1, rowEnd + 1):
                res.append(matrix[j][colEnd])

            if colStart == colEnd:
                break

            for k in range(colEnd - 1, colStart - 1, -1):
                res.append(matrix[rowEnd][k])

            for x in range(rowEnd - 1, rowStart, -1):
                res.append(matrix[x][colStart])

            colStart += 1
            colEnd -= 1
            rowStart += 1
            rowEnd -= 1
        print(res)

        return res