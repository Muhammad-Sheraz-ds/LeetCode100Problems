class Solution:
    def iniate(self):
        self.cl = board[i][j]
    def floodFill(self, data: List[List[int]], sr: int, sc: int, bc):
        self.n = len(data)
        self.m = len(data[0])
        self.iniate()

    def floodFill_(self, data: List[List[int]], sr: int, sc: int, bc):
        n = len(data)
        self.n = len(data)
        self.m = len(data[0])
        self.iniate()
        if sr < 0 or sr == height or sc < 0 or sc == width:
            return

        if data[sr][sc] != bc:
            return

        data[sr][sc] = self.cl
        floodFill_(data, height, width, sr - 1, sc, bc, fc)
        floodFill_(data, height, width, sr, sc + 1, bc, fc)
        floodFill_(data, height, width, sr + 1, sc, bc, fc)
        floodFill_(data, height, width, sr, sc - 1, bc, fc)

