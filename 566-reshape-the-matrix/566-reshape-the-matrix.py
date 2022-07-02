class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        oldCol = len(mat[0])
        result = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                elementNo = i * c + j
                row = elementNo // oldCol
                col = elementNo % oldCol
                result[i][j] = mat[row][col]
        return result