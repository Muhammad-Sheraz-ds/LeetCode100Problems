class Solution:
    def findArray(self, pref):
        n = len(pref)
        if n ==0:
            return []
        heap = [pref[0]]*n
        for i in range(1,n):
            heap[i] = pref[i]^heap[i-1]
        return heap
