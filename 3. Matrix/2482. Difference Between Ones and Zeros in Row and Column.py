

class Solution:
    def onesMinusZeros(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        c = [[0,0] for j in range(cols)]
        r = [[0,0] for j in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    r[i][1]+=1
                else:
                    r[i][0]+=1
        for i in range(cols):
            for j in range(rows):
                if grid[i][j]==0:
                    c[i][1]+=1
                else:
                    c[i][0]+=1
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = r[i][0] + c[i][0] - r[i][1] - c[i][1]
        return grid


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        ones_row = [0] * rows
        ones_col = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 1:
                    continue
                ones_row[i] += 1
                ones_col[j] += 1

        for i in range(rows):
            for j in range(cols):
                grid[i][j] = (2 * ones_row[i]) - cols + (2 * ones_col[j]) - rows

        return grid
