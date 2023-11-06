class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0 for _ in range(m)] for _ in range(n)]

        # Initialize the first row and first column
        dp[0][0] = 1  # Starting point

        # Initialize the first column
        for i in range(1, n):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        # Initialize the first row
        for j in range(1, m):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        # Calculate unique paths
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n - 1][m - 1]
