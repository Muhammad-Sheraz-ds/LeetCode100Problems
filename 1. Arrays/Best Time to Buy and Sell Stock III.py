class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        k = 2  # Maximum number of transactions allowed

        # Initialize a 2D array to store the maximum profit
        # dp[i][j] represents the maximum profit on day i with j transactions
        dp = [[0] * (k + 1) for _ in range(n)]
        for j in range(1, k + 1):
            max_diff = -prices[0]  # The maximum difference to store the previous transaction's profit

            for i in range(1, n):
                dp[i][j] = max(dp[i - 1][j], prices[i] + max_diff)
                max_diff = max(max_diff, dp[i][j - 1] - prices[i])

        return dp[n - 1][k]


'''class Solution:
    def maxProfit(self, prices):
        self.n = len(prices)
        s=0
        i,profit = self.find_profit(prices)
        if i==0:
            return 0
        elif i==self.n-1:
            return profit
        else:
            i,s=self.find_profit(prices,i+1)
        return profit+s

    def find_profit(self,prices,i=1):
        profit = 0
        index = 0
        v = prices[0]
        while i < self.n:
            cur = prices[i] - v
            if cur > profit:
                profit = cur
                index = i
            if prices[i] < v:
                v = prices[i]
                m = i
            i += 1
        return index,profit
'''