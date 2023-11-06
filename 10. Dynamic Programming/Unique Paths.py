class Solution:
    def uniquePaths(self, m, n):
        dp = [[0 for i in range(n)] for j in range(m)]
        self.counts=0
        self.aux_traversal(dp,m,n,0,0)
        for i in dp:
            for j in i:
                self.counts+=j
        return self.counts

    def aux_traversal(self,dp,m,n,i,j):
        if dp[i][j] != 0:
            self.counts+=1
            return
        c=0
        if i==m-1 and j == n-1:
            self.counts+=1
            dp[i][j]=1
            return
        if i!=m-1:
            c+=1
            self.aux_traversal(dp,m,n,i+1,j)
        if j!=n-1:
            self.aux_traversal(dp,m,n,i,j+1)
            c+=1
        dp[i][j]+=c
