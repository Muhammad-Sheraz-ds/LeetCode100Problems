class Solution:
    def findMaxAverage(self, nums, k):
        s = sum(nums[0:k])
        m = s / k
        i = k
        while i < len(nums):
            s -= nums[i - k]
            s += nums[i]
            m = max(m, s / k)
            i += 1
        return m


