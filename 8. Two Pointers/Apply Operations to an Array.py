class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0: return []
        c = 0
        i = 0
        zero = [0]*n
        while i < n-1:
            if nums[i] == nums[i + 1]:
                nums[i]*=2
                nums[i+1] = 0
            if nums[i]!=0:
                zero[c] = nums[i]
                c+=1
            i += 1
        if nums[i] != 0:
            zero[c] = nums[i]
        return zero
