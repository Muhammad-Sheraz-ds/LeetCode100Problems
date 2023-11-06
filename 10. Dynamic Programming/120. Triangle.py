class Solution:
    def minimumTotal(self, triangle) -> int:
        self.rows = len(triangle)
        rows = len(triangle)
        if rows == 0:
            return 0
        i = 0
        dp = []
        while i < rows:
            j = 0
            l = []
            while j <= i:
                l.append(False)
                j += 1
            dp.append(l)
            i += 1
        self.dp=dp

        return self.aux_sum(triangle, triangle[0][0], 0, 0)

    def is_border(self, i, j):
        if i >= self.rows:
            return True
        return False

    def aux_sum(self, triangle, s, i=0, j=0):
        if not self.is_border(i + 1, j) and self.dp[i][j]==None:
            s1 = self.aux_sum(triangle, s + triangle[i + 1][j], i + 1, j)
            s2 = self.aux_sum(triangle, s + triangle[i + 1][j + 1], i + 1, j + 1)
            self.dp[i][j] = min(s1, s2)
        return self.dp[i][j]




class Solution:
    def minimumTotal(self, triangle) -> int:
        self.rows = len(triangle)
        rows = len(triangle)
        if rows == 0:
            return 0
        i = 0
        dp = []
        while i < rows:
            j = 0
            l = []
            while j <= i:
                l.append(False)
                j += 1
            dp.append(l)
            i += 1
        self.dp=dp

        return self.aux_sum(triangle, triangle[0][0], 0, 0)

    def is_border(self, i, j):
        if i >= self.rows:
            return True
        return False

    def aux_sum(self, triangle, s, i=0, j=0):
        if not self.is_border(i + 1, j) and self.dp[i][j]==None:
            if self.dp[i + 1][j]!=None:
                s1 = self.dp[i + 1][j]
            else:
                s1 = self.aux_sum(triangle, s + triangle[i + 1][j], i + 1, j)
            if self.dp[i + 1][j+1]!=None:
                s2 = self.dp[i + 1][j+1]
            else:
                s2 = self.aux_sum(triangle, s + triangle[i + 1][j + 1], i + 1, j + 1)
            self.dp[i][j] = min(s1, s2)
            return self.dp[i][j]
        return self.dp[i][j]


'''