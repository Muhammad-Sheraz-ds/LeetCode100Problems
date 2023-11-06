class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = dict()
        n = len(nums)
        if n == 0: return 0
        c = 0
        i = 0
        while i < n:
            try:
                d[nums[i]] += 1
            except:
                d[nums[i]] = 1
            nums[c] = nums[i]
            if d[nums[i]]<3:
                c+=1

            i += 1
        return c