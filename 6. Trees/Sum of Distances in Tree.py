class Solution:
    def sumOfDistancesInTree(self, n, edges):
        self.res = [0 for i in range(n)]
        for i in range(n-1):
            val = edges[i][1]
            index = edges[i][0]
            self.res[val] = self.res[index]+1
        sum = [0]*n
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                a=abs(self.res[i] - self.res[j])
                if i==0:
                    a=2
                sum[i]+=a
        return sum



