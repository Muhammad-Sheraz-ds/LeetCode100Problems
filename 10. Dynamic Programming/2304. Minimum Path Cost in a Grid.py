class Solution:
    def find_min_sum(self,grid,moveCost,i,j):
        m = moveCost[grid[i]][j]
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                moveCost[i][j]+=grid[i][j]
        r = len(grid)
        c = len(grid[0])
        total = 0
        pre_min = moveCost[grid[0][0]]
        for i in range(1,r):
            for j in range(c):
                mn = 100000000
                for k in range(c):
                    mn = min(moveCost[grid[i-1][k]][j],mn)
                total+=mn
        return total







