class Solution:
    def rotate(self, matrix) -> None:
        self.tarnspose(matrix)
        n = len(matrix)
        i=0
        j=n-1
        m = n
        while i<j:
            d = 0
            while d < n:
                matrix[d][i],matrix[d][j] = matrix[d][j],matrix[d][i]
                d+=1
            i+=1
            j-=1

    def tarnspose(self,matrix):
        n = len(matrix)
        m = n
        seen = [[False for i in range(n)] for i in range(m)]
        for r in range(n):
            for c in range(n):
                if seen[r][c] ==False:
                    matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
                    seen[c][r]=True
                    seen[r][c]=True
s =Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])