import copy

class Solution:
    def rotate(self, nums, k) -> None:
        n = len(nums)
        a = copy.deepcopy(nums)
        for i in range(n):
            nums[i]=a[i-k]
    


