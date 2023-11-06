class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        d = dict()
        for i in range(len(nums)):
            try:
                if abs(d[nums[i]] - i)-1 <= indexDiff and  abs(nums[i]-nums[d[nums[i]]])<=valueDiff:
                    return True


            except:
                pass
            d[nums[i]] = i
        return False