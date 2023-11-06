import heapq
import math
class Solution:
    def maxStarSum(self, vals, edges, k):
        m = [[] for i in range(len(vals))]
        for x, y in edges:
            if vals[y] > 0:
                heapq.heappush(m[x], vals[y])  # For each node, push this neighbors value to its heap
                if len(m[x]) > k:  # If the Min-Heap size is more than K.
                    heapq.heappop(m[x])  # Pop the smallest Neighbour value as we can't use it anyway.

            if vals[x] > 0:
                heapq.heappush(m[y], vals[x])  # Repeat the same for other neighbor
                if len(m[y]) > k:
                    heapq.heappop(m[y])

        res = -math.inf
        for i in range(len(vals)):  # We'll try to maximize the star with each node being center
            tot = vals[i]  # Our total will be value of that node as it has to be included.

            for nei_value in m[i]:  # We will check each value in the heap for the node.
                tot += nei_value  # We have already excluded neg values when pushing to Min-Heap

            res = max(res, tot)  # We'll maximize our result

        return res

