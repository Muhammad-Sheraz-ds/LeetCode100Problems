class Solution:
    def construct2DArray(self, mat, r, c) -> List[List[int]]:
        n = len(mat)
        if n != r * c:
            return mat
        if r == 1:
            return [mat]
        a = [[None for i in range(c)] for i in range(r)]
        for row in range(r):
            for col in range(c):
                a[row][col] = mat[row * n + col]
        return a

