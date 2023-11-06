class Solution:
    def findCenter(self, edges):
        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]
