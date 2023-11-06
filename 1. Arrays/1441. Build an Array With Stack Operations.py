class Solution:
    def buildArray(self, target, n):
        ans = []
        dp = {}
        i=1
        for v in target:
            dp[v]=True
        while i <= target[-1]:
            ans.append("Push")
            if i not in dp:
                ans.append("Pop")
            i+=1
        return ans