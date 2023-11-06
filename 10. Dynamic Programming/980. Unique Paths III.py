class Solution:
    def in_boundry(self, r, c):
        return 0 <= r < self.n and 0 <= c < self.m
    def uniquePathsIII(self, grid):
        self.counts =0
        self.n = len(grid)
        self.m = len(grid[0])
        s=0,0
        for i in range(self.n):
            stop=False
            for j in range(self.m):
                if grid[i][j]==1:
                    s=i,j
                    stop=True
                    break
            if stop:
                break
        self.dp = [[False for i in range(self.m)] for ji in range(self.n)]
        self.traverse(grid,s[0], s[1])
        return self.counts
    def traverse(self, grid, r, j):
        if self.in_boundry(r,j) and not self.dp[r][j] and grid[r][j]!=-1:
            if grid[r][j]==2:
                self.counts+=1
                return
            self.dp[r][j] = True
            self.traverse(grid,r-1,j)
            self.traverse(grid,r,j-1)
            self.traverse(grid,r,j+1)
            self.traverse(grid,r+1,j)


