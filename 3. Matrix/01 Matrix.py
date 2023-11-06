
class Solution:
    def in_boundary(self, i, j):
        return 0 <= i < self.rows and 0 <= j < self.cols

    def updateMatrix(self, mat):
        self.rows = len(mat)
        self.cols = len(mat[0])
        self.dp = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.iterate(mat, i, j)
        return mat

    def iterate(self, mat, r, c):
        if self.in_boundary(r, c):
            if not self.dp[r][c]:
                self.dp[r][c] = True
                if mat[r][c] == 1:
                    # Ensure to add base cases to terminate recursion when out of bounds
                    top = self.iterate(mat, r - 1, c) if r > 0 else float('inf')
                    left = self.iterate(mat, r, c - 1) if c > 0 else float('inf')
                    right = self.iterate(mat, r, c + 1) if c < self.cols - 1 else float('inf')
                    bottom = self.iterate(mat, r + 1, c) if r < self.rows - 1 else float('inf')

                    mat[r][c] = min(top, left, right, bottom) + 1
            return mat[r][c]
        return 1000000  # Return 0 when out of bounds

input_matrix = [
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]
]

solution = Solution()
output_matrix = solution.updateMatrix(input_matrix)

# Print the output matrix
for row in output_matrix:
    print(row)



'''class Solution:
    def in_boundry(self,i,j):
        return 0<=i<self.rows and  0<=j<self.cols

    def updateMatrix(self, mat):
        self.rows = len(mat)
        self.cols = len(mat[0])
        self.dp = [[False for i in range(self.cols)] for j in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.iterate(mat,i,j)
        return mat
    def iterate(self,mat,r,c):
        if self.in_boundry(r,c):
            if not self.dp[r][c]:
                self.dp[r][c]=True
                if mat[r][c] == 1:
                    mat[r][c] = min(self.iterate(mat,r-1,c),self.iterate(mat,r,c-1),self.iterate(mat,r,c+1),self.iterate(mat,r+1,c))+1
            return mat[r][c]
        return 100000

'''
class Solution:
    def in_boundry(self, i, j):
        return 0 <= i < self.rows and 0 <= j < self.cols

    def updateMatrix(self, mat):
        self.rows = len(mat)
        self.cols = len(mat[0])
        self.dp = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.iterate(mat, i, j)
        return self.dp

    def iterate(self, mat, r, c):
        if self.in_boundry(r, c):
            if self.dp[r][c] is None:
                self.dp[r][c]=True

                if mat[r][c] == 0:
                    self.dp[r][c] = 0
                else:
                    # Ensure to add base cases to terminate recursion when out of bounds
                    top = self.iterate(mat, r - 1, c) if r > 0 else float('inf')
                    left = self.iterate(mat, r, c - 1) if c > 0 else float('inf')
                    right = self.iterate(mat, r, c + 1) if c < self.cols - 1 else float('inf')
                    bottom = self.iterate(mat, r + 1, c) if r < self.rows - 1 else float('inf')

                    self.dp[r][c] = min(top, left, right, bottom) + 1
            return self.dp[r][c]
        return 100000

''''''