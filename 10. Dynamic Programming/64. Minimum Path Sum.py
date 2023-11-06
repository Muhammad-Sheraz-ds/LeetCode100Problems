class Solution:
    def in_boundry(self, r, c):
        return 0 <= r < self.n and 0 <= c < self.m

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        dp = [[None for i in range(self.m)] for ji in range(self.n)]
        dp[self.n - 1][self.m - 1] = grid[self.n - 1][self.m - 1]
        return self.min_sum(grid, dp, 0, 0)

    def min_sum(self, grid, dp, r, j):
        if not self.in_boundry(r, j):
            return 10000000000

        s = 0
        if dp[r][j] == None:
            dp[r][j] = grid[r][j] + min(self.min_sum(grid, dp, r, j + 1), self.min_sum(grid, dp, r + 1, j))
        return dp[r][j]
