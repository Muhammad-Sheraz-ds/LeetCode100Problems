class Solution:
    def maxProfit(self, prices):
        self.n = len(prices)
        i=1
        sell=False
        profit = 0
        pur_val = prices[0]
        while i < self.n:
            if prices[i] < pur_val:
                pur_val=prices[i]
            elif prices[i]>pur_val:
                profit += prices[i]-pur_val
                pur_val=prices[i]

            i+=1
        return profit
