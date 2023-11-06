class Solution:
    def return_index(self,i,r,c):
        i = (i)%(r*c)
        return i//c,i%c


    def shiftGrid(self, grid, k) -> List[List[int]]:
        r = len(grid)
        c = len(grid[0])
        new_grid = [[0 for col in range(c)]for row in range(r)]
        for row in range(r):
            for col in range(c):
                nr,nc = self.return_index(row*c+col+k,r,c)
                new_grid[nr][nc] = grid[row][col]
        return new_grid



