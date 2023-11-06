class Solution:
    def generateMatrix(self, n) -> List[List[int]]:
        self.counts = 1
        rows = n
        cols = n
        cl = cols
        self.dp=[[False for i in range(n)] for k in range(n)]
        i = 0
        matrix = [[None for i in range(n)] for k in range(n)]
        limit = rows // 2
        while i < limit:
            self.print_outside_wall(matrix, i, i, rows, cols)
            cols -= 1
            rows -= 1
            i+=1
        if n%2==1:
            matrix[n//2][n//2]=self.counts
        return matrix
    def print_outside_wall(self, matrix, r, c, rows, cols):

        for i in range(c, cols):
            matrix[r][i] = self.counts
            self.counts+=1

        for j in range(r + 1, rows - 1):
            matrix[j][cols - 1] = self.counts
            self.counts += 1
        for i in range(cols - 1, c - 1, -1):
            matrix[rows - 1][i] = self.counts
            self.counts += 1
        for j in range(rows - 2, c, -1):
            matrix[j][c] = self.counts
            self.counts += 1
