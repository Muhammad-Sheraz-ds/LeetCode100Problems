class Solution:
    def matrixReshape(self, mat, r,c):
        n = len(mat)
        m= len(mat[0])
        if n*m!=r*c:
            return mat
        array = [None]*(n*m)
        for row in range(r):
            for col in range(c):
                array[row*c+col]= mat[row][col]
        if r == 1:
            return [array]
        a = [[None for i in range(c)]for i in range(r)]
        for row in range(r):
            for col in range(c):
                a[row][col] = array[row * c + col]
        return a

