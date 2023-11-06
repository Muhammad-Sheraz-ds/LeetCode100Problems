class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.ans = []
        rows = len(matrix)
        cols = len(matrix[0])
        cl = cols
        k = 0
        i = 0
        self.dp = [[False for i in range(cols)] for k in range(rows)]
        if cols == 1:
            for i in range(rows):
                self.ans.append(matrix[i][0])
            return self.ans

        limit = rows // 2
        if rows%2==0:
            i=0
            while rows > limit:
                if i <= rows and i < cols:
                    self.print_outside_wall(matrix, i, i, rows, cols)
                cols -= 1
                rows -= 1
                i+=1
        else:
            i = 0
            while rows >= limit:
                if i <= rows and i < cols:
                    self.print_outside_wall(matrix, i, i, rows, cols)
                cols -= 1
                rows -= 1
                i += 1

        return self.ans
    def print_outside_wall(self, matrix, r, c, rows, cols):
        if r == rows - 1:
            for i in range(c, cols):
                if not self.dp[r][i]:
                    self.ans.append(matrix[r][i])
                    self.dp[r][i] = True

            return

        for i in range(c, cols):
            if not self.dp[r][i]:
                self.ans.append(matrix[r][i])
                self.dp[r][i] = True

        for j in range(r + 1, rows - 1):
            if not self.dp[j][cols - 1]:
                self.ans.append(matrix[j][cols - 1])
                self.dp[j][cols - 1] = True
        for i in range(cols - 1, c - 1, -1):
            if not self.dp[rows - 1][i]:
                self.ans.append(matrix[rows - 1][i])
                self.dp[rows - 1][i] = True
        for j in range(rows - 2, c, -1):
            if not self.dp[j][c]:
                self.ans.append(matrix[j][c])
                self.dp[j][c] = True
