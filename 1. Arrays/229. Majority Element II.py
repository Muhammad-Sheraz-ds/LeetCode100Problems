class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        d = dict()
        for i in range(n):
            if nums[i] in d:
                d[nums[i]] += 1
                nums[i]=None
            else:
                d[nums[i]] = 1
        ans = []
        for i in range(n):
            if nums[i]!=None and (d[nums[i]] > (n/3)):
                ans.append(nums[i])




