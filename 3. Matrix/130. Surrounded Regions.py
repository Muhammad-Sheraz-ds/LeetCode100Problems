class Solution:
    def not_surrounded(self, board, i, j):
        l = []
        cont = True
        x = [i]
        y = [j]
        d = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        while x != []:
            v = x.pop(0)
            w = y.pop(0)
            l.append([v, w])
            self.visited[v][w] = True
            if self.is_border(v, w):
                cont = False

            for i in d:
                if 0<=v + i[0]<self.n and 0<=w + i[1]<self.m and board[v + i[0]][w + i[1]] == 'O' and not self.visited[v + i[0]][w + i[1]]:
                    self.visited[v + i[0]][w + i[1]] = True
                    x.append(v + i[0])
                    y.append(w + i[1])
        if cont:
            for i in l:
                board[i[0]][i[1]] = 'X'

    def is_border(self, i, j):
        if i == 0 or j == 0 or i == self.n - 1 or j == self.m - 1:
            return True
        return False

    def solve(self, board) -> None:
        n = len(board)
        self.n = n
        m = len(board[0])
        self.m = m
        self.visited = [[False for i in range(m)] for j in range(n)]
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'O' and not self.visited[row][col]:
                    self.not_surrounded(board, row, col)
                else:
                    self.visited[row][col] = True
