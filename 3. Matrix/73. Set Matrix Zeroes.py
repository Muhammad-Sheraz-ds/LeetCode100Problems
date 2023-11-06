class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        rows_list = []
        cols_list = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0:
                    rows_list.append(row)
                    cols_list.append(col)
        dp=[False]*rows
        for i in range(len(rows_list)):
            if not dp[rows_list[i]]:
                matrix[rows_list[i]] = [0]*cols
        dp = [[False for i in range(cols)] for j in range(rows)]
        for i in range(len(cols_list)):
            for j in range(rows)
                matrix[j][cols_list[i]] = 0
    def fill_zero(self,matrix,dp,r,c,rows,cols):
        for i in range(rows):
            dp[i][c] =True
            matrix[i][c]=0
        for i in range(cols):
            dp[i][r] =True
            matrix[i][r]=0