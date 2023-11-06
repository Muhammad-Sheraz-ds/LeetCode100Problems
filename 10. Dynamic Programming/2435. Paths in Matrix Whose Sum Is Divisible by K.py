class Solution:
    def in_boundry(self, r, c):
        return 0 <= r < self.n and 0 <= c < self.m

    def numberOfPaths(self, grid, k):
        self.n = len(grid)
        self.k =k
        self.m = len(grid[0])
        self.dp = [[None for i in range(self.m)] for ji in range(self.n)]
        self.dp[self.n - 1][self.m - 1] = 1
        return self.min_sum(0, 0)

    def min_sum(self, grid, dp, r, j):
        if not self.in_boundry(r, j):
            return 0
        if dp[r][j] != None:


        dp[r][j] = self.min_sum(grid, dp, r, j + 1), self.min_sum(grid, dp, r + 1, j)
        return dp[r][j]
