from collections import Counter
class Solution:
    def singleNumber(self, nums):
        n = len(nums)
        count = Counter(nums)
        for val in nums:
            if count[val] != 3:
                return val
