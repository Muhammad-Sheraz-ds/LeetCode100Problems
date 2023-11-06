class Solution:
    def searchRange(self, nums, target):
        n = len(nums)
        ans = [-1, -1]
        i = 0
        while i < n:
            if nums[i] == target:
                ans[0] = i
                j = i+1
                while j < n and nums[j] == target:
                    j += 1
                ans[1] = j-1
                break
            i += 1
        return ans

