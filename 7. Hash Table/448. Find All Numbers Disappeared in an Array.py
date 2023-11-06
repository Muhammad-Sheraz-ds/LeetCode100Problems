class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        ans = []
        d = [None] * (n + 1)
        for val in nums:
            d[val] = val
        i = 1
        while i <= n:
            if d[i] == None:
                ans.append(i)
            i += 1
        return ans