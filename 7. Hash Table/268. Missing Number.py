class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        d = [None]*(n+1)
        for val in nums:
            d[val] = val
        i = 0
        while i<=n:
            if d[i]==None:
                return i
            i += 1
