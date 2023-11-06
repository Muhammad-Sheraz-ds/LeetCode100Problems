class Solution:
    def generate(self, rows):
        a = []
        i = 0
        while i < rows:
            j = 0
            l = []
            while j <= i:
                l.append(1)
                j += 1
            a.append(l)
            i += 1
        if rows<3:
            return a
        for row in range(2,rows):
            for col in range(1,row):
                a[row][col] = a[row-1][col-1] + a[row-1][col]
        return a





