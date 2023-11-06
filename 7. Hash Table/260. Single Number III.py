from collections import Counter
class Solution:
    def singleNumber(self, nums):
        n = len(nums)
        ans = []
        count = Counter(nums)
        for val in nums:
            if count[val] == 1:
                ans.append(val)
        return ans
print(1^3)