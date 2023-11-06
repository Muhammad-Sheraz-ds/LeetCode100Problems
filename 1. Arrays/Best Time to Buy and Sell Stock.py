class Solution:
    def maxProfit(self, prices):
        self.n = len(prices)
        i=1
        profit = 0
        v = prices[0]
        while i < self.n:
            cur = prices[i] - v
            if cur>profit:
                profit = cur
            if prices[i]<v:
                v= prices[i]
                m=i
            i+=1
        return profit
