class Solution:
    def flipAndInvertImage(self, image):
        n = len(image)
        invert_image = [[0 for i in range(n)] for j in range(n)]
        for row in range(n):
            for col in range(n):
                val = 0
                if image[row][col] == 0:
                    val=1
                invert_image[row][n-1-col]=val
        return invert_image
