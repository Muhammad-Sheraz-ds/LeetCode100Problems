class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0: return 0
        c = 0
        i = 0
        while i < n:
            nums[c] = nums[i]
            if nums[i] != val:
                c += 1
            i += 1
        return c