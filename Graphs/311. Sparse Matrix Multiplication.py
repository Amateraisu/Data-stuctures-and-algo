def compress(matrix):
    m = len(matrix)
    n = len(matrix[0])
    res = [[] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != 0:
                res[i].append([j, matrix[i][j]])

    return res


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        # List of Lists way
        mat1_com = compress(mat1)
        mat2_com = compress(mat2)

        m = len(mat1)
        n = len(mat2[0])
        x = len(mat1[0])
        res = [[0 for i in range(n)] for j in range(m)]
        for r in range(m):
            for col, val in mat1_com[r]:
                for col2, val2 in mat2_com[col]:
                    new = val * val2
                    res[r][col2] += new

        return res
        # essentialy lets look at how we multiply matrixes
        # traditional way

        # m = len(mat1)
        # n = len(mat2[0])
        # x = len(mat1[0])
        # res = [[0 for i in range(n)] for j in range(m)]

        # for i in range(m):
        #     for k in range(n):
        #         for j in range(x):

        #             t = mat1[i][j] * mat2[j][k]
        #             res[i][k] += t

        # return res