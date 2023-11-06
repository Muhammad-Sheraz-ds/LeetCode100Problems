class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        dp = dict()
        n = len(nums)
        m = -10**5
        for i in range(n):
            if nums[i]> m:
                m = nums[i]
            for j in range(i,n):
                if nums[j] <= nums[i]:
