class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n==0: return 0
        c = 1
        i=1
        prev = nums[0]
        while i < n:
            if nums[i]!=prev:
                c+=1
            prev = nums[i]
            nums[c] = nums[i]
            i+=1
        return c
