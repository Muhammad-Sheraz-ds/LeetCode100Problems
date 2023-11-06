class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        d = dict()
        for i in range(len(nums)):
            try:
                if abs(d[nums[i]] - i) <= k:
                    return True
                d[nums[i]] = i
            except:
                d[nums[i]] = i

        return False