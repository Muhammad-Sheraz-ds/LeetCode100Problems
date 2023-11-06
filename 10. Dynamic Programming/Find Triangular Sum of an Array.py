class Solution:
    def triangularSum(self, trianaglr):
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
        self.dp = dp